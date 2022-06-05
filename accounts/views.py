from django.shortcuts                import redirect, render
from django.contrib                  import messages
from django.contrib.auth             import authenticate , login, logout
from django.contrib.auth.views       import PasswordChangeView
from django.contrib.messages.views   import SuccessMessageMixin
from django.contrib.auth.decorators  import login_required
from django.urls                     import reverse_lazy
from .models                         import Profile  
from .forms                          import CreateUserForm, Login_Form, UpdateUserForm, UpdateProfileForm
from django.views.generic            import View
# Create your views here.


def SignUp_SignUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    form_CreateUser = CreateUserForm()
    form_LoginUser  = Login_Form()
    if request.method == "POST" and 'CreateUser' in request.POST:
        form_CreateUser = CreateUserForm(request.POST)

        if form_CreateUser.is_valid():
            form_CreateUser.save()
            return redirect('SignUp-SignIn')
        else:
            messages.error(request, form_CreateUser.errors)


    if request.method == "POST" and 'LoginUser' in request.POST:
        form_LoginUser = Login_Form(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'USERNAME OR PASSWORD ERROR')


    context = {  
        'LoginUser':form_LoginUser,
        'CreateUser':form_CreateUser
         }
    return render(request, 'SignIn_SignUp.html',context)


# LogoutUser Views
def LogoutUser(request):
    logout(request)
    return redirect('SignUp-SignIn')

# profile Views
@login_required(login_url='SignIn')
def profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('Profile')

    profile =   Profile
    return render(request, 'profile.html', {'profile' : profile,'user_form': user_form,'profile_form': profile_form})


# Profiles_Users Views
def Profiles_Users(request, slug):
    Detail_ = Profile.objects.get(slug = slug)
    context = {"Detail":Detail_}
    return render(request, 'profiles_users.html', context)

# ChangePasswordView CBV
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')