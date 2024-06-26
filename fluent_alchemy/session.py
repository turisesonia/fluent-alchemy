from typing import Optional
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker, scoped_session


class ScopedSessionHandler:
    _session: Optional[scoped_session] = None

    @classmethod
    def make_session(cls, engine: Engine):
        if not isinstance(engine, Engine):
            raise ValueError("Only support Sqlalchemy Engine Object")

        cls._session = scoped_session(sessionmaker(engine))

    @classmethod
    def teardown_session(cls):
        if cls._session:
            cls._session.remove()
