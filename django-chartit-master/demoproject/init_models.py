import os
cmd = 'python manage.py makemigrations'
os.system(cmd)
cmd = 'python manage.py migrate'
os.system(cmd)
