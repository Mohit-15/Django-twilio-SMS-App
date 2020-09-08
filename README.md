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

## Screenshots
![ContactForm](https://firebasestorage.googleapis.com/v0/b/raspberrypi-6c5f9.appspot.com/o/Capture.PNG?alt=media&token=f4be9837-741e-48d9-b4fd-2681fe4db745)  
![ThankYou](https://firebasestorage.googleapis.com/v0/b/raspberrypi-6c5f9.appspot.com/o/Capture2.PNG?alt=media&token=b35a0396-e6b0-4a42-a64e-c209efee7eef) 
![SMS](https://firebasestorage.googleapis.com/v0/b/raspberrypi-6c5f9.appspot.com/o/Capture3.PNG?alt=media&token=50907ee5-7782-4a0b-9dd7-d5c619e1a070)
