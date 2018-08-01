@fixture.spark.session
Feature: Sample case of BDD using a Spark context

    Scenario: Do a simple Spark operation
        Given I have a simple dataframe 2x1
        When I duplicate the initial columns 2 times
        And I duplicate the initial rows 1 times
        Then I should have 12 cells in all