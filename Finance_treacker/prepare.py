from config import DATA_DIR, DATA_FILE


def prepare():
    DATA_DIR.mkdir(exist_ok=True)
    filename = DATA_FILE
    return filename