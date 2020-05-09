Feature: Create Event
  In order to create an Event
  As a establishment owner
  I want to create an event along with its name, the band list, state, date and description and I want the
    establishment set as the owner.

  Background: There are registered user, an establishment created by one of them, and there is also a band created by one of them.
    Given There is an establishment

    Scenario: 
    Given There are Establishments
      | user        | password | name     | address     | mail                 | mobile    |
      | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
    And There is a band
      | user          | password | web_link                             | playlist                                    | mail                 | mobile    | name      |
      | Skeewiff      | patata   | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | skeewiff@gmail.com   | 100000001 | skeewiff  |
    When I create a event
      |  name            |  band                 |  state  |  date  |  description  |  establishment  |
      |  Acampada Jove   |  skeewiff@gmail.com   |  SR     |  1     |  Large descr  |  Tremola        |
    Then I'm viewing the details page for event by "user"



    Scenario: 
    Given There are Establishments
        | user        | password | name     | address     | mail                 | mobile    |
        | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
        | Atope       | patata   | Atope    | C.Majo n 10 | atope@gmail.com      | 200000002 |
        | Pecadets    | dracs    | Pecadets | C.Majo n 11 | pecadets@gmail.com   | 300000003 |
    And There are bands
        | user          | password | web_link                             | playlist                                                        | mail                 | mobile    | name          |
        | Skeewiff      | patata   | https://soundcloud.com/skeewiff      |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | skeewiff@gmail.com   | 100000001 | Skeewiff      |
        | Drei-jazz     | patata   | https://soundcloud.com/drei-jazz     |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | drei-jazz@gmail.com  | 200000002 | Drei-jazz     |
        | Tessatiorina  | dracs    | https://soundcloud.com/tessatioarina |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | tessatio@gmail.com   | 300000003 | Tessatiorina  |
    When I crate an event
        |  name            |  band                 |  state  |  date  |  description  |  establishment  |
        |  Acampada Jove   |  skeewiff@gmail.com   |  CL     |  1     |  Large descr  |  Pecadets       |
    Then I'm viewing the details page for event by "user"






