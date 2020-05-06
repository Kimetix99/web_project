from behave import *
use_step_matcher("parse")


@given(u'Exists band registered by "user2"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists band registered by "user2"')


@given(u'Exists event at establishment "Bar The Bar"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists event at establishment "Bar The Bar"')


@when(u'I view the details for event "Event 1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I view the details for event "Event 1"')


@when(u'I edit the current event')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit the current event')


@then(u'I\'m viewing the details page for event at establishment "Bar The Bar" by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for event at establishment "Bar The Bar" by "user1"')


@then(u'There are 1 events')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 events')


@given(u'I\'m not logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m not logged in')