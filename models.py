from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', backref='publisher')


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    publisher_id = Column(Integer, ForeignKey('publisher.id'))
    stocks = relationship('Stock', backref='book')


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    shop_id = Column(Integer, ForeignKey('shop.id'))
    count = Column(Integer)
    sales = relationship('Sale', backref='stock')


class Sale(Base):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    date_sale = Column(Date)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    count = Column(Integer)


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    stocks = relationship('Stock', backref='shop')
