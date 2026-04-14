<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SNEECH — All-in-One Pentesting Framework</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Bebas+Neue&family=IBM+Plex+Mono:wght@300;400;600&display=swap" rel="stylesheet">
<style>
  :root {
    --black:   #000000;
    --green:   #00ff41;
    --cyan:    #00d4ff;
    --dim:     #1a1a1a;
    --mid:     #0a0a0a;
    --muted:   #3a3a3a;
    --text:    #c8c8c8;
    --accent:  #ff3c3c;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html { scroll-behavior: smooth; }

  body {
    background: var(--black);
    color: var(--text);
    font-family: 'IBM Plex Mono', monospace;
    overflow-x: hidden;
    cursor: crosshair;
  }

  /* ── scanline overlay ── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,255,65,0.015) 2px,
      rgba(0,255,65,0.015) 4px
    );
    pointer-events: none;
    z-index: 9999;
  }

  /* ── noise grain ── */
  body::after {
    content: '';
    position: fixed;
    inset: -200%;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
    opacity: 0.06;
    pointer-events: none;
    z-index: 9998;
    animation: grain 0.5s steps(1) infinite;
  }

  @keyframes grain {
    0%,100% { transform: translate(0,0); }
    10%      { transform: translate(-2%,-3%); }
    20%      { transform: translate(3%,2%); }
    30%      { transform: translate(-1%,4%); }
    40%      { transform: translate(4%,-1%); }
    50%      { transform: translate(-3%,3%); }
    60%      { transform: translate(2%,-4%); }
    70%      { transform: translate(-4%,1%); }
    80%      { transform: translate(1%,3%); }
    90%      { transform: translate(3%,-2%); }
  }

  /* ── HERO ── */
  .hero {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: clamp(2rem, 8vw, 7rem);
    position: relative;
    border-bottom: 1px solid var(--muted);
    overflow: hidden;
  }

  .hero-bg-grid {
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,255,65,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,255,65,0.03) 1px, transparent 1px);
    background-size: 48px 48px;
    animation: gridpulse 6s ease-in-out infinite;
  }

  @keyframes gridpulse {
    0%,100% { opacity: 0.4; }
    50%      { opacity: 1; }
  }

  .hero-corner {
    position: absolute;
    top: 2rem; right: 2rem;
    font-size: 0.65rem;
    color: var(--muted);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    font-family: 'Share Tech Mono', monospace;
  }

  .hero-corner span {
    color: var(--green);
    animation: blink 1.2s step-end infinite;
  }

  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

  .ascii-logo {
    font-family: 'Share Tech Mono', monospace;
    font-size: clamp(0.5rem, 1.4vw, 0.85rem);
    color: var(--green);
    line-height: 1.15;
    white-space: pre;
    text-shadow: 0 0 20px rgba(0,255,65,0.5);
    animation: fadeup 0.8s ease both;
    position: relative;
    z-index: 1;
  }

  .hero-tagline {
    margin-top: 2rem;
    font-size: clamp(0.7rem, 1.8vw, 1rem);
    color: var(--cyan);
    letter-spacing: 0.3em;
    text-transform: uppercase;
    font-family: 'Share Tech Mono', monospace;
    animation: fadeup 0.8s 0.2s ease both;
    position: relative;
    z-index: 1;
  }

  .hero-desc {
    margin-top: 1.5rem;
    max-width: 56ch;
    font-size: clamp(0.8rem, 1.5vw, 0.95rem);
    line-height: 1.8;
    color: var(--text);
    animation: fadeup 0.8s 0.4s ease both;
    position: relative;
    z-index: 1;
  }

  .hero-cta {
    margin-top: 2.5rem;
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    animation: fadeup 0.8s 0.6s ease both;
    position: relative;
    z-index: 1;
  }

  .btn {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    text-decoration: none;
    padding: 0.75rem 1.75rem;
    border: 1px solid var(--green);
    color: var(--green);
    background: transparent;
    cursor: pointer;
    transition: all 0.2s;
    position: relative;
    overflow: hidden;
  }

  .btn::before {
    content: '';
    position: absolute;
    inset: 0;
    background: var(--green);
    transform: translateX(-101%);
    transition: transform 0.2s;
    z-index: -1;
  }

  .btn:hover { color: var(--black); }
  .btn:hover::before { transform: translateX(0); }

  .btn-ghost {
    border-color: var(--muted);
    color: var(--text);
  }

  .btn-ghost::before { background: var(--muted); }
  .btn-ghost:hover { color: var(--black); }

  /* ── VERSION BADGE ── */
  .v-badge {
    display: inline-block;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    padding: 0.25rem 0.7rem;
    border: 1px solid var(--accent);
    color: var(--accent);
    margin-bottom: 1.5rem;
    animation: fadeup 0.8s ease both;
    position: relative;
    z-index: 1;
  }

  /* ── SECTION BASE ── */
  section {
    padding: clamp(3rem, 8vw, 6rem) clamp(2rem, 8vw, 7rem);
    border-bottom: 1px solid var(--muted);
  }

  .section-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--green);
    margin-bottom: 1rem;
  }

  .section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(2.5rem, 6vw, 5rem);
    letter-spacing: 0.05em;
    color: #fff;
    line-height: 0.95;
    margin-bottom: 2.5rem;
  }

  /* ── STATS BAR ── */
  .stats {
    background: var(--mid);
    border-top: 1px solid var(--muted);
    border-bottom: 1px solid var(--muted);
    padding: 0;
  }

  .stats-inner {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
  }

  .stat {
    padding: 2rem 2.5rem;
    border-right: 1px solid var(--muted);
    opacity: 0;
    animation: fadeup 0.6s ease forwards;
  }

  .stat:last-child { border-right: none; }
  .stat:nth-child(1) { animation-delay: 0.1s; }
  .stat:nth-child(2) { animation-delay: 0.2s; }
  .stat:nth-child(3) { animation-delay: 0.3s; }
  .stat:nth-child(4) { animation-delay: 0.4s; }

  .stat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(2.5rem, 4vw, 3.5rem);
    color: var(--green);
    line-height: 1;
    text-shadow: 0 0 30px rgba(0,255,65,0.3);
  }

  .stat-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: 0.4rem;
    filter: brightness(2);
  }

  /* ── CATEGORIES ── */
  .categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1px;
    background: var(--muted);
    border: 1px solid var(--muted);
    margin-top: 2rem;
  }

  .cat-card {
    background: var(--black);
    padding: 2rem;
    transition: background 0.2s;
    position: relative;
    overflow: hidden;
  }

  .cat-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    background: var(--green);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
  }

  .cat-card:hover { background: var(--dim); }
  .cat-card:hover::after { transform: scaleX(1); }

  .cat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    color: var(--muted);
    line-height: 1;
    filter: brightness(2);
    transition: color 0.2s;
  }

  .cat-card:hover .cat-num { color: var(--green); }

  .cat-name {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    color: #fff;
    margin-top: 0.75rem;
    text-transform: uppercase;
  }

  .cat-desc {
    font-size: 0.75rem;
    color: var(--text);
    margin-top: 0.5rem;
    line-height: 1.6;
    opacity: 0.7;
  }

  .cat-tools {
    margin-top: 1rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }

  .tag {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem;
    padding: 0.2rem 0.5rem;
    border: 1px solid var(--muted);
    color: var(--muted);
    letter-spacing: 0.05em;
    filter: brightness(2);
    transition: all 0.2s;
  }

  .cat-card:hover .tag {
    border-color: rgba(0,255,65,0.3);
    color: rgba(0,255,65,0.6);
  }

  /* ── FEATURES ── */
  .features-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
  }

  .feature {
    border-left: 2px solid var(--green);
    padding-left: 1.5rem;
    opacity: 0;
    animation: fadein 0.5s ease forwards;
  }

  .feature:nth-child(1) { animation-delay: 0.1s; }
  .feature:nth-child(2) { animation-delay: 0.2s; }
  .feature:nth-child(3) { animation-delay: 0.3s; }
  .feature:nth-child(4) { animation-delay: 0.4s; }

  .feature-title {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: var(--green);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
  }

  .feature-body {
    font-size: 0.82rem;
    line-height: 1.75;
    color: var(--text);
    opacity: 0.85;
  }

  /* ── TERMINAL BLOCK ── */
  .terminal-section {
    background: var(--mid);
  }

  .terminal {
    background: #0a0a0a;
    border: 1px solid var(--muted);
    border-radius: 2px;
    overflow: hidden;
    max-width: 700px;
    margin-top: 2rem;
  }

  .terminal-bar {
    background: var(--dim);
    padding: 0.6rem 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    border-bottom: 1px solid var(--muted);
  }

  .dot { width: 10px; height: 10px; border-radius: 50%; }
  .dot-r { background: #ff5f57; }
  .dot-y { background: #febc2e; }
  .dot-g { background: #28c840; }

  .terminal-title {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    color: var(--muted);
    margin-left: 0.5rem;
    filter: brightness(2);
  }

  .terminal-body {
    padding: 1.5rem;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    line-height: 2;
  }

  .t-prompt { color: var(--green); }
  .t-cmd    { color: #fff; }
  .t-out    { color: var(--text); opacity: 0.7; }
  .t-cyan   { color: var(--cyan); }
  .t-dim    { color: var(--muted); filter: brightness(2); }

  /* ── STACK ── */
  .stack-row {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 2rem;
  }

  .stack-item {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    padding: 0.6rem 1.2rem;
    border: 1px solid var(--muted);
    color: var(--text);
    letter-spacing: 0.1em;
    transition: all 0.2s;
  }

  .stack-item:hover {
    border-color: var(--cyan);
    color: var(--cyan);
    box-shadow: 0 0 12px rgba(0,212,255,0.15);
  }

  /* ── FOOTER ── */
  footer {
    padding: 3rem clamp(2rem, 8vw, 7rem);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
  }

  .footer-logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.5rem;
    color: var(--green);
    letter-spacing: 0.1em;
    text-shadow: 0 0 15px rgba(0,255,65,0.3);
  }

  .footer-note {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    color: var(--muted);
    filter: brightness(2);
    letter-spacing: 0.1em;
  }

  .footer-link {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    color: var(--green);
    text-decoration: none;
    letter-spacing: 0.1em;
    opacity: 0.7;
    transition: opacity 0.2s;
  }

  .footer-link:hover { opacity: 1; }

  /* ── DISCLAIMER ── */
  .disclaimer {
    background: rgba(255,60,60,0.04);
    border: 1px solid rgba(255,60,60,0.2);
    padding: 1rem 1.5rem;
    margin-top: 2rem;
    max-width: 700px;
    display: flex;
    gap: 1rem;
    align-items: flex-start;
  }

  .disclaimer-icon {
    font-family: 'Share Tech Mono', monospace;
    color: var(--accent);
    font-size: 0.75rem;
    white-space: nowrap;
    margin-top: 0.1rem;
  }

  .disclaimer-text {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    line-height: 1.7;
    color: var(--text);
    opacity: 0.7;
  }

  /* ── ANIMATIONS ── */
  @keyframes fadeup {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  @keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
  }

  /* ── RESPONSIVE ── */
  @media (max-width: 768px) {
    .stats-inner { grid-template-columns: repeat(2, 1fr); }
    .stat { border-right: none; border-bottom: 1px solid var(--muted); }
    .stat:nth-child(odd) { border-right: 1px solid var(--muted); }
    .stat:last-child { border-bottom: none; }
  }

  @media (max-width: 480px) {
    .stats-inner { grid-template-columns: 1fr 1fr; }
    .ascii-logo { font-size: 0.42rem; }
    footer { flex-direction: column; }
  }
</style>
</head>
<body>

<!-- ═══════════ HERO ═══════════ -->
<section class="hero">
  <div class="hero-bg-grid"></div>
  <div class="hero-corner">STATUS: ACTIVE <span>█</span></div>

  <div class="v-badge">// VERSION 2.2 — STABLE</div>

  <pre class="ascii-logo">
 ____  _   _ _____  _____ ____ _   _
/ ___|| \ | | ____|| ____/ ___| | | |
\___ \|  \| |  _|  |  _|| |   | |_| |
 ___) | |\  | |___ | |__| |___|  _  |
|____/|_| \_|_____|_____\___|_| |_|  </pre>

  <p class="hero-tagline">All-in-One Pentesting Framework</p>

  <p class="hero-desc">
    A terminal-based security toolkit giving ethical hackers and cybersecurity
    students a single interactive menu to discover, install, and launch
    45+ industry-standard offensive security tools.
  </p>

  <div class="hero-cta">
    <a class="btn" href="https://github.com/Kaztral-ar/sneech" target="_blank">
      git clone sneech
    </a>
    <a class="btn btn-ghost" href="#categories">
      explore tools
    </a>
  </div>
</section>

<!-- ═══════════ STATS ═══════════ -->
<div class="stats">
  <div class="stats-inner">
    <div class="stat">
      <div class="stat-num">45+</div>
      <div class="stat-label">Security Tools</div>
    </div>
    <div class="stat">
      <div class="stat-num">7</div>
      <div class="stat-label">Categories</div>
    </div>
    <div class="stat">
      <div class="stat-num">3.6+</div>
      <div class="stat-label">Python Required</div>
    </div>
    <div class="stat">
      <div class="stat-num">2</div>
      <div class="stat-label">Platforms (Linux + Android)</div>
    </div>
  </div>
</div>

<!-- ═══════════ ABOUT ═══════════ -->
<section>
  <div class="section-label">// 00 — Overview</div>
  <h2 class="section-title">What Is<br>SNEECH?</h2>
  <p style="max-width:62ch;font-size:0.9rem;line-height:1.9;color:var(--text);opacity:0.85;">
    SNEECH is an open-source, terminal-based security framework built in pure Python 3.
    It eliminates the need to remember individual tool commands or installation steps —
    instead wrapping the entire pentesting workflow into a single, navigable CLI interface.
    Tools are pulled on-demand via <code style="color:var(--green);font-family:'Share Tech Mono',monospace">git clone</code>
    or the system package manager, keeping the core lean with zero runtime dependencies.
  </p>
  <div class="disclaimer">
    <div class="disclaimer-icon">[!] LEGAL</div>
    <div class="disclaimer-text">
      SNEECH is intended for legal penetration testing and educational purposes only.
      Always obtain written authorisation before testing any system you do not own.
      The author is not responsible for any misuse.
    </div>
  </div>
</section>

<!-- ═══════════ CATEGORIES ═══════════ -->
<section id="categories">
  <div class="section-label">// 01 — Tool Matrix</div>
  <h2 class="section-title">Seven<br>Domains</h2>

  <div class="categories-grid">

    <div class="cat-card">
      <div class="cat-num">01</div>
      <div class="cat-name">Information Gathering</div>
      <div class="cat-desc">Reconnaissance, DNS enumeration, OSINT, and port scanning to map the attack surface.</div>
      <div class="cat-tools">
        <span class="tag">Nmap</span><span class="tag">Masscan</span>
        <span class="tag">Sublist3r</span><span class="tag">theHarvester</span>
        <span class="tag">Shodan</span><span class="tag">Whois</span>
        <span class="tag">DNSenum</span><span class="tag">CMSmap</span>
      </div>
    </div>

    <div class="cat-card">
      <div class="cat-num">02</div>
      <div class="cat-name">Password Attacks</div>
      <div class="cat-desc">Hash cracking, network authentication brute-forcing, and custom wordlist generation.</div>
      <div class="cat-tools">
        <span class="tag">Hydra</span><span class="tag">Hashcat</span>
        <span class="tag">John</span><span class="tag">Ncrack</span>
        <span class="tag">CUPP</span><span class="tag">Crunch</span>
      </div>
    </div>

    <div class="cat-card">
      <div class="cat-num">03</div>
      <div class="cat-name">Wireless Testing</div>
      <div class="cat-desc">WPA/WPA2 cracking, WPS PIN attacks, evil-twin access point generation.</div>
      <div class="cat-tools">
        <span class="tag">Aircrack-ng</span><span class="tag">Reaver</span>
        <span class="tag">Fluxion</span><span class="tag">Wifite2</span>
        <span class="tag">Pixiewps</span>
      </div>
    </div>

    <div class="cat-card">
      <div class="cat-num">04</div>
      <div class="cat-name">Exploitation</div>
      <div class="cat-desc">Automated injection attacks, shellcode tooling, browser exploitation, and framework access.</div>
      <div class="cat-tools">
        <span class="tag">SQLmap</span><span class="tag">Metasploit</span>
        <span class="tag">Commix</span><span class="tag">BeEF</span>
        <span class="tag">ShellNoob</span><span class="tag">ATScan</span>
      </div>
    </div>

    <div class="cat-card">
      <div class="cat-num">05</div>
      <div class="cat-name">Sniffing & Spoofing</div>
      <div class="cat-desc">Man-in-the-middle attacks, SSL stripping, packet capture, and ARP cache poisoning.</div>
      <div class="cat-tools">
        <span class="tag">Bettercap</span><span class="tag">Wireshark</span>
        <span class="tag">Ettercap</span><span class="tag">SSLstrip</span>
        <span class="tag">tcpdump</span><span class="tag">arpspoof</span>
      </div>
    </div>

    <div class="cat-card">
      <div class="cat-num">06</div>
      <div class="cat-name">Web Hacking</div>
      <div class="cat-desc">Directory busting, CMS scanning, XSS frameworks, and web technology fingerprinting.</div>
      <div class="cat-tools">
        <span class="tag">Gobuster</span><span class="tag">Feroxbuster</span>
        <span class="tag">Nikto</span><span class="tag">WPScan</span>
        <span class="tag">WhatWeb</span><span class="tag">Burp Suite</span>
        <span class="tag">Dirsearch</span>
      </div>
    </div>

    <div class="cat-card">
      <div class="cat-num">07</div>
      <div class="cat-name">Post Exploitation</div>
      <div class="cat-desc">Privilege escalation, persistence mechanisms, payload generation, and credential extraction.</div>
      <div class="cat-tools">
        <span class="tag">Mimikatz</span><span class="tag">msfvenom</span>
        <span class="tag">Empire</span><span class="tag">LinEnum</span>
        <span class="tag">pspy</span><span class="tag">POET</span>
      </div>
    </div>

  </div>
</section>

<!-- ═══════════ FEATURES ═══════════ -->
<section style="background:var(--mid);">
  <div class="section-label">// 02 — Core Features</div>
  <h2 class="section-title">Built For<br>Operators</h2>

  <div class="features-list">
    <div class="feature">
      <div class="feature-title">Auto-Update Engine</div>
      <div class="feature-body">
        Checks GitHub on every launch. The ★ banner appears when a new version exists.
        Press [0] to pull changes — SNEECH diffs new tool functions, menu entries,
        and removed tools, then offers an automatic restart.
      </div>
    </div>
    <div class="feature">
      <div class="feature-title">Cross-Platform</div>
      <div class="feature-body">
        Runs natively on Linux and Termux (Android). An <code style="color:var(--green);font-family:'Share Tech Mono',monospace">IS_TERMUX</code> flag
        switches between <code style="color:var(--green);font-family:'Share Tech Mono',monospace">sudo apt-get</code> and
        <code style="color:var(--green);font-family:'Share Tech Mono',monospace">pkg install</code> — no manual config needed.
      </div>
    </div>
    <div class="feature">
      <div class="feature-title">Shell-Safe Inputs</div>
      <div class="feature-body">
        All user-supplied values (targets, IPs, file paths, API keys) are
        sanitized via Python's <code style="color:var(--green);font-family:'Share Tech Mono',monospace">shlex.quote()</code>
        before execution — 39 call sites protected.
      </div>
    </div>
    <div class="feature">
      <div class="feature-title">Zero Runtime Deps</div>
      <div class="feature-body">
        Core runs on Python 3.6+ stdlib only. Individual tools are pulled
        on-demand via <code style="color:var(--green);font-family:'Share Tech Mono',monospace">git clone</code> or the system package manager
        — nothing pre-installed, nothing wasted.
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ TERMINAL QUICKSTART ═══════════ -->
<section class="terminal-section">
  <div class="section-label">// 03 — Quick Start</div>
  <h2 class="section-title">Get<br>Running</h2>

  <div class="terminal">
    <div class="terminal-bar">
      <span class="dot dot-r"></span>
      <span class="dot dot-y"></span>
      <span class="dot dot-g"></span>
      <span class="terminal-title">bash — 80×24</span>
    </div>
    <div class="terminal-body">
      <div><span class="t-prompt">user@kali:~$</span> <span class="t-cmd">git clone https://github.com/Kaztral-ar/sneech.git</span></div>
      <div><span class="t-out">Cloning into 'sneech'...</span></div>
      <div><span class="t-out">remote: Enumerating objects: done.</span></div>
      <div>&nbsp;</div>
      <div><span class="t-prompt">user@kali:~$</span> <span class="t-cmd">cd sneech && sudo ./install.sh</span></div>
      <div><span class="t-out">[+] Checking Python 3... OK (3.11.2)</span></div>
      <div><span class="t-out">[+] Checking Git... OK</span></div>
      <div><span class="t-out">[+] Copying files to /opt/sneech...</span></div>
      <div><span class="t-out">[OK] Installation complete!</span></div>
      <div>&nbsp;</div>
      <div><span class="t-prompt">user@kali:~$</span> <span class="t-cmd">sneech</span></div>
      <div><span class="t-cyan">[*] Checking for updates...</span></div>
      <div><span class="t-dim">  ── Main Menu ──────────────────</span></div>
      <div><span class="t-cmd">[1]</span><span class="t-out">  Information Gathering</span></div>
      <div><span class="t-cmd">[2]</span><span class="t-out">  Password Attacks</span></div>
      <div><span class="t-cmd">[7]</span><span class="t-out">  Post Exploitation</span></div>
      <div><span class="t-prompt">sneech~#</span> <span class="t-cmd">█</span></div>
    </div>
  </div>

  <div style="margin-top:2rem;">
    <div class="section-label" style="margin-bottom:0.75rem;">// Termux (Android)</div>
    <div class="terminal" style="max-width:500px;">
      <div class="terminal-bar">
        <span class="dot dot-r"></span><span class="dot dot-y"></span><span class="dot dot-g"></span>
        <span class="terminal-title">termux</span>
      </div>
      <div class="terminal-body">
        <div><span class="t-prompt">$</span> <span class="t-cmd">pkg install git python</span></div>
        <div><span class="t-prompt">$</span> <span class="t-cmd">git clone https://github.com/Kaztral-ar/sneech.git</span></div>
        <div><span class="t-prompt">$</span> <span class="t-cmd">cd sneech && ./install.sh</span></div>
        <div><span class="t-prompt">$</span> <span class="t-cmd">sneech</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ STACK ═══════════ -->
<section>
  <div class="section-label">// 04 — Stack</div>
  <h2 class="section-title">Built With</h2>
  <div class="stack-row">
    <div class="stack-item">Python 3.6+</div>
    <div class="stack-item">Bash</div>
    <div class="stack-item">Git</div>
    <div class="stack-item">shlex / subprocess</div>
    <div class="stack-item">Linux / Termux</div>
  </div>
</section>

<!-- ═══════════ FOOTER ═══════════ -->
<footer>
  <div class="footer-logo">SNEECH</div>
  <div class="footer-note">© 2025 SNEECH PROJECT — MIT LICENSE</div>
  <a class="footer-link" href="https://github.com/Kaztral-ar/sneech" target="_blank">
    → github.com/Kaztral-ar/sneech
  </a>
</footer>

</body>
</html>

