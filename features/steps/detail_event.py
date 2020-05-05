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

@when(u'I show event information')
def step_impl(context):
    context.browser.visit(context.get_url('event_detail'))


@then(u'I\'m viewing of the event information.')
def step_impl(context):
    name = context.browser.find_by_name('name')
    state = context.browser.find_by_name('state')
    date = context.browser.find_by_name('date')
    description = context.browser.find_by_name('description')
    establishment = context.browser.find_by_name('establishment')
    assert row['name'] == names.text
    assert row['state'] == state.text
    assert row['date'] == date.text
    assert row['description'] == description.text
    assert row['establishment'] == establishment.text



