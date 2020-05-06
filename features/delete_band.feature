Feature: Delete a band
  In order to delete an band
  As the owner of the band
  I want to be able to delete my band instance

  Background:  There are some bands
    Given There are bands
      | user        | password | web_link                             | playlist                                    | mail                 | mobile    |
      | Tremola     | patata   | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | https://soundcloud.com/drei-jazz     |  https://soundcloud.com/dj-elye/sets/jazz   | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | https://soundcloud.com/tessatioarina |  https://soundcloud.com/dj-elye/sets/jazz   | pecadets@gmail.com   | 300000003 |


    Scenario:
      Given I'm registrated as user "Tremola" with password "patata"
      When I try deleting the band with email "tremola@gmail.com"
      Then There is no band with the email "tremola@gmail.com"
      And I'm viewing home
