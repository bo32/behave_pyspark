# BDD Testing with Behave on a Pyspark project

Run the tests (at the root of the project):
```bash
$ behave
```
or 
```bash
$ python -m behave
```

The aim of having 2 BDD tests is to show that the unique Spark session (initialized in `features/environment.py`) is provided to the 2 test executions.

Strangely, Behave cannot manage to find `findpsark` dependency when running the tests (while with `unittest` it actually does). Therefore the import of Spark is manually set up in the `features/pyspark_provider.py` file.

Useful documentation about Behave: 
* http://behave.github.io/behave.example/
* http://behave.readthedocs.io/en/latest/
