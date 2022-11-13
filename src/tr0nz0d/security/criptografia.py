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

from cryptography.fernet import Fernet


def _gen_key():
    key = Fernet.generate_key()
    return key


class Criptografia():
    def __init__(self) -> None:
        self.key = _gen_key()

    def criptografar(self, text: str) -> list[bytes]:
        """ Criptografa o conteúdo passado e retorna o conteúdo e a chave.

        Parâmetros
        -----------
        text: :class:`str`
            Texto a ser encriptado.

        Returns
        -----------
        [mensagem, chave]: :class:`list`
            Uma lista contendo a mensagem criptografada e a chave.
        """
        self.key = _gen_key()
        text = str(text)
        text_encode = text.encode()
        f = Fernet(self.key)
        text_criptografada = f.encrypt(text_encode)

        return [text_criptografada, self.key]

    def descriptografar(self, text: bytes) -> str:
        """Descriptografa o conteúdo passado com a chave armazenada e retorna o texto literal.

        Parâmetros
        -----------
        text: :class:`bytes`
            Texto criptografado a ser descriptografado.

        Returns
        -----------
        text: :class:`str`
            O texto literal descriptografado.

        Raises
        -----------
        InvalidToken
            Se a chave armazenada não for válida para descriptografar o texto.
        """
        if type(text) != bytes:
            text = str(text).encode()
        f = Fernet(self.key)
        text_bytes = f.decrypt(text)
        text_txt = str(text_bytes, "utf-8")

        return text_txt

    def descriptografar_com_chave(self, text: bytes, custom_key: bytes) -> str:
        """Descriptografa o texto passado utilizando a chave disponibilizada e retorna o texto literal.

        Parâmetros
        -----------
        text: :class:`bytes`
            Texto criptografado a ser descriptografado.
        custom_key: :class:`bytes`
            A chave que criptografou o texto.

        Returns
        -----------
        text: :class:`str`
            O texto literal descriptografado.

        Raises
        -----------
        InvalidToken
            Se a chave passada não for válida para a descriptografia do texto.
        """
        if type(text) != bytes:
            text = str(text).encode()
        f = Fernet(custom_key)
        text_bytes = f.decrypt(text)
        text_txt = str(text_bytes, "utf-8")

        return text_txt
