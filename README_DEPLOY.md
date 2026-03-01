# Deploying to PythonAnywhere

Quick steps to deploy this Django project to PythonAnywhere.

1. Push your repo to GitHub (or upload/zip and put on PythonAnywhere).

2. On PythonAnywhere console:

```bash
# clone
git clone https://github.com/USERNAME/REPO.git
cd REPO

# create virtualenv (choose python version available on PythonAnywhere)
python3.11 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

# set environment variables on the Web tab or via bash export for testing
export DJANGO_SECRET_KEY='your-secret'
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS='yourusername.pythonanywhere.com'

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

3. PythonAnywhere Web tab configuration
- Source code: `/home/YOUR_PYTHONANYWHERE_USERNAME/REPO`
- Virtualenv: `/home/YOUR_PYTHONANYWHERE_USERNAME/REPO/venv`
- WSGI file: ensure `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')` and project path are added.
- Static files mapping: `/static/` -> `/home/.../REPO/staticfiles`
- Media files mapping: `/media/` -> `/home/.../REPO/media`
- Add environment variables under the Web tab (or in a `.env` and load them securely).

Notes:
- `db.sqlite3` works on PythonAnywhere for small projects but consider PostgreSQL for production.
- Make sure `DJANGO_DEBUG=False` in production.
