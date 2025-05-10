# Define the alphanumeric to morse mapping between letters and morse code
# This is defined for A-Z, 0-9 and the punctuation .,?!:;' as well as spaces
# All other characters will be ignored and replaced with a space
ALPHA_TO_MORSE = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "0": "-----",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    ".": "._._.",
    ",": "__..__",
    "?": "..__..",
    "!": "_._.__",
    ":": "___...",
    ";": "_._._.",
    "'": ".____.",
    " ": "   "
}

# Define the morse to alphanumeric mapping between letters and morse code
# This is defined for A-Z, 0-9 and the punctuation .,?!:;' as well as spaces
# All other characters will be ignored and replaced with a space
MORSE_TO_ALPHA = dict((value, key) for key, value in ALPHA_TO_MORSE.items())


# Define a function to encode an alphanumeric message
def translator(msg, direction):
    """
    Takes in a message (either alphanumeric or morse code) and translates it (to morse code or alphanumeric
    respectively)

    Args:
        msg (string): a message to translate into either morse code or alphanumeric
        direction (string): 1 = translate to Morse code, 2 = translate to alphanumeric

    Returns:
        string: a translated message
    """
    upper_case_msg = msg.upper()

    if direction == "1":
        return " ".join([ALPHA_TO_MORSE[letter] for letter in upper_case_msg if letter in ALPHA_TO_MORSE])
    else:
        upper_case_msg = ''.join(letter for letter in upper_case_msg if letter in ['.', '_', " "])
        words = upper_case_msg.split("   ")
        split_msg = [word.split(" ") for word in words]

        translated_word_list = []
        for word in split_msg:
            translated_word = "".join([MORSE_TO_ALPHA[letter] for letter in word if letter in MORSE_TO_ALPHA])
            translated_word_list.append(translated_word)
        return " ".join(translated_word_list)
