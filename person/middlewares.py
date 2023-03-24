from django.contrib.auth.models import User


class UserMiddlewares:
    def get_user_by_email_phone_username(username_phone_email, password):
        
        if User.objects.filter(username=username_phone_email).exists():
            user = User.objects.get(username=username_phone_email)
            passcheck = user.check_password(password)
            return user if passcheck else False
        
        elif User.objects.filter(email=username_phone_email).exists():
            user = User.objects.get(email=username_phone_email)
            passcheck = user.check_password(password)
            return user if passcheck else False

        elif User.objects.filter(primary_phone=username_phone_email).exists():
            user = User.objects.get(primary_phone=username_phone_email)
            passcheck = user.check_password(password)
            return user if passcheck else False

        else:
            return False
