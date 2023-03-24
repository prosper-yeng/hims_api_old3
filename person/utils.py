from django.core.mail import send_mail
from django.conf import settings
import random
import string


def send_forget_password_mail(link, user):
    subject = "HIMS"
    message = f""" Hi {user.get_full_name()}, 
	\n Click on the link below to reset your password for your Hims Account
	\n {link}
	\n
	\n This was intended for {user.email}
	"""

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)


def get_user_ip_address(request):
    user_ip_address = request.META.get("HTTP_X_FORWARDED_FOR")
    if user_ip_address:
        ip = user_ip_address.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_random_string(length):
    # choose from all lowercase letter
    characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for i in range(length))
    return password
