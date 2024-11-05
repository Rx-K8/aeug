from loguru import logger

from aeug.logger_config import LOG_DIR


def setup_logger(name: str, level: str = "INFO"):
    log_file = LOG_DIR / f"{{time}}_{name}.log"
    logger.add(
        log_file,
        backtrace=True,
        level=level,
        mode="w",
        encoding="utf-8",
    )

    return logger


CUSTOM_LOGGER = setup_logger("aeug")
