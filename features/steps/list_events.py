from behave import *
use_step_matcher("parse")

@given(u'There are events')
def step_impl(context):
    from apps.main.models import Event, Band, Establishment
    from django.utils import timezone
    for row in context.table:
        date = timezone.now() + timezone.timedelta(days=int(row['date']))
        band = Band.objects.get(email=row['band'])
        est = Establishment.objects.get(name=row['establishment'])
        ev = Event(
                name=row['name'],
                state=row['state'],
                date=date,
                description=row['description'],
                establishment=est
                )
        ev.save()
        ev.band.add(band)
        ev.save()

@when(u'I list events')
def step_impl(context):
    context.browser.visit(context.get_url('event_list'))


@then(u'I\'m viewing a list containing some of the events')
def step_impl(context):
    names = context.browser.find_by_name('list_name')
    descriptions = context.browser.find_by_name('list_description')
    for i, row in enumerate(context.table):
        assert row['name'] in names[i].text
        assert row['description'] == descriptions[i].text

@then(u'The list contains {count:n} events')
def step_impl(context, count):
    assert count == len(context.browser.find_by_name('list_name'))


