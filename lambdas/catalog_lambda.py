import boto3

glue = boto3.client("glue")

def lambda_handler(event, context):
    glue.start_crawler(
        Name="encrypted_data_crawler"
    )
    return {"status": "CATALOG_UPDATED"}
