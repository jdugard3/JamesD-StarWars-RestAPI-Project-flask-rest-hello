"""empty message

Revision ID: 8787123d6f78
Revises: 2bf5ad11c117
Create Date: 2024-06-06 00:09:13.603565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8787123d6f78'
down_revision = '2bf5ad11c117'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('birth_year', sa.String(length=250), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_column('birth_year')

    # ### end Alembic commands ###
