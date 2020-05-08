Feature: Delete a band
  In order to delete an band
  As the owner of the band
  I want to be able to delete my band instance

  Background:  There are some bands
    Given There are bands
      | user        | password | name       | web_link                             | playlist                                    | mail                 | mobile    |
      | Tremola     | patata   | itaca band | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | els manel  | https://soundcloud.com/drei-jazz     |  https://soundcloud.com/dj-elye/sets/jazz   | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | metallica  | https://soundcloud.com/tessatioarina |  https://soundcloud.com/dj-elye/sets/jazz   | pecadets@gmail.com   | 300000003 |


  Scenario:
    Given I'm logged as user "Tremola" with password "patata"
    When I try deleting the band with "email" "tremola@gmail.com"
    And I click button named "delete"
    Then There is no band with the "email" "tremola@gmail.com"
    #And Server responds with page containing 302
    Then There are 2 bands

  Scenario:
    Given I'm logged as user "Tremola" with password "patata"
    When I try deleting the band with "email" "pecadets@gmail.com"
    Then There is a band with "email" "pecadets@gmail.com"
    #And Server responds with page containing 403
    And There are 3 bands
