from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import connection
from psycopg2.extras import Json
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def home(request):
    return render(request, 'home.html')


@csrf_exempt
def processdata(request):
    results = {}
    hash = request.GET.get('hash', '')
    if request.user.pk:
        vUserID = request.user.pk
        vPrivileged = 1 if (request.user.is_superuser or request.user.groups.filter(name='Аналитик').exists() or request.user.groups.filter(name='Гражданин').exists() or request.user.groups.filter(name='Специалист').exists()) else 0
    else:
        vUserID = 0
        vPrivileged = 0
    if hash.startswith('hv'):
        c = connection.cursor()
        try:
            c.execute("BEGIN")
            if request.method == 'POST':
                pdata = json.loads(request.body.decode('utf-8'))
                pdata['files'] = request.FILES if request.FILES else None
                params = Json(pdata)
            else:
                params = Json(request.GET)

            c.callproc("func_" + request.path.split('/')[2] , [vUserID, params, vPrivileged])
            results = c.fetchone()[0]
            c.execute("COMMIT")
        except Exception as e:
            results = {"error": str(e)}
        finally:
            c.close()
    return JsonResponse(results, safe=False)
