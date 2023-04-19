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
    

    for i, message in enumerate(messages):
        
        if i == 0:
            alignment = "center-left"
        
        # Switch align for all messages after pinned
        if i > 0:
            if current_message.user != messages[i - 1].user:
                if alignment == "center-left":
                    alignment = "center-right" 
                else:
                    alignment = "center-left"
            else:
                if alignment == "center-left":
                    alignment = "center-left"
                else:
                    alignment = "center-right"
        
        if message == current_message:
            return alignment
    return alignment



# @register.simple_tag
# def get_alignment(messages, current_message):
#     alignment = 'left'
#     for message in messages:
#         if message == current_message:
#             return alignment
#         alignment = 'right' if alignment == 'left' else 'left'
#     return alignment