Feature: Delete an event
  In order to delete an event
  As the owner of the establishment owner of the event
  I want to be able to delete my event instance

  Background: There are some events
    Given There are establishments
      | user        | password | name     | address     | mail                 | mobile    |
      | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | Atope    | C.Majo n 10 | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | Pecadets | C.Majo n 11 | pecadets@gmail.com   | 300000003 |
    And There are bands
      | user          | password | web_link                             | playlist                                    | mail                 | mobile    | name         |
      | Skeewiff      | patata   | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | skeewiff@gmail.com   | 100000001 | skeewiff     |      
      | Drei-jazz     | patata   | https://soundcloud.com/drei-jazz     |  https://soundcloud.com/dj-elye/sets/jazz   | drei-jazz@gmail.com  | 200000002 | drei-jazz    |
      | Tessatiorina  | dracs    | https://soundcloud.com/tessatioarina |  https://soundcloud.com/dj-elye/sets/jazz   | tessatio@gmail.com   | 300000003 | tessatio     |
    And There are events
      |  name            |  band                 |  state  |  date  |  description  |  establishment  |
      |  Acampada Jove   |  skeewiff@gmail.com   |  CL     |  1     |  Large descr  |  Pecadets       |
      |  Festiuet        |  drei-jazz@gmail.com  |  FN     |  -1    |  Medium desc  |  Atope          |
      |  PrimaveraSound  |  tessatio@gmail.com   |  SR     |  4     |  Short descr  |  Tremola        |




  Scenario:
    Given I'm logged as user "Tremola" with password "patata"
    When I try deleting the event with "name" "PrimaveraSound"
    Then There is no event with the "name" "PrimaveraSound"
    And Im vewing deletion successful page
    And There are 2 events

  Scenario:
    Given I'm logged as user "Tremola" with password "patata"
    When I try deleting the event with "name" "Festiuet"
    Then There is a event with "name" "Festiuet"
    And I'm viewing deletion unsuccessful page
    And There are 3 events

