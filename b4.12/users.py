import datetime

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):
    """
    Описывает структуру таблицы athelete, содержащую данные об атлетах
    """
    __tablename__ = 'user'

    id = sa.Column(sa.String(36), primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """

    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    print("Привет! Я запишу твои данные!")
    first_name = input("Ваше имя: ")
    last_name = input("Фамилия: ")
    gender = input("Какого вы пола? (варианты: Male, Female) ")
    email = input("адрес вашей электронной почты: ")
    birthdate = input("Введите дату рождения в формате ГГГГ-ММ-ДД. Например, 1999-01-01: ")
    height = input("А какой у вас рост в метрах? (Для разделения целой и десятичной части используйте точку)")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email
        birthdate=birthdate,
        height=height
    )
    return user

def main():

    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Данные сохранены")


if __name__ == "__main__":
    main()