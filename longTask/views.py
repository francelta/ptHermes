from django.http import JsonResponse
from .tasks import tarea_pesada
 

def start_tarea_pesada(request):

    result = tarea_pesada.delay('Test tarea pesada')
    return JsonResponse({'status': 'Tarea iniciada', 'task_id': result.id})


