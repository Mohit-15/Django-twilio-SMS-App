# Django-twilio-SMS-App
#### Contact form web app for sending the reference number and QRcode link through SMS with API service of Twilio.

## Steps for using this application
1. Create account on twilio and get your auth key and account seed, and add in contact_form/views.py
2. Run the following commands in the terminal: 
      * First install all the requirements in your systems \
        ` pip install -r reuirements.txt `
      * for collecting the static files \
        ` python manage.py collectstatic `
      * Now make the migrations and migrate the models \
        ` python manage.py makemigrations ` \
        ` python manage.py migrate `
      * Run the server at localhost:8000 \
        ` python manage.py runserver`
