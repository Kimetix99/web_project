from behave import *
use_step_matcher("parse")


@given(u'Exists establishment registered by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists establishment registered by "user1"')


@when(u'I edit the establishment with name "Bar The Bar"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit the establishment with name "Bar The Bar"')


@then(u'I\'m viewing the details page for establishment by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for establishment by "user1"')


@then(u'There are 1 establishments')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 establishments')


@given(u'I\'m not logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m not logged in')


@when(u'I view the details for establishment "Bar The Bar"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I view the details for establishment "Bar The Bar"')


@then(u'I\'m viewing the details page for band by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for band by "user1"')
