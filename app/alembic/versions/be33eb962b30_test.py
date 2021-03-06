"""test

Revision ID: be33eb962b30
Revises: ad9cbef78cc4
Create Date: 2022-06-13 01:45:07.292905

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'be33eb962b30'
down_revision = 'ad9cbef78cc4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('article', 'source_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_article_source_id'), 'article', ['source_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_article_source_id'), table_name='article')
    op.alter_column('article', 'source_id',
               existing_type=sa.INTEGER(),
               nullable=True)