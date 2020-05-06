Feature: Edit a Establishement
  In order to change the parameters of the establishment
  As the owner of the establishment
  I want to be able to edit the name, address, contact, and image.

  Background: There are registered users and an establishment by one of them
    Given Exists user "user2" with password "password"
    And There are establishments
     | user        | password | name     | address     | mail                 | mobile    |
     | user1       | password | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |





  Scenario: Edit owned establishment registry email
    Given I'm registrated as user "user1" with password "password"
    When I edit the establishment with name "Tremola"
      | email     |
      | b@b.com   |
    Then I'm viewing the details page for establishment
      | name            | address         | email     | mobile      | image             |
      | Bar The Bar     | Carrer Major, 2 | b@b.com   | 123456789   | features/img.png  |
    And There are 1 establishments

  Scenario: Try to edit establishment but not logged in
    When I visit the establishment with name "Tremola"
    Then There is no name "edit"

  Scenario: Try to edit establishment but not the owner no edit button
    Given I'm registrated as user "user2" with password "password"
    When I visit the establishment with name "Tremola"
    Then There is no name "edit"

  Scenario: Force edit establishment but not the owner permission exception
    Given I'm registrated as user "user2" with password "password"
    When I edit the establishment with name "Tremola"
      | email     |
      | b@b.com   |
    Then Server responds with page containing 403
    When I visit the establishment with name "Tremola"
    Then I'm viewing the details page for establishment
      | name     | address     | mail                 | mobile    |
      | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
