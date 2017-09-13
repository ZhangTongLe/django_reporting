一.URL dispatcher路由配置文件
1.URLconf is pure Python code and is a simple mapping between URL patterns (simple regular expressions) to Python functions (your views).

(一)How Django processes a request

Django determines the root URLconf module to use. Ordinarily, this is the value of the ROOT_URLCONF setting, but if the incoming HttpRequest object has a urlconf attribute (set by middleware), its value will be used in place of the ROOT_URLCONF setting.
Django loads that Python module and looks for the variable urlpatterns. This should be a Python list of django.conf.urls.url() instances.
Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL.
Once one of the regexes matches, Django imports and calls the given view, which is a simple Python function (or a class-based view). The view gets passed the following arguments:
An instance of HttpRequest.
If the matched regular expression returned no named groups, then the matches from the regular expression are provided as positional arguments.
The keyword arguments are made up of any named groups matched by the regular expression, overridden by any arguments specified in the optional kwargs argument to django.conf.urls.url().
If no regex matches, or if an exception is raised during any


(二)Named groups

In Python regular expressions, the syntax for named regular-expression groups is (?P<name>pattern), where name is the name of the group and pattern is some pattern to match.

例子
url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
A request to /articles/2003/03/03/ would call the function views.article_detail(request, year='2003', month='03', day='03').

(三).Captured arguments are always strings

url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
…the year argument passed to views.year_archive() will be a string,
not an integer, even though the [0-9]{4} will only match integer strings.

(四)Specifying defaults for view arguments
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/$', views.page),
    url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
]

# View (in blog/views.py)
def page(request, num="1"):
    # Output the appropriate page of blog entries, according to num.
    ...

 the page() function will use its default argument for num, "1". If the second pattern matches, page() will use whatever num value was captured by the regex.


(五)Including other URLconfs
from django.conf.urls import include, url

urlpatterns = [
    # ... snip ...
    url(r'^community/', include('django_website.aggregator.urls')),
    url(r'^contact/', include('django_website.contact.urls')),
    # ... snip ...
]


例子2
from django.conf.urls import include, url

from apps.main import views as main_views
from credit import views as credit_views

extra_patterns = [
    url(r'^reports/$', credit_views.report),
    url(r'^reports/(?P<id>[0-9]+)/$', credit_views.report),
    url(r'^charge/$', credit_views.charge),
]

urlpatterns = [
    url(r'^$', main_views.homepage),
    url(r'^help/', include('apps.help.urls')),
    url(r'^credit/', include(extra_patterns)),
]

# /credit/reports/   credit_views.report() 

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/', include([
        url(r'^history/$', views.history),
        url(r'^edit/$', views.edit),
        url(r'^discuss/$', views.discuss),
        url(r'^permissions/$', views.permissions),
    ])),
]

(六)Captured parameters

An included URLconf receives any captured parameters from parent URLconfs, so the following example is valid:

# In settings/urls/main.py
from django.conf.urls import include, url

urlpatterns = [
    url(r'^(?P<username>\w+)/blog/', include('foo.urls.blog')),
]

# In foo/urls/blog.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog.index),
    url(r'^archive/$', views.blog.archive),


(七)Nested arguments
(八)Passing extra options to view functions

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/(?P<year>[0-9]{4})/$', views.year_archive, {'foo': 'bar'}),
]
# In this example, for a request to /blog/2005/, Django will call views.year_archive(request, year='2005', foo='bar').

# to pass metadata and options to views.

二.Writing views
# A view function, or view for short, is simply a Python function that takes a Web request and returns a Web response
# his response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really

(一)例子
 # Each view function takes an HttpRequest object as its first parameter, which is typically named request
 # The view returns an HttpResponse object that contains the generated response. Each view function is responsible for returning an HttpResponse object.
(二)Returning errors
from django.http import HttpResponse, HttpResponseNotFound

def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')


from django.http import HttpResponse

def my_view(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)

(三)The Http404 exception
from django.http import Http404
from django.shortcuts import render
from polls.models import Poll

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'polls/detail.html', {'poll': p})

(四)Customizing error views
handler404 = 'mysite.views.my_custom_page_not_found_view'
handler500 = 'mysite.views.my_custom_error_view'
handler403 = 'mysite.views.my_custom_permission_denied_view'
handler400 = 'mysite.views.my_custom_bad_request_view'

三.View decorators
(一)Allowed HTTP methods
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass

 # These decorators will return a django.http.HttpResponseNotAllowed if the conditions are not met.
 (二)Conditional view processing¶

四.File Uploads

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

# A view handling this form will receive the file data in request.FILES, which is a dictionary containing a key for each FileField (or ImageField, or other FileField subclass) in the form. So the data from the above form would be accessible as request.FILES['file'].


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

五.Django shortcut functions
from django.http import HttpResponse
from django.template import loader

def my_view(request):
    # View code here...
    t = loader.get_template('myapp/index.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='application/xhtml+xml')

from django.shortcuts import render

def my_view(request):
    # View code here...
    return render(request, 'myapp/index.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml')


from django.shortcuts import redirect

def my_view(request):
    ...
    object = MyModel.objects.get(...)
    return redirect(object)

def my_view(request):
    ...
    return redirect('some-view-name', foo='bar')

def my_view(request):
    ...
    return redirect('/some/url/')

def my_view(request):
    ...
    return redirect('https://example.com/')

          