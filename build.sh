set -o errexit  # exit on error

pip install -r requirements.txt


python manage.py migrate