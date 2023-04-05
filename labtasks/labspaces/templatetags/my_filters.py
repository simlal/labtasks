from django import template

register = template.Library()

@register.filter
def get_timesince(timesince_last_message, labspace_id):
    return timesince_last_message.get(labspace_id, 'No messages yet')