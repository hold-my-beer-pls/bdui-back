#!/usr/bin/env bash
set -e

PROJECT_DIR="/home/user-hack/apps/backend"
cd "$PROJECT_DIR"

echo ">>> Pull latest code"
git fetch --all
git reset --hard origin/main

# Проверяем, есть ли venv, если нет — создаём
if [ ! -d "venv" ]; then
    echo ">>> Creating virtual environment"
    python3 -m venv venv
fi

echo ">>> Activating virtual environment"
source venv/bin/activate

echo ">>> Installing dependencies"
pip install -r requirements.txt

deactivate

echo ">>> Restarting backend service"
sudo systemctl restart backend.service

echo ">>> Deploy finished!"
