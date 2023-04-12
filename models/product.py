# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey
# импортируем модуль для связки таблиц
from sqlalchemy.orm import relationship, backref
# класс-конструктор для работы с декларативным стилем работы с SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# импортируем модель Категория для связки моделей
from models.category import Category

# инициализация декларативного стиля
Base = declarative_base()


class Products(Base):
    """
    Класс-модель для описания таблицы "Категория товара",
    основан на декларативном стиле SQLAlchemy
    """
    # Название таблицы
    __tablename__ = 'products'

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))
    # для каскадного удаления данных из таблиц
    category = relationship(
        Category,
        backref=backref('products',
                        uselist=True,
                        cascade='delete, all'))

    def __str__(self):
        return f'{self.name} {self.title} {self.price}'