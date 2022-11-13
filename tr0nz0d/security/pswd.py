# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from random import randint, choices, shuffle

_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']
_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ç', 'Ç']
_simbolos = ['"', "'", '\\', '/', '*', '-', '+', '!', '@', '#', '$', '%', '¨', '&', '(', ')', '{', '}', '[', ']', '`', '´', '~', '^', '?', '°', '₢', '•', '→', '←', '◄', '►']


def _select_char() -> str:
    shuffle_val_init = randint(1, 5)
    shuffle_val_end = randint(6, 9)

    for _ in range(shuffle_val_init, shuffle_val_end):
        shuffle(_numeros)
        shuffle(_letras)
        shuffle(_simbolos)

    num = choices(_numeros, k=5)
    let = choices(_letras, k=5)
    sim = choices(_simbolos, k=5)

    sequence = [f'{num[randint(0, 4)]}', f'{let[randint(0, 4)]}', f'{sim[randint(0, 4)]}']

    for _ in range(shuffle_val_init, shuffle_val_end):
        shuffle(sequence)
        shuffle(sequence)

    char = sequence[randint(0, 2)]

    return char


def _create_key(list1: list, list2: list, list3: list, lenght: int) -> str:
    min_index = 0
    max_index = lenght - 1
    key = ''
    char_lists = [list1, list2, list3]
    for _ in range(lenght):
        shuffle(char_lists[0])
        shuffle(char_lists[1])
        shuffle(char_lists[2])
        shuffle(char_lists)

        key = key + f'{char_lists[randint(0, 2)][randint(min_index, max_index)]}'

    return key


class Pass():
    def gerar(self, lenght: int) -> str:
        """ Cria uma senha com um comprimento passado.\n
        [Os dados gerados não são armazenados em nenhum local]

        Parâmetros
        -----------
        lenght: :class:`int`
            Tamanho da senha ou código que deve ser gerado.

        Returns
        -----------
        pass: :class:`str`
            A senha criada em texto literal.

        Raises
        -----------
        ValueError
            Se o comprimento passado não for um número inteiro válido.
        """
        if type(lenght) != int:
            try:
                lenght = int(lenght)
            except ValueError:
                raise ValueError('Comprimento da senha não é um número inteiro válido.')

        caracteres_1 = []
        caracteres_2 = []
        caracteres_3 = []
        for _ in range(lenght):
            caractere_1 = _select_char()
            caracteres_1.append(caractere_1)
            caractere_2 = _select_char()
            caracteres_2.append(caractere_2)
            caractere_3 = _select_char()
            caracteres_3.append(caractere_3)

        key = _create_key(caracteres_1, caracteres_2, caracteres_3, lenght)

        return key
