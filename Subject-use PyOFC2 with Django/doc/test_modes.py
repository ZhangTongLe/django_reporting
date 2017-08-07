import os
# cmd = 'python manage.py makemigrations blogs'
# cmd='python manage.py sqlmigrate blogs 0001'
cmd='python manage.py migrate'
# Operations to perform:
#   Apply all migrations: admin, auth, blogs, contenttypes, sessions
# Running migrations:
#   Applying blogs.0001_initial... OK
os.system(cmd)

# [1]Change your models (in models.py).
# [2]Run python manage.py makemigrations to create migrations for those changes
# [3]Run python manage.py migrate to apply those changes to the database.