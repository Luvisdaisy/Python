from io import BytesIO

from reportlab.pdfgen import canvas
import xlwt
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from polls.models import Subject, Teacher, User
import polls.utils as utils


# Create your views here.


def show_subjects(request):
    """查看学科"""
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


def show_teachers(request):
    """查看老师"""
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
    """评价"""
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
    """登录"""
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


def export_teachers_excel(request):
    """导出教师列表"""
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('教师列表')
    queryset = Teacher.objects.all().select_related('subject')
    colnames = ('姓名', '介绍', '好评数', '差评数', '学科')
    for index, name in enumerate(colnames):
        sheet.write(0, index, name)
    props = ('name', 'detail', 'good_count', 'bad_count', 'subject')
    for row, teacher in enumerate(queryset):
        for col, prop in enumerate(props):
            value = getattr(teacher, prop, '')
            if isinstance(value, Subject):
                value = value.name
            sheet.write(row + 1, col, value)
    buffer = BytesIO()
    wb.save(buffer)
    resp = HttpResponse(buffer.getvalue(), content_type='application/vnd.ms-excel')
    filename = 'teachers.xls'
    resp['Content-Disposition'] = 'attachment; filename=%s' % filename
    return resp


def export_pdf(request: HttpRequest) -> HttpResponse:
    """导出pdf报表"""
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setFont('Helvetica', 80)
    pdf.setFillColorRGB(0.2, 0.5, 0.3)
    pdf.drawString(100, 550, 'hello,world!')
    pdf.showPage()
    pdf.save()
    resp = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    resp['Content-Disposition'] = 'inline; filename="demo.pdf"'
    return resp


def get_teachers_data(request):
    """教师统计图表"""
    queryset = Teacher.objects.all().only('name', 'good_count', 'bad_count')
    names = [teacher.name for teacher in queryset]
    good_counts = [teacher.good_count for teacher in queryset]
    bad_counts = [teacher.bad_count for teacher in queryset]

    return JsonResponse({'names': names, 'good': good_counts, 'bad': bad_counts})
