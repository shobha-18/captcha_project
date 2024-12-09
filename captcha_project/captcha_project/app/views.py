from django.shortcuts import render,redirect
from .forms import  CaptchaForm
from pymongo import MongoClient

# Create your views here.
client=MongoClient('localhost',27017)
db=client.captcha_data
def data(request):

    if request.method=='POST':
        form=CaptchaForm(request.POST)
        if form.validate():
            return render("success.html")
        else:
            return render("fail.html")
    else:
        form = CaptchaForm()
    return render(request, 'index.html', {'form': form})