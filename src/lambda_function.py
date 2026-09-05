from src import app
from src.routes.contacts_routes import *

def lambda_handler(event, context):
    return app.resolve(event, context)