from behave import *

use_step_matcher("parse")

@given(u'I\'m registrated as  user "{user}" with password "{password}"')
def step_impl(context, user, password):
    from django.contrib.auth import get_user_model
    get_user_model().objects.create_user(username=user, password=password, email='tremola@gmail.com')
    context.browser.visit(context.get_url('/accounts/login/?next=/band/create/)'))
    context.browser.fill('username',user)
    context.browser.fill('password', password)
    context.browser.find_by_name('loginsubmit').first.click()


@when(u'I try deleting the band with email "tremola@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I try deleting the band with email "tremola@gmail.com"')
    


@then(u'There is no band with the email "tremola@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There is no band with the email "tremola@gmail.com"')


@then(u'I\'m viewing deletion successful page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing deletion successful page')


@given(u'I\'m registrated as user "Tremola" with password "patata"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m registrated as user "Tremola" with password "patata"')


@when(u'I try deleting the band with email "pecadets@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I try deleting the band with email "pecadets@gmail.com"')


@then(u'There is a band with email "pecadets@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There is a band with email "pecadets@gmail.com"')


@then(u'I\'m viewing deletion unsuccessful page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing deletion unsuccessful page')


