from pathlib import Path

# CACHE_DIR = Path.home() / ".cache" / "aeug"
CACHE_DIR = Path(__file__).parents[1].resolve()
VALOUTPUT_DIR = CACHE_DIR / "val_outputs"

LOG_DIR = CACHE_DIR / "logs"
