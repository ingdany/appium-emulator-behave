from behave import given, when, then
# from features.pages.setup_pages import SetupPages

@given("The App is launched")
def step_impl(context):
    pass

@when("User click the Next button")
def step_impl(context):
    context.setup_pages.click_next_button()

@when("User click the Next Get Started button")
def step_impl(context):
    print("User click the Next Get Started button")


@when("User click the Agree and Continue button")
def step_impl(context):
    print("User click the Agree and Continue button")


@when('User selects "{country}" from Countries List')
def step_impl(context):
    print(f"User selects {context.country} from Countries List")


@when('User selects "{city}" in the Clinics List')
def step_impl(context):
    print(f"User selects {context.city} in the Clinics List")


@when('User sets Phone Number "{phone}" and click Next button')
def step_impl(context):
    print(f'User sets Phone Number "{context.phone}" and click Next button')


@when('User sets "{pin}" as the Security Pin Number')
def step_impl(context):
    print(f'User sets "{context.pin}" as the Security Pin Number')


@then("User can access to the Patient List Page")
def step_impl(context):
    print("User can access to the Patient List Page")
