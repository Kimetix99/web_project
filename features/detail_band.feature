Feature: Detail band
  In order to know more about a band
  As a user
  I want to be able to know their web link, contact information, the image and I want to be able to listen
    to their playlist.

  Background: There are some bands.
    Given There are bands
      | user        | password | web_link                             | playlist                                    | mail                 | mobile    |
      | Tremola     | patata   | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | https://soundcloud.com/drei-jazz     |  https://soundcloud.com/dj-elye/sets/jazz   | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | https://soundcloud.com/tessatioarina |  https://soundcloud.com/dj-elye/sets/jazz   | pecadets@gmail.com   | 300000003 |

  Scenario:
    When I show band profile
    Then I'm viewing the band profile with all the information of the band. 
      | user        | password | web_link                             | playlist                                    | mail                 | mobile    |
      | Tremola     | patata   | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | https://soundcloud.com/drei-jazz     |  https://soundcloud.com/dj-elye/sets/jazz   | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | https://soundcloud.com/tessatioarina |  https://soundcloud.com/dj-elye/sets/jazz   | pecadets@gmail.com   | 300000003 |
