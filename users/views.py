from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import OrgRegisterForm, StuRegisterForm, StuLoginForm, OrgLoginForm
from .models import Organization, Student
from profiles.forms import StuProfileForm, OrgProfileForm
from .models import set_password, check_password_hash
from profiles.models import StuProfile, OrgProfile, Profile_relationship
from projects.models import Project
# Create your views here.

def org_register(request):
    if request.method == 'POST':
        form = OrgRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            if len(Organization.objects.filter(username=username)) != 0:
                info = {'error': 'User Exists!'}
                return render(request, 'users/sign_up.html', info)
            else:
                password = form.cleaned_data['password']
                form.save()
                messages.success(request, 'Congratulations')
                return HttpResponseRedirect('/users')
    else:
        form = OrgRegisterForm()
    return render(request, 'users/sign_in.html', locals())

def stu_register(request):
    if request.method == 'POST':
        form = StuRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            if len(Student.objects.filter(username=username)) != 0:
                info = {'error': 'User Exists!'}
                return render(request, 'users/sign_up.html', info)
            else:
                password = form.cleaned_data['password']
                form.save()
                messages.success(request, 'Congratulations')
                return HttpResponseRedirect('/users')
    else:
        form = StuRegisterForm()
    return render(request, 'users/sign_up.html', locals())

def org_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        org = Organization.objects.filter(username=username).first()
        if org == None:
            messages.error(request, 'Username or Password may be incorrect')
            return render(request, 'users/sign_in.html', locals())
        if not check_password_hash(password, org.password):
            messages.error(request, 'Username or Password may be incorrect')
            return render(request, 'users/sign_in.html', locals())

        request.session['username'] = org.username
        request.session['id'] = org.id
        request.session['mark'] = 0
        messages.success(request, 'Welcome Back!')
        return HttpResponseRedirect('/users')
    else:
        form = OrgLoginForm()
    return render(request, 'users/sign_in.html', locals())

def stu_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        stu = Organization.objects.filter(username=username).first()
        if stu == None:
            messages.error(request, 'Username or Password may be incorrect')
            return render(request, 'users/sign_in.html', locals())
        if not check_password_hash(password, stu.password):
            messages.error(request, 'Username or Password may be incorrect')
            return render(request, 'users/sign_in.html', locals())

        #TODO: ENCRYPT THIS
        request.session['username'] = stu.username
        request.session['id'] = stu.id
        request.session['mark'] = 0
        messages.success(request, 'Welcome Back!')
        return HttpResponseRedirect('/users')
    else:
        form = StuLoginForm()
    return render(request, 'users/sign_in.html', locals())

def logout(request):
    request.session.flush()
    return redirect(reverse('projects:index'))

def edit_info_stu(request, id):
    # TODO: AUTH REQUIRED
    stu = Student.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Student.objects.filter(id=id).update(username=username,
                                            email=email, phone=phone)
        messages.success(request, 'Edit Saved')
        return HttpResponseRedirect('/users/edit_info_stu/%s' % id, )
    return render(request, 'student/stu_info_edit.html', locals())


def edit_profile_stu(request, id):
    # TODO: AUTH REQUIRED
    profile = StuProfile.objects.filter(user_id=id).first()
    if request.method == 'POST':
        form = StuProfileForm(request.POST, instance=profile)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Edit Saved')
            except:
                form.cleaned_data['user_id'] = int(id)
                profile.objects.create(**form.cleaned_data)
                messages.success(request, 'Added')
    else:
        form = StuProfileForm(instance=profile)
    return render(request, 'student/stu_profile_edit.html', locals())


def edit_info_org(request, id):
    # TODO: AUTH REQUIRED
    org = Organization.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Student.objects.filter(id=id).update(username=username,
                                            email=email, phone=phone)
        messages.success(request, 'Edit Saved')
        return HttpResponseRedirect('/users/edit_info_stu/%s' % id, )
    return render(request, 'student/org_info_edit.html', locals())


def edit_profile_org(request, id):
    # TODO: AUTH REQUIRED
    profile = OrgProfile.objects.filter(user_id=id).first()
    if request.method == 'POST':
        form = OrgProfileForm(request.POST, instance=profile)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Edit Saved')
            except:
                form.cleaned_data['user_id'] = int(id)
                profile.objects.create(**form.cleaned_data)
                messages.success(request, 'Added')
    else:
        form = StuProfileForm(instance=profile)
    return render(request, 'organization/org_profile_edit.html', locals())

def get_project_list(request):
    # TODO: AUTH REQUIRED
    try:
        stu_id = int(request.session['id'])
        profile = StuProfile.objects.filter(user_id=stu_id).first()
        project_id_list = Profile_relationship.objects.filter(profile_id=profile.id)
        project_list = [Project.objects.filter(id=project_id.project_id)[0] for project_id in project_id_list]
    except:
        info = 'No Projects Avaliable'
    return render(request, 'student/get_project_list.html', locals())

def dashboard(request):
    return render(request, 'users/student-dashboard.html', locals())