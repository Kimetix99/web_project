Feature: Edit a band
  In order to change the parameters of the band
  As the owner of the band
  I want to be able to edit the web link, playlist, contact, and image

  Background: There are registered users and a band by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists a band registered by "user1"
      | web_link            | playlist                                                      | email     | mobile    | image             |
      | https://google.com  | https://soundcloud.com/djhostyle/sets/top-reggaeton-2020-hits | a@a.com   | 123456789 | features/img.png  |

  Scenario: Edit owned band registry email
    Given I login as user "user1" with password "password"
    When I edit the user's "user1" band
      | email     |
      | b@b.com   |
    Then I'm viewing the details page for band by "user1"
      | web_link            | playlist                                                      | email     | mobile    | image             |
      | https://google.com  | https://soundcloud.com/djhostyle/sets/top-reggaeton-2020-hits | b@b.com   | 123456789 | features/img.png  |
    And There are 1 bands

  Scenario: Try to edit band but not logged in
    Given I'm not logged in
    When I view the details for band of "user1"
    Then There is no "edit" link available

  Scenario: Try to edit band but not the owner no edit button
    Given I login as user "user2" with password "password"
    When I view the details for band of "user1"
    Then There is no "edit" link available

  Scenario: Force edit band but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the band of "user1"
      | email           |
      | b@b.com         |
    Then Server responds with page containing "403 Forbidden"
    When I view the details for band of "user1"
    Then I'm viewing the details page for band by "user1"
      | web_link            | playlist                                                      | email     | mobile    | image             |
      | https://google.com  | https://soundcloud.com/djhostyle/sets/top-reggaeton-2020-hits | a@a.com   | 123456789 | features/img.png  |
