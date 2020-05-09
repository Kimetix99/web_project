"""
Functions to make the life easier
"""

def delete_from_model(context, model, **kwargs):
    kwargs = kwargs['kwargs']
    pr = model.objects.filter(**kwargs).first()
    print(f'{model.__name__.lower()}/delete/{pr.pk}')
    context.browser.visit(context.get_url(f'/{model.__name__.lower()}/delete/{pr.pk}'))
    

def has_from_model(model, **kwargs):
    kwargs = kwargs['kwargs']
    return model.objects.filter(**kwargs).first() != None

