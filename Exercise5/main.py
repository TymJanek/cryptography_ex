import string
import random

from src.Decryptor import Decryptor
from src.Encryptor import Encryptor


if __name__ == '__main__':
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = list(string.ascii_lowercase)
    random.Random(4).shuffle(shuffled_alphabet)    # set seed for easier testing

    key = 8

    enc = Encryptor(alphabet, shuffled_alphabet, key)
    encryptor = enc.encrypt()
    print('Encrypted text: \n', encryptor, '\n')

    dec = Decryptor(alphabet, shuffled_alphabet, encryptor, key)
    decryptor = dec.decrypt()
    print('Decrypted text: \n', decryptor)
