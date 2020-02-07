from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ExcelModel, UserModel
from .forms import RegisterForm
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import login
import csv


class IndexView(TemplateView):
    template_name = 'user_data/index.html'

    def get(self, request, *args, **kwargs):
        form = None
        if request.user.is_authenticated:
            form = ExcelModel.objects.filter(user=request.user)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        excel_file = request.FILES["excel_file"]
        form = ExcelModel()
        form.excelfile = excel_file
        form.user = request.user
        form.save()
        # excel_data = pandas.read_csv('media/{}'.format(form.excelfile), low_memory=False)
        # print(excel_data)
        with open('media/{}'.format(form.excelfile), 'r') as f:
            excel_data = csv.reader(f)
            count = 0
            for row in excel_data:
                if count == 0:
                    count = 1
                    continue
                print(row)
                cost = 0.0
                if int(row[18])==0 or int(row[5])==0 or int(row[7])==0:
                    cost = 0.0
                else:
                    cost = float(row[18])/float(((float(row[5])*float(row[7]))/100))
                UserModel.objects.create(
                    ex_file=form,
                    unique_id=row[1],
                    username=row[2],
                    social_platform=row[3],
                    media=row[4],
                    followers=row[5],
                    following=row[6],
                    engagement=row[7],
                    authenticity=row[8],
                    highlight_reel_count=row[9],
                    is_business_account=row[10],
                    is_private=row[11],
                    is_verified=row[12],
                    is_barter=row[13],
                    business_category=row[14],
                    join_date=row[15],
                    last_updated_on=row[16],
                    status=row[17],
                    price_per_pic_post=row[18],
                    cost_per_engagement=cost
                )
        return redirect('user_data:detail', val=form.id)

@login_required
def DetailView(request, val, *args, **kwargs):
    excel_data = UserModel.objects.filter(ex_file=val).order_by('authenticity', 'cost_per_engagement')
    template_name = 'user_data/detail.html'
    context = {
        'excel_data': excel_data
    }
    return render(request, template_name, context)


class SignupView(TemplateView):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data['email'],
                                       first_name=form.cleaned_data['first_name'],
                                       password=make_password(form.cleaned_data['password1']))
            login(request, user)
            return redirect('user_data:index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
