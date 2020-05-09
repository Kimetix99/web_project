from behave import *

use_step_matcher("parse")

@then(u'There are {num:n} events')
def step_impl(context, num):
    from apps.main.models import Event
    assert len(Event.objects.all()) == num

