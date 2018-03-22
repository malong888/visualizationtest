from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def test(request):
	data = {
		'x': ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
		'y': [5, 20, 36, 10, 10, 20],
		'y1': [100, 90, 50, 80, 80, 70],
		'y2': [43, 54, 67, 88, 99, 44]
	}
	return JsonResponse(data)

def index(request):
	return render(request,'index.html')