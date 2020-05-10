Feature: Detail band
  In order to know more about a band
  As a user
  I want to be able to know their web link, contact information, the image and I want to be able to listen
    to their playlist.

  Background: There are some bands.
    Given There are bands
      | user        | password | name       | web_link                             |  playlist                                                       | mail                 | mobile    |
      | Tremola     | patata   | itaca band | https://soundcloud.com/skeewiff      |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | els manel  | https://soundcloud.com/drei-jazz     |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | metallica  | https://soundcloud.com/tessatioarina |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | pecadets@gmail.com   | 300000003 |

  Scenario: Show band information
    When I visit the band with name "itaca band"
    Then I view all of the band information. 
      | name        | web_link                             | mail                 | mobile    |
      | itaca band  | https://soundcloud.com/skeewiff      | tremola@gmail.com    | 100000001 |
