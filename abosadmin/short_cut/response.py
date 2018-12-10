from django.http import JsonResponse
# from django.utils.translation import ugettext_lazy, ugettext as _


def form_to_response(data, msg='', error=0):
    rsp = {
        'error': error,
        'msg': msg,
        'data': data
    }
    return JsonResponse(data=rsp)


#eof
