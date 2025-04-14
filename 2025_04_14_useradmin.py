class User: # создаем класс User
    def __init__(self, user_id, name):
        self.__user_id = user_id  # защищенный атрибут
        self.__name = name         # защищенный атрибут
        self.__access_level = 'user'  # защищенный атрибут уровень доступа, значение по умолчанию = user

    def get_user_id(self): # метод get_user_id предоставляет доступ к чтению атрибута user_id
        return self.__user_id

    def get_name(self): # метод get_name предоставляет доступ к чтению атрибута name
        return self.__name

    def get_access_level(self): # метод get_access_level предоставляет доступ к чтению атрибута access_level
        return self.__access_level

    def set_name(self, new_name): # метод set_name предоставляет доступ к изменению атрибута name
        self.__name = new_name


class Admin(User): # создаем класс Admin,
                   # класс Admin наследует атрибуты и методы от родительского класса User,
                   # но имеет дополнительные (свои) методы
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # admin имеет уровень доступа для администраторов
        self.__users = []  # admin имеет доступ к списку пользователей

    def add_user(self, user): # метод добавления пользователя
        if isinstance(user, User):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Можно добавлять только объекты класса User.")

    def remove_user(self, user): # метод удаления пользователя
        if user in self.__users:
            self.__users.remove(user)
            print(f"Пользователь {user.get_name()} удален.")
        else:
            print("Пользователь не найден в списке.")

    def list_users(self): # метод получения списка пользователей
        print("Список пользователей:")
        for user in self.__users:
            print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")


# Проверка работы программы
if __name__ == "__main__":
    admin = Admin(1, "Admin1")
    user1 = User(2, "User1")
    user2 = User(3, "User2")

    admin.list_users()

    admin.add_user(user1)
    admin.add_user(user2)

    admin.list_users()

    admin.remove_user(user1)
    admin.list_users()