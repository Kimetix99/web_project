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


@when(u'I show establishment profile')
def step_impl(context):
    context.browser.visit(context.get_url('establishment_detail'))


@then(u'I\'m viewing the establishment profile with all the information of the establishment')
def step_impl(context):
    from apps.main.models import Establishment
    print(len(Establishment.objects.all()))
    name = context.browser.find_by_name('name')
    address = context.browser.find_by_name('address')
    mail = context.browser.find_by_name('mail')
    mobile = context.browser.find_by_name('mobile')
    user_name = context.browser.find_by_name('user_name')
    assert row['name'] == name.text
    assert row['address'] == address.text
    assert row['mail'] == mail.text
    assert row['mobile'] == mobile.text
    assert row['user_name'] == user_name.text

