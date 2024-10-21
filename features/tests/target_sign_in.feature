# Created by dchku at 10/17/2024
Feature: Tests for target search functionality


  # Enter feature description here

  Scenario: Logged out user can access Sign in
    Given Open target main page
    When click on the Sign In icon
    And click on the Sign In button from the right-side navigation menu
    Then The expected outcome is seeing the Sign In form