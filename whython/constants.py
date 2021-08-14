# *###################
# * IMPORTS
# *###################

import string
import emoji

# *###################
# * CONSTANTS
# *###################

emojis = []
for emoji_ in emoji.EMOJI_UNICODE["en"]:
    emojis.append(emoji.EMOJI_UNICODE["en"][emoji_])

DIGITS = '0123456789'
LETTERS = string.ascii_letters
EMOJIS = "".join(emojis)
LETTERS_DIGITS = LETTERS + DIGITS + EMOJIS
QUOTES = "'\""