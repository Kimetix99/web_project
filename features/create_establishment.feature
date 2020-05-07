Feature: Create Establishment
  In order to create establishment
  As a user
  I want to create an establishment along with the name, address, contact_email, contact_mobile, image, and
    owner must be set to me

    Background: There is a registrated user
      Given Exists a user "user" with password "password"

    Scenario: Create a Establishment with a name, address, contact_email, contact_mobile, image
      Given I login as user "user" with password "password"
      When I create a establishment
        | name        | address       | mobile     | image     | user      |
        | Tremola     | C.Major n 9   | 100000001  |           | Tremola   |
      Then I'm viewing the details page for establishment by "user"
        | name        | address       | mobile     | image     | user      |
        | Tremola     | C.Major n 9   | 100000001  |           | Tremola   |
      And There are 1 establishment