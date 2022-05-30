import UI
import logger


def button_click():
    data = UI.enter_user()
    logger.export_logger(data)
