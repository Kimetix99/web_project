Feature: Edit a Establishement
  In order to change the parameters of the establishment
  As the owner of the establishment
  I want to be able to edit the name, address, contact, and image.

  Background: There are registered users and an establishment by one of them
    Given Exists user "user1" with password "password"
    And Exists user "user2" with password "password"
    And Exists establishment registered by "user1"
      | name            | address         | email     | mobile      | image             |
      | Bar The Bar     | Carrer Major, 2 | a@a.com   | 123456789   | features/img.png  |

  Scenario: Edit owned establishment registry email
    Given I login as user "user1" with password "password"
    When I edit the establishment with name "Bar The Bar"
      | email     |
      | b@b.com   |
    Then I'm viewing the details page for establishment by "user1"
      | name            | address         | email     | mobile      | image             |
      | Bar The Bar     | Carrer Major, 2 | b@b.com   | 123456789   | features/img.png  |
    And There are 1 establishments

  Scenario: Try to edit establishment but not logged in
    Given I'm not logged in
    When I view the details for establishment "Bar The Bar"
    Then There is no "edit" link available

  Scenario: Try to edit establishment but not the owner no edit button
    Given I login as user "user2" with password "password"
    When I view the details for establishment "Bar The Bar"
    Then There is no "edit" link available

  Scenario: Force edit establishment but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the establishment with name "Bar The Bar"
      | email     |
      | b@b.com   |
    Then Server responds with page containing "403 Forbidden"
    When I view the details for band of "user1"
    Then I'm viewing the details page for band by "user1"
      | name            | address         | email     | mobile      | image             |
      | Bar The Bar     | Carrer Major, 2 | a@a.com   | 123456789   | features/img.png  |
