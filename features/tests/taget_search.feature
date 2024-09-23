# Created by dchku at 9/17/2024
Feature: Tests for target search functionality

#
  Scenario: User can search for coffee
    Given Open target main page
    When  Search for coffee
    Then Verify that correct search results shown for coffee



  Scenario: User can search for tea
    Given Open target main page
    When  Search for tea
    Then Verify that correct search results shown for tea


    Scenario Outline: User can search for product
      Given Open target main page
      When  Search for <search_word>
      Then Verify that correct search results shown for <search_result>
      Examples:
      |search_word|  |search_result|
      |coffee     |  |coffee       |
      |mug        |  |mug          |
      |speaker    |  |speaker      |


Scenario: User can verify item in the cart
    Given Open target main page
    When  Search for coffee
    And   Add product to cart
    And   view cart
    Then  Verify product is shawn in the cart











#Feature: Target Sign In Navigation
#
#  Scenario: Logged Out User Navigates to Sign In Form
#    Given Open target main page
#    When  click on the Sign In link
#    And click on the Sign In button from the right-side navigation menu
#    Then The expected outcome is seeing the Sign In form




