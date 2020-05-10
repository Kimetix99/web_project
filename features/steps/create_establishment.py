from behave import *

use_step_matcher("parse")

@when(u'I try to establish an establishment')
def step_impl(context):
    context.browser.visit(
        context.get_url('establishment_create')
    )

