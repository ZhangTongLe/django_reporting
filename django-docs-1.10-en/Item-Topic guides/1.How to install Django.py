一.How to install Django
1.Install virtualenv and virtualenvwrapper
注1.:provide a dedicated environment for each Django project you create. 
注2:Then create a virtual environment for your project:

pip install virtualenvwrapper-win
mkvirtualenv myproject
workon myproject

2.Install Django
pip install django

3.Install Apache and mod_wsgi
If you want to use Django on a production site, use Apache with mod_wsgi.
mod_wsgi can operate in one of two modes: an embedded mode and a daemon mode

4.Install uWSGI and nginx.

5.Get your database running
(1)MySQL-mysqlclient
(2) cx_Oracle
(3) manage.py migrate command to automatically create database tables for your models (after first installing Django and creating a project), you’ll need to ensure that Django has permission to create and alter tables in the database you’re using

6.Remove any old versions of Django
$ python -c "import django; print(django.__path__)"
['C:\\software\\Anaconda3\\lib\\site-packages\\django']

