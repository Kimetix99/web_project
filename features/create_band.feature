Feature: Create Band
  In order to create a band
  As a user
  I want to create a band along with its web link, playlist, contact information and image, and I want to be
  set as the owner.

  Background:
    Given Exists user "user" with password "password"

  Scenario:
    Given I'm registrated as user "user" with password "password"
    When I try to establish as band with web_link "https://google.com" playlist "https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0" contacte_email "a@a.com" contacte_mobil "123780"
    Then I'm viewing detail page of band with web_link "https://google.com" playlist "https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0" contacte_email "a@a.com" contacte_mobil "123780"

  Scenario:
    When I try to establish a band
    Then I'm viewing login page.

