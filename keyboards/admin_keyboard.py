from keyboards.keyboard import Keyboard
from data import UserService

"""
Клавиатура для администратора
"""

class AdminKeyboard(Keyboard):

    def start_kb(self):
        kb = self._keyboard(['Количество пользователей'])
        return kb
    
