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


def apenas_numeros(cpf):
    cpf = str(cpf)
    return sub(r'\D', '', cpf)


class CPF:
    def gerar(self) -> str:
        """Gera um CPF aleatório.

        Returns
        -----------
        cpf: :class:`str`
            O CPF não formatado.
        """
        numero = str(randint(100000000, 999999999))
        novo_cpf = numero
        reverso = 10
        total = 0

        for index in range(19):
            if index > 8:
                index -= 9

            total += int(novo_cpf[index]) * reverso

            reverso -= 1
            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                novo_cpf += str(d)

        return novo_cpf

    def formatar(self, cpf: str) -> str:
        """Formata um CPF para conter os caracteres de divisão.

        Parâmetros
        -----------
        cpf: :class:`str`
            CPF que deve ser formatado.

        Returns
        -----------
        cpf: :class:`str`
            O CPF formatado.

        Raises
        -----------
        ValueError
            Se o CPF passado não tiver um comprimento de 11 caracteres.
        """
        cpf = str(cpf)

        cpf = apenas_numeros(cpf)

        if len(str(cpf)) != 11:
            raise ValueError('CPF deve conter um comprimento de 11 caracteres.')

        formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
        return formatado

    def gerar_formatado(self):
        """Gera um CPF aleatório e o retorna já formatado.

        Returns
        -----------
        cpf: :class:`str`
            O CPF criado e formatado.
        """
        cpf = self.gerar()
        cpf_formatado = self.formatar(cpf)

        return cpf_formatado

    def validar(self, cpf: str) -> bool:
        """Verifica a autenticidade matemática de um CPF.

        Parâmetros
        -----------
        cpf: :class:`str`
            CPF que deve ser validado.

        Returns
        -----------
        válido: :class:`bool`
            `True` caso o CPF for válido, caso contrário, `False`.
        """
        cpf = str(cpf)
        cpf = sub(r'\D', '', cpf)

        if not cpf.isnumeric() or len(str(cpf)) != 11:
            return False
        else:
            cpf_original = cpf[:-2]
        novo_cpf = ''
        digito1 = 0
        digito2 = 0
        current = 0
        valor_soma1 = 0
        valor_soma2 = 0

        # Dígito 1
        for c in range(10, 1, -1):
            for n in cpf_original[current]:
                valor1 = int(n) * c
                valor_soma1 += valor1
                current += 1
                break
        calculo1 = 11 - (valor_soma1 % 11)
        calculo1_2 = calculo1 > 9
        digito1 = 0 if calculo1_2 else calculo1
        current = 0

        # Dígito 2
        for c in range(11, 1, -1):
            for n in (cpf_original + str(digito1))[current]:
                valor2 = int(n) * c
                valor_soma2 += valor2
                current += 1
                break
        calculo2 = 11 - (valor_soma2 % 11)
        calculo2_2 = calculo2 > 9
        digito2 = 0 if calculo2_2 else calculo2

        novo_cpf = cpf_original + str(digito1) + str(digito2)

        sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

        if cpf == novo_cpf and not sequencia:
            return True
        else:
            return False
