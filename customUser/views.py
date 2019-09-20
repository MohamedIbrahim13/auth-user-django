from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm,UserChangeForm

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} Account has been created')
            return redirect('login')

    else:
        form=UserCreationForm()

    return render(request,'customUser/register.html',{'form':form})


@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserChangeForm(request.POST,request.FILES,instance=request.user)
        #p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid(): #and p_form.is_valid()
            u_form.save()
            #p_form.save()
            messages.success(request,f'Your Profile has been updated')
            return redirect('profile')
    else:
        u_form=UserChangeForm(instance=request.user)
        #p_form=ProfileUpdateForm(instance=request.user.profile)

    return render(request,'customUser/profile.html',{'u_form':u_form}) #,'p_form':p_form

