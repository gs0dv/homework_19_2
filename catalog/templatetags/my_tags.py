from django import template

register = template.Library()

url_default_image = 'https://rublevbar.com/files/oldestate/image/no_product.jpg'


def build_path(val):
    if val:
        return f'/media/{val}'

    return url_default_image


@register.filter()
def mediapath(val):
    return build_path(val)


@register.simple_tag
def mediapath(val):
    return build_path(val)
