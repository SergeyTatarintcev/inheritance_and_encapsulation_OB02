class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    # Геттеры
    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Сеттеры
    def set_name(self, name):
        self.__name = name

    def set_access_level(self, level):
        if level in ['user', 'admin']:
            self.__access_level = level
        else:
            raise ValueError("Недопустимый уровень доступа")

    def __str__(self):
        return f"User(ID: {self.__user_id}, Name: {self.__name}, Access: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name, admin_level=1):
        super().__init__(user_id, name)
        self.__admin_level = admin_level
        self.set_access_level('admin')

    def get_admin_level(self):
        return self.__admin_level

    def set_admin_level(self, level):
        if isinstance(level, int) and level > 0:
            self.__admin_level = level
        else:
            raise ValueError("Уровень администратора должен быть положительным целым числом")

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            raise TypeError("Можно добавлять только объекты класса User")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь с ID {user_id} удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def __str__(self):
        return f"Admin(ID: {self.get_id()}, Name: {self.get_name()}, Admin Level: {self.__admin_level})"


# Пример использования:

# Список пользователей
user_list = []

# Создаем администратора
admin = Admin(1, "Иван", admin_level=2)

# Создаем обычных пользователей
user1 = User(2, "Алексей")
user2 = User(3, "Мария")

# Добавляем пользователей
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)

# Удаляем пользователя
admin.remove_user(user_list, 2)

# Выводим оставшихся пользователей
