from behave import *

use_step_matcher("re")

@when(u'I create a establishment')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url(''))
        if context.browser.url == context.get_url(''):
            form = context.browser.find_by_tag('').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('submit').first.click()


@then(u'I\'m viewing the details page for establishment by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for establishment by "user"')


@then(u'There are 1 establishment')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 establishment')