from django.http import HttpResponse, Http404
import datetime

def hello(request):
	return HttpResponse("hellp world sas")

def current_dt(request):
	now = datetime.datetime.now()
	html = "<html><body> it is %s </body></html>" % now
	return HttpResponse(html)

def hours_ahead (request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	now = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "delay %s, will be %s" % (offset, now)
	return HttpResponse(html)
