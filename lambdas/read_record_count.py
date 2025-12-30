import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")

    response = s3.list_objects_v2(
        Bucket="processed-bucket",
        Prefix="preprocessed/"
    )

    record_count = response.get("KeyCount", 0)

    return {
        "recordResult": {
            "record_count": record_count
        }
    }
