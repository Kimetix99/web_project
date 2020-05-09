Feature: Create Event
  In order to create an Event
  As a establishment owner
  I want to create an event along with its name, the band list, state, date and description and I want the
    establishment set as the owner.
<<<<<<< HEAD

  Background: There are registered user, an establishment created by one of them, and there is also a band created by one of them.
    Given There are Establishments
      | user        | password | name     | address     | mail                 | mobile    |
      | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
    And There are bands
      | user          | password | web_link                             | playlist                                                        | mail                 | mobile    | name      |
      | Skeewiff      | patata   | https://soundcloud.com/skeewiff      |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | skeewiff@gmail.com   | 100000001 | skeewiff  |


  Scenario: 
    Given I'm logged as user "Tremola" with password "patata"
    When I try to create an event
    And I fill the form with
      |  name            |  state          |  date      |  description  | submit_name  |
      |  Acampada Jove   |  Searching      |  1/2/2021  |  Large descr  | eventsubmit  | 
    Then I view all of the event information. 
      |  name            |  state  |  date            |  description  |  establishment  |
      |  Acampada Jove   |  SR     |  Jan, 2 2021     |  Large descr  |  Tremola        |

=======
>>>>>>> bf844a963f27538a6b877c3878a529cda227e7d7
