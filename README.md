# django-encrypt-and-decrypt
django-encrypt_and_decrypt
To setup a local development environment:

Create a virtual environment in which to install Python pip packages. With virtualenv,
virtualenv venv            # create a virtualenv
source venv/bin/activate   # activate the Python virtualenv 

or 
with virtualenvwrapper,

mkvirtualenv -p python3 {{project_name}}   # create and activate environment
workon {{project_name}}   # reactivate existing environment
Clone GitHub Project bash
git clone https://github.com/swamypotharaveni/django-encrypt-and-decrypt.git
cd python_project Install development dependencies,


pip install -r requirements.txt
Migrate Databases
bash
python manage.py makemigrations

python manage.py migrate
Run the web application locally,
```bash

python manage.py runserver # 127.0.0.1:8000
Create Superuser,
```bash

python manage.py createsuperuser
eamil settings
#open settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER ='add your email id'
EMAIL_HOST_PASSWORD =" add your password"

follow this documentation
https://cryptography.io
