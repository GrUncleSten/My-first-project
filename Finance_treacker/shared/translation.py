from shared.text import ru
from shared.text import en

def translate(key,lang,**kwargs):
    if lang == "English":
        return en[key].format(**kwargs)
    elif lang == "Russian":
        return ru[key].format(**kwargs)
    else:
        raise ValueError("Unknown language")

