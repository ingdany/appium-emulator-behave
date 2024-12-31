Feature: Setup App

  Scenario: Validate if user can access the App
    Given The App is Launched
    When User click the Next button
    And User click the Next Get Started button
    And User click the Agree and Continue button
    And User selects "Demo Country" from Countries List
    And User selects "Assam" in the Clinics List
    And User sets Phone Number "1234567890" and click Next button
    And User sets "1234" as the Security Pin Number
    # And User sets "Admin Dany" as the Role and Full Name
    # And User skip Location
    # And User selects "Araihazar One" as a Facility
    # And User Avoids the Watch Video
    Then User can access to the Patient List Page
