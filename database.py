import os
from pynamodb.models import Model
from pynamodb.attributes import (NumberAttribute, UnicodeAttribute)

# condtionally set host meta attribute unless in production.
environment = os.getenv("PYTHON_ENV") or "development"


class DiscordUserModel(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = "dynamodb-user"
        if environment == "development":
            print('using local')
            host = "http://localhost:8000"
    id = NumberAttribute(hash_key=True)
    first_name = UnicodeAttribute(null=True)
    last_name = UnicodeAttribute(null=True)
    github = UnicodeAttribute(null=True)


DiscordUserModel.create_table(read_capacity_units=1, write_capacity_units=1)
