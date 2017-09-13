一.BASE VEIWS
(一)VEIW
from django.http import HttpResponse
from django.views import View

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

# 1.classmethod as_view(**initkwargs)
# Returns a callable view that takes a request and returns a response:

urlpatterns = [
    url(r'^mine/$', MyView.as_view(), name='my-view'),
]

(二)TemplateView
# class django.views.generic.base.TemplateView
# Renders a given template, with the context containing parameters captured in the URL.

(三)RedirectView
# class django.views.generic.base.RedirectView
# Redirects to a given URL.