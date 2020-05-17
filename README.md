# CASA-Track
A form tracking Django application for CASA of San Luis Obispo.

## Django Overview

### The MVT Framework
Django projects follow the Model View Template framework (MVT). It is very similar to the popular [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) framework, but has a couple key differences. The main difference is that Django itself handles interactions between the Models and Views, which is known to be the behavior of the Controller in the MVC framework. The 'Template' part of MVT refers to the HTML templates that you provide to Django that serve as the "UI" of the application, which can include Django Templating language (Jinja) that serve to transfer data from the View (in views.py) to the Template (HTML file).


### Models (models.py) https://docs.djangoproject.com/en/2.1/topics/db/models/
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

### Views (views.py) https://docs.djangoproject.com/en/2.1/topics/http/views/
Views are Python functions that takes a Web request, along with any additional data, and returns a Web response. The returned web response can be created using logic passed into the function and can be the HTML contents of a page, a redirect, an error, or really anything. By convention, each URL has its own View function, mapped in by urls.py.

### Url Mapping (urls.py) https://www.tutorialspoint.com/django/django_url_mapping.htm
When a user makes a request for a page on your web app, Django controller takes over to look for the corresponding view via the url.py file, and then return the HTML response or a 404 not found error, if not found. In url.py, the most important thing is the "urlpatterns" tuple. It’s where you define the mapping between URLs and views. 
 
### Templates (Django Template System) https://docs.djangoproject.com/en/2.1/topics/templates/
Being a web framework, Django needs a convenient way to generate HTML dynamically. The most common approach relies on templates. A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.

### Forms (forms.py) https://docs.djangoproject.com/en/2.1/topics/forms/
A way to streamline form data into a data object/class within django

## Jinja http://jinja.pocoo.org/
A python templating engine used throught the project.
