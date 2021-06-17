import math


class Decryptor:

    def __init__(self, alphabet, shuffled_alphabet, cipher_text, key):
        self.reworked_text = ''
        self.key = key
        self.result = ''
        self.alphabet = alphabet
        self.shuffled_alphabet = shuffled_alphabet
        self.cipher_text = cipher_text
        self.plaintext = ''

    def transpose_back(self):
        """ transposes message back by columns
            made with help from https://inventwithpython.com/hacking/chapter9.html """
        column_count = math.ceil(len(self.cipher_text) / self.key)
        row_count = self.key
        boxes_count = (column_count * row_count) - len(self.cipher_text)
        self.reworked_text = [''] * column_count

        col = 0
        row = 0

        for symbol in self.cipher_text:
            self.reworked_text[col] += symbol
            col += 1

            if (col == column_count) or (col == column_count - 1 and row >= row_count - boxes_count):
                col = 0
                row += 1

        self.reworked_text = ''.join(self.reworked_text)

    def substitute_back(self):
        """ substitutes back characters from shuffled alphabet to original message"""
        alphabet = ''.join(self.alphabet)
        key = ''.join(self.shuffled_alphabet)

        for letter in self.reworked_text:
            if letter.lower() in key:
                self.plaintext += alphabet[key.find(letter.lower())]
            else:
                self.plaintext += letter

    def reverse(self):
        """ reverses text to original message"""
        self.plaintext = self.plaintext[::-1]

    def decrypt(self):
        """ usage of all defined methods in order to decode message
            methods used: column transposition, character substitution and message reversal
        :return: original message before encoding
        """
        self.transpose_back()
        self.substitute_back()
        self.reverse()

        return self.plaintext
