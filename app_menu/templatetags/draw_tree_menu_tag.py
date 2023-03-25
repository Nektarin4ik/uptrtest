from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

from app_menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name, parent=None):
    request = context['request']
    active_url = request.path
    menu_items = MenuItem.objects.all().prefetch_related('parent', 'children')
    print(parent)

    def build_menu_items(parent, depth=0, ancestor_items=''):
        if parent:
            items = parent.children.all()
        else:
            items = menu_items.filter(name=menu_name)
        menu_html = f'<ul>' if parent else '<ul>'
        for item in items:
            is_active = item.url == active_url
            active_class = 'active' if is_active else ''
            url = reverse(item.url) if item.url.startswith('name:') else item.url
            menu_html += f'<li class="{active_class}"><a href="{url}">{item.name}</a>'
            if depth < 2 and item.children.exists():
                menu_html += build_menu_items(item, depth=depth + 1)
            menu_html += '</li>'
        menu_html += '</ul>'
        return menu_html

    return mark_safe(build_menu_items(None))


