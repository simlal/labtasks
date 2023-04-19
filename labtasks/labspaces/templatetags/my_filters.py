from django import template

register = template.Library()

@register.filter
def get_timesince(timesince_last_message, labspace_id):
    return timesince_last_message.get(labspace_id, 'No messages yet')

@register.simple_tag
def is_same_user_as_previous(messages, current_message):
    for i, message in enumerate(messages):
        if message == current_message and i > 0:
            return messages[i-1].user == current_message.user
    return False

@register.simple_tag
def get_alignment(messages, current_message):
    alignment = "center-left"
    prev_user = None
    for message in messages:
        if message.user != prev_user and prev_user is not None:
            if alignment == "center-left":
                alignment = "center-right"
            else:
                alignment = "center-left"
        if message == current_message:
            return alignment
        prev_user = message.user
    return alignment
