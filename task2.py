from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Sale, Shop

# Установите соединение с базой данных
engine = create_engine('postgresql://postgres:"введите свой пароль Postgres"@localhost:5432/"Введите название вашей БД"')
Session = sessionmaker(bind=engine)
session = Session()

# Введите имя или идентификатор издателя
publisher_name = input("Введите имя или идентификатор издателя: ")

# Выполните запрос выборки
sales = session.query(Book.title, Shop.name, Sale.price, Sale.date)\
    .join(Sale, Book.id == Sale.book_id)\
    .join(Shop, Sale.shop_id == Shop.id)\
    .join(Publisher, Book.publisher_id == Publisher.id)\
    .filter(Publisher.name == publisher_name)\
    .all()

# Выведите результат построчно
for sale in sales:
    book_title, shop_name, price, date = sale
    print(f"{book_title} | {shop_name} | {price} | {date.strftime('%d-%m-%Y')}")

# Закройте сессию
session.close()
