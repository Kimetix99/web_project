Feature: Edit a Establishement
  In order to change the parameters of the establishment
  As the owner of the establishment
  I want to be able to edit the name, address, contact, and image.

  Background: There are registered users and an establishment by one of them
    Given Exists user "user2" with password "password"
    And There are establishments
     | user        | password | name     | address     | mail                 | mobile    |
     | user1       | password | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |


  Scenario: Edit owned establishment registry email
    Given I'm logged as user "user1" with password "password"
    When I visit the establishment with name "Tremola"
    And I click button named "edit"
    And I fill camp "name" with value "Cremola"
    And I click button named "establishmenteditsubmit"
    Then I view all of the establishment information. 
      | name     | address     | mail                 | mobile    | user   |
      | Cremola  | C.Major n 9 | tremola@gmail.com    | 100000001 | user1  |
    And There are 1 establishments

  Scenario: Try to edit establishment but not logged in
    When I visit the establishment with name "Tremola"
    Then There is no name "edit"

  Scenario: Try to edit establishment but not the owner no edit button
    Given I'm logged as user "user2" with password "password"
    When I visit the establishment with name "Tremola"
    Then There is no name "edit"

  #Scenario: Force edit establishment but not the owner permission exception
    #Given I'm logged as user "user2" with password "password"
    #When I try to visit edit page of establishment "Tremola"
    #Then Title is "403 Forbidden"
    #Then Server responds with page containing 403
    # See edit_band.feature to know the reasons for the comment

