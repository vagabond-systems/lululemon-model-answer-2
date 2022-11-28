import json


def record_transaction(event, context):
    # extract the request body from the event object
    request_body = event["body"]
    print(request_body)

    # load the json in the request body into a python object
    transaction = json.loads(request_body)
    print(transaction)

    # create a successful response
    response_body = {
        "success": True
    }
    response = {"statusCode": 200, "body": json.dumps(response_body)}

    # respond
    return response
