import findspark
findspark.init()

# import os
# import sys
# from glob import glob

# spark_home = '/home/david/spark-2.2.1-bin-hadoop2.7'
# # python_path = 'python3'
# os.environ['SPARK_HOME'] = spark_home
# # os.environ['PYSPARK_PYTHON'] = python_path
# spark_python = os.path.join(spark_home, 'python')
# py4j = glob(os.path.join(spark_python, 'lib', 'py4j-*.zip'))[0]
# sys.path[:0] = [spark_python, py4j]
