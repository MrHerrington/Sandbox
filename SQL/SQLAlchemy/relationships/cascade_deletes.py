from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship('Child', back_populates='parent', passive_deletes=True)


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id', ondelete='CASCADE'))
    parent = relationship('Parent', back_populates='children')


engine = create_engine("sqlite://")
event.listen(engine, 'connect', lambda c, _: c.execute('pragma foreign_keys=on'))
Base.metadata.create_all(engine)
Session = sessionmaker(engine)

session = Session()

parent = Parent()
parent.children.append(Child())
parent.children.append(Child())
parent.children.append(Child())

session.add(parent)
session.commit()

print("Before delete, children = {0}".format(session.query(Child).count()))
print("Before delete, parent = {0}".format(session.query(Parent).count()))

session.delete(parent)

print("After delete, children = {0}".format(session.query(Child).count()))
print("After delete, parent = {0}".format(session.query(Parent).count()))

session.rollback()

print("After rollback, children = {0}".format(session.query(Child).count()))
print("After rollback, parent = {0}".format(session.query(Parent).count()))

session.close()
