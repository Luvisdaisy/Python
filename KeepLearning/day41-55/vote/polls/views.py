from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from polls.models import Subject, Teacher, User
import polls.utils as utils
# Create your views here.



def show_subjects(request):
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


def show_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
            return render(request, 'teachers.html', {
                'subject': subject,
                'teachers': teachers})
    except(ValueError, Subject.DoesNotExist):
        return redirect('/')


def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    if request.session.get('userid'):
        try:
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('/praise/'):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count += 1
                count = teacher.bad_count
            teacher.save()
            data = {'code': 20000, 'mesg': '投票成功', 'count': count}
        except (ValueError, Teacher.DoesNotExist):
            data = {'code': 20001, 'mesg': '投票失败'}
    else:
        data = {'code': 20002, 'mesg': '请先登录'}
    return JsonResponse(data)


def get_captcha(request: HttpRequest) -> HttpResponse:
    """验证码"""
    captcha_text = utils.gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = utils.Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')


def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:
                password = utils.gen_md5_digest(password)
                user = User.objects.filter(username=username, password=password).first()
                if user:
                    request.session['user_id'] = user.no
                    request.session['username'] = user.username
                    return redirect('/')
                else:
                    hint = '用户名或密码错误'
            else:
                hint = '请输入有效的用户名和密码'
        else:
            return HttpResponse('请启用 Cookie，然后重试。')
    request.session.set_test_cookie()
    return render(request, 'login.html', {'hint': hint})


def logout(request):
    """退出登录"""
    request.session.flush()
    return redirect('/')
