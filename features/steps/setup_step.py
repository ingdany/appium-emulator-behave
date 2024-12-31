from behave import given, when, then

@given("The App is launched")
def step_impl(context):
    pass

@when("User click the Next button")
def step_impl(context):
    context.setup_pages.click_next_button()

@when("User click the Next Get Started button")
def step_impl(context):
    context.setup_pages.click_get_started_button()

@when("User click the Agree and Continue button")
def step_impl(context):
    context.setup_pages.click_agree_and_continue_button()

@when('User selects "{country}" from Countries List')
def step_impl(context, country):
    context.setup_pages.select_country(country)

@when('User selects "{city}" in the Clinics List')
def step_impl(context, city):
    context.setup_pages.select_city(city)

@when('User sets Phone Number "{phone}" and click Next button')
def step_impl(context, phone):
    context.setup_pages.set_phone_number(phone)

@when('User sets "{roleUser}" as the Role and Full Name')
def step_impl(context, roleUser):
    context.setup_pages.set_role_full_name(roleUser)

@when('User sets "{pin}" as the Security Pin Number')
def step_impl(context, pin):
    context.setup_pages.set_pin(pin)

@when("User click the Skip button")
def step_impl(context):
    context.setup_pages.click_skip_button()
    
@when('User selects "{facility}" as a Facility')
def step_impl(context, facility):
    context.setup_pages.select_facility(facility)
    

@when("User Avoids the Watch Video")
def step_impl(context):
    context.setup_pages.click_skip2_button()

@then("User can access to the Patient List Page")
def step_impl(context):
    context.setup_pages.click_allow_button()
    context.setup_pages.is_there_search_patient_button()
    pass