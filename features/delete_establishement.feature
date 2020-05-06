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
    Given I'm registrated as user "Tremola" with password "patata"
    When I try deleting the establishment with email "tremola@gmail.com"
    Then There is no establishment with the email "tremola@gmail.com"
    And I'm viewing deletion successful page

  Scenario:
    Given I'm registrated as user "Tremola" with password "patata"
    When I try deleting the establishment with email "pecadets@gmail.com"
    Then There is am establishment with the email "pecadets@gmail.com"
    And I'm viewing deletion unsuccessful page
