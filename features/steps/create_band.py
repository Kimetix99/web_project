from behave import *
from util import from_row_to_dict

use_step_matcher("parse")


@given(u'Exists user "{user}" with password "{password}"')
def step_impl(context, user, password):
    from django.contrib.auth import get_user_model
    get_user_model().objects.create_user(username=user, password=password, email='b@b.c')


@given(u'I\'m logged as user "{user}" with password "{password}"')
def step_impl(context, user, password):
    context.browser.visit(context.get_url('/accounts/login/?next=/band/create/)'))
    context.browser.fill('username', user)
    context.browser.fill('password', password)
    context.browser.find_by_name('loginsubmit').first.click()

@when(u'I fill the form with')
def step_impl(context):
    for row in context.table:
        for head in row.headings:
            if head == 'submit_name':
                continue
            if head == 'state':
                context.browser.find_by_name(head).select_by_text(row[head])
                continue
            context.browser.fill(head, row[head])
        context.browser.find_by_name(row['submit_name']).first.click()

@then(u'I\'m viewing detail page of band with web_link "{web}" playlist "{playlist}" contacte_email "{mail}" contacte_mobil "{mobile}"')
def step_impl(context, web, playlist, mail, mobile):
    from apps.main.models import Band
    for row in context.table:
        kwargs = from_row_to_dict(row)
        assert context.browser.url == context.get_url(Band.objects.filter(**kwargs).first())

@when(u'I try to establish a band')
def step_impl(context):
    context.browser.visit(context.get_url('band_create'))


@then(u'I\'m viewing login page with "{next_page}"')
def step_impl(context, next_page):
    assert context.browser.url == context.get_url(f'/accounts/login/?next={next_page}')


