from behave import *
use_step_matcher("parse")

@given(u'There are establishments')
def step_impl(context):
    from apps.main.models import Establishment
    for i in context.table:
        print(i)
    raise NotImplementedError(u'STEP: Given There are establishments')


@when(u'I list establishments')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I list establishments')


@then(u'I\'m viewing a list containing some of the establishments')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing a list containing some of the establishments')


@then(u'The list contains 3 establishments')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The list contains 3 establishments')