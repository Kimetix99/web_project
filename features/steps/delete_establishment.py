from behave import *
from apps.main.models import Establishment
from .util import delete_from_model, has_from_model

use_step_matcher("parse")

@when(u'I try deleting the establishment with "{field}" "{email}"')
def step_impl(context, field, email):
    delete_from_model(Establishment, kwargs={field=name})

    

@then(u'There is no establishment with the email "tremola@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There is no establishment with the email "tremola@gmail.com"')


@when(u'I try deleting the establishment with email "pecadets@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I try deleting the establishment with email "pecadets@gmail.com"')


@then(u'There is am establishment with the email "pecadets@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There is am establishment with the email "pecadets@gmail.com"')



