from behave import *

use_step_matcher("parse")


@then(u'There are {num:n} establishments')
def step_impl(context, num):
    from apps.main.models import Establishment
    assert len(Establishment.objects.all()) == num


@when(u'I try to visit edit page of establishment "{name}"')
def step_impl(context, name):
    from apps.main.models import Establishment
    est = Establishment.objects.get(name=name)
    context.browser.visit(
            context.get_url(f'/establishment/edit/{est.pk}/'))
