from behave import *
use_step_matcher("parse")


@given(u'Exists a user "user1" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists a user "user1" with password "password"')


@given(u'Exists a user "user2" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists a user "user2" with password "password"')


@given(u'Exists a band registered by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists a band registered by "user1"')


@given(u'I login as user "user1" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I login as user "user1" with password "password"')


@when(u'I edit the user\'s "user1" band')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit the user\'s "user1" band')


@then(u'I\'m viewing the details page for band by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for band by "user1"')


@then(u'There are 1 bands')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 bands')


@given(u'I\'m not logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m not logged in')


@when(u'I view the details for band of "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I view the details for band of "user1"')


@then(u'There is no "edit" link available')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There is no "edit" link available')


@given(u'I login as user "user2" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I login as user "user2" with password "password"')


@when(u'I edit the band of "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit the band of "user1"')


@then(u'Server responds with page containing "403 Forbidden"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Server responds with page containing "403 Forbidden"')


@then(u'I\'m viewing the details page for band by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for band by "user1"')

