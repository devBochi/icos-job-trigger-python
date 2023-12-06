import os
import json
import ibm_boto3
from ibm_botocore.client import Config, ClientError

# Create resource with credentials for ICOS sdk
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=os.environ.get("API_KEY"),
    ibm_service_instance_id=os.environ.get("SERV_ID"),
    config=Config(signature_version="oauth"),
    endpoint_url=os.environ.get("ENDPOINT")
)

# We parse the metadata that comes from the ICOS put event

event = json.loads(os.environ.get("CE_DATA"))

print("Fetching event data...")

print("------------------")

# With the info of the event, we can get the object and do whatever we want
def get_item(bucket_name, item_name):
    print("Retrieving item from bucket: {0}, key: {1}".format(bucket_name, item_name))
    try:
        file = cos.Object(bucket_name, item_name).get()
        print("File Contents: {0}\n".format(file["Body"].read()))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve file contents: {0}".format(e))

get_item(event["bucket"],event["key"])

print("Thanks for using Code Engine!\n")

print("-----------------")