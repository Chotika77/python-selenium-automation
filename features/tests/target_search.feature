# Created by dchku at 9/17/2024
Feature: Tests for target search functionality


  Scenario: User can search for coffee
    Given Open target main page
    When  Search for coffee
    Then Verify that correct search results shown for coffee
    Then Verify product coffee in URL



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
    When  Search for mug
    And   Click on Add to Cart button
#    And   Store product name
    And   Confirm Add to Cart button from side navigation
    And   Open cart page
    Then  Verify cart has 1 item(s)
#     And   Verify cart has correct product











#Feature: Target Sign In Navigation
#
#  Scenario: Logged Out User Navigates to Sign In Form
#    Given Open target main page
#    When  click on the Sign In link
#    And click on the Sign In button from the right-side navigation menu
#    Then The expected outcome is seeing the Sign In form


Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image

