# locators/locators.py

# Локаторы для страницы регистрации
REGISTRATION_NAME_FIELD = "//input[@name='name']"
REGISTRATION_EMAIL_FIELD = "//input[@name='email']"
REGISTRATION_PASSWORD_FIELD = "//input[@name='password']"
REGISTRATION_BUTTON = "//button[text()='Зарегистрироваться']"

# Локаторы для страницы входа
LOGIN_EMAIL_FIELD = "//input[@name='email']"
LOGIN_PASSWORD_FIELD = "//input[@name='password']"
LOGIN_BUTTON = "//button[text()='Войти']"

# Локаторы для перехода в личный кабинет
PERSONAL_ACCOUNT_BUTTON = "//a[text()='Личный кабинет']"
RESET_PASSWORD_BUTTON = "//button[text()='Сброс пароля']"

# Локаторы для перехода из личного кабинета в конструктор и на логотип
CONSTRUCTOR_BUTTON = "//a[text()='Конструктор']"
LOGO_BUTTON = "//a[@href='/']"

# Локаторы для выхода из аккаунта
LOGOUT_BUTTON = "//button[text()='Выйти']"

# Локаторы для конструктора
BUNS_TAB = "//span[text()='Булки']"
SAUCES_TAB = "//span[text()='Соусы']"
FILLINGS_TAB = "//span[text()='Начинки']"
