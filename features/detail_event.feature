Feature: Detail event
  In order to know more about an event
  As a user
  I want to be able to know the name, the band list, the state, the date, the descriptions as well as
    address and the establishment were it's going to happen.

  Background: There are some events.
    Given There are establishments
      | user        | password | name     | address     | mail                 | mobile    |
      | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | Atope    | C.Majo n 10 | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | Pecadets | C.Majo n 11 | pecadets@gmail.com   | 300000003 |
    And There are bands
      | user          | password | web_link                             | playlist                                    | mail                 | mobile    |
      | Skeewiff      | patata   | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | skeewiff@gmail.com   | 100000001 |
      | Drei-jazz     | patata   | https://soundcloud.com/drei-jazz     |  https://soundcloud.com/dj-elye/sets/jazz   | drei-jazz@gmail.com  | 200000002 |
      | Tessatiorina  | dracs    | https://soundcloud.com/tessatioarina |  https://soundcloud.com/dj-elye/sets/jazz   | tessatio@gmail.com   | 300000003 |
    And There are events
      |  name            |  band                 |  state  |  date  |  description  |  establishment  |
      |  Acampada Jove   |  skeewiff@gmail.com   |  CL     |  1     |  Large descr  |  Pecadets       |
      |  Festiuet        |  drei-jazz@gmail.com  |  FN     |  -1    |  Medium desc  |  Atope          |
      |  PrimaveraSound  |  tessatio@gmail.com   |  SR     |  4     |  Short descr  |  Tremola        |


  Scenario: Show event information
    When I show event information
    Then I'm viewing of the event information.
      |  name            |  band                 |  state  |  date  |  description  |  establishment  |
      |  Acampada Jove   |  skeewiff@gmail.com   |  CL     |  1     |  Large descr  |  Pecadets       |
    And The list contains 1 events