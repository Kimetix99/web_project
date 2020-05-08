from behave import *
from util import has_from_model, delete_from_model
from apps.main.models import Event

use_step_matcher("parse")

@when(u'I try deleting the event with "{field}" "{value}"')
def step_impl(context, field, value):
    delete_from_model(context, Event, kwargs={field:value})


@then(u'There is no event with the "{field}" "{value}"')
def step_impl(context, field, value):
    assert not has_from_model(Event, kwargs={field:value})


@then(u'There is a event with "{field}" "{value}"')
def step_impl(context, field, value):
    assert has_from_model(Event, kwargs={field:value})

