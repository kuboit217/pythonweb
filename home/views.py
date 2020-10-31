from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .forms import RegisterForm

# Create your views here.

def index(request):#views cho trang chủ
   return render(request,'pages/home.html')

def contact(request):#views trang liên hệ
   return render(request,'pages/contact.html')

def handler404(request,Exception):#view lỗi 404
    return render(request, 'pages/errors.html', {})


def handler500(request):#view lỗi 500
    return render(request, 'pages/errors.html')
def register(request):#view trang đăng ký
   form = RegisterForm()
   #gửi dữ liệu để save
   if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
         form.save_user()
         return HttpResponseRedirect('/')
   return render(request, 'pages/register.html', {'form':form})