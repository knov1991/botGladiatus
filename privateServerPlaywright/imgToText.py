import easyocr
import warnings

def imgtotext():
    warnings.filterwarnings("ignore", message="'pin_memory' argument is set")
    reader = easyocr.Reader(['en', 'pt'], gpu=False, verbose=False)
    result = reader.readtext('screenshots/bot.jpg')
    for (bbox, text, prob) in result:
        return text