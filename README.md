# SNEECH — All-in-One Pentesting Framework

```
  ____  _   _ _____  _____ ____ _   _
 / ___|| \ | | ____|| ____/ ___| | | |
 \___ \|  \| |  _|  |  _|| |   | |_| |
  ___) | |\  | |___ | |__| |___|  _  |
 |____/|_| \_|_____|_____\___|_| |_|

  All-in-One Pentesting Framework v2.2
```

> **For educational and authorised security testing only.**

---

## Quick Start

```bash
git clone https://github.com/Kaztral-ar/sneech.git
cd sneech
chmod +x install.sh
sudo ./install.sh
sneech
```

**Termux (Android):**
```bash
pkg install git python
git clone https://github.com/Kaztral-ar/sneech.git
cd sneech && ./install.sh
sneech
```

**Without installing:**
```bash
python3 sneech.py
```

---

## Tools

| # | Category | Tools |
|---|---|---|
| 1 | Information Gathering | Nmap, Masscan, Port Scan, Host→IP, Whois, DNSenum, Sublist3r, theHarvester, SET, XSStrike, Doork, CMSmap, User Scan, Shodan, Crips |
| 2 | Password Attacks | CUPP, Ncrack, Hydra, Hashcat, John, Crunch |
| 3 | Wireless Testing | Reaver, Pixiewps, Fluxion, Aircrack-ng, Wifite2 |
| 4 | Exploitation | SQLmap, ATScan, ShellNoob, Commix, JBoss-autopwn, Metasploit, BeEF |
| 5 | Sniffing & Spoofing | SSLstrip, Wireshark, Ettercap, Bettercap, tcpdump, arpspoof |
| 6 | Web Hacking | WPScan, Nikto, WhatWeb, Dirsearch, Feroxbuster, Gobuster, Burp Suite, XSSer, SQLmap, Shell Finder |
| 7 | Post Exploitation | Shell Finder, POET, Weeman, msfvenom, LinEnum, pspy, Mimikatz, Empire |

---

## Auto-Update System

SNEECH checks GitHub for updates every time it starts.

- A **★ banner** appears if a new version is available
- Option **[0]** from the main menu runs the updater
- After pulling, SNEECH shows exactly what changed:
  - New `tool_*` functions added
  - New menu entries added
  - Tools removed
  - Full git commit log
- Offers to **restart automatically** to load new code

### Adding a new tool (for contributors)

1. Add a `def tool_yourname():` function in `sneech.py`
2. Add it to the relevant `MENU_*` dict
3. Commit and push to GitHub

SNEECH will detect the new `tool_*` function on next update and show it in the changelog automatically.

---

## Requirements

- Python 3.6+
- Git
- Root / sudo (recommended for full tool access)

---

## Project Structure

```
sneech/
├── sneech.py          # Main script — all tools + menus
├── install.sh         # Installer (Linux & Termux)
├── uninstall.sh       # Clean removal
├── requirements.txt   # Python deps (minimal)
├── CHANGELOG.md       # Version history
├── README.md          # This file
└── .sneech_state.json # Auto-generated: tracks version & known tools
```

---

## Disclaimer

SNEECH is intended for **legal penetration testing and educational purposes only**.
Always obtain written authorisation before testing any system you do not own.
The author is not responsible for any misuse.

---

## License — MIT

Copyright (c) 2025 SNEECH Project  
https://github.com/Kaztral-ar/sneech
