import six
from django.core.mail import send_mail
from django.template.context import Context
from django.utils.html import strip_tags
from django.template import Template
from django.conf import settings

from apps.email.models import EMail


def send_email(email_name, recipients, context, sender=settings.DEFAULT_FROM_EMAIL):
    """
    Send an email using a template saved in the database
    :param email_name: The name of the email template in the database
    :param recipients: A string or a list of recipients
    :param context: Context with variables rendered with the email_name subject and text templates
    :param sender: The sender of the email, default is settings.DEFAULT_FROM_EMAIL
    """
    try:
        email = EMail.objects.get(name=email_name)
    except EMail.DoesNotExist:
        raise Exception('Missing email {}, add it in the Django Admin.'.format(email_name))

    context = Context(context)

    text_template = Template(email.text)
    html_text = text_template.render(context)
    plain_text = strip_tags(html_text)
    html_text = html_text.replace('\n', '<br>\n')

    subject_template = Template(email.subject)
    subject = subject_template.render(context)

    if isinstance(recipients, six.string_types):
        recipients = [recipients]

    send_mail(subject, plain_text, sender, recipients, html_message=html_text)
