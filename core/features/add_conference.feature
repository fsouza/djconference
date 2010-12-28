Feature: Add a new conference
  In order to simplify my life
  As a conference manager
  I want to create a new conference on my system

  Scenario: Adding a new conference with all data
    Given that I am on the new conference page
    When I fill the conference "title" with "PythonBrasil"
    And I fill the conference "description" with "Encontro anual da comunidade Python do Brasil."
    And I click on "Save" button
    Then the conference "PythonBrasil" should be in the database
    And I should be redirected to the conferences list page
    And the conference "PythonBrasil" should appear in the list
