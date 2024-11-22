import logging
# Налаштування логування
logging.basicConfig(level=logging.DEBUG,
                    filename='logs.log',
                    filemode='w',
                    encoding='UTF-8',
                    format='%(levelname)s:%(asctime)s - %(message)s'
                    )
# Створимо клас Animal
class Animal:
    def __init__(self, name, species):
        self.name = name # Ім'я тварини
        self.species = species # Вид тварини
        logging.debug(f'Created Animal: {self.name}, Species: {self.species}')

    def show_info(self):
        # Логування інформації про об'єкт (рівень DEBUG)
        logging.debug(f'Animal Info - Name: {self.name}, Species: {self.species}')
        # Виведення інформації в консоль
        print(f'Animal Info - Name: {self.name}, Species: {self.species}')

# Створюємо об'єкт класу Animal
try:
    animal1 = Animal("Leo", "Lion")  # Створення об'єкта, логуватиметься повідомлення DEBUG
    animal1.show_info()  # Виведемо інформацію про тварину, це також буде записано в лог як DEBUG
except Exception as e:
    # Якщо виникає помилка, записуємо її в лог як Error
    logging.error(f'Error occurred: {str(e)}')

# Додатковий приклад виключення (помилка)
try:
    # Викликаємо помилку: ділення на нуль
    result = 10 / 0
except ZeroDivisionError as e:
    # Логування помилки
    logging.error(f'Error occurred: {str(e)}')  # Записуємо як помилку (Error)