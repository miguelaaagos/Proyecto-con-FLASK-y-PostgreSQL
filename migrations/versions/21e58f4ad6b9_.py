"""empty message

Revision ID: 21e58f4ad6b9
Revises: 1c1b2bb655b2
Create Date: 2023-11-15 16:27:48.594395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21e58f4ad6b9'
down_revision = '1c1b2bb655b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=200),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)

    # ### end Alembic commands ###
