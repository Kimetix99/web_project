Feature: List all bands
  In order to list all the bands
  As a user
  I want to list all the bands.

  Background: There are some bands.
    Given There are bands
      | user        | password | name       | web_link                             | playlist                                    | mail                 | mobile    |
      | Tremola     | patata   | itaca band | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | els manel  | https://soundcloud.com/drei-jazz     |  https://soundcloud.com/dj-elye/sets/jazz   | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | metallica  | https://soundcloud.com/tessatioarina |  https://soundcloud.com/dj-elye/sets/jazz   | pecadets@gmail.com   | 30000000  |
  
  Scenario: List them all
    When I list bands
    Then I'm viewing a list containing some of the bands
      | name        | mail                 | mobile    |
      | itaca band  | tremola@gmail.com    | 100000001 |
      | els manel   | atope@gmail.com      | 200000002 |
      | metallica   | pecadets@gmail.com   | 300000003 |
    And The list contains 3 bands
