# CASA-Track
A form tracking Django application for CASA of San Luis Obispo.

## Project Purpose

## Environnment

## Django Overview
Follows the model view template frame work (MVT). Django takes care of controller hence no C (Controller)


### Models (models.py) https://docs.djangoproject.com/en/2.1/topics/db/models/
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

### Views (views.py) https://docs.djangoproject.com/en/2.1/topics/http/views/
a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. 

### Url Mapping (urls.py) https://www.tutorialspoint.com/django/django_url_mapping.htm
When a user makes a request for a page on your web app, Django controller takes over to look for the corresponding view via the url.py file, and then return the HTML response or a 404 not found error, if not found. In url.py, the most important thing is the "urlpatterns" tuple. It’s where you define the mapping between URLs and views. 
 
### Templates (Django Template System) https://docs.djangoproject.com/en/2.1/topics/templates/
Being a web framework, Django needs a convenient way to generate HTML dynamically. The most common approach relies on templates. A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.

### Forms (forms.py) https://docs.djangoproject.com/en/2.1/topics/forms/
A way to streamline form data into a data object/class within django

## Jinja http://jinja.pocoo.org/
A python templating engine used throught the project.
