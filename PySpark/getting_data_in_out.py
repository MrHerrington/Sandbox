from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()  # create spark session

df = spark.createDataFrame([
    ['red', 'banana', 1, 10],
    ['blue', 'banana', 2, 20],
    ['red', 'carrot', 3, 30],
    ['blue', 'grape', 4, 40],
    ['red', 'carrot', 5, 50],
    ['black', 'carrot', 6, 60],
    ['red', 'banana', 7, 70],
    ['red', 'grape', 8, 80]
], schema=['color', 'fruit', 'v1', 'v2'])

########################################################################################################################

# CSV format
df.write.csv('foo.csv', header=True, mode='overwrite')
df.toPandas().to_csv('foo.csv', header=True, mode='w', index=False)

spark.read.csv('foo.csv', header=True).show()

# parquet format
df.write.parquet('foo.parquet', mode='overwrite')
df.toPandas().to_parquet('foo.parquet')

# ORC format
df.write.orc('foo.orc', mode='overwrite')
df.toPandas().to_orc('foo.orc')
