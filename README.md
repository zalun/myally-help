# My Ally
## Therapy help in the time of trouble

Display an immediate online contact to available therapists.

## Info

Free help for people in group trauma.
Epidemy, natural disasters etc.

A website with a list of active Therapists.
A Therapist is displayed as a name / info / links to contacts
There is an info of the number of therapists currently on-line, to make people aware that they might wait a moment for the next therapist.

Admin should be aware of number of people seeking contact.

Website should use a sophisticated mechanism to actively update the information to avoid double-booking.

To register one needs to be invited by coordinator in the country.
There might be many Coordinators per Country.

Login with e-mail/password.

## Development

### Bootstrap 4
https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html

### Database:

Cause
 - name
 - countries (many to many)
 - description
 - website

Country
*using `django-countries`*
https://pypi.org/project/django-countries/
 
Language
- name

Profile
  - first name
  - last name 

Coordinator
  - link to Profile
  - link to Country
  
Invitation
  - link to Coordinator
  - code
  - country

Therapist
  - link to Profile (one to one)
  - link to Cause (one to many)
  - link to Country (one to many)
  - specialisation
  - languages
  - on-line (bool)
  - busy (bool)
  - contacts:
    - phone number
    - WhatsApp
    - Skype
    - ...

Telemetry
 - therapist
 - cause
 - time available
 - time busy

Logging
 - registration
 - logins
 - switch availability
 - switch busy


## Deployment
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04

Create a `myally/security.py` file with the content:

```
DEBUG = True
POSTGRESQL_HOST = "somehost"
POSTGRESQL_DATABASE = "somedb"
POSTGRESQL_USER = "someuser"
POSTGRESQL_PASSWORD = "somepassword"
ALLOWED_HOSTS = ["myally.pl"]
STATIC_ROOT = "/path/to/static"
````
