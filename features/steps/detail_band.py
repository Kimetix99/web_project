from behave import *
use_step_matcher("parse")

@given(u'There are bands')
def step_impl(context):
    from apps.main.models import Band
    from django.contrib.auth import get_user_model
    User = get_user_model()
    for row in context.table:
        user = User.objects.create_user(
                username=row['user'], password=row['password']
                )
        Band(
                web_link=row['web_link'],
                playlist=row['playlist'],
                email=row['mail'],
                mobile=row['mobile'],
                user=user
                ).save()


@when(u'Show band information')
def step_impl(context):
    context.browser.visit(context.get_url('band_detail'))


@then(u'I show all of the band information.')
def step_impl(context):
    web_link = context.browser.find_by_name('web_link')
    playlist = context.browser.find_by_name('playlist')
    contacte_email = context.browser.find_by_name('contacte_email')
    contacte_mobil = context.browser.find_by_name('contacte_mobil')
    assert row['web_link'] == web_link.text
    assert row['playlist'] == playlist.text
    assert row['contacte_email'] == contacte_email.text
    assert row['contacte_mobil'] == contacte_mobil.text

