from alchemy import user_table, engine

conn = engine.connect()

ins = user_table.insert()

new_user = ins.values(name="Anderson", idade=24, senha="senhaTeste")

conn.execute(new_user)