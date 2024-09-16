from selenium.webdriver.common.by import By


class Locators:
    REGISTRATION_NAME_FIELD = (By.XPATH, ".//label[text()='Имя']")  # Поле "Имя" на странице регистрации
    REGISTRATION_EMAIL_FIELD = (By.XPATH, ".//label[text() ='Email']")  # Поле "Email" на странице регистрации
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, ".//label[text() ='Пароль']")  # Поле "Пароль" на странице регистрации
    REGISTRATION_BUTTON_FIELD = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"

    LOGIN_EMAIL_FIELD = (By.XPATH, ".//input[@name='name']")  # Поле "Email" на странице входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")  # Поле "Пароль" на странице входа
    LOGIN_BUTTON_MAIN = (
        By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_BUTTON_IN_ACCOUNT = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти" в личном кабинете
    LOGIN_BUTTON_REGISTRATION = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка "Войти" в странице регистрации
    LOGIN_BUTTON_FORGOT_PASSWORD = (
        By.XPATH, ".//a[text() = 'Войти']")  # Кнопка "Войти" на странице восстановления пароля
    PASS_ERROR_LABEL = (By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка "Неверный пароль"

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет" для перехода в него
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка "Конструктор"
    LOGO = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выйти"

    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']")
