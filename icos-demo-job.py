import os
import json
import ibm_boto3
from ibm_botocore.client import Config, ClientError

# Create resource with credentials for ICOS sdk
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=os.environ("API_KEY"),
    ibm_service_instance_id=os.environ("SERV_ID"),
    config=Config(signature_version="oauth"),
    endpoint_url=os.environ("ENDPOINT")
)

# We parse the metadata that comes from the ICOS put event
eventInfo = json.dumps(os.environ("CE_DATA"))

params = {
    "Bucket" : eventInfo.bucket, 
    "Key": eventInfo.key
};

print(params)   

# With the info of the event, we can get the object and do whatever we want
def get_item(bucket_name, item_name):
    print("Retrieving item from bucket: {0}, key: {1}".format(bucket_name, item_name))
    try:
        file = cos.Object(bucket_name, item_name).get()
        print("File Contents: {0}".format(file["Body"].read()))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve file contents: {0}".format(e))

get_item(params["Bucket"], params["Key"])