"""test

Revision ID: 79ff91028630
Revises: be33eb962b30
Create Date: 2022-06-13 03:06:58.031320

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '79ff91028630'
down_revision = 'be33eb962b30'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_suspicious_article_article_id', table_name='suspicious_article')
    op.create_index(op.f('ix_suspicious_article_article_id'), 'suspicious_article', ['article_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_suspicious_article_article_id'), table_name='suspicious_article')
    op.create_index('ix_suspicious_article_article_id', 'suspicious_article', ['article_id'], unique=False)
