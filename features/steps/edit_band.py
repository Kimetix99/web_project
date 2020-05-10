from behave import *

use_step_matcher("parse")

@then(u'There are {num:n} bands')
def step_impl(context, num):
    from apps.main.models import Band
    assert len(Band.objects.all()) == num


@when(u'I try to visit edit page of band "{name}"')
def step_impl(context, name):
    from apps.main.models import Band
    band = Band.objects.get(name=name)
    context.browser.visit(
            context.get_url(f'/band/edit/{band.pk}/'))

