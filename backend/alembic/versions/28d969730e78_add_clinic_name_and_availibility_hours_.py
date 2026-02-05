"""add clinic_name and availibility_hours to doctor

Revision ID: 28d969730e78
Revises: 
Create Date: 2026-02-02 09:57:46.516267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28d969730e78'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('doctor', sa.Column('clinic_name', sa.String(), nullable=True))
    op.add_column('doctor', sa.Column('availability_hours', sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    pass
