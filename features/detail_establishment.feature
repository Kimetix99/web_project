Feature: Detail establishment
  In order to know more about an establishment
  As a user
  I want to be able to know the names, the address, the contact information and the image

  Background: There are some establishments.
    Given There are establishments
      | user        | password | name     | address     | mail                 | mobile    |
      | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | Atope    | C.Majo n 10 | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | Pecadets | C.Majo n 11 | pecadets@gmail.com   | 300000003 |
  
  Scenario: Show establishment information
    When I visit the establishment with name "Tremola"
    Then I view all of the establishment information. 
      | name     | address     | mail                 | mobile    | user        |
      | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 | Tremola     |

