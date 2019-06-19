 # HL7 Broker Prototype

This Broker is to integrate Clinic System with Medical instruments through HL7 Protocol. Medical Devices such as blood analysis, Cardiology, NICU, ICU, Radiology are all using HL7 protocol to communicate and update their work lists. As most of software are now using web services, a Broker between medical devices and web based software is an essential part.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

### Python version 
```
3.7.3 
```
### Django version 
```
2.1.8 
```

### Django Rest framework version 
```
3.9.4
```

### System dependencies

You need to install **DCM4CHE** , create VM with the attached DCM iso file

As for the database we are using **mysql**.

### Installing

After cloning the project, you need to run

```bash
pip3 install python-dotenv
pip install hl7apy
```


You need to create ` .env` file that will hold environment variables.
First, you need to create it.
```bash
touch .env
```
Edit `.env` file and add the following variables.
```yml
DATABASE_NAME = YOUR_DB_NAME
DATABASE_USER = YOUR_DB_USER
DATABASE_PASSWORD = YOUR_DB_PASSWORD
STRIPE_PUBLISHABLE_KEY = xxxxxxxxx
STRIPE_SECRET_KEY = xxxxxxxx
```
#### Database initialization
To create your database
 
```python3
Python3 manage.py makemigrations
Python3 manage.py migrate
```
Load initial data as fixtures (db.json):
```python3
Python3 manage.py loaddata db.json
Python3 manage.py loaddata membership.json

```

Run these commands after initializing the Database, 

```python3
pip3 install libsass django-compressor django-sass-processor 
pip3 install django-extensions
```

## Needed libraries
```
certifi==2019.3.9
chardet==3.0.4
confusable-homoglyphs==3.2.0 
defusedxml==0.6.0
Django==2.1.8
django-adminlte2==0.4.1
django-allauth==0.39.1
django-allauth-templates-bootstrap4==0.34.12 
django-appconf==1.0.3
django-compressor==2.3
django-crispy-forms==1.7.2 
django-dotenv==1.4.2
django-extensions==2.1.9 
django-filter==2.1.0
django-jet==1.0.8
django-registration==3.0.1
django-sass-processor==0.7.3
django-widget-tweaks==1.4.5
djangorestframework==3.9.4
hl7apy==1.3.2 i
dna==2.8 l
ibsass==0.19.1 
Markdown==3.1
mysqlclient==1.4.2
post1 oauthlib==3.0.1 
pkg-resources==0.0.0
PyMySQL==0.9.3
python-dotenv==0.10.3
python3-openid==3.1.0
pytz==2019.1 rcssmin==1.0.6 
requests==2.21.0
requests-oauthlib==1.2.0 
rjsmin==1.1.0
six==1.12.0
stripe==2.29.4 
urllib3==1.24.3
<<<<<<< HEAD
```


#### python3 manage.py runserver
Starts the broker server
=======
```
>>>>>>> 0fe30a7db93456bd89b3cb0c0e1a22ba1a42a848
