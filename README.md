# My Ally
## Therapy help in the time of trouble


## Development
Free help for people in group trauma.
Epidemy, natural disasters etc.

A website with a list of active therapists.
A therapist is displayed as a name / info / links to contacts
There is an info of the number of therapists currently on-line, to make people aware that they might wait a moment for the next therapist.

Admin should be aware of number of people seeking contact.

Website should use a sophisticated mechanism to actively update the information to avoid double-booking.

To register one needs to be authorised by an admin in the country.
Login with e-mail/password.

Database:
----------------
Cause
 - name
 - countries (one to many)
 - description
 - website

Country
 - name
 
Language
- name

Therapist
  - first name
  - last name
  - cause (one to many)
  - country (one to many)
  - specialisation
  - languages
  - short bio
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

