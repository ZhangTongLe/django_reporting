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