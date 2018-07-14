from sqlalchemy import select
from alchemy import user_table

s = select([user_table])

for row in s.execute():
    print(row)
