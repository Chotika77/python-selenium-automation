# Created by dchku at 9/18/2024
Feature: Tests for cart functionality


       Scenario: User can Verify Empty Cart Message
              Given Open target main page
              When click on the cart icon
              Then I should see the message "Your cart is empty"