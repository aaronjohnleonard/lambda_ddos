import boto3
import json

lam = boto3.client('lambda')

for x in range(1000):
    print(x)
    response = lam.invoke(
            Payload=json.dumps({"url":<Your Website>, "num_requests": 1000}).encode(),
        FunctionName='ddostest',
        InvocationType='Event'
    )

print(response)

