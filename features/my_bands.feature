Feature: List all of my bands
  In order to list all of my bands the bands
  As a user
  I want to list all of my bands the bands.

  Background: There are some bands.
    Given There are bands
      | user        | password | name       | web_link                             | playlist                                                        | mail                 | mobile    |
      | Tremola     | patata   | itaca band | https://soundcloud.com/skeewiff      |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | els manel  | https://soundcloud.com/drei-jazz     |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | metallica  | https://soundcloud.com/tessatioarina |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | pecadets@gmail.com   | 300000003 |
    And There are some more bands
      |  user       |  name               | web_link                             | playlist                                                        | mail                   | mobile    |
      | Tremola     | estrellats          | https://soundcloud.com/skeewiff      |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | estrellats@gmail.com   | 100000001 |
      | Tremola     | amics de les arts   | https://soundcloud.com/drei-jazz     |  https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0   | adla@gmail.com         | 200000002 |

  Scenario: List my bands
    Given I'm logged as user Tremola and password patata
    When I list my bands
    Then I'm viewing a list containing some of the bands
      | name                | mail                  | mobile    |
      | itaca band          | tremola@gmail.com     | 100000001 |
      | estrellats          | estrellats@gmail.com  | 200000002 |
      | amics de les arts   | adla@gmail.com        | 300000003 |
    And The list contains 3 bands
