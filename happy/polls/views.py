from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am bold font from the context"}
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
	return render_to_response('rango/index.html', context_dict, context)
def about(request):
	return HttpResponse("hello rango tumne mera kaat diya")
