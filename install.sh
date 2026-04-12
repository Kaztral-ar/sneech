#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
#  SNEECH Installer v2.2
# ─────────────────────────────────────────────────────────────
set -e

RED='\033[91m'; GREEN='\033[92m'; YELLOW='\033[93m'
CYAN='\033[96m'; BOLD='\033[1m'; DIM='\033[2m'; NC='\033[0m'

clear

echo -e "${CYAN}${BOLD}"
echo "  ____  _   _ _____  _____ ____ _   _ "
echo " / ___|| \ | | ____|| ____/ ___| | | |"
echo " \___ \|  \| |  _|  |  _|| |   | |_| |"
echo "  ___) | |\  | |___ | |__| |___|  _  |"
echo " |____/|_| \_|_____|_____|\___|_| |_| "
echo -e "${NC}${DIM}  All-in-One Pentesting Framework v2.2${NC}"
echo ""
echo -e "  ${DIM}────────────────────────────────────────${NC}"
echo ""

IS_TERMUX=false
[ "$PREFIX" = "/data/data/com.termux/files/usr" ] && IS_TERMUX=true

if [ "$IS_TERMUX" = false ] && [ "$EUID" -ne 0 ]; then
    echo -e "  ${YELLOW}[!]${NC} Not running as root — some steps may require sudo."
    echo ""
fi

echo -e "  ${CYAN}[>]${NC} Press ENTER to install, Ctrl+C to abort."
read -r

if [ "$IS_TERMUX" = true ]; then
    INSTALL_DIR="$PREFIX/share/sneech"
    BIN_DIR="$PREFIX/bin"
else
    INSTALL_DIR="/opt/sneech"
    BIN_DIR="/usr/local/bin"
fi

echo -e "  ${GREEN}[+]${NC} Checking Python 3..."
if ! command -v python3 &>/dev/null; then
    echo -e "  ${YELLOW}[!]${NC} Python 3 not found. Installing..."
    if [ "$IS_TERMUX" = true ]; then pkg install -y python
    else apt-get install -y python3 python3-pip 2>/dev/null || true; fi
else
    echo -e "  ${GREEN}[OK]${NC} $(python3 --version)"
fi

echo -e "  ${GREEN}[+]${NC} Checking Git..."
if ! command -v git &>/dev/null; then
    echo -e "  ${YELLOW}[!]${NC} Git not found. Installing..."
    if [ "$IS_TERMUX" = true ]; then pkg install -y git
    else apt-get install -y git 2>/dev/null || true; fi
else
    echo -e "  ${GREEN}[OK]${NC} $(git --version)"
fi

[ -d "$INSTALL_DIR" ] && { echo -e "  ${YELLOW}[!]${NC} Removing old install..."; rm -rf "$INSTALL_DIR"; }
mkdir -p "$INSTALL_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo -e "  ${GREEN}[+]${NC} Copying files to $INSTALL_DIR ..."
cp -r "$SCRIPT_DIR/"* "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/sneech.py"

# Ensure the install directory is a proper git repo pointing at the real remote
if [ -d "$SCRIPT_DIR/.git" ]; then
    # Copy the .git directory so update engine works immediately
    cp -r "$SCRIPT_DIR/.git" "$INSTALL_DIR/"
    git -C "$INSTALL_DIR" remote set-url origin "https://github.com/Kaztral-ar/sneech.git" 2>/dev/null || true
elif ! git -C "$INSTALL_DIR" rev-parse --is-inside-work-tree &>/dev/null; then
    echo -e "  ${YELLOW}[!]${NC} Initialising git repo for update support..."
    git -C "$INSTALL_DIR" init -q
    git -C "$INSTALL_DIR" remote add origin "https://github.com/Kaztral-ar/sneech.git"
fi

echo -e "  ${GREEN}[+]${NC} Creating launcher at $BIN_DIR/sneech ..."
mkdir -p "$BIN_DIR"
printf '#!/usr/bin/env bash\nexec python3 "%s/sneech.py" "$@"\n' "$INSTALL_DIR" > "$BIN_DIR/sneech"
chmod +x "$BIN_DIR/sneech"

COMMIT=$(git -C "$INSTALL_DIR" rev-parse --short HEAD 2>/dev/null || echo "unknown")
python3 - << PYEOF
import json
state = {'version': '2.2', 'last_commit': '$COMMIT', 'known_tools': []}
with open('$INSTALL_DIR/.sneech_state.json', 'w') as f:
    json.dump(state, f, indent=2)
print('  \033[92m[+]\033[0m State file initialised.')
PYEOF

echo ""
echo -e "  ${DIM}────────────────────────────────────────${NC}"
echo -e "  ${GREEN}${BOLD}[OK] Installation complete!${NC}"
echo ""
echo -e "  Run:     ${CYAN}${BOLD}sneech${NC}"
echo -e "  Update:  press ${BOLD}[0]${NC} from the main menu"
echo ""
echo -e "  ${DIM}For authorised pentesting and education only.${NC}"
echo ""
