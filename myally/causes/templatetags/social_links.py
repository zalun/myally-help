from django import template

register = template.Library()


@register.filter(name="whatsapp")
def whatsapp(value):
    return "".join(i for i in value if i.isdigit())
