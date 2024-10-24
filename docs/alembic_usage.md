## Initialize Alembic (if not already initialized)

    alembic init alembic

## Create a New Migration after modifying models

    alembic revision --autogenerate -m "Add new table"

## Apply the Migration to the database

    alembic upgrade head

## Check the Current Migration

    alembic current

## View Migration History

    alembic history

## Rollback to a Previous Migration (if needed)

    alembic downgrade <revision>
