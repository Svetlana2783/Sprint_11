# Локаторы для страницы регистрации
REGISTRATION_PAGE_URL = "https://stellarburgers.nomoredomains.site"
REGISTRATION_NAME_FIELD = "//input[@name='name']"
REGISTRATION_EMAIL_FIELD = "//input[@name='email']"
REGISTRATION_PASSWORD_FIELD = "//input[@name='password']"
REGISTRATION_BUTTON = "//button[text()='Зарегистрироваться']"

# Локаторы для страницы входа
# вход по кнопке «Войти в аккаунт» на главной
LOGIN_PAGE_URL = "https://stellarburgers.nomoredomains.sbs/login"
LOGIN_EMAIL_FIELD = "//input[@name='email']"
LOGIN_PASSWORD_FIELD = "//input[@name='password']"
LOGIN_BUTTON = "//button[text()='Войти']"
# вход через кнопку «Личный кабинет»
PERSONAL_ACCOUNT_BUTTON = "//a[text()='Личный кабинет']"
# вход через кнопку в форме регистрации
REGISTRATION_BUTTON = "//a[text()='Войти']"
# вход через кнопку в форме восстановления пароля
RESET_PASSWORD_BUTTON = "//a[text()='Войти']"

# Локаторы для перехода в личный кабинет
PERSONAL_ACCOUNT_BUTTON = "//a[text()='Личный кабинет']"
# Локаторы для перехода из личного кабинета в конструктор и на логотип
CONSTRUCTOR_BUTTON = "//a[text()='Конструктор']"
LOGO_BUTTON = "//a[@href='/']"

#Локаторы для выхода из аккаунта
LOGOUT_BUTTON = "//button[text()='Выйти']"

# Локаторы для конструктора
CONSTRUCTOR_BUTTON = "//a[text()='Конструктор']"
BUNS_TAB = "//span[text()='Булки']"
SAUCES_TAB = "//span[text()='Соусы']"
FILLINGS_TAB = "//span[text()='Начинки']"
