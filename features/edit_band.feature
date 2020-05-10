Feature: Edit a band
  In order to change the parameters of the band
  As the owner of the band
  I want to be able to edit the web link, playlist, contact, and image

  Background: There are registered users and a band by one of them
    Given Exists user "user2" with password "password"
    And There are bands
      | user        | password | web_link                             |  playlist                                   | mail                 | mobile    | name              |
      | user1       | password | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | tremola@gmail.com    | 100000001 | itaca band        |

  Scenario: Edit owned band registry email
    Given I'm logged as user "user1" with password "password"
    When I visit the band with name "itaca band"
    And I click button named "edit"
    And I fill camp "email" with value "b@b.com"
    Then I view all of the band information. 
      | name        | web_link                             | playlist                                    | mail     | mobile    |
      | itaca band  | https://soundcloud.com/skeewiff      |  https://soundcloud.com/dj-elye/sets/jazz   | b@b.com  | 100000001 |
    And There are 1 bands

  Scenario: Try to edit band but not logged in
    When I visit the band with name "itaca band"
    Then There is no name "edit"

  Scenario: Try to edit a band but I am not the owner so there is no edit button
    Given I'm logged as user "user2" with password "password"
    When I visit the band with name "itaca band"
    Then There is no name "edit"

  #Scenario: Force edit band but not the owner permission exception
    #Given I'm logged as user "user2" with password "password"
    #When I try to visit edit page of band "itaca band"
    #Then Title is "403 Forbidden"
    #Then Server responds with page containing 403
    #Splinter is in beta, so even the title page or getting the h2 breaks.
    #Commented the scenario, as when splinter makes out of beta could be used
