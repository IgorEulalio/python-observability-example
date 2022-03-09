import json
from aws_lambda_powertools import Metrics, Logger, Tracer
from src.game_service import get_game
from src.shared import NotFoundException

logger = Logger()
metrics = Metrics()
tracer = Tracer()

@metrics.log_metrics(capture_cold_start_metric=True)
@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    path_params = event["pathParameters"]
    game_id = path_params.get("game_id")

    logger.info("Retrieving game_id %s", game_id)

    try:
        game = get_game(game_id)
    except NotFoundException:
        metrics.add_metric(name="GameNotFound", unit="Count", value=1)
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Game not found"}),
        }


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "game": game
        }),
    }
