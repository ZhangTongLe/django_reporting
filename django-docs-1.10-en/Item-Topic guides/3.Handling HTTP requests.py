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

