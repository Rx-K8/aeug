import loguru 

from aeug.logger_config import LOG_DIR


def setup_logger(name: str, level: str = "INFO"):
    log_file = LOG_DIR / f"{{time}}_{name}.log"
    loguru.logger.add(
        log_file,
        backtrace=True,
        level=level,
        mode="w",
        encoding="utf-8",
    )

    return loguru.logger


logger = setup_logger("aeug")
