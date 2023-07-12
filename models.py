from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publishers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', backref='publisher')


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    sales = relationship('Sale', backref='book')


class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sales = relationship('Sale', backref='shop')


class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    shop_id = Column(Integer, ForeignKey('shops.id'))
    price = Column(Integer)
    date = Column(Date)
