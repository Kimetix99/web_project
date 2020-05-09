Feature: Create Establishment
  In order to create establishment
  As a user
  I want to create an establishment along with the name, address, email, mobile, image, and
    owner must be set to me

    Background: There is a registrated user
      Given Exists a user "user" with password "password"

    Scenario: Create a Establishment with a name, address, email, mobile, image
      Given I login as user "user" with password "password"
      When I create a establishment
        | user        | password | name     | address     | mail                 | mobile    |
        | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
      Then I'm viewing the details page for establishment by "user"
        | user        | password | name     | address     | mail                 | mobile    |
        | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
      And There are 1 establishment
