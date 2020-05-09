from behave import *

use_step_matcher("re")

@given(u'Exists a user "user" with password "password"')
def step_impl(context, user, password):
    from django.contrib.auth import get_user_model
    get_user_model().objects.create_user(username=user, password=password, email='b@b.c')


@given(u'I login as user "user" with password "password"')
def step_impl(context):
    context.browser.visit(context.get_url('/accounts/login/?next=/establishment/create/)'))
    context.browser.fill('username', "user")
    context.browser.fill('password', "password")
    context.browser.find_by_name('loginsubmit').first.click()

@when(u'I create a establishment')
def step_impl(context, name, address, email, mobile):
    context.browser.visit(
        context.get_url('establishment_create')
    )
    assert context.browser.url == context.get_url('establishment_create')
    context.browser.fill('name', name)
    context.browser.fill('address', address)
    context.browser.fill('email', email)
    context.browser.fill('mobile', mobile)
    context.browser.find_by_name('establishmentsubmint').first.click()


@then(u'I\'m viewing the details page for establishment by "user"')
def step_impl(context, name, address, email, mobile):
    from apps.main.models import Establishment
    establishment = Establishment.objects.filter(
        name=name,
        address=address,
        email=email,
        mobile=mobile).get()
    assert context.browser.url == context.get_url(establishment)


@then(u'There are 1 establishment')
def step_impl(context):
    assert context.browser.url == context.get_url('/accounts/login/?next=/establishment/create')