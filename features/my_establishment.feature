Feature: List all the establishments
  In order to list all the establishments
  As a user
  I want to list all the establishments.

  Background: There are some establishments.
    Given There are establishments
      | user        | password | name     | address     | mail                 | mobile    |
      | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | Atope    | C.Majo n 10 | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | Pecadets | C.Majo n 11 | pecadets@gmail.com   | 300000003 |
  
  Scenario: List them all
    Given I'm logged as user Tremola and password patata
    When I list establishments
    Then I'm viewing a list containing some of the establishments
      | name     | address     |
      | Tremola  | C.Major n 9 |
    And The list contains 1 establishments
