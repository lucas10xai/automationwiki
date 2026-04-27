#!/usr/bin/env bash
# ============================================================
# deploy.sh — 10XAI Digital Garden Deploy Script
# Dùng trên máy local (Mac) để commit và push lên GitHub
# ============================================================
set -euo pipefail

# ---------- Màu sắc output ----------
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m' # No Color

log()  { echo -e "${CYAN}[10XAI]${NC} $1"; }
ok()   { echo -e "${GREEN}[✓]${NC} $1"; }
warn() { echo -e "${YELLOW}[!]${NC} $1"; }
err()  { echo -e "${RED}[✗]${NC} $1"; exit 1; }

# ---------- Config ----------
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GITHUB_REMOTE="origin"
BRANCH="v4"
COMMIT_MSG="${1:-"chore: sync vault content $(date '+%Y-%m-%d %H:%M')"}"

# ---------- Bước 1: Kiểm tra git ----------
log "Kiểm tra trạng thái repository..."
cd "$REPO_ROOT"

if ! git rev-parse --git-dir > /dev/null 2>&1; then
  err "Không phải git repository! Hãy chạy từ thư mục my-digital-garden."
fi

# ---------- Bước 2: Thêm toàn bộ thay đổi ----------
log "Staging các thay đổi..."
git add -A

if git diff --cached --quiet; then
  warn "Không có thay đổi mới. Bỏ qua commit."
else
  git commit -m "$COMMIT_MSG"
  ok "Đã commit: $COMMIT_MSG"
fi

# ---------- Bước 3: Push lên GitHub ----------
log "Đẩy code lên GitHub (${GITHUB_REMOTE}/${BRANCH})..."
git push "$GITHUB_REMOTE" "$BRANCH"
ok "Push thành công!"

# ---------- Bước 4: Trigger deploy trên VPS ----------
VPS_HOST="${VPS_HOST:-}"  # Đặt biến môi trường VPS_HOST trước khi chạy

if [[ -n "$VPS_HOST" ]]; then
  log "Kết nối VPS và deploy..."
  ssh "$VPS_HOST" << 'REMOTE'
    set -e
    cd ~/my-digital-garden
    echo "[VPS] Pulling latest code..."
    git pull origin main
    echo "[VPS] Rebuilding & restarting containers..."
    docker compose pull cloudflared 2>/dev/null || true
    docker compose up -d --build --remove-orphans
    echo "[VPS] Deploy hoàn tất!"
    docker compose ps
REMOTE
  ok "VPS deploy thành công! Site: https://notes.10xai.top"
else
  warn "Biến VPS_HOST chưa được đặt."
  echo ""
  echo "  Để auto-deploy lên VPS, chạy lệnh:"
  echo -e "  ${YELLOW}VPS_HOST=user@your-vps-ip ./deploy.sh${NC}"
  echo ""
  echo "  Hoặc SSH thủ công vào VPS và chạy:"
  echo -e "  ${YELLOW}cd ~/my-digital-garden && git pull && docker compose up -d --build${NC}"
fi

echo ""
ok "Deploy pipeline hoàn tất!"
