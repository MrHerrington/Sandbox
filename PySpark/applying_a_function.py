from datetime import datetime, date
import pandas as pd
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import pandas_udf


spark = SparkSession.builder.getOrCreate()  # create spark session

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])

########################################################################################################################

# Case №1


@pandas_udf('long')
def pandas_plus_one(series: pd.Series) -> pd.Series:
    # Simply plus one by using pandas Series.
    return series + 1


df.select(pandas_plus_one(df.a)).show()


# Case №2


def pandas_filter_func(iterator):
    for pandas_df in iterator:
        yield pandas_df[pandas_df.a == 1]


df.mapInPandas(pandas_filter_func, schema=df.schema).show()
