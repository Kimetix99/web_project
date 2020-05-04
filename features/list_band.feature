Feature: List all bands
  In order to list all the bands
  As a user
  I want to list all the bands.

  Background: There are some bands.
    Given There are bands
      | user        | password | web_link                             | playlist                                    | mail                 | mobile    |
      | Tremola     | patata   | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | https://soundcloud.com/drei-jazz     |  https://soundcloud.com/dj-elye/sets/jazz   | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | https://soundcloud.com/tessatioarina |  https://soundcloud.com/dj-elye/sets/jazz   | pecadets@gmail.com   | 300000003 |
  
  Scenario: List them all
    When I list bands
    Then I'm viewing a list containing some of the bands
      | mail                 | mobile    |
      | tremola@gmail.com    | 100000001 |
      | atope@gmail.com      | 200000002 |
      | pecadets@gmail.com   | 300000003 |
    And The list contains 3 bands
