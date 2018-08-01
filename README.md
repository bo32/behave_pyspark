# BDD Testing with Behave on a Pyspark project

Run the tests (at the root of the project):
```bash
$ behave
```
or 
```bash
$ python -m behave
```

In order to store the test results in an output file, run as following:
```bash
$ behave -f json -o reports/results.json
```

The aim of having 2 BDD tests is to show that the unique Spark session (initialized in `features/environment.py`) is provided to the 2 test executions.

Requires `SPARK_HOME` to be defined in order to use `findspark`.

Useful documentation about Behave: 
* http://behave.github.io/behave.example/
* http://behave.readthedocs.io/en/latest/
