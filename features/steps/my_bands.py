from behave import *
use_step_matcher("parse")

@given(u'I\'m logged as user Tremola and password patata')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m logged as user Tremola and password patata')


@when(u'I list my bands')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I list my bands')
