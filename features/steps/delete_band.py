from behave import *
from util import has_from_model, delete_from_model
from apps.main.models import Band

use_step_matcher("parse")

@then(u'I\'m vewing deletion successful page')
def step_impl(context):
    try:
        context.browser.find_by_name("successful_delation")
    except:
        assert False, "There is no name 'successful_delation'"


@when(u'I try deleting the band with "{field}" "{value}"')
def step_impl(context, field, value):
    delete_from_model(context, Band, kwargs={field:value})


@then(u'There is no band with the "{field}" "{value}"')
def step_impl(context, field, value):
    assert not has_from_model(Band, kwargs={field:value})


@then(u'There is a band with "{field}" "{value}"')
def step_impl(context, field, value):
    assert has_from_model(Band, kwargs={field:value})


@then(u'I\'m viewing deletion successful page')
def step_impl(context):
    print(context.browser.status_code)

@then(u'I\'m viewing deletion unsuccessful page')
def step_impl(context):
    try:
        context.browser.find_by_name('unsuccessful_delete').first
    except:
        assert False, "It wan not an unsuccessfully deleted page"

@then(u'Title is "{title}"')
def step_impl(context, title):
    assert context.browser.find_by_tag('title').first == title, f'{context.browser.find_by_tag("title").first} == {title}'

