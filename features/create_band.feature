Feature: Create Band
  In order to create a band
  As a user
  I want to create a band along with its web link, playlist, contact information and image, and I want to be
  set as the owner.

  Background:
    Given Exists user "user" with password "password"

  Scenario:
    Given I'm logged as user "user" with password "password"
    When I try to establish a band
    And I fill the form with
      | web_link           |  playlist                                                    |  email   | mobile | name        |  submit_name |
      | https://google.com | https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0 | a@a.com  | 123780 | itaca band  |  bandsubmit  | 
    Then I view all of the band information. 
      | name        | web_link                | mail      | mobile |
      | itaca band  | https://google.com      | a@a.com   | 123780 |

  Scenario:
    When I try to establish a band
    Then I'm viewing login page with "/band/create"

