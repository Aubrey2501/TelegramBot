from .config import DEFAULT_COMMANDS, CANCEL_TEXT, MAX_HOTELS_COUNT, MAX_PHOTOS_COUNT

MESSAGES = {
    "start": "Привет, {0}!\nЧтобы увидеть список команд, введите /help",
    "help": "\n".join([f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]),
    "cancel": "Команда отменена.\nЧтобы увидеть список команд, введите /help",
    "lowprice": "Это поиск самых дешевых отелей.",
    "highprice": "Это поиск самых дорогих отелей в городе",
    "bestdeal": "Это поиск самых близких к центру города отелей",
    "get_city": "Для начала введите город для поиска:"
    + CANCEL_TEXT,
    "get_hotels_count": "Введите количество отелей для просмотра (не больше {0})".format(
        MAX_HOTELS_COUNT) + CANCEL_TEXT,
    "cities_error": "К сожалению, города не найдены. Попробуйте снова." + CANCEL_TEXT,
    "success_cities": "Выберете нужный город (район города) из списка: ",
    "success_hotels": "Выберете отель из списка: ",
    "hotels_count_error": "Количество отелей должно быть числом и меньше {0}".format(MAX_HOTELS_COUNT),
    "get_photos_count": "Введите количество фотографий отелей, которое необходимо вывести (не больше {0})".format(
        MAX_PHOTOS_COUNT) + CANCEL_TEXT,
    "photos_count_error": "Количество фотографий должно быть числом и меньше {0}".format(MAX_PHOTOS_COUNT),
    "get_start_date": "На какие даты будем искать? \nВведите начальную дату (dd-mm-yyyy): " + CANCEL_TEXT,
    "get_end_date": "Введите конечную дату (dd-mm-yyyy): " + CANCEL_TEXT,
    "get_adults_count": "Сколько взрослых будет проживать в номере?" + CANCEL_TEXT,
    "adults_count_error": "Количество взрослых должно быть не менее 1 и не более 3 человек",
    "get_children_age": "Возраст детей (до 13 лет) через запятую (например, 5,11). Если нет, введите '0'" + CANCEL_TEXT,
    "children_age_error": "Неправильно введены данные. Возраст детей вводится через запятую и не должен"
    " превышать 13 лет "
    "\nЕсли с Вами нет детей, введите '0'" + CANCEL_TEXT,
    "get_date_error": "Ошибка ввода даты. Попробуйте еще раз" + CANCEL_TEXT,
    "get_currency": "В какой валюте выводить цены на отели (RUB, USD, ...)?" + CANCEL_TEXT,
    "currency_error": "Код валюты должен состоять из трех латинских букв. Попробуйте еще раз",
    "request_problem": "Не удалось получить информацию из базы данных. \nК сожалению придется начать все сначала",
    "no_hotels": "Не удалось найти отели по заданным параметрам. Попробуйте снова.",
    "show_hotels": "Получаем данные об отелях. Подождите...",
    "other": "Нет такой команды или обработка последнего действия прервалась. Попробуйте нажать /start",
    "get_prices_range": "Введите диапазон цен в формате минимальная_цена-максимальная_цена" + CANCEL_TEXT,
    "get_distances_range": "Введите диапазон расстояния от центра в формате минимальное_расстояние-максимальное_расстояние" + CANCEL_TEXT,
    "prices_range_error": "Ошибка формата диапазона. Попробуйте еще раз" + CANCEL_TEXT,
    "distances_range_error": "Ошибка формата диапазона. Попробуйте еще раз" + CANCEL_TEXT,
}