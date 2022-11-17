from .configs import config, init_config


def allowed_file(filename):
    path = "../settings.ini"
    # Инициализируем конфиг по вышеуказанному пути
    init_config(path)
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower() in config['FLASK_APP']['ALLOWED_EXTENSIONS'])
