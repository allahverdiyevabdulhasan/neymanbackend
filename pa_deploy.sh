#!/bin/bash
# Run this on PythonAnywhere Bash console (adjust python version if needed)

REPO_URL="https://github.com/allahverdiyevabdulhasan/neymanbackend.git"
PROJECT_DIR="neymanbackend"

# Clone repo (skip if already cloned)
if [ ! -d "$PROJECT_DIR" ]; then
  git clone "$REPO_URL"
fi

cd "$PROJECT_DIR" || exit 1

# create venv if missing
if [ ! -d "venv" ]; then
  python3.11 -m venv venv || python3 -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

# You can either export env vars here for quick testing, or set them in the Web tab
# export DJANGO_SECRET_KEY='your-secret'
# export DJANGO_DEBUG=False
# export DJANGO_ALLOWED_HOSTS='yourusername.pythonanywhere.com'

python manage.py migrate
python manage.py collectstatic --noinput

echo "Deployment steps completed. If you haven't, set environment variables in the Web tab and edit the WSGI file as instructed in PA_WSGI_SNIPPET.txt"
