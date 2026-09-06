from src import app
from aws_lambda_powertools import Logger
from src.routes.contacts_routes import *

logger = Logger()

@logger.inject_lambda_context
def lambda_handler(event, context):
    return app.resolve(event, context)