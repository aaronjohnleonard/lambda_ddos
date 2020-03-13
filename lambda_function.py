import json
from urllib.request import urlopen
import threading

def lambda_handler(event, context):
    
    threads = []
    for x in range(event['num_requests']):
        print(x)
        thread = threading.Thread(target=send_request, args=(event['url'],))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    
    return {
        'statusCode': 200,
        'body': json.dumps({"success":True})
    }

def send_request(url):
    with urlopen(url) as response:
        response_content = response.read().decode('utf-8')

if __name__ == "__main__":
    lambda_handler({"url":<Your Website>, "num_requests": 1000}, None)
