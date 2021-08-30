from django import template
from ..forms import ContactForm

register = template.Library()


@register.inclusion_tag("contact/tags/form.html")
def contact_form():
    # from movie_project.contact.forms import ContactForm
    return {"contact_form": ContactForm()}