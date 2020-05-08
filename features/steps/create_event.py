from behave import *

use_step_matcher("parse")


@given(u'There is an establishment')
def step_impl(context, num):
    from apps.main.models import Establishment
    assert len(Establishment.objects.all()) == num


@given(u'There is a band')
def step_impl(context, num):
    from apps.main.models import Band
    assert len(Band.objects.all()) == num


@when(u'I create a event')
def step_impl(context, name, band, state, date, description, establishment):
    context.browser.visit(
        context.get_url('event_create')
    )
    assert context.browser.url == context.get_url('event_create')
    context.browser.fill('name', name)
    context.browser.fill('band', band)
    context.browser.fill('state', state)
    context.browser.fill('date', date)
    context.browser.fill('description', description)
    context.browser.fill('establishment', establishment)
    context.browser.find_by_name('bandsubmit').first.click()


@then(u'I\'m viewing the details page for event by "user"')
def step_impl(context, name, band, state, date, description, establishment):
    from apps.main.models import Event
    event = Event.objects.filter(
        name=name,
        band=band,
        state=state,
        date=date,
        description=description,
        establishment=establishment).get()
    assert context.browser.url == context.get_url(event)
