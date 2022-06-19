"""
Your module description
"""

## Standard SQS Queue script for this project

import boto3

## Obtains service resource
sqs = boto3.resource('sqs')

## Queue will be created. Output will returns an SQS.queue instance
queue = sqs.create_queue(QueueName='python-project-queue')

##Allows you access to identifiers and attributes
print(queue.url)
