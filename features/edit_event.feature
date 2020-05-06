Feature: Edit an event
  In order to change the parameters of the event
  As the owner of the establishement owner of the event
  I want to be able to edit the name, the band list, the state, the date, and the description.

  Background: There are registered users, an establishment created by one of them, and an event organized in that establishment
    Given Exists user "user1" with password "password"
    And Exists user "user2" with password "password"
    And Exists establishment registered by "user1"
      | name            | address         | email     | mobile      | image             |
      | Bar The Bar     | Carrer Major, 2 | a@a.com   | 123456789   | features/img.png  |
    And Exists band registered by "user2"
      | web_link            | playlist                                                      | email     | mobile    | image             |
      | https://google.com  | https://soundcloud.com/djhostyle/sets/top-reggaeton-2020-hits | a@a.com   | 123456789 | features/img.png  |
    And Exists event at establishment "Bar The Bar"
      | name            | band            | state     | date        | description       |
      | Event 1         | c@c.com         | SR        | 1           | descr             |

  Scenario: Edit owned event
    Given I login as user "user1" with password "password"
    When I view the details for event "Event 1"
    And I edit the current event
      | state   |
      | CL      |
    Then I'm viewing the details page for event at establishment "Bar The Bar" by "user1"
      | name            | band            | state     | date        | description       |
      | Event 1         | c@c.com         | CL        | 1           | descr             |
    And There are 1 events

  Scenario: Try to edit event but not logged in
    Given I'm not logged in
    When I view the details for event "Event 1"
    Then There is no "edit" link available

  Scenario: Try to edit event but now the owner
    Given I login as user "user2" with password "password"
    When I view the details for event "Event 1"
    Then There is no "edit" link available
