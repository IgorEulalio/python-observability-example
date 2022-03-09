import os
import boto3
from src.shared import NotFoundException
from botocore.exceptions import ClientError
from aws_lambda_powertools import Metrics, Logger, Tracer

logger = Logger()
tracer = Tracer()


@tracer.capture_method
def get_game(game_id, dynamodb=None):
    table_name = os.getenv("TABLE_NAME")

    if not dynamodb:
        logger.info("Initializing DDB Table %s", table_name)
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)
    try:
        response = table.get_item(Key={'game_id': game_id})
        try:
            return response["Item"]
        except KeyError as e:
            logger.error("Product with id %s not exist.", game_id)
            raise NotFoundException
    except ClientError as e:
        logger.error("Error: " + str(e.response['Error']['Message']))
        raise Exception
