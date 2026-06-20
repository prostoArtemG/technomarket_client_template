"""Add nav_groups and nav_categories lookup tables.

Revision ID: 0005
Revises: 0004
Create Date: 2026-06-20

These tables store emoji and sort_order for each unique group_name /
category value found in the products table.  They are populated by the
CMS bot; if a name has no row the site falls back to the static map in
app/category_meta.py.
"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op

revision = "0005"
down_revision = "0004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "nav_groups",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(128), nullable=False),
        sa.Column("emoji", sa.String(32), nullable=False, server_default=""),
        sa.Column("sort_order", sa.Integer(), nullable=False, server_default="100"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", name="uq_nav_groups_name"),
    )

    op.create_table(
        "nav_categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(128), nullable=False),
        sa.Column("emoji", sa.String(32), nullable=False, server_default=""),
        sa.Column("group_name", sa.String(128), nullable=True),
        sa.Column("sort_order", sa.Integer(), nullable=False, server_default="100"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", name="uq_nav_categories_name"),
    )


def downgrade() -> None:
    op.drop_table("nav_categories")
    op.drop_table("nav_groups")
