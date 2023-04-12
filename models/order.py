from sqlalchemy.orm import relationship, backref
# импортируем модель Продуктов для связки моделей
from models.product import Products
# класс-конструктор для работы с декларативным стилем работы с SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey, DateTime

# инициализация декларативного стиля
Base = declarative_base()





class Order(Base):
    """
    Класс для создания таблицы "Заказ",
    основан на декларативном стиле SQLAlchemy
    """
    # название таблицы
    __tablename__ = 'orders'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('product.id'))
    user_id = Column(Integer)

    # для каскадного удаления данных из таблицы
    products = relationship(
        Products,
        backref=backref('orders',
                        uselist=True,
                        cascade='delete, all'))

    def __str__(self):
        return f'{self.quantity} {self.data}'

