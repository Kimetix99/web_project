Feature: Create Event
  In order to create an Event
  As a establishment owner
  I want to create an event along with its name, the band list, state, date and description and I want the
    establishment set as the owner.

  Background: There are registered user, an establishment created by one of them, and there is a band also created by one of them.
    Given There is an establishment

  Scenario: Create a Band with a name, band list, state, date, description
      | user        | password | name     | address     | mail                 | mobile    |
      | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
    And There is a band
      | user          | password | web_link                             | playlist                                    | mail                 | mobile    | name      |
      | Skeewiff      | patata   | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | skeewiff@gmail.com   | 100000001 | skeewiff  |
    When I create a event
      |  name            |  band                 |  state  |  date  |  description  |  establishment  |
      |  Acampada Jove   |  skeewiff@gmail.com   |  SR     |  1     |  Large descr  |  Tremola        |
    Then I'm viewing the details page for event by "user"