from datetime import datetime, date
from pyspark.sql import SparkSession, Row, Column
from pyspark.sql.functions import upper


spark = SparkSession.builder.getOrCreate()  # create spark session

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])

########################################################################################################################

# spark df is lazily evaluated and simply selecting a column does not trigger the computation, but it returns a Column instance  # noqa: E501
print(df.a)
print(type(df.c) is type(upper(df.c)) is type(df.c.isNull()))

df.select(df.a, upper(df.c).alias('upper_c')).show()  # return new table expression
df.withColumn('upper_c', upper(df.c)).show()  # assign new column instance
df.filter(df.a == 1).show()  # selecting a subset of rows
