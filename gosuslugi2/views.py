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
    if (request.user.is_superuser or request.user.groups.filter(name='Аналитик').exists() or request.user.groups.filter(name='Гражданин').exists() or request.user.groups.filter(name='Специалист').exists()) and 'hv' in hash:
        c = connection.cursor()
        try:
            c.execute("BEGIN")
            if request.method == 'POST':
                params = Json(json.loads(request.body.decode('utf-8')))
            else:
                params = Json(request.GET)
            c.callproc("func_" + request.path.split('/')[2] , [hash, params])
            results = c.fetchone()[0]
            c.execute("COMMIT")
        except Exception as e:
            results = {"error": str(e)}
        finally:
            c.close()
    return JsonResponse(results, safe=False)
