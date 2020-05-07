from behave import *

use_step_matcher("parse")


@when(u'I try deleting the band with email "tremola@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I try deleting the band with email "tremola@gmail.com"')
    


@then(u'There is no band with the email "tremola@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There is no band with the email "tremola@gmail.com"')


@then(u'I\'m viewing deletion successful page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing deletion successful page')


@when(u'I try deleting the band with email "pecadets@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I try deleting the band with email "pecadets@gmail.com"')


@then(u'There is a band with email "pecadets@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There is a band with email "pecadets@gmail.com"')


@then(u'I\'m viewing deletion unsuccessful page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing deletion unsuccessful page')


