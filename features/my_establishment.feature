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
    Given I'm logged as user "Tremola" and password "patata"
    When I get my establishment
    Then I view all of the establishment information. 
     | name     | address     | mail                 | mobile    | user        |
     | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 | Tremola     |
