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

from random import randint
from re import sub

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def _apenas_numeros(cnpj) -> str:
    cnpj = str(cnpj)
    return sub(r'\D', '', cnpj)


def _eh_sequencia(cnpj) -> bool:
    cnpj = str(cnpj)
    sequencia = cnpj[0] * len(str(cnpj))
    if sequencia == cnpj:
        return True
    else:
        return False


def _calcula_digito(cnpj, digito) -> str:
    cnpj = str(cnpj)
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]

    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return "99999999999999"

    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'


class CNPJ:
    def gerar(self) -> str:
        """Gera um CNPJ aleatório.

        Returns
        -----------
        cnpj: :class:`str`
            O CNPJ não formatado.
        """
        primeiro_digito = randint(0, 9)
        segundo_digito = randint(0, 9)
        segundo_bloco = randint(100, 999)
        terceiro_bloco = randint(100, 999)
        quarto_bloco = '0001'

        inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}00'

        novo_cnpj = _calcula_digito(cnpj=inicio_cnpj, digito=1)
        novo_cnpj = _calcula_digito(cnpj=novo_cnpj, digito=2)

        return novo_cnpj

    def formatar(self, cnpj: str) -> str:
        """Formata um CNPJ para conter os caracteres de divisão.

        Parâmetros
        -----------
        cnpj: :class:`str`
            CNPJ que deve ser formatado.

        Returns
        -----------
        cnpj: :class:`str`
            O CNPJ formatado.

        Raises
        -----------
        ValueError
            Se o CNPJ passado não tiver um comprimento de 14 caracteres.
        """
        cnpj = str(cnpj)

        cnpj = _apenas_numeros(cnpj)

        if len(str(cnpj)) != 14:
            raise ValueError('CNPJ deve conter um comprimento de 14 caracteres.')

        formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
        return formatado

    def gerar_formatado(self):
        """Gera um CNPJ aleatório e o retorna já formatado.

        Returns
        -----------
        cnpj: :class:`str`
            O CNPJ criado e formatado.
        """
        cnpj = self.gerar()
        cnpj_formatado = self.formatar(cnpj)

        return cnpj_formatado

    def validar(self, cnpj: str) -> bool:
        """Verifica a autenticidade matemática do CNPJ.

        Parâmetros
        -----------
        cnpj: :class:`str`
            CNPJ que deve ser validado.

        Returns
        -----------
        valido: :class:`bool`
            `True` caso o CNPJ for válido, caso contrário, `False`.
        """
        cnpj = str(cnpj)
        cnpj = _apenas_numeros(cnpj)

        try:
            if _eh_sequencia(cnpj):
                return False

            novo_cnpj = _calcula_digito(cnpj=cnpj, digito=1)
            novo_cnpj = _calcula_digito(cnpj=novo_cnpj, digito=2)
        except Exception as e:
            print(e)
            return False

        if novo_cnpj == cnpj:
            return True
        else:
            return False
