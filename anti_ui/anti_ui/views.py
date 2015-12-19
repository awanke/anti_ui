from django.http import HttpResponse
import datetime

def hello(request):
	return HttpResponse("hellp world sas")

def current_dt(request):
	now = datetime.datetime.now()
	html = "<html><body> it is %s </body></html>" % now
	return HttpResponse(html)
