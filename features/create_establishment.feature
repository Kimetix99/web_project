Feature: Create Establishment
  In order to create establishment
  As a user
  I want to create an establishment along with the name, address, email, mobile, image, and
    owner must be set to be me

    Background: There is a registrated user
      Given Exists user "user" with password "password"

    Scenario: Create a Establishment with a name, address, email, mobile, image
      Given I'm logged as user "user" with password "password"
      When I try to establish an establishment
      And I fill the form with
        | name     | address     | email                 | mobile    | submit_name         |
        | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 | establishmentsubmit | 
      Then I view all of the establishment information. 
        | name     | address     | mail                 | mobile    | user        |
        | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 | user        |
      And There are 1 establishments
