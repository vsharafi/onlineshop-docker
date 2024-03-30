from django import template


register = template.Library()

@register.filter
def trans_number(value):
    value = str(value)
    e_to_p_table = value.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
    return value.translate(e_to_p_table)
