Feature: BDD using a Spark context and a Datatable

    @fixture.spark.session
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