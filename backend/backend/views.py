from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout

def oauth(request):
    if(request.user.is_authenticated):
        token, created = Token.objects.get_or_create(user=request.user)
        print(token)
        return redirect("/token=" + str(token))
    return redirect("/login")

def logout(request):
    logout(request)
    return redirect("/")