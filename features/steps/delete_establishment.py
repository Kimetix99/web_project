from behave import *
from apps.main.models import Establishment
from util import delete_from_model, has_from_model

use_step_matcher("parse")

@when(u'I try deleting the establishment with "{field}" "{value}"')
def step_impl(context, field, value):
    delete_from_model(context, Establishment, kwargs={field:value})
    

@then(u'There is no establishment with the "{field}" "{value}"')
def step_impl(context, field, value):
    assert not has_from_model(Establishment, kwargs={field:value})


@then(u'There is an establishment with the "{field}" "{value}"')
def step_impl(context, field, value):
    assert has_from_model(Establishment, kwargs={field:value})


