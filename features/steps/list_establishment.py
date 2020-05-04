from behave import *
use_step_matcher("parse")

@given(u'There are establishments')
def step_impl(context):
    from apps.main.models import Establishment
    from django.contrib.auth import get_user_model
    User = get_user_model()
    for row in context.table:
        user = User.objects.create_user(
                username=row['user'], password=row['password']
                )
        Establishment(
                name=row['name'],
                address=row['address'],
                email=row['mail'],
                mobile=row['mobile'],
                user=user
                ).save()


@when(u'I list establishments')
def step_impl(context):
    context.browser.visit(context.get_url('establishment_list'))


@then(u'I\'m viewing a list containing some of the establishments')
def step_impl(context):
    from apps.main.models import Establishment
    print(len(Establishment.objects.all()))
    establishments = context.browser.find_by_name('list_element')
    for i, row in enumerate(context.table):
        assert row['name'] == establishments[i].text

@then(u'The list contains {count:n} establishments')
def step_impl(context, count):
    assert count == len(context.browser.find_by_name('list_element'))
