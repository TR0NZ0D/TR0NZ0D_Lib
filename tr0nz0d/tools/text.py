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


class TextFormat():
    def line_print(self, text: str, char_tl: str, char_md: str, char_tr: str, char_sides: str, char_bl: str, char_br: str) -> None:
        """Imprime na tela um texto encapsulado no caractere desejado.

        Este método deve ser utilizado apenas para impressão de uma única linha,
        para multiplas linhas, utilize o método `text_print`.

        Parâmetros
        -----------
        text: :class:`str`
            O texto a ser encapsulado e impresso.
        char_tl: :class:`str`
            O caractere a ser utilizado no topo esquerdo.
            Ex: `╔`
        char_md: :class:`str`
            O caractere a ser utilizado nos centros horizontais.
            Ex: `═`
        char_tr: :class:`str`
            O caractere a ser utilizado no topo direito.
            Ex: `╗`
        char_sides: :class:`str`
            O caractere a ser utilizado nos centros verticais.
            Ex: `║`
        char_bl: :class:`str`
            O caractere a ser utilizado na base esquerda.
            Ex: `╚`
        char_br: :class:`str`
            O caractere a ser utilizado na base direita.
            Ex: `╝`
        """
        if type(text) != str:
            text = str(text)

        char_tl, char_md, char_tr, char_sides, char_bl, char_br = str(char_tl), str(char_md), str(char_tr), str(char_sides), str(char_bl), str(char_br)

        qtd = len(text) + 4
        print(f'{char_tl}' + f'{char_md}' * qtd + f'{char_tr}')
        print(f'{char_sides} ' + ' ' * (qtd - 2) + f' {char_sides}')
        print(f'{char_sides}  {text}  {char_sides}')
        print(f'{char_sides} ' + ' ' * (qtd - 2) + f' {char_sides}')
        print(f'{char_bl}' + f'{char_md}' * qtd + f'{char_br}')

    def text_print(self, texto: str, char_tl: str, char_md: str, char_tr: str, char_sides: str, char_bl: str, char_br: str) -> None:
        """Imprime na tela o texto encapsulado no caractere desejado.

        Parâmetros
        -----------
        texto: :class:`str`
            O texto a ser encapsulado e impresso. Pode ser utilizadas docstrings `'''texto'''` para enviar múltiplas linhas.
        char_tl: :class:`str`
            O caractere a ser utilizado no topo esquerdo.
            Ex: `╔`
        char_md: :class:`str`
            O caractere a ser utilizado nos centros horizontais.
            Ex: `═`
        char_tr: :class:`str`
            O caractere a ser utilizado no topo direito.
            Ex: `╗`
        char_sides: :class:`str`
            O caractere a ser utilizado nos centros verticais.
            Ex: `║`
        char_bl: :class:`str`
            O caractere a ser utilizado na base esquerda.
            Ex: `╚`
        char_br: :class:`str`
            O caractere a ser utilizado na base direita.
            Ex: `╝`
        """
        splited_text = texto.split('\n')
        data = []
        data.append(splited_text)
        for text in data:
            max_lenght = 0
            _index = 0
            _max = len(text[_index])
            for _ in text:
                if len(text[_index]) > _max:
                    _max = len(text[_index])
                max_lenght = _max
                _index += 1

            index = 0
            for _ in text:
                qtd = max_lenght + 4
                if index == 0:
                    print(f'{char_tl}' + f'{char_md}' * qtd + f'{char_tr}')
                    print(f'{char_sides} ' + ' ' * (qtd - 2) + f' {char_sides}')
                _text = f'{char_sides}  {text[index]}  {char_sides}'
                _text_len = len(_text)
                if _text_len < max_lenght + 5:
                    _text = f'{char_sides}  {text[index]}  '
                    while len(_text) < max_lenght + 5:
                        _text += ' '
                    _text += f'{char_sides}'

                print(_text)
                if index % 2 == 1:
                    print(f'{char_sides} ' + ' ' * (qtd - 2) + f' {char_sides}')

                if index == len(text) - 1:
                    print(f'{char_sides} ' + ' ' * (qtd - 2) + f' {char_sides}')
                    print(f'{char_bl}' + f'{char_md}' * qtd + f'{char_br}')
                index += 1
