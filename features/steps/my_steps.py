from behave import *

use_step_matcher("parse")

@given(u'There are some more bands')
def step_impl(context):
    from apps.main.models import Band
    from django.contrib.auth import get_user_model
    User = get_user_model()
    for row in context.table:
        user = User.objects.get(username=row['user'])
        Band(
                name=row['name'],
                web_link=row['web_link'],
                playlist=row['playlist'],
                email=row['mail'],
                mobile=row['mobile'],
                user=user
                ).save()


@when(u'I list my bands')
def step_impl(context):
    raise NotImplementedError('Needs the web!')

@when(u'I get my establishment')
def step_impl(context):
    raise NotImplementedError('Needs the web!')
