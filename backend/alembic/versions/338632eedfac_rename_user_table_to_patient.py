"""rename user table to patient

Revision ID: 338632eedfac
Revises: 28d969730e78
Create Date: 2026-02-02 10:29:27.337182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '338632eedfac'
down_revision: Union[str, Sequence[str], None] = '28d969730e78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.rename_table("user", "patient")


def downgrade() -> None:
    """Downgrade schema."""
    op.rename_table("patient", "user")
