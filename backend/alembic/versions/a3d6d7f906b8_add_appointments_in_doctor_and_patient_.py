"""add appointments in doctor and patient models

Revision ID: a3d6d7f906b8
Revises: 338632eedfac
Create Date: 2026-02-03 09:42:53.432622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3d6d7f906b8'
down_revision: Union[str, Sequence[str], None] = '338632eedfac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
