from behave import *

use_step_matcher("parse")

@when(u'I try to create an event')
def step_impl(context):
    context.browser.visit(
        context.get_url('event_create')
    )


# @when(u'I fill the event form')
# def step_impl(context):
    # from apps.main.models import Band
    # for row in context.table:
        # band = Band.objects.filter(email=row['band'])
        # dicc = {h:row[h] for h in row.headings}
        # dicc['band'] = band
        # for key, value in dicc.items():
            # context.browser.fill(key, value)
        # context.browser.find_by_name('eventsubmit').first.click()

