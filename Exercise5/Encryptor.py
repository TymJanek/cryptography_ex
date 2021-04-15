def read_file(filename):
    """ method opening text file and reading its content
    :param filename: text file name
    :return message from text file:
    """
    f = open(filename, "r")
    file_text = f.read()
    return file_text


class Encryptor:

    def __init__(self, alphabet, shuffled_alphabet, key):
        self.plain_text = read_file("cipher.txt")
        self.reworked_text = read_file("cipher.txt")
        self.key = key
        self.result = ''
        self.ciphertext = None
        self.alphabet = alphabet
        self.shuffled_alphabet = shuffled_alphabet

    def reverse(self):
        """ reverses message """
        self.plain_text = self.plain_text[::-1]

    def remove_spaces(self):
        """ removes spaces """
        self.plain_text = self.plain_text.replace(' ', '')

    def change_case(self):
        """ changes case to lowercase """
        self.plain_text = self.plain_text.lower()

    def substitute(self):
        """ substitutes all characters from english alphabet(lowercase only) to corresponding characters from
            shuffled alphabet """
        alphabet = ''.join(self.alphabet)
        shuffled_alphabet = ''.join(self.shuffled_alphabet)

        for letter in self.plain_text:
            if letter.lower() in alphabet:
                self.result += shuffled_alphabet[alphabet.find(letter.lower())]
            else:
                self.result += letter

    def transpose(self):
        """ transposes message by columns using given numeral key
            made with help from https://inventwithpython.com/hacking/chapter8.html """
        self.ciphertext = [''] * self.key
        for col in range(self.key):
            pointer = col

            while pointer < len(self.result):
                self.ciphertext[col] += self.result[pointer]
                pointer += self.key

        self.ciphertext = ''.join(self.ciphertext)

    def encrypt(self):
        """ usage of defined methods in order to encode message
            methods used: message reversal, case -> lowercase, character substitution and column transposition
        :return: ciphered text
        """
        self.reverse()
        # self.remove_spaces()
        self.change_case()
        self.substitute()
        self.transpose()

        return self.ciphertext
