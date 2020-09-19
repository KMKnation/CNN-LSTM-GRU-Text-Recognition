import re
PORT_TO_HOST = 5556
OUTPUT_DIR = 'image_ocr'

INPUT_WIDTH = 128 #256
INPUT_HEIGHT = 32 #32
WORDS_PER_EPOCH = 80000
RNN_SIZE = 256 #256
SPLIT_WORD = '|||'

MAX_STRING_LEN = 18#18
regex = r'(?=.*?[A-Z])(?=.*?[a-z])(?!.*?[=?<>()]).{8,20}$'
currencies = ['$', '₹', '€']
alphabet = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_$₹€.,:;()<>[]*+-/!|?@%&=\'\" ' #91 new classes
# print(alphabet[len(alphabet) - 4])


# only a-z and space..probably not to difficult
# to expand to uppercase and symbols

def is_valid_str(in_str):
    search = re.compile(regex, re.UNICODE).search
    # return bool(search(in_str))
    return True


# Translation of characters to unique integer values
def text_to_labels(text):
    ret = []
    for char in text:
        label = alphabet.find(char)
        if label == -1:
            label = len(alphabet) - 1
        ret.append(label)
    return ret


# Reverse translation of numerical classes back to characters
def labels_to_text(labels):
    ret = []
    for c in labels:
        if c == len(alphabet):  # CTC Blank
            ret.append("")
        else:
            ret.append(alphabet[c])
    return "".join(ret)
