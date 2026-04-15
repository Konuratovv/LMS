from sqlalchemy.orm.base import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    