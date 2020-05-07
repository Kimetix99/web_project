"""
    Edit utils for features
"""
from behave import *

use_step_matcher("parse")

@then(u'There is no name "{name}"')
def step_impl(context, name):
    try:
        name = context.browser.find_by_name(name)
        assert False, f"It containe name {name}"
    except:
        pass  # Is expected to fail


@when(u'I fill camp "{name}" with value "{value}"')
def step_impl(context, name, value):
    context.browser.fill("name", value)


@then(u'Server responds with page containing {status_code:n}')
def step_impl(context, status_code):
    assert context.browser.status_code == status_code


@when(u'I click button named "{name}"')
def step_impl(context, name):
    context.browser.find_by_name(name).first.click()




