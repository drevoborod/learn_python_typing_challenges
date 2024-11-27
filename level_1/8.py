import decimal
from decimal import Decimal
import uuid
from uuid import UUID


def get_user_balance(user_id: UUID) -> Decimal:
    pass


if __name__ == "__main__":
    assert get_user_balance(user_id=uuid.uuid4()) == decimal.Decimal("265.2")
