Feature: List all bands
  In order to list all the bands
  As a user
  I want to list all the bands.

  Background: There are some bands.
    Given There are bands
      | user        | password | name       | web_link                             | playlist                                                        | mail                 | mobile    |
      | Tremola     | patata   | itaca band | https://soundcloud.com/skeewiff      |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | els manel  | https://soundcloud.com/drei-jazz     |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | metallica  | https://soundcloud.com/tessatioarina |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | pecadets@gmail.com   | 300000003 |
  
  Scenario: List them all
    When I list bands
    Then I'm viewing a list containing some of the bands
      | name        | mail                 | mobile    |
      | itaca band  | tremola@gmail.com    | 100000001 |
      | els manel   | atope@gmail.com      | 200000002 |
      | metallica   | pecadets@gmail.com   | 300000003 |
    And The list contains 3 bands
