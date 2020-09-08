from django.shortcuts import render, redirect
from .models import ContactForm
from django.contrib import messages
import random
from twilio.rest import Client

# Create your views here.
def home(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone = request.POST.get("phone")
		subject = request.POST.get("subject")
		query = request.POST.get("query")
		key = random.randint(999,9999)

		if phone:
			form = ContactForm(name = name, email = email, phone = phone, subject = subject, query = query, ref_number = key)
			form.save()
			account_sid = 'Your_auth_seed'
			auth_token = 'your_auth_token'
			client = Client(account_sid, auth_token)

			message = client.messages.create(
			                              body='Hi there! your ref_number is {} and the code for verification is "http://127.0.0.1:8000/codes_media/{}"'.format(form.ref_number, form.qr_code),
			                              from_= 'twilio number',
			                              to = '+91{}'.format(form.phone)
			                          )

			print(message.sid)
			return render(request, 'thankyou.html', {'name': form.name})
		else:
			messages.info(request, "Please provide the contact number")
			return render(request, 'index.html')

	return render(request, 'index.html')
