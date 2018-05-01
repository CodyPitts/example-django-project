# example-django-project

Note that this assumes you are working with a mac. For those on Windows, ¯\\_(ツ)_/¯

Make sure you have Python 3 and pip installed (you want the version of pip from Python 3, which might mean using the command ```pip3``` instead of ```pip```).

```
pip install virtualenv
pip install virtualenvwrapper
```

Add the following to your bash_profile:
```
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

Now run ```mkvirtualenv <your-env-here>```, and you should see the name of your virtualenv prepended to your command line. If not, run ```workon <your-env-here>``` to enter it, and ```deactivate``` to leave it.

Once inside your virtualenv and in the directory with requirements.txt, run ```pip install -r requirements.txt``` to install the listed packages. At any time, you can run ```pip freeze``` to see the packages you have installed in your current environment.

In the directory containing the manage.py file, run ```python manage.py migrate``` to synchronize your database, and then ```python manage.py createsuperuser``` to make yourself an account. You can run ```python manage.py runserver``` at any point to spin up a local version of your site.

Access the app section at /simple_app, and the api section at /simple_api.
