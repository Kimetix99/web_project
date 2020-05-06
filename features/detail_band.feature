Feature: Detail band
  In order to know more about a band
  As a user
  I want to be able to know their web link, contact information, the image and I want to be able to listen
    to their playlist.

  Background: There are some bands.
    Given There are bands
      | user        | password | name       | web_link                             | playlist                                    | mail                 | mobile    |
      | Tremola     | patata   | itaca band | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | els manel  | https://soundcloud.com/drei-jazz     |  https://soundcloud.com/dj-elye/sets/jazz   | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | metallica  | https://soundcloud.com/tessatioarina |  https://soundcloud.com/dj-elye/sets/jazz   | pecadets@gmail.com   | 30000000  |
  Scenario: Show band information
    When I visit the band with name "itaca band"
    Then I view all of the band information. 
      | name        | web_link                             | playlist                                    | mail                 | mobile    |
      | itaca band  | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 |