# Daily Mood Journal

## Setup
```bash
python3 -m venv ./venv/
# bash
source ./venv/bin/activate
# or fish
source ./venv/bin/activate.fish
pip install -r ./requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata ./base_data.json
python manage.py runserver
# of use F5 in visual studio code.
```