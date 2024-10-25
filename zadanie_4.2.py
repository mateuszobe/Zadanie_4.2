def czy_slowo_jest_palindromem(word):
    """
    Owa funkcja sprawdza czy dane słowo jest palindromem.
    Argumentem jest tutaj słowo (word).
    Wynikiem jest bool - 'True' jeśli słowo jest palindromem i 'False' jeżeli nie jest.
    """
    return word == word[::-1]