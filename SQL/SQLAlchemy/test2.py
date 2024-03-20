from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from test1 import Base

main_engine = sa.create_engine(
    'postgres://localhost:5432/habr_sql?sslmode=disable',
    echo=True,
)

DBSession = sessionmaker(
    binds={
        Base: main_engine,
    },
    expire_on_commit=False,
)


@contextmanager
def session_scope():
    """Provides a transactional scope around a series of operations."""
    session = DBSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


if __name__ == '__main__':
    with session_scope() as s:
        questions = s.query(Question).filter(
            Question.topic_id == t1_id,
        ).order_by(Question.id.desc()).limit(10).all()
