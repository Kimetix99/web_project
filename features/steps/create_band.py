from behave import *

use_step_matcher("parse")


@given(u'Exists user "{user}" with password "{password}"')
def step_impl(context, user, password):
    from django.contrib.auth import get_user_model
    get_user_model().objects.create_user(username=user, password=password, email='b@b.c')


@given(u'I\'m registrated as user')
def step_impl(context):
    context.browser.visit(context.get_url('/accounts/login/?next=/band/create/)'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', "user")
    context.browser.fill('password', "password")
    form.find_by_id('id_submit').first.click()

@when(u'I try to establish as band with web_link "{web}" playlist "{playlist}" contacte_email "{mail}" contacte_mobil "{mobile}"')
def step_impl(context, web, playlist, mail, mobile):
    pass

@then(u'I\'m viewing detail page of band with web_link "{web}" playlist "{playlist}" contacte_email "{mail}" contacte_mobil "{mobile}"')
def step_impl(context, web, playlist, mail, mobile):
    print(mail)
    pass

@when(u'I try to establish a band')
def step_impl(context):
    pass

@then(u'I\'m viewing login page.')
def step_impl(context):
    pass
