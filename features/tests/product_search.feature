Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown

    Feature: Tests for product page

  Scenario: User can select colors
    Given Open target product A-54551690 page
    Then Verify user can click through colors