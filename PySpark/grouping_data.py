from pyspark.sql import SparkSession
import pandas as pd

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

print('Case №1')
df.groupby('color').avg().show()

print('Case №2')


def plus_mean(pandas_df):
    return pandas_df.assign(v1=pandas_df.v1 - pandas_df.v1.mean())


df.groupby('color').applyInPandas(plus_mean, schema=df.schema).show()

print('Case №3')


def plus_mean(pandas_df):
    return pandas_df.assign(v1=pandas_df.v1 - pandas_df.v1.mean())


df.groupby('color').applyInPandas(plus_mean, schema=df.schema).show()

print('Case №4')
df1 = spark.createDataFrame([
    (20000101, 1, 1.0),
    (20000101, 2, 2.0),
    (20000102, 1, 3.0),
    (20000102, 2, 4.0)
], schema=('time', 'id', 'v1'))

df2 = spark.createDataFrame([
    (20000101, 1, 'x'),
    (20000101, 2, 'y')
], schema=('time', 'id', 'v2'))


def merge_ordered(l, r):
    return pd.merge_ordered(l, r)


df1.groupby('id').cogroup(df2.groupby('id')).applyInPandas(
    merge_ordered, schema='time int, id int, v1 double, v2 string').show()
