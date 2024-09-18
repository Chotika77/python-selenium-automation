# Created by dchku at 9/17/2024
#Feature: Tests for target search functionality
#  # Enter feature description here
#
#  Scenario: User can search for a product
#    Given Open target main page
#    When  Search for a product
#    Then Verify that correct search results are shown

Feature: Shopping Cart Verification on Target

  Scenario: User can Verify Empty Cart Message
       Given Open target main page
       When click on the cart icon
       Then  I should see the message "Your cart is empty"


Feature: Target Sign In Navigation

  Scenario: Logged Out User Navigates to Sign In Form
    Given Open target main page
    When  click on the Sign In link
    And click on the Sign In button from the right-side navigation menu
    Then The expected outcome is seeing the Sign In form




