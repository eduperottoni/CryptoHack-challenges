from exceptions.exceptions import InvalidAttributeException
import string

class CaesarCipher:
    """Class to handle with Caesar ciphers (Roman Cipher)

    Attributes:
        translation: A integer that indicates the translation in the alphabet
        ciphertext: A string representing the original (encrypted text)
        plaintext: A string representing the decrypted text
        replacement_dict: A replacement dict to implrove the time of letter's substitution
        alphabet: The alphabet that is used in the methods
    """
    def __init__(self, translation:int = 0):
        if translation >= 0:
            self.__build_replacement_dict()
        self.__translation = translation
        self.__ciphertext = ''
        self.__plaintext = ''
        self.__replacement_dict = {}
        self.__alphabet = string.ascii_lowercase
    

    def __build_replacement_dict(self):
        """
        Build a replacement_dict to letter's substitution
        """
        transl = self.__translation
        dictionary = self.__replacement_dict
        alp_len = len(self.__alphabet)
        for index, letter in enumerate(self.__alphabet):
            if (index + transl < alp_len):
                dictionary[letter] = self.__alphabet[index + transl]
            else:
                dictionary[letter] = self.__alphabet[transl - (alp_len - index)]



    def load_ciphertext(self, ciphertext:str):
        self.__ciphertext = ciphertext


    def load__plaintext(self, plaintext:str):
        self.__plaintext = plaintext

    
    def cipher(self):
        plain = self.__plaintext
        cipher = self.__ciphertext
        if plain == '' or cipher != '': 
            raise InvalidAttributeException(f'PLAINTEXT is empty or CIPHERTEXT is not empty')
        ...

            


#Register challenge - just a Caesar's cipher

#1 - First, we make a frequence analysis 
