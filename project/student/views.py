from django.shortcuts import render
from .forms import UserForm
from .login_form import LoginForm
from .models import User


def login(request):
    if request.method == 'POST':  # if the form has been filled

        form = LoginForm(request.POST or None)
        u=False
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            all_users = User.objects.all()
            if all_users:
                for user in all_users:
                  if username==user.username and password==user.password:
                    u=True
                    obj=user

            if u==True:
                request.session['username'] = obj.username
                return render(request, 'student/showdata.html',
                              {'obj': obj })
            else:
                form=LoginForm()
                return render(request, 'student/login.html',
                              {'is_registered':True,'form':form, 'all_users': all_users})




        else:
            print(form.errors)

            return render(request, 'student/login.html',
                          {'form': form})  # Redirect after POST

    else:
        form = LoginForm()  # an unboundform

        return render(request, 'student/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':  # if the form has been filled

        form = UserForm(request.POST or None)

        if form.is_valid():
            # All the data is valid

            username = request.POST.get('username', '')
            name = request.POST.get('name', '')
            dob = request.POST.get('dob', '')
            email = request.POST.get('email', '')
            roll = request.POST.get('roll', '')
            phone = request.POST.get('phone', '')
            department = request.POST.get('department', '')
            password = request.POST.get('password', '')
            password1 = request.POST.get('password1', '')
            if password != password1:
                raise form.ValidationError("Passwords must match")
                return render(request, 'student/signup.html', {'form': form})

            else:

              user_obj = User(username=username,name=name,dob=dob, email=email,roll=roll,phone=phone,department=department, password=password)
              user_obj.save()
              form = LoginForm()
              return render(request, 'student/login.html', {'form':form})  # Redirect after POST

        else:
         print(form.errors)
         return render(request, 'student/signup.html', {'form': form})

    else:
        form = UserForm()  # an unboundform

        return render(request, 'student/signup.html', {'form': form})


def showdata(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request,'student/showdata.html', {"username": username})
    else:
        return render(request, 'login.html', {})
    all_users = User.objects.all()
    return render(request, 'student/showdata.html', {'all_users': all_users, })




def logout(request):
   try:
      del request.session['username']
   except:
      pass
      return render(request, 'student/login.html', {})

