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
      Given Exists user "user" with password "password"
      And I am the owner of the band "Tremola"
      When I try deleting the band "Tremola"
      Then There is no band with the name of the deleted band
      And I'm viewing home
