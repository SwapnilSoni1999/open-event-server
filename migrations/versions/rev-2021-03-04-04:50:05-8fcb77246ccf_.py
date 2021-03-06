"""empty message

Revision ID: 8fcb77246ccf
Revises: 23ccdfcae6a0
Create Date: 2021-03-04 04:50:05.850507

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '8fcb77246ccf'
down_revision = '23ccdfcae6a0'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exhibitors_sessions',
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('exhibitor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exhibitor_id'], ['exhibitors.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('session_id', 'exhibitor_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exhibitors_sessions')
    # ### end Alembic commands ###
