from behave import given, when, then, step

import pyspark_provider
from pyspark.sql.functions import lit

@given('I have a simple dataframe {n_rows:d}x{n_cols:d}')
def step_impl(context, n_rows, n_cols):
    schema = [ str(i) for i in range(0, n_cols) ]
    
    rows = []
    row = ['Test' for i in range(0, n_cols)]
    for i in range(0, n_rows):
        rows.append(row)
    
    context.df = context.session.createDataFrame(rows, schema)

@when('I duplicate the initial columns {number:d} times')
def step_impl(context, number):
    n_cols = len(context.df.columns)
    for i in range(0, n_cols * number):
        context.df = context.df.withColumn(str(i + n_cols), lit('Test'))

@when('I duplicate the initial rows {number:d} times')
def step_impl(context, number):
    tmp = context.df
    for i in range(0, number):
        context.df = context.df.union(tmp)


@then('I should have {number:d} cells in all')
def step_impl(context, number):
    count_cols = len(context.df.columns)
    count_rows = context.df.count()
    assert(count_cols * count_rows == number)