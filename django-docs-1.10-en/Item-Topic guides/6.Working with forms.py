# In HTML, a form is a collection of elements inside <form>...</form> that allow a visitor to do things like enter text, select options, manipulate objects or controls, and so on, and then send that information back to the server.
# Some of these form interface elements - text input or checkboxes - are fairly simple and are built into HTML itself. Others are much more complex; 
# an interface that pops up a date picker or allows you to move a slider or manipulate controls will typically use JavaScript and CSS as well as HTML form <input> elements to achieve these effects.

# As well as its <input> elements, a form must specify two things:

# where: the URL to which the data corresponding to the user’s input should be returned
# how: the HTTP method the data should be returned by

 # one of type="text" for the username, one of type="password" for the password, and one of type="submit" for the “Log in” button
 # the URL specified in the <form>’s action attribute - /admin/ - and that it should be sent using the HTTP mechanism specified by the method attribute - post.


 # GET and POST are the only HTTP methods to use when dealing with forms.

# Django’s login form is returned using the POST method, in which the browser bundles up the form data, encodes it for transmission, sends it to the server, and then receives back its response.

# GET, by contrast, bundles the submitted data into a string, and uses this to compose a URL. The URL contains the address where the data must be sent, as well as the data keys and values. You can see this in action if you do a search in the Django documentation, which will produce a URL of the form https://docs.djangoproject.com/search/?q=forms&release=1.

# a request that makes changes in the database - should use POST.

 # GET should be used only for requests that do not affect the state of the system.

 # GET would also be unsuitable for a password form, because the password would appear in the URL, and thus, also in browser history and server logs, all in plain text.

# Handling forms is a complex business



Sublime Text 3 build 3143 LICENSE
Raw
 sublime.txt
—– BEGIN LICENSE —–
TwitterInc
200 User License
EA7E-890007
1D77F72E 390CDD93 4DCBA022 FAF60790
61AA12C0 A37081C5 D0316412 4584D136
94D7F7D4 95BC8C1C 527DA828 560BB037
D1EDDD8C AE7B379F 50C9D69D B35179EF
2FE898C4 8E4277A8 555CE714 E1FB0E43
D5D52613 C3D12E98 BC49967F 7652EED2
9D2D2E61 67610860 6D338B72 5CF95C69
E36B85CC 84991F19 7575D828 470A92AB
—— END LICENSE ——

Django handles three distinct parts of the work involved in forms:

preparing and restructuring data to make it ready for rendering
creating HTML forms for the data
receiving and processing submitted forms and data from the client


一.Forms in Django
1.The Django Form class
In a similar way that a model class’s fields map to database fields, a form class’s fields map to HTML form <input> elements.
(A ModelForm maps a model class’s fields to HTML form <input> elements via a Form; this is what the Django admin is based upon.)

2.Instantiating, processing, and rendering forms¶

When rendering an object in Django, we generally:

get hold of it in the view (fetch it from the database, for example)
pass it to the template context
expand it to HTML markup using template variables

When we instantiate a form, we can opt to leave it empty or pre-populate it, for example with:

data from a saved model instance (as in the case of admin forms for editing)
data that we have collated from other sources
data received from a previous HTML form submission

二.Building a form

in order to obtain the user’s name. You’d need something like this in your template:

<form action="/your-name/" method="post">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
    <input type="submit" value="OK">
</form>

return the form data to the URL /your-name/, using the POST method.

If the template context contains a current_name variable, that will be used to pre-fill the your_name field.

Now you’ll also need a view corresponding to that /your-name/ URL which will find the appropriate key/value pairs in the request, and then process them.


三.Building a form in Django

1.The Form class

forms.py
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


The field’s maximum allowable length is defined by max_length. This does two things. 
It puts a maxlength="100" on the HTML <input> (so the browser should prevent the user from entering more than that number of characters in the first place). 
It also means that when Django receives the form back from the browser, it will validate the length of the data.

The whole form, when rendered for the first time, will look like:

<label for="your_name">Your name: </label>
<input id="your_name" type="text" name="your_name" maxlength="100" required />

2.The view

Form data sent back to a Django website is processed by a view, generally the same view which published the form. This allows us to reuse some of the same logic.

views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


If the form is submitted using a POST request, the view will once again create a form instance and populate it with data from the request: form = NameForm(request.POST) 
This is called “binding data to the form” (it is now a bound form).

We call the form’s is_valid() method; f is_valid() is True, we’ll now be able to find all the validated form data in its cleaned_data attribute.
 We can use this data to update the database or do other processing before sending an HTTP redirect to the browser telling it where to go next.

3.The template
We don’t need to do much in our name.html template. The simplest example is:

<form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit" />
</form>

All the form’s fields and their attributes will be unpacked into HTML markup from that {{ form }} by Django’s template language.

