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

Created by: Gabriel Menezes de Antonio (TR0NZ0D)
"""
import unittest

from tr0nz0d.tools.cpf import CPF


class TestCPFTools(unittest.TestCase):
    """Test case for cpf tools"""
    tools = CPF()
    divided_cpf = "998.097.640-30"
    numbers_cpf = "99809764030"
    invalid_divided_cpf = "998.097.640-99"
    invalid_numbers_cpf = "99809764099"
    invalid_sequential_divided_cpf = "111.111.111-11"
    invalid_sequential_numbers_cpf = "11111111111"
    invalid_missing_numbers_divided_cpf = "98.097.640-30"
    invalid_missing_numbers_numbers_cpf = "9809764030"
    invalid_exceed_numbers_divided_cpf = "1998.097.640-30"
    invalid_exceed_numbers_numbers_cpf = "199809764030"

    def test_cpf_generation(self):
        """Test cpf generation"""
        gen_cpf = self.tools.gerar()
        self.assertEqual(len(gen_cpf), 11)

    def test_cpf_formatting(self):
        """Test cpf formatting"""
        gen_cpf = self.tools.gerar()
        formatted = self.tools.formatar(gen_cpf)
        self.assertEqual(len(formatted), 14)

    def test_cpf_generation_formatted(self):
        """Test cpf formatted generation"""
        formatted_gen_cpf = self.tools.gerar_formatado()
        self.assertEqual(len(formatted_gen_cpf), 14)

    def test_valid_numbers_cpf(self):
        """Test cpf number validation"""
        valid_cpf = self.tools.validar(self.numbers_cpf)
        self.assertTrue(valid_cpf)

    def test_valid_divided_cpf(self):
        """Test cpf divided validation"""
        valid_cpf = self.tools.validar(self.divided_cpf)
        self.assertTrue(valid_cpf)

    def test_invalid_divided_cpf(self):
        """Test invalid cpf divided validation"""
        invalid_cpf = self.tools.validar(self.invalid_divided_cpf)
        self.assertFalse(invalid_cpf)

    def test_invalid_numbers_cpf(self):
        """Test invalid cpf numbers validation"""
        invalid_cpf = self.tools.validar(self.invalid_numbers_cpf)
        self.assertFalse(invalid_cpf)

    def test_invalid_sequential_divided_cpf(self):
        """Test invalid cpf squential divided validation"""
        invalid_cpf = self.tools.validar(self.invalid_sequential_divided_cpf)
        self.assertFalse(invalid_cpf)

    def test_invalid_sequential_numbers_cpf(self):
        """Test invalid cpf sequential numbers validation"""
        invalid_cpf = self.tools.validar(self.invalid_sequential_numbers_cpf)
        self.assertFalse(invalid_cpf)

    def test_invalid_missing_numbers_divided_cpf(self):
        """Test invalid cpf missing numbers divided validation"""
        invalid_cpf = self.tools.validar(self.invalid_missing_numbers_divided_cpf)
        self.assertFalse(invalid_cpf)

    def test_invalid_missing_numbers_numbers_cpf(self):
        """Test invalid cpf missing numbers validation"""
        invalid_cpf = self.tools.validar(self.invalid_missing_numbers_numbers_cpf)
        self.assertFalse(invalid_cpf)

    def test_invalid_exceed_numbers_divided_cpf(self):
        """Test invalid cpf exceed numbers divided validation"""
        invalid_cpf = self.tools.validar(self.invalid_exceed_numbers_divided_cpf)
        self.assertFalse(invalid_cpf)

    def test_invalid_exceed_numbers_numbers_cpf(self):
        """Test invalid cpf exceed numbers validation"""
        invalid_cpf = self.tools.validar(self.invalid_exceed_numbers_numbers_cpf)
        self.assertFalse(invalid_cpf)


if __name__ == "__main__":
    unittest.main()
