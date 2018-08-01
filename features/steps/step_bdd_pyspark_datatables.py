from behave import given, when, then, step

import pyspark_provider
from pyspark.sql import functions as F

@given('I have {number:d} items')
def step_impl(context, number):
    context.items_count = number

@when('I buy the following items')
def step_impl_(context):
    rows = [ row.cells for row in context.table ]
    df = context.session.createDataFrame(rows, context.table.headings)

    # Update the money left
    df = df.withColumn('Expense', F.col('Quantity') * F.col('Price'))
    
    expense = df.agg({'Expense': 'sum'}).collect()[0][0]
    context.amount -= expense

    # Update the amount of items
    count_bought_items = df.agg({'Quantity': 'sum'}).collect()[0][0]
    context.items_count += count_bought_items

@given('I have {number:d} euros')
def step_impl(context, number):
    context.amount = number

@then('I should have {number:d} euros left')
def step_impl(context, number):
    assert(context.amount == number)

@then('I should have {number:d} items in all')
def step_impl(context, number):
    assert(context.items_count == number)


@when('I sell the following items')
def step_impl(context):
    rows = [ row.cells for row in context.table ]
    df = context.session.createDataFrame(rows, context.table.headings)
    
    # Update the money left
    df = df.withColumn('Profit', F.col('Quantity') * F.col('Price'))
    
    profit = df.agg({'Profit': 'sum'}).collect()[0][0]
    context.amount += profit

    # Update the amount of items
    count_sold_items = df.agg({'Quantity': 'sum'}).collect()[0][0]
    context.items_count -= count_sold_items