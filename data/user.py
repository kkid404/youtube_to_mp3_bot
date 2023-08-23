from typing import Union

from sqlalchemy import Column, Integer, String

from data.data import session, Base

"""
Модуль в котором определяется модель User в базе данных 
и класс UserService для управления данными.
"""

class User(Base):
    __tablename__ = 'users_mp3'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    chat_id = Column(String(30), nullable=False, unique=True)

class UserService:

    @staticmethod
    def add(chat_id: str, name: str) -> int:
        """
        Добавляет пользователя в базу данных

        Args:
        -------
            chat_id: str
            телеграм id пользователя
            
            name: str
            имя пользователя телеграм
        
        Returns:
        -------
            id созданного пользователя
        """
        user = User(chat_id=str(chat_id), name=str(name))
        session.add(user)
        session.commit()
        return user.id



    @staticmethod
    def get_by_id(chat_id: str) -> Union[User, bool]:
        """
        Возвращает информацию о пользовате в базе данных

        Args:
        -------
            chat_id: str
            телеграм id пользователя
        
        Returns:
        -------
            User: класс пользователя
            False: если пользователь не найден
        """
        user = session.query(User).filter(User.chat_id == str(chat_id)).first()
        if user:
            return user
        else:
            return False
    
    @staticmethod
    def get_all() -> dict:
        """
        Возвращает информацию о всех пользователях в базе данных

        
        Returns:
        -------
            Словарь: список всех полей пользователей из базы данных
        """
        chat_ids = []
        names = []
        users = session.query(User).all()
        for user in users:
            chat_ids.append(user.chat_id)
            names.append(user.name)
        return {"chat_id" : chat_ids, "names" : names}
    
    @staticmethod
    def delete(chat_id: str) -> None:
        """
        Удаляет пользователя из базы данных

        Args:
        -------
            id: int
            id пользователя в базе данных
        
        Returns:
        -------
            None
        """
        user = session.query(User).filter(User.chat_id == str(chat_id)).first()
        session.delete(user)
        session.commit()