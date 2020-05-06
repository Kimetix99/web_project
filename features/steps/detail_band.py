from behave import *
use_step_matcher("parse")


@when(u'I visit the band with name "{band_name}"')
def step_impl(context, band_name):
    from apps.main.models import Band
    band = Band.objects.get(name = band_name)
    context.browser.visit(context.get_url(band))


@then(u'I view all of the band information.')
def step_impl(context):
    name = context.browser.find_by_name('name')
    web_link = context.browser.find_by_name('web_link')
    playlist = context.browser.find_by_name('playlist')
    email = context.browser.find_by_name('email')
    mobile = context.browser.find_by_name('mobile')
    for i, row in enumerate(context.table):
        assert row['name'] == name[i].text
        assert row['web_link'] == web_link[i].text
        assert row['playlist'] == playlist[i].text
        assert row['mail'] == email[i].text
        assert row['mobile'] == mobile[i].text

