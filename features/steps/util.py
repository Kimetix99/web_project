"""
Functions to make the life easier
"""

def delete_from_model(model, **kwargs):
    return model.objects.filter(**kwargs).delete()

def has_from_model(model, **kwargs):
    return model.objects.filter(**kwargs).first() != None
