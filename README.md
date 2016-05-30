Store email templates in the database and send it with a simple function call.

# Installation
* Add the app to your INSTALLED_APPS list
* Migrate the database

# Usage
* Create an email template in the admin. The name field is the name you need to refer to the email in code
* Send the email with send_email function in the django_database_url.email module

# Template format
The email template is a standard django template, with one exception: Every newline gets replaced with a <br> HTML tag.
This makes editing much easier (especially for non-technical people).

In addition, a plain text version of the rendered text is generated using the django utils function strip_tags.
To generate correct links in the plain text version, use the following syntax:

    <a href="http://example.com">http://example.com</a>

# Translations
This project has no builtin translation support, use something like [Django Model Translation](http://django-modeltranslation.readthedocs.io) or similar.

