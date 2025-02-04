import random
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.utils.translation import gettext as _
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from datetime import datetime, timedelta, timezone
import pytz


from .forms import UserRegisterForm, VerifyCodeForm
from utils import send_otp_code
from .models import OtpCode, MyUser

class UserRegisterView(View):
    form_class = UserRegisterForm
    def get(self, request):
        form= self.form_class
        return render(request, 'user_register.html', {'form':form})
    
    def post(self, request):
        form =self.form_class(request.POST)
        if form.is_valid():
            otp = OtpCode.objects.filter(phone_number = form.cleaned_data['phone'])
            if otp.exists():
                messages.error(request, _('we send your code already'))
                return redirect('core:verify_code')
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info']={
                'first_name':form.cleaned_data['first_name'],
                'last_name':form.cleaned_data['last_name'],
                'phone_number':form.cleaned_data['phone'],
                'password':form.cleaned_data['password2'],
            }
            messages.success(request, _('we sent you a code'))
            return redirect('core:verify_code')
        return render(request, 'user_register.html', {'form':form})