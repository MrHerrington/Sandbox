from datetime import datetime, date
from pyspark.sql import SparkSession, Row


spark = SparkSession.builder.getOrCreate()  # create spark session

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])

########################################################################################################################

df.show(1)  # limit df to 1 row

spark.conf.set('spark.sql.repl.eagerEval.enabled', True)  # eager evaluation in notebooks such as Jupyter
df.show()

df.show(1, vertical=True)  # the rows can also be shown vertically

print(df.columns)  # get list of column names

df.printSchema()  # get df schema

df.select("a", "b", "c").describe().show()  # show the summary of the df

print(df.collect())  # collects the distributed data to the driver side as the local data in Python
# in order to avoid throwing an out-of-memory exception, use DataFrame.take() or DataFrame.tail()
print(df.take(1))
print(df.tail(1))

print(df.toPandas())  # conversion spark df to pandas df
