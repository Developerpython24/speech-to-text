import arabic_reshaper
from bidi.algorithm import get_display


def convert(text):
    reshape = arabic_reshaper.reshape(text)
    rtl = get_display(reshape)
    return rtl



d = convert("سلام")
print(d)

