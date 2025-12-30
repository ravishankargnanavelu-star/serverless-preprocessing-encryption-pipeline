import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import *

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

input_path = "s3://processed-bucket/preprocessed/"
output_path = "s3://processed-bucket/encrypted/"

df = spark.read.parquet(input_path)

encrypted_df = df.withColumn(
    "sensitive_data",
    sha2(col("sensitive_data"), 256)
)

encrypted_df.write.mode("overwrite").parquet(output_path)
