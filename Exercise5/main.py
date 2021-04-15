import string


from Decryptor import Decryptor
from Encryptor import Encryptor


if __name__ == '__main__':
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = list(string.ascii_lowercase)
    key = 8

    enc = Encryptor(alphabet, shuffled_alphabet, key)
    encryptor = enc.encrypt()
    print('Encrypted text: \n', encryptor, '\n')

    dec = Decryptor(alphabet, shuffled_alphabet, encryptor, key)
    decryptor = dec.decrypt()
    print('Decrypted text: \n', decryptor)




