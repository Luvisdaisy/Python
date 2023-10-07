"""
自定义验证登录中间件
"""
from django.http import JsonResponse
from django.shortcuts import redirect

LOGIN_REQUIRED_URLS = {'/praise', '/criticize', 'excel', 'teachers_data'}


def check_login_middleware(get_resp):
    def wrapper(request, *args, **kwargs):
        if request.path in LOGIN_REQUIRED_URLS:
            if 'userid' not in request.session:
                if request.is_ajax():
                    return JsonResponse({'code': 10003, 'mesg': '请先登录'})
                else:
                    backurl = request.get_full_path()
                    return redirect(f'/login?backurl={backurl}')
        return get_resp(request, *args, **kwargs)

    return wrapper
