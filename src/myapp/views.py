from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

# Create your views here.
def hello(request):
    name = "murphyki"
    html = "<html><body>Hi %s. this seems to have worked!</body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "murphyki"
    template = get_template("hello.html")
    html = template.render(Context({'name':name}))
    return HttpResponse(html)