from behave import given, when, then, step

import pyspark_provider
from pyspark.sql.functions import lit

@given('I have a simple dataframe 1x1')
def step_impl(context):
    schema = ['0']
    rows = [['Test']]
    context.df = context.session.createDataFrame(rows, schema)

@when('I duplicate the columns {number:d} times')
def step_impl(context, number):
    for i in range(1, number + 1):
        context.df = context.df.withColumn(str(i), lit('Test'))

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