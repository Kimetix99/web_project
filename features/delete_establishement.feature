Feature: Delete a Establishement
  In order to delete an establishment
  As the owner of the establishment
  I want to be able to delete my establishment instance

  Background: There are some establishments.
    Given There are establishments
      | user        | password | name     | address     | mail                 | mobile    |
      | Tremola     | patata   | Tremola  | C.Major n 9 | tremola@gmail.com    | 100000001 |
      | Atope       | patata   | Atope    | C.Majo n 10 | atope@gmail.com      | 200000002 |
      | Pecadets    | dracs    | Pecadets | C.Majo n 11 | pecadets@gmail.com   | 300000003 |

    Scenario: 
      Given Exists user "user" with password "password"
      And I am the owner of the establishment "Atope"
      When I try deleting the establishment "Tremola"
      Then




    Scenario:
      Given Exists user "user" with password "password"
      And I am the owner of the band "Tremola"
      When I try deleting the band "Tremola"
      Then There is no band with the name of the deleted band
      And I'm viewing home
