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


