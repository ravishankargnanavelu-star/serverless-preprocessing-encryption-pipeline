import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import *

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

input_path = "s3://raw-bucket/input/"
output_path = "s3://processed-bucket/preprocessed/"

df = spark.read.parquet(input_path)

clean_df = (
    df.filter(col("id").isNotNull())
      .withColumn("processed_ts", current_timestamp())
)

clean_df.write.mode("overwrite").parquet(output_path)
