# lambda_ddos
Use AWS lambda functions to test your site's ability to withstand ddos attacks

### How to run
Using your AWS account, create a new lambda function named ddostest and push lambda_function.py to it. On your local machine, change the destination URL in local_runner.py, and run. 

### What it will do
The lambda function will send x number of asynchronous requests, and the runner will call the lambda y number of times asynchronously, resulting in LOTS of requests in a short amount of time
