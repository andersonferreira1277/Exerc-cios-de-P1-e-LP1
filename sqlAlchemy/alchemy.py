from sqlalchemy import (create_engine, MetaData, DateTime, Column,
                        String, Integer, Table)
from datetime import datetime

engine = create_engine('sqlite:///banco.sqlite3', echo=True)

metadate = MetaData(bind=engine)

user_table = Table('users', metadate,
                   Column('id', Integer, primary_key=True),
                   Column('name', String, index=True),
                   Column('idade', Integer, nullable=False),
                   Column('senha', String),
                   Column('criado_em', DateTime, default=datetime.now()),
                   Column('atualizado_em', DateTime, default=datetime.now(),
                          onupdate=datetime.now()))

metadate.create_all()


