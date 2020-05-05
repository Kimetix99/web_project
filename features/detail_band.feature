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

  Scenario: Show band information
    When I show all of the band information. 
      | web_link                             | playlist                                    | mail                 | mobile    |
      | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 |
      | https://soundcloud.com/drei-jazz     |  https://soundcloud.com/dj-elye/sets/jazz   | atope@gmail.com      | 200000002 |
      | https://soundcloud.com/tessatioarina |  https://soundcloud.com/dj-elye/sets/jazz   | pecadets@gmail.com   | 300000003 |
    And The list contains 3 bands