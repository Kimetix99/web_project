from behave import *
use_step_matcher("parse")


@when(u'I visit the event with name "{event_name}"')
def step_impl(context, event_name):
    from apps.main.models import Event
    event = Event.objects.get(name = event_name)
    context.browser.visit(context.get_url(event))


@then(u'I view all of the event information.')
def step_impl(context):
    names = context.browser.find_by_name('name')
    state = context.browser.find_by_name('state')
    # date = context.browser.find_by_name('date')
    description = context.browser.find_by_name('description')
    establishment = context.browser.find_by_name('establishment')
    for i, row in enumerate(context.table):
        assert row['name'] == names[i].text
        assert row['state'] == state[i].text
        # assert row['date'] == date[i].text
        assert row['description'] == description[i].text
        assert row['establishment'] == establishment[i].text



