#!/usr/bin/env bash
# SNEECH Uninstaller
RED='\033[91m'; GREEN='\033[92m'; YELLOW='\033[93m'; CYAN='\033[96m'; BOLD='\033[1m'; NC='\033[0m'

IS_TERMUX=false
[ "$PREFIX" = "/data/data/com.termux/files/usr" ] && IS_TERMUX=true

if [ "$IS_TERMUX" = true ]; then
    INSTALL_DIR="$PREFIX/share/sneech"; BIN_DIR="$PREFIX/bin"
else
    INSTALL_DIR="/opt/sneech"; BIN_DIR="/usr/local/bin"
fi

echo -e "\n  ${RED}${BOLD}SNEECH Uninstaller${NC}\n"
echo -e "  ${YELLOW}[!]${NC} This will remove:"
echo -e "      $INSTALL_DIR"
echo -e "      $BIN_DIR/sneech"
echo ""
read -rp "  Continue? [y/N]: " ans
[[ "$ans" =~ ^[Yy]$ ]] || { echo "  Cancelled."; exit 0; }

[ -d "$INSTALL_DIR" ] && rm -rf "$INSTALL_DIR" && echo -e "  ${GREEN}[+]${NC} Removed $INSTALL_DIR"
[ -f "$BIN_DIR/sneech" ] && rm -f "$BIN_DIR/sneech" && echo -e "  ${GREEN}[+]${NC} Removed $BIN_DIR/sneech"
echo -e "\n  ${GREEN}[OK]${NC} SNEECH uninstalled.\n"
