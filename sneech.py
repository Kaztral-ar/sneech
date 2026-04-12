#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  ____  _   _ _____  _____ ____ _   _
# / ___|| \ | | ____|| ____/ ___| | | |
# \___ \|  \| |  _|  |  _|| |   | |_| |
#  ___) | |\  | |___ | |__| |___|  _  |
# |____/|_| \_|_____|_____\___|_| |_|
#
#  All-in-One Pentesting Framework v2.2
#  For Educational & Authorised Testing Only
#

import os, sys, re, json, time, shlex, socket, hashlib, platform, subprocess

# ══════════════════════════════════════════════════════════════════════════════
#  CONFIG
# ══════════════════════════════════════════════════════════════════════════════

VERSION     = "2.2"
GITHUB_REPO = "https://github.com/Kaztral-ar/sneech.git"
INSTALL_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE  = os.path.join(INSTALL_DIR, ".sneech_state.json")

# Detect Termux (Android) — root checks and install paths differ
IS_TERMUX = os.environ.get("PREFIX", "").startswith("/data/data/com.termux")

# ══════════════════════════════════════════════════════════════════════════════
#  COLOURS
# ══════════════════════════════════════════════════════════════════════════════

class C:
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RESET   = "\033[0m"

# ══════════════════════════════════════════════════════════════════════════════
#  UI HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def clr():
    os.system("clear" if platform.system() != "Windows" else "cls")

def banner(update_available=False):
    logo = [
        r" ____  _   _ _____  _____ ____ _   _ ",
        r"/ ___|| \ | | ____|| ____/ ___| | | |",
        r"\___ \|  \| |  _|  |  _|| |   | |_| |",
        r" ___) | |\  | |___ | |__| |___|  _  |",
        r"|____/|_| \_|_____|_____\___|_| |_| ",
    ]
    bar = "\u2500" * 40
    print(f"\n{C.CYAN}{C.BOLD}", end="")
    for line in logo:
        print(f"  {line}")
    print(f"{C.RESET}{C.DIM}  {bar}")
    print(f"  All-in-One Pentesting Framework v{VERSION}")
    print(f"  github.com/Kaztral-ar/sneech  |  Educational Use Only")
    print(f"  {bar}{C.RESET}")
    if update_available:
        print(f"\n  {C.YELLOW}{C.BOLD}\u2605  Update available \u2014 press [0] to update!{C.RESET}")
    print()

def separator(label=""):
    bar = "\u2500" * 40
    if label:
        pad = max(1, (40 - len(label) - 2) // 2)
        print(f"\n{C.DIM}  {chr(0x2500)*pad} {label} {chr(0x2500)*pad}{C.RESET}\n")
    else:
        print(f"{C.DIM}  {bar}{C.RESET}")

def prompt(ps="sneech"):
    try:
        return input(f"  {C.GREEN}{C.BOLD}{ps}~# {C.RESET}").strip()
    except (KeyboardInterrupt, EOFError):
        print(f"\n\n  {C.YELLOW}[!]{C.RESET} Use [99] to exit cleanly.\n")
        return ""

def ok(msg):   print(f"  {C.GREEN}[+]{C.RESET} {msg}")
def err(msg):  print(f"  {C.RED}[-]{C.RESET} {msg}")
def warn(msg): print(f"  {C.YELLOW}[!]{C.RESET} {msg}")
def info(msg, colour=C.CYAN): print(f"  {colour}[i]{C.RESET} {msg}")

def confirm(q):
    try:
        return input(f"  {C.YELLOW}[?]{C.RESET} {q} {C.DIM}[y/N]{C.RESET}: ").strip().lower() in ("y", "yes")
    except (KeyboardInterrupt, EOFError):
        return False

def ask(prompt_text):
    try:
        return input(f"  {C.CYAN}[>]{C.RESET} {prompt_text}: ").strip()
    except (KeyboardInterrupt, EOFError):
        return ""

def sanitize(value):
    """
    Shell-safe quote a user-supplied value via shlex.quote.
    Returns '' if the input is blank, so callers can guard with `if not value`.
    """
    if not value:
        return ""
    return shlex.quote(value)

def run(cmd):
    """Execute a shell command, printing it first. Returns exit code."""
    print(f"\n  {C.DIM}$ {cmd}{C.RESET}\n")
    ret = os.system(cmd)
    if ret != 0:
        err(f"Command exited with code {ret}")
    return ret

def pause():
    try:
        input(f"\n  {C.DIM}Press ENTER to continue\u2026{C.RESET}")
    except (KeyboardInterrupt, EOFError):
        pass

# ══════════════════════════════════════════════════════════════════════════════
#  UPDATE ENGINE
# ══════════════════════════════════════════════════════════════════════════════

def _file_hash(path):
    try:
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return ""

def _load_state():
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def _save_state(state):
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)
    except Exception:
        pass

def _extract_tool_names(filepath):
    try:
        with open(filepath) as f:
            src = f.read()
        names = re.findall(r"^def (tool_\w+)\s*\(", src, re.MULTILINE)
        return sorted(n for n in names if n not in ("tool_update", "tool_check_updates"))
    except Exception:
        return []

def _extract_menu_labels(filepath):
    try:
        with open(filepath) as f:
            src = f.read()
        return sorted(re.findall(r'"\d+",\s*"([^"]+)"', src))
    except Exception:
        return []

def _git_ok():
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False

def _is_git_repo():
    r = subprocess.run(
        ["git", "-C", INSTALL_DIR, "rev-parse", "--is-inside-work-tree"],
        capture_output=True, text=True)
    return r.returncode == 0

def _git_pull():
    r = subprocess.run(
        ["git", "-C", INSTALL_DIR, "pull", "--ff-only"],
        capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr).strip()

def _current_commit():
    r = subprocess.run(
        ["git", "-C", INSTALL_DIR, "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else "unknown"

def _remote_commit():
    """Fetch origin and return the short HEAD commit hash, or '' on failure."""
    try:
        subprocess.run(["git", "-C", INSTALL_DIR, "fetch", "--quiet"],
                       capture_output=True, timeout=10)
        r = subprocess.run(
            ["git", "-C", INSTALL_DIR, "rev-parse", "--short", "origin/HEAD"],
            capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:
        return ""

def _git_log_since(old_commit):
    r = subprocess.run(
        ["git", "-C", INSTALL_DIR, "log", f"{old_commit}..HEAD", "--oneline", "--no-decorate"],
        capture_output=True, text=True)
    return [l.strip() for l in r.stdout.strip().splitlines() if l.strip()]

def tool_check_updates():
    """Silent startup check. Returns True if updates exist on GitHub."""
    if not _git_ok() or not _is_git_repo():
        return False
    try:
        remote = _remote_commit()          # single network call — no double-fetch
        if not remote:
            return False
        return remote != _current_commit()
    except Exception:
        return False

def tool_update():
    clr(); banner(); separator("Update SNEECH")

    if not _git_ok():
        err("Git is not installed.  Run:  sudo apt install git"); return
    if not _is_git_repo():
        err("SNEECH is not a git repository.")
        info(f"Re-install:  git clone {GITHUB_REPO}", C.YELLOW); return

    script        = os.path.join(INSTALL_DIR, "sneech.py")
    hash_before   = _file_hash(script)
    tools_before  = set(_extract_tool_names(script))
    lbls_before   = set(_extract_menu_labels(script))
    commit_before = _current_commit()
    remote        = _remote_commit()

    info(f"Installed : {C.CYAN}{commit_before}{C.RESET}  (v{VERSION})")
    if remote:
        info(f"Latest    : {C.CYAN}{remote}{C.RESET}")

    if remote and remote == commit_before:
        print(); ok("Already up to date."); return

    print()
    if not confirm("Pull latest version from GitHub?"):
        warn("Update cancelled."); return

    print(f"\n  {C.DIM}$ git pull --ff-only{C.RESET}\n")
    success, output = _git_pull()
    col = C.GREEN if success else C.RED
    for line in output.splitlines():
        print(f"  {col}[git]{C.RESET} {line}")

    if not success:
        print(); err("Pull failed — see above.")
        info("Try:  git -C " + INSTALL_DIR + " stash  then update again.", C.YELLOW)
        return

    hash_after   = _file_hash(script)
    tools_after  = set(_extract_tool_names(script))
    lbls_after   = set(_extract_menu_labels(script))
    commit_after = _current_commit()
    changed      = hash_before != hash_after
    new_tools    = sorted(tools_after  - tools_before)
    gone_tools   = sorted(tools_before - tools_after)
    new_lbls     = sorted(lbls_after   - lbls_before)

    print(); separator("Changelog")
    if changed:
        ok(f"Updated  {C.DIM}{commit_before[:7]} \u2192 {commit_after[:7]}{C.RESET}")
    else:
        ok("No file changes (metadata update only).")

    for line in _git_log_since(commit_before):
        print(f"    {C.DIM}\u2022{C.RESET} {line}")

    if new_tools:
        print(f"\n  {C.GREEN}{C.BOLD}\u2795 New tools ({len(new_tools)}):{C.RESET}")
        for t in new_tools:
            print(f"    {C.GREEN}+{C.RESET}  {t.replace('tool_','').replace('_',' ').title()}  {C.DIM}[{t}]{C.RESET}")

    if new_lbls:
        print(f"\n  {C.CYAN}{C.BOLD}\u2795 New menu entries ({len(new_lbls)}):{C.RESET}")
        for lbl in new_lbls:
            print(f"    {C.CYAN}+{C.RESET}  {lbl}")

    if gone_tools:
        print(f"\n  {C.YELLOW}{C.BOLD}\u2796 Removed ({len(gone_tools)}):{C.RESET}")
        for t in gone_tools:
            print(f"    {C.YELLOW}-{C.RESET}  {t.replace('tool_','').replace('_',' ').title()}")

    if changed and not new_tools and not new_lbls and not gone_tools:
        info("Bug fixes / improvements (no tool list changes).")

    _save_state({"version": VERSION, "last_commit": commit_after,
                 "known_tools": sorted(tools_after)})

    print()
    if changed:
        info(f"{C.YELLOW}Restart required to load new code.{C.RESET}")
        if confirm("Restart SNEECH now?"):
            print(f"  {C.DIM}Restarting\u2026{C.RESET}"); time.sleep(0.6)
            os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        ok("No restart needed.")

# ══════════════════════════════════════════════════════════════════════════════
#  TOOLS — INFORMATION GATHERING
# ══════════════════════════════════════════════════════════════════════════════

def tool_nmap():
    info("Nmap \u2014 Network exploration & port scanner.")
    choice = ask("(1) Run scan  (2) Install via apt")
    if choice == "2":
        confirm("Install Nmap?") and run("sudo apt-get install -y nmap")
        return
    target = sanitize(ask("Target IP / range / hostname"))
    if not target: return
    flags = ask("Flags (blank = -sV -O -Pn --open)")
    safe_flags = flags if flags else "-sV -O -Pn --open"
    run(f"nmap {safe_flags} {target}")

def tool_masscan():
    info("Masscan \u2014 Fastest internet-scale port scanner.")
    choice = ask("(1) Run scan  (2) Install via apt")
    if choice == "2":
        confirm("Install Masscan?") and run("sudo apt-get install -y masscan")
        return
    target = sanitize(ask("Target IP / CIDR (e.g. 192.168.1.0/24)"))
    if not target: return
    ports = ask("Ports (blank = 0-65535)")
    rate  = ask("Rate packets/sec (blank = 1000)")
    safe_ports = sanitize(ports) if ports else "0-65535"
    safe_rate  = sanitize(rate)  if rate  else "1000"
    run(f"sudo masscan {target} -p{safe_ports} --rate={safe_rate}")

def tool_ports():
    target = sanitize(ask("Target IP"))
    if target: run(f"nmap -sV --open -Pn {target}")

def tool_host_to_ip():
    host = ask("Hostname")
    if not host: return
    try:
        ip = socket.gethostbyname(host)
        ok(f"{host}  \u2192  {C.GREEN}{C.BOLD}{ip}{C.RESET}")
    except socket.gaierror as e:
        err(str(e))

def tool_whois():
    target = sanitize(ask("Domain or IP"))
    if target: run(f"whois {target}")

def tool_dnsenum():
    info("DNSenum \u2014 DNS enumeration & zone transfer.")
    confirm("Install dnsenum?") and run("sudo apt-get install -y dnsenum")
    target = sanitize(ask("Target domain"))
    if target: run(f"dnsenum {target}")

def tool_sublist3r():
    info("Sublist3r \u2014 Fast subdomain enumeration.")
    run("git clone https://github.com/aboul3la/Sublist3r.git --quiet 2>/dev/null || true")
    run("pip3 install -r Sublist3r/requirements.txt -q 2>/dev/null || true")
    target = sanitize(ask("Target domain"))
    if target: run(f"python3 Sublist3r/sublist3r.py -d {target}")

def tool_theharvester():
    info("theHarvester \u2014 OSINT email, subdomain & name harvesting.")
    confirm("Install theHarvester?") and run("sudo apt-get install -y theharvester")
    target = sanitize(ask("Target domain (e.g. example.com)"))
    if not target: return
    source = ask("Source (blank = google,bing,duckduckgo)")
    safe_source = sanitize(source) if source else "google,bing,duckduckgo"
    run(f"theHarvester -d {target} -b {safe_source}")

def tool_setoolkit():
    info("Social-Engineer Toolkit (SET).")
    if confirm("Clone & install SET?"):
        run("git clone https://github.com/trustedsec/social-engineer-toolkit.git --quiet 2>/dev/null || true")
        run("cd social-engineer-toolkit && sudo python3 setup.py")
    else:
        run("sudo setoolkit")

def tool_xsstrike():
    info("XSStrike \u2014 Advanced XSS detection & exploitation.")
    run("git clone https://github.com/s0md3v/XSStrike.git --quiet 2>/dev/null || true")
    run("pip3 install -r XSStrike/requirements.txt -q 2>/dev/null || true")
    run("python3 XSStrike/xsstrike.py")

def tool_doork():
    info("Doork \u2014 Passive Google dork vulnerability auditor.")
    if confirm("Install Doork?"):
        run("pip3 install beautifulsoup4 requests -q")
        run("git clone https://github.com/AeonDave/doork --quiet 2>/dev/null || true")
    target = sanitize(ask("Target domain"))
    if target: run(f"cd doork && python3 doork.py -t {target} -o log.log")

def tool_cmsmap():
    info("CMSmap \u2014 CMS vulnerability scanner (WP/Joomla/Drupal).")
    run("git clone https://github.com/Dionach/CMSmap.git --quiet 2>/dev/null || true")
    target = sanitize(ask("Target URL"))
    if target: run(f"python3 CMSmap/cmsmap.py {target}")

def tool_crips():
    info("Crips \u2014 IP tools & network info.")
    if not os.path.isdir("Crips"):
        run("git clone https://github.com/Manisso/Crips.git --quiet 2>/dev/null || true")
    # Kept in one bash -c call so the cd persists across statements
    run("bash -c 'cd Crips && sudo bash ./update.sh && python3 crips.py'")

def tool_scan_users():
    import urllib.request, urllib.parse, ssl
    site = ask("Target website (e.g. http://target.com)")
    if not site: return
    base  = re.sub(r"https?://(www\.)?", "", site).split("/")[0]
    users = re.sub(r"[.\-]", "", base)
    found = 0
    ctx   = ssl.create_default_context()
    print()
    while len(users) > 2:
        try:
            resp = urllib.request.urlopen(
                f"{site}/cgi-sys/guestbook.cgi?user={urllib.parse.quote(users)}",
                timeout=5, context=ctx
            ).read().decode(errors="replace")
            if "invalid username" not in resp.lower():
                ok(f"Found: {C.GREEN}{users}{C.RESET}"); found += 1
        except Exception:
            pass
        users = users[:-1]
    info(f"Done. {found} user(s) found.")

def tool_shodan():
    info("Shodan CLI \u2014 Search internet-connected devices.")
    confirm("Install Shodan CLI?") and run("pip3 install shodan -q")
    key = ask("Shodan API key (blank to skip init)")
    if key: run(f"shodan init {sanitize(key)}")
    q = ask("Search query (e.g. apache port:80)")
    if q: run(f"shodan search {sanitize(q)}")

# ══════════════════════════════════════════════════════════════════════════════
#  TOOLS — PASSWORD ATTACKS
# ══════════════════════════════════════════════════════════════════════════════

def tool_cupp():
    info("CUPP \u2014 Common User Passwords Profiler.")
    run("git clone https://github.com/Mebus/cupp.git --quiet 2>/dev/null || true")
    run("python3 cupp/cupp.py -i")

def tool_ncrack():
    info("Ncrack \u2014 High-speed network authentication cracker.")
    confirm("Install Ncrack?") and run("sudo apt-get install -y ncrack")
    t = sanitize(ask("Target  e.g. ssh://192.168.1.1"))
    if t: run(f"ncrack {t}")

def tool_hydra():
    info("Hydra \u2014 Fast online password cracker.")
    confirm("Install Hydra?") and run("sudo apt-get install -y hydra")
    info("Example: -l admin -P wordlist.txt ssh://192.168.1.1", C.DIM)
    args = ask("Hydra arguments")
    if args: run(f"hydra {args}")

def tool_hashcat():
    info("Hashcat \u2014 World\u2019s fastest GPU password cracker.")
    confirm("Install Hashcat?") and run("sudo apt-get install -y hashcat")
    info("Example: -m 0 hash.txt wordlist.txt", C.DIM)
    args = ask("Hashcat arguments")
    if args: run(f"hashcat {args}")

def tool_john():
    info("John the Ripper \u2014 Classic password cracker.")
    confirm("Install John?") and run("sudo apt-get install -y john")
    f = sanitize(ask("Hash file path"))
    w = sanitize(ask("Wordlist path (blank = default)"))
    if f: run(f"john {f}" + (f" --wordlist={w}" if w else ""))

def tool_crunch():
    info("Crunch \u2014 Custom wordlist generator.")
    confirm("Install Crunch?") and run("sudo apt-get install -y crunch")
    mn  = sanitize(ask("Min length"))
    mx  = sanitize(ask("Max length"))
    cs  = sanitize(ask("Charset (e.g. abc123)"))
    out = sanitize(ask("Output file"))
    if mn and mx and cs and out:
        run(f"crunch {mn} {mx} {cs} -o {out}")

# ══════════════════════════════════════════════════════════════════════════════
#  TOOLS — WIRELESS TESTING
# ══════════════════════════════════════════════════════════════════════════════

def tool_reaver():
    info("Reaver \u2014 WPA/WPA2 WPS PIN brute-force.")
    if confirm("Install Reaver & dependencies?"):
        run("sudo apt-get install -y reaver pixiewps aircrack-ng")

def tool_pixiewps():
    info("Pixiewps \u2014 Offline WPS pixie-dust attack.")
    confirm("Install Pixiewps?") and run("sudo apt-get install -y pixiewps")

def tool_fluxion():
    info("Fluxion \u2014 Evil-twin Wi-Fi attack / WPA capture.")
    if confirm("Clone Fluxion?"):
        run("git clone https://github.com/FluxionNetwork/fluxion.git --quiet 2>/dev/null || true")
        run("cd fluxion/install && sudo chmod +x install.sh && sudo ./install.sh")
    run("cd fluxion && sudo ./fluxion.sh")

def tool_aircrack():
    info("Aircrack-ng \u2014 802.11 WEP/WPA/WPA2 cracking suite.")
    confirm("Install Aircrack-ng?") and run("sudo apt-get install -y aircrack-ng")
    iface = sanitize(ask("Wireless interface (e.g. wlan0)"))
    if iface: run(f"sudo airmon-ng start {iface}")

def tool_wifite():
    info("Wifite2 \u2014 Automated wireless attack tool.")
    confirm("Install Wifite?") and run("sudo apt-get install -y wifite")
    run("sudo wifite")

# ══════════════════════════════════════════════════════════════════════════════
#  TOOLS — EXPLOITATION
# ══════════════════════════════════════════════════════════════════════════════

def tool_sqlmap():
    info("SQLmap \u2014 Automatic SQL injection & DB takeover.")
    run("git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev --quiet 2>/dev/null || true")
    target = sanitize(ask("Target URL (e.g. http://site.com/page?id=1)"))
    if not target: return
    extra = ask("Extra flags (blank = --batch)")
    run(f"python3 sqlmap-dev/sqlmap.py -u {target} {extra or '--batch'}")

def tool_atscan():
    info("ATScan \u2014 Advanced dork + vuln scanner.")
    if confirm("Clone ATScan?"):
        run("git clone https://github.com/AlisamTechnology/ATSCAN.git --quiet 2>/dev/null || true")
    run("cd ATSCAN && perl atscan.pl")

def tool_shellnoob():
    info("ShellNoob \u2014 Shellcode writing & conversion toolkit.")
    if confirm("Clone & install ShellNoob?"):
        run("git clone https://github.com/reyammer/shellnoob.git --quiet 2>/dev/null || true")
        run("cd shellnoob && sudo python3 shellnoob.py --install")

def tool_commix():
    info("Commix \u2014 Automated OS command injection.")
    run("git clone https://github.com/commixproject/commix.git --quiet 2>/dev/null || true")
    args = ask("Args (e.g. --url http://target.com/page?id=1)")
    if args: run(f"python3 commix/commix.py {args}")

def tool_jboss():
    info("JBoss-autopwn \u2014 Deploy JSP shell on JBoss AS.")
    info("Usage after clone: ./e.sh <ip> <port>", C.YELLOW)
    if confirm("Clone jboss-autopwn?"):
        run("git clone https://github.com/SpiderLabs/jboss-autopwn.git --quiet 2>/dev/null || true")

def tool_metasploit():
    info("Metasploit Framework \u2014 Industry-standard exploitation.")
    confirm("Launch msfconsole?") and run("msfconsole")

def tool_beef():
    info("BeEF \u2014 Browser Exploitation Framework.")
    confirm("Install BeEF?") and run("sudo apt-get install -y beef-xss")
    run("sudo beef-xss")

# ══════════════════════════════════════════════════════════════════════════════
#  TOOLS — SNIFFING & SPOOFING
# ══════════════════════════════════════════════════════════════════════════════

def tool_sslstrip():
    info("SSLstrip \u2014 MITM SSL stripping attack.")
    if confirm("Clone & install SSLstrip?"):
        run("git clone https://github.com/moxie0/sslstrip.git --quiet 2>/dev/null || true")
        run("sudo apt-get install -y python3-twisted")
        run("cd sslstrip && sudo python3 setup.py install")

def tool_wireshark():
    info("Wireshark \u2014 Graphical packet analyser.")
    confirm("Install Wireshark?") and run("sudo apt-get install -y wireshark")
    run("sudo wireshark &")

def tool_ettercap():
    info("Ettercap \u2014 Comprehensive MITM suite.")
    confirm("Install Ettercap?") and run("sudo apt-get install -y ettercap-graphical")
    run("sudo ettercap -G &")

def tool_bettercap():
    info("Bettercap \u2014 Swiss army knife for network attacks.")
    confirm("Install Bettercap?") and run("sudo apt-get install -y bettercap")
    run("sudo bettercap")

def tool_tcpdump():
    info("tcpdump \u2014 CLI packet capture.")
    confirm("Install tcpdump?") and run("sudo apt-get install -y tcpdump")
    iface = sanitize(ask("Interface (blank = default)"))
    filt  = ask("Filter (e.g. port 80, blank = none)")
    out   = sanitize(ask("Save to file? (blank = print to screen)"))
    cmd   = "sudo tcpdump"
    if iface: cmd += f" -i {iface}"
    if filt:  cmd += f" {filt}"
    if out:   cmd += f" -w {out}"
    run(cmd)

def tool_arpspoof():
    info("arpspoof \u2014 ARP cache poisoning / MITM.")
    confirm("Install dsniff (provides arpspoof)?") and run("sudo apt-get install -y dsniff")
    iface = sanitize(ask("Interface (e.g. eth0)"))
    tgt   = sanitize(ask("Target IP"))
    gw    = sanitize(ask("Gateway IP"))
    if iface and tgt and gw:
        print(f"\n  {C.DIM}Open two terminals and run:{C.RESET}")
        print(f"    sudo arpspoof -i {iface} -t {tgt} {gw}")
        print(f"    sudo arpspoof -i {iface} -t {gw} {tgt}")

# ══════════════════════════════════════════════════════════════════════════════
#  TOOLS — WEB HACKING
# ══════════════════════════════════════════════════════════════════════════════

def tool_wpscan():
    info("WPScan \u2014 WordPress vulnerability scanner.")
    if confirm("Install WPScan?"):
        run("sudo apt-get install -y ruby && sudo gem install wpscan")
    target = sanitize(ask("WordPress URL"))
    if target: run(f"wpscan --url {target} --enumerate u,p,t")

def tool_nikto():
    info("Nikto \u2014 Web server misconfiguration & vuln scanner.")
    confirm("Install Nikto?") and run("sudo apt-get install -y nikto")
    target = sanitize(ask("Target URL"))
    if target: run(f"nikto -h {target}")

def tool_whatweb():
    info("WhatWeb \u2014 Web technology fingerprinting.")
    confirm("Install WhatWeb?") and run("sudo apt-get install -y whatweb")
    target = sanitize(ask("Target URL (e.g. http://target.com)"))
    if not target: return
    aggr = ask("Aggression level 1-4 (blank = 1)")
    safe_aggr = aggr if aggr and aggr.isdigit() and aggr in "1234" else "1"
    run(f"whatweb {target} -a {safe_aggr}")

def tool_dirsearch():
    info("Dirsearch \u2014 Web path brute-forcer.")
    run("git clone https://github.com/maurosoria/dirsearch.git --quiet 2>/dev/null || true")
    target = sanitize(ask("Target URL"))
    if not target: return
    exts = ask("Extensions (blank = php,html,js,txt)")
    safe_exts = sanitize(exts) if exts else "php,html,js,txt"
    run(f"python3 dirsearch/dirsearch.py -u {target} -e {safe_exts}")

def tool_feroxbuster():
    info("Feroxbuster \u2014 Fast, recursive content discovery tool.")
    if confirm("Install Feroxbuster?"):
        run("sudo apt-get install -y feroxbuster 2>/dev/null || "
            "curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/main/install-nix.sh "
            "| sudo bash -s /usr/local/bin")
    target = sanitize(ask("Target URL"))
    if not target: return
    wl = sanitize(ask("Wordlist (blank = /usr/share/seclists/Discovery/Web-Content/common.txt)"))
    safe_wl = wl if wl else "/usr/share/seclists/Discovery/Web-Content/common.txt"
    run(f"feroxbuster --url {target} --wordlist {safe_wl} --auto-bail")

def tool_gobuster():
    info("Gobuster \u2014 Fast directory/DNS/vhost brute-forcer.")
    confirm("Install Gobuster?") and run("sudo apt-get install -y gobuster")
    target = sanitize(ask("Target URL"))
    wl     = sanitize(ask("Wordlist (blank = /usr/share/wordlists/dirb/common.txt)"))
    mode   = ask("Mode (dir/dns/vhost, blank = dir)")
    if target:
        safe_wl   = wl   if wl   else "/usr/share/wordlists/dirb/common.txt"
        safe_mode = mode if mode in ("dir", "dns", "vhost") else "dir"
        run(f"gobuster {safe_mode} -u {target} -w {safe_wl}")

def tool_burpsuite():
    info("Burp Suite \u2014 Web application security testing platform.")
    info("Community edition: https://portswigger.net/burp/communitydownload", C.YELLOW)
    confirm("Launch Burp Suite?") and run("burpsuite &")

def tool_xsser():
    info("XSSer \u2014 Automated XSS testing framework.")
    confirm("Install XSSer?") and run("sudo apt-get install -y xsser")
    target = sanitize(ask("Target URL"))
    if target: run(f"xsser --url {target}")

def tool_shellfinder():
    import urllib.request, urllib.parse, ssl
    dirs = ['/uploads/', '/upload/', '/files/', '/documents/', '/docs/',
            '/pictures/', '/pics/', '/photos/', '/admin/upload/',
            '/users/', '/tmp/', '/data/', '/assets/uploads/']
    shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php',
              'sh.php', 'x.php', 'up.php', 'cmd.php', 'c99.php', 'r57.php']
    target = ask("Target URL (e.g. http://target.com)").rstrip("/")
    if not target: return
    ctx = ssl.create_default_context()
    found_dirs, found_shells = [], []
    print(); info("Scanning upload directories\u2026")
    for d in dirs:
        try:
            code = urllib.request.urlopen(target + d, timeout=5, context=ctx).getcode()
            if code in (200, 403):
                ok(f"{target+d}  [{code}]"); found_dirs.append(target + d)
        except Exception:
            pass
    if found_dirs:
        info("Checking for web shells\u2026")
        for d in found_dirs:
            for s in shells:
                try:
                    if urllib.request.urlopen(d + s, timeout=5, context=ctx).getcode() == 200:
                        ok(f"{C.RED}Shell:{C.RESET} {d+s}"); found_shells.append(d + s)
                except Exception:
                    pass
    print()
    info(f"Dirs: {len(found_dirs)}  |  Shells: {C.RED}{len(found_shells)}{C.RESET}")

# ══════════════════════════════════════════════════════════════════════════════
#  TOOLS — POST EXPLOITATION
# ══════════════════════════════════════════════════════════════════════════════

def tool_weeman():
    info("Weeman \u2014 HTTP server for phishing attacks.")
    if confirm("Clone & run Weeman?"):
        run("git clone https://github.com/evait-security/weeman.git --quiet 2>/dev/null || true")
        run("python3 weeman/weeman.py")

def tool_poet():
    info("POET \u2014 Simple persistent post-exploitation tool.")
    if confirm("Clone POET?"):
        run("git clone https://github.com/mossberg/poet.git --quiet 2>/dev/null || true")
        run("python3 poet/server.py")

def tool_msfvenom():
    info("msfvenom \u2014 Metasploit payload generator & encoder.")
    info("Example: -p linux/x86/meterpreter/reverse_tcp LHOST=<IP> LPORT=4444 -f elf > shell.elf", C.DIM)
    args = ask("msfvenom arguments")
    if args: run(f"msfvenom {args}")

def tool_linenum():
    info("LinEnum \u2014 Linux privilege escalation enumeration.")
    run("git clone https://github.com/rebootuser/LinEnum.git --quiet 2>/dev/null || true")
    run("chmod +x LinEnum/LinEnum.sh && bash LinEnum/LinEnum.sh")

def tool_pspy():
    info("pspy \u2014 Monitor Linux processes without root.")
    arch = ask("Architecture (64 / 32, blank = 64)")
    bit  = "32" if arch == "32" else "64"
    run(f"wget -q https://github.com/DominicBreuker/pspy/releases/latest/download/pspy{bit} "
        f"-O pspy && chmod +x pspy && ./pspy")

def tool_mimikatz():
    info("Mimikatz \u2014 Windows credential extraction.")
    info("Run on Windows pivot or via Wine.", C.YELLOW)
    if confirm("Clone Mimikatz?"):
        run("git clone https://github.com/gentilkiwi/mimikatz.git --quiet 2>/dev/null || true")
        ok("Done. Use pre-built binaries from the /releases page.")

def tool_empire():
    info("Empire \u2014 PowerShell post-exploitation C2 framework.")
    if confirm("Clone Empire?"):
        run("git clone https://github.com/EmpireProject/Empire.git --quiet 2>/dev/null || true")
        run("cd Empire && sudo bash setup/install.sh")

# ══════════════════════════════════════════════════════════════════════════════
#  MENU DEFINITIONS
# ══════════════════════════════════════════════════════════════════════════════

MENU_INFO = {
    "title": "Information Gathering", "colour": C.CYAN,
    "items": [
        ("1",  "Nmap          \u2013 Network scanner",          tool_nmap),
        ("2",  "Masscan       \u2013 Ultra-fast port scanner",  tool_masscan),
        ("3",  "Port Scan     \u2013 Quick open-port scan",     tool_ports),
        ("4",  "Host \u2192 IP    \u2013 DNS resolve",              tool_host_to_ip),
        ("5",  "Whois         \u2013 Domain/IP lookup",         tool_whois),
        ("6",  "DNSenum       \u2013 DNS enumeration",          tool_dnsenum),
        ("7",  "Sublist3r     \u2013 Subdomain finder",         tool_sublist3r),
        ("8",  "theHarvester  \u2013 OSINT harvester",          tool_theharvester),
        ("9",  "SET           \u2013 Social-Engineer Toolkit",  tool_setoolkit),
        ("10", "XSStrike      \u2013 XSS detector",             tool_xsstrike),
        ("11", "Doork         \u2013 Google dork auditor",      tool_doork),
        ("12", "CMSmap        \u2013 CMS vuln scanner",         tool_cmsmap),
        ("13", "Scan Users    \u2013 CMS user enum",            tool_scan_users),
        ("14", "Shodan        \u2013 IoT/internet search",      tool_shodan),
        ("15", "Crips         \u2013 IP tools",                 tool_crips),
    ],
}

MENU_PASSWD = {
    "title": "Password Attacks", "colour": C.YELLOW,
    "items": [
        ("1", "CUPP    \u2013 Custom wordlist generator",  tool_cupp),
        ("2", "Ncrack  \u2013 Network auth cracker",      tool_ncrack),
        ("3", "Hydra   \u2013 Online password cracker",   tool_hydra),
        ("4", "Hashcat \u2013 GPU hash cracker",          tool_hashcat),
        ("5", "John    \u2013 John the Ripper",           tool_john),
        ("6", "Crunch  \u2013 Wordlist generator",        tool_crunch),
    ],
}

MENU_WIRELESS = {
    "title": "Wireless Testing", "colour": C.GREEN,
    "items": [
        ("1", "Reaver      \u2013 WPS brute-force",       tool_reaver),
        ("2", "Pixiewps    \u2013 Pixie-dust attack",     tool_pixiewps),
        ("3", "Fluxion     \u2013 Evil-twin attack",      tool_fluxion),
        ("4", "Aircrack-ng \u2013 WEP/WPA cracking",     tool_aircrack),
        ("5", "Wifite2     \u2013 Automated Wi-Fi tool",  tool_wifite),
    ],
}

MENU_EXPLOIT = {
    "title": "Exploitation Tools", "colour": C.RED,
    "items": [
        ("1", "SQLmap      \u2013 SQL injection tool",         tool_sqlmap),
        ("2", "ATScan      \u2013 Dork + vuln scanner",       tool_atscan),
        ("3", "ShellNoob   \u2013 Shellcode toolkit",         tool_shellnoob),
        ("4", "Commix      \u2013 Command injection",         tool_commix),
        ("5", "JBoss-autopwn",                                tool_jboss),
        ("6", "Metasploit  \u2013 Exploitation framework",    tool_metasploit),
        ("7", "BeEF        \u2013 Browser exploit framework", tool_beef),
    ],
}

MENU_SNIFF = {
    "title": "Sniffing & Spoofing", "colour": C.BLUE,
    "items": [
        ("1", "SSLstrip  \u2013 MITM SSL stripper",    tool_sslstrip),
        ("2", "Wireshark \u2013 Packet analyser",      tool_wireshark),
        ("3", "Ettercap  \u2013 MITM framework",       tool_ettercap),
        ("4", "Bettercap \u2013 Network attack kit",   tool_bettercap),
        ("5", "tcpdump   \u2013 CLI packet capture",   tool_tcpdump),
        ("6", "arpspoof  \u2013 ARP cache poisoning",  tool_arpspoof),
    ],
}

MENU_WEB = {
    "title": "Web Hacking", "colour": C.MAGENTA,
    "items": [
        ("1",  "WPScan       \u2013 WordPress scanner",       tool_wpscan),
        ("2",  "Nikto        \u2013 Web server scanner",      tool_nikto),
        ("3",  "WhatWeb      \u2013 Tech fingerprinting",     tool_whatweb),
        ("4",  "Dirsearch    \u2013 Directory brute-force",   tool_dirsearch),
        ("5",  "Feroxbuster  \u2013 Recursive dir fuzzer",    tool_feroxbuster),
        ("6",  "Gobuster     \u2013 Fast dir/dns buster",     tool_gobuster),
        ("7",  "Burp Suite   \u2013 Web proxy/scanner",       tool_burpsuite),
        ("8",  "XSSer        \u2013 XSS framework",           tool_xsser),
        ("9",  "SQLmap       \u2013 SQL injection",           tool_sqlmap),
        ("10", "Shell Finder \u2013 Upload dir scanner",      tool_shellfinder),
    ],
}

MENU_POST = {
    "title": "Post Exploitation", "colour": C.RED,
    "items": [
        ("1", "Shell Finder \u2013 Find uploaded shells",    tool_shellfinder),
        ("2", "POET         \u2013 Persistent reverse shell", tool_poet),
        ("3", "Weeman       \u2013 Phishing HTTP server",    tool_weeman),
        ("4", "msfvenom     \u2013 Payload generator",       tool_msfvenom),
        ("5", "LinEnum      \u2013 Linux privesc enum",      tool_linenum),
        ("6", "pspy         \u2013 Process monitor",         tool_pspy),
        ("7", "Mimikatz     \u2013 Windows credentials",     tool_mimikatz),
        ("8", "Empire       \u2013 PowerShell C2",           tool_empire),
    ],
}

MAIN_ITEMS = [
    ("1", "Information Gathering",  MENU_INFO),
    ("2", "Password Attacks",       MENU_PASSWD),
    ("3", "Wireless Testing",       MENU_WIRELESS),
    ("4", "Exploitation Tools",     MENU_EXPLOIT),
    ("5", "Sniffing & Spoofing",    MENU_SNIFF),
    ("6", "Web Hacking",            MENU_WEB),
    ("7", "Post Exploitation",      MENU_POST),
]

MAIN_COLOURS = [C.CYAN, C.YELLOW, C.GREEN, C.RED, C.BLUE, C.MAGENTA, C.RED]

# ══════════════════════════════════════════════════════════════════════════════
#  MENU RENDERING
# ══════════════════════════════════════════════════════════════════════════════

def show_submenu(menu_def):
    while True:
        clr()
        banner()
        c = menu_def["colour"]
        separator(menu_def["title"])
        for key, label, _ in menu_def["items"]:
            print(f"  {c}{C.BOLD}[{key:>2}]{C.RESET}  {label}")
        print(f"\n  {C.DIM}[99]{C.RESET}  \u2190 Back to main menu\n")

        ch = prompt(f"sneech/{menu_def['title'].split()[0].lower()}")
        if ch in ("99", ""):
            return

        matched = False
        for key, _, fn in menu_def["items"]:
            if ch == key:
                matched = True
                clr(); banner(); separator(menu_def["title"]); print()
                fn()
                pause()
                break

        if not matched:
            err(f"Invalid option \u2014 choose 1\u2013{len(menu_def['items'])} or 99.")
            time.sleep(1)

def show_main_menu(update_available=False):
    clr()
    banner(update_available)
    # Skip root warning on Termux — non-root is expected there
    if not IS_TERMUX and os.geteuid() != 0:
        warn(f"{C.BOLD}Not running as root \u2014 some tools may fail.{C.RESET}")
        print()
    separator("Main Menu")
    for i, (key, label, _) in enumerate(MAIN_ITEMS):
        col = MAIN_COLOURS[i % len(MAIN_COLOURS)]
        print(f"  {col}{C.BOLD}[{key}]{C.RESET}  {label}")
    print()
    upd_col = C.YELLOW if update_available else C.DIM
    upd_tag = f"  {C.YELLOW}{C.BOLD}\u2605 NEW VERSION{C.RESET}" if update_available else ""
    print(f"  {upd_col}{C.BOLD}[0]{C.RESET}  Update SNEECH{upd_tag}")
    print(f"  {C.DIM}[99]{C.RESET}  Exit\n")

# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

def main():
    if sys.version_info < (3, 6):
        print(f"SNEECH requires Python 3.6+  "
              f"(current: {sys.version_info.major}.{sys.version_info.minor})")
        sys.exit(1)

    # Silent startup update check — failure is non-fatal
    update_available = False
    try:
        update_available = tool_check_updates()
    except Exception:
        pass

    while True:
        show_main_menu(update_available)
        ch = prompt()

        if ch == "99":
            clr()
            print(f"\n  {C.CYAN}[*]{C.RESET} Thanks for using SNEECH. Stay ethical.\n")
            sys.exit(0)

        if ch == "0":
            clr(); tool_update(); pause()
            try:
                update_available = tool_check_updates()
            except Exception:
                update_available = False
            continue

        if ch == "":
            continue

        matched = False
        for key, _, menu_def in MAIN_ITEMS:
            if ch == key:
                matched = True
                show_submenu(menu_def)
                break

        if not matched:
            err("Invalid option \u2014 choose 0\u20137 or 99.")
            time.sleep(1)

if __name__ == "__main__":
    main()
