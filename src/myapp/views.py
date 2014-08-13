from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
def hello_simple(request):
    name = "murphyki"
    html = "<html><body>Hi %s. this seems to have worked!</body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "murphyki"
    template = get_template("hello.html")
    html = template.render(Context({'name':name}))
    return HttpResponse(html)

def hello_template_simple(request):
    name = "murphyki"
    return render_to_response("hello.html", {'name':name})

class HelloTemplateView(TemplateView):
    template_name = "hello_class.html"
    def get_context_data(self, **kwargs):
        #context = super(HelloTemplateView, self).get_context_data(**kwargs)
        context = TemplateView.get_context_data(self, **kwargs)
        context['name']  = "murphyki"
        return context