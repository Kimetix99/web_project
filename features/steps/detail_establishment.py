from behave import *
use_step_matcher("parse")


@when(u'I visit the establishment with name "{establishment_name}"')
def step_impl(context, establishment_name):
    from apps.main.models import Establishment
    establishment = Establishment.objects.get(name = establishment_name)
    context.browser.visit(context.get_url(establishment))


@then(u'I view all of the establishment information.')
def step_impl(context):
    from apps.main.models import Establishment
    name = context.browser.find_by_name('name')
    address = context.browser.find_by_name('address')
    mail = context.browser.find_by_name('mail')
    mobile = context.browser.find_by_name('mobile')
    user_name = context.browser.find_by_name('user_name')
    for i, row in enumerate(context.table):
        print(name[i].text, address[i].text, mail[i].text, mobile[i].text, user_name[i].text)
        assert row['name'] in name[i].text, f"{row['name']}, {name[i].text}"
        print('name done')
        assert row['address'] == address[i].text, f'{row["address"]} == {address[i].text}'
        print('name done')
        assert row['mail'] == mail[i].text, f'{row["mail"]} == {mail[i].text}' 
        print('name done')
        assert row['mobile'] == mobile[i].text, f'{row["mobile"]} == {mobile[i].text}'
        print('name done')
        assert row['user'] == user_name[i].text, f'{row["user"]} == {user_name[i].text}'

