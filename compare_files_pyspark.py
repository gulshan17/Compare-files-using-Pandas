# %%
from pyspark.sql import SparkSession
# %%
spark = SparkSession.builder.getOrCreate()
# %%
df1 = spark.read.csv('file1.csv', header = True, inferSchema = True)
df2 = spark.read.csv('file2.csv', header = True, inferSchema = True)
# %%
"""
the column names in both the dataframes should be same and in the same order
"""
records_present_in_df1_not_in_df2 = df1.join(other = df2,
                                                on = df1.columns,
                                                how = 'anti')
# %%
records_present_in_df2_not_in_df1 = df2.join(other = df1,
                                                on = df1.columns,
                                                how = 'anti')
# %%
