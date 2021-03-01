import os
from pynamodb.models import Model
from pynamodb.attributes import NumberAttribute

# condtionally set host meta attribute unless in production.
environment = os.getenv("PYTHON_ENV") or "development"


class DiscordUserModel(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = "dynamodb-user"
        if environment == "development":
            host = "http://localhost:8000"
    id = NumberAttribute(hash_key=True)


DiscordUserModel.create_table(read_capacity_units=1, write_capacity_units=1)
