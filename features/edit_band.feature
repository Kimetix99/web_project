Feature: Edit a band
  In order to change the parameters of the band
  As the owner of the band
  I want to be able to edit the web link, playlist, contact, and image

  Background: There are registered users and a band by one of them
    Given Exists a user "user2" with password "password"
    And There are bands
      | user        | password | web_link                             |  playlist                                   | mail                 | mobile    | name              |
      | user1       | password | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 | itaca band        |

  Scenario: Edit owned band registry email
    Given I'm registrated as user "user1" with password "password"
    When I edit the user's "user1" band
      | email     |
      | b@b.com   |
    Then I'm viewing the details page for band by "user1"
      | web_link            | playlist                                                      | email     | mobile    | image             |
      | https://google.com  | https://soundcloud.com/djhostyle/sets/top-reggaeton-2020-hits | b@b.com   | 123456789 | features/img.png  |
    And There are 1 bands

  Scenario: Try to edit band but not logged in
    When I visit the band with name "itaca band"
    Then There is no name "edit"

  Scenario: Try to edit a band but I am not the owner so there is no edit button
    Given I'm registrated as user "user2" with password "password"
    When I visit the band with name "itaca band"
    Then There is no name "edit"

  Scenario: Force edit band but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the band of "user1"
      | email           |
      | b@b.com         |
    Then Server responds with page containing 403
    When I visit the band with name "itaca band"
    Then I'm viewing the details page for band
      | name        | web_link            | playlist                                                      | email     | mobile    |
      | itaca band  | https://google.com  | https://soundcloud.com/djhostyle/sets/top-reggaeton-2020-hits | a@a.com   | 123456789 |
