@fixture.spark.session
Feature: Buy and sell some objects, with BDD using a Spark context and a Datatable

    Scenario: Buy some items listed in a Data table
        Given I have 10 euros
        And I have 0 items
        When I buy the following items
            | Label  | Quantity | Price |
            | Coffee | 3        | 1     |
            | Cake   | 1        | 3     |
            | Tea    | 2        | 0.5   |
        Then I should have 6 items in all
        And I should have 3 euros left

    Scenario: Sell some items (without checking if we have the items in stocks)
        Given I have 2 euros
        And I have 2 items
        When I sell the following items
            | Label     | Quantity | Price |
            | Apple pie | 1        | 3     |
        Then I should have 1 items in all
        And I should have 5 euros left