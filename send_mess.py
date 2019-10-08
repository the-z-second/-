import logging
import boto3
from botocore.exceptions import ClientError

msg_body = ""
sqs_queue_url = ""
def send_sqs_message(sqs_queue_url, msg_body):
    # Send the SQS message
    sqs_client = boto3.client('sqs')
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=msg_body)
    except ClientError as e:
        logging.error(e)
        return None
    return msg

def main():
    """Exercise send_sqs_message()"""

    # Assign this value before running the program
    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                         format='%(levelname)s: %(asctime)s: %(message)s')

    # Send some SQS messages
   # for i in range(1, 6):
    #    msg_body ="we"
            #f'SQS message #{i}'
    msg = send_sqs_message(sqs_queue_url, msg_body)
    if msg is not None:
        logging.info(f'Sent SQS message ID: {msg["MessageId"]}')
