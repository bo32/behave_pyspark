# BDD Testing with Behave on a Pyspark project

Run the tests (at the root of the project):
```bash
$ behave
```
or 
```bash
$ python -m behave
```

Strangely, Behave cannot manage to find `findpsark` dependency when running the tests (while with `unittest` it actually does). Therefore the import of Spark is manually set up in the `pyspark_provider.py` file.

Useful documentation about Behave: 
* http://behave.github.io/behave.example/
* http://behave.readthedocs.io/en/latest/
