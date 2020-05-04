from behave import *

use_step_matcher("parse")


@given(u'Exists user "{user}" with password "{password}"')
def step_impl(context, user, password):
    from django.contrib.auth import get_user_model
    get_user_model().objects.create_user(username=user, password=password, email='b@b.c')


@given(u'I\'m registrated as user')
def step_impl(context):
    context.browser.visit(context.get_url('/accounts/login/?next=/band/create/)'))
    context.browser.fill('username', "user")
    context.browser.fill('password', "password")
    context.browser.find_by_name('loginsubmit').first.click()

@when(u'I try to establish as band with web_link "{web}" playlist "{playlist}" contacte_email "{mail}" contacte_mobil "{mobile}"')
def step_impl(context, web, playlist, mail, mobile):
    context.browser.visit(
            context.get_url('band_create')
            )
    assert context.browser.url == context.get_url('band_create')
    context.browser.fill('web_link', web)
    context.browser.fill('playlist', playlist)
    context.browser.fill('email', mail)
    context.browser.fill('mobile', mobile)
    context.browser.find_by_name('bandsubmit').first.click()

@then(u'I\'m viewing detail page of band with web_link "{web}" playlist "{playlist}" contacte_email "{mail}" contacte_mobil "{mobile}"')
def step_impl(context, web, playlist, mail, mobile):
    from apps.main.models import Band
    band = Band.objects.filter(
            web_link=web,
            playlist=playlist,
            email=mail,
            mobile=mobile).get()
    assert context.browser.url == context.get_url(band)

@when(u'I try to establish a band')
def step_impl(context):
    context.browser.visit(context.get_url('band_create'))


@then(u'I\'m viewing login page.')
def step_impl(context):
    assert context.browser.url == context.get_url('/accounts/login/?next=/band/create')


