import os

from flask import Flask

from .routes import route
from .configs import config, init_config


def create_flask_app():
    app = Flask(__name__)

    # Подключаем все роуты приложения
    route(app)

    # Считываем переменную окружения "CONFIG_PATH", если она есть,
    # то берём путь из неё, иначе указанный по умолчанию "./settings.ini"
    path = os.environ.get('CONFIG_PATH') if os.environ.get(
        'CONFIG_PATH') else "./settings.ini"
    # Инициализируем конфиг по вышеуказанному пути
    init_config(path)
    # Обновляем конфигурацию приложения Flask
    # Если файл не найден или данные которые используются при обновлении отсутствуют,
    # то вылетит Exception - KeyError
    try:
        app.config.update(dict(
            SECRET_KEY=str(config['FLASK_APP']['FLASK_APP_SECRET_KEY'])
        ))
        print(f"\n\033[32m Сервер запустился с конфигом:\n\033[32m {path}\n")
    except KeyError:
        print(f"\033[31m Файл {path} не найден или неверный")

    return app
