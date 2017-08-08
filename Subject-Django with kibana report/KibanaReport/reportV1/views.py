from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect ;

# Create your views here.
def index(request):
    return render_to_response(r"index.html")
def raw_index(request):
    return HttpResponseRedirect(r"http://172.28.11.167:5601/app/kibana#/dashboard/6475ddc0-7812-11e7-9ef2-0956a1f086a4?_g=(refreshInterval%3A(display%3AOff%2Cpause%3A!f%2Cvalue%3A0)%2Ctime%3A(from%3A'Thu%20Aug%2003%202017%2013%3A24%3A40%20GMT%2B0800'%2Cmode%3Aabsolute%2Cto%3A'Thu%20Aug%2003%202017%2013%3A32%3A17%20GMT%2B0800'))")