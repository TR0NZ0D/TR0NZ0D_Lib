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

from tr0nz0d.tools.cnpj import CNPJ


class TestCNPJTools(unittest.TestCase):
    """Test case for cnpj tools"""
    tools = CNPJ()
    divided_cnpj = "34.095.155/0001-70"
    numbers_cnpj = "34095155000170"
    invalid_divided_cnpj = "34.095.155/0001-99"
    invalid_numbers_cnpj = "34095155000199"
    invalid_sequential_divided_cnpj = "11.111.111/1111-11"
    invalid_sequential_numbers_cnpj = "11111111111111"
    invalid_missing_numbers_divided_cnpj = "4.095.155/0001-70"
    invalid_missing_numbers_numbers_cnpj = "4095155000170"
    invalid_exceed_numbers_divided_cnpj = "154.095.155/0001-70"
    invalid_exceed_numbers_numbers_cnpj = "154095155000170"

    def test_cnpj_generation(self):
        """Test for cnpj generation"""
        gen_cnpj = self.tools.gerar()
        self.assertEqual(len(gen_cnpj), 14)

    def test_cnpj_formatting(self):
        """Test for cnpj formatting"""
        gen_cnpj = self.tools.gerar()
        formatted = self.tools.formatar(gen_cnpj)
        self.assertEqual(len(formatted), 18)

    def test_cnpj_generation_formatted(self):
        """Test for cnpj formatted generation"""
        formatted_gen_cnpj = self.tools.gerar_formatado()
        self.assertEqual(len(formatted_gen_cnpj), 18)

    def test_valid_numbers_cnpj(self):
        """Test for cnpj number validation"""
        valid_cnpj = self.tools.validar(self.numbers_cnpj)
        self.assertTrue(valid_cnpj)

    def test_valid_divided_cnpj(self):
        """Test for cnpj divided validation"""
        valid_cnpj = self.tools.validar(self.divided_cnpj)
        self.assertTrue(valid_cnpj)

    def test_invalid_divided_cnpj(self):
        """Test for invalid cnpj divided validation"""
        invalid_cnpj = self.tools.validar(self.invalid_divided_cnpj)
        self.assertFalse(invalid_cnpj)

    def test_invalid_numbers_cnpj(self):
        """Test for invalid cnpj numbers validation"""
        invalid_cnpj = self.tools.validar(self.invalid_numbers_cnpj)
        self.assertFalse(invalid_cnpj)

    def test_invalid_sequential_divided_cnpj(self):
        """Test for invalid cnpj sequential divided validation"""
        invalid_cnpj = self.tools.validar(self.invalid_sequential_divided_cnpj)
        self.assertFalse(invalid_cnpj)

    def test_invalid_sequential_numbers_cnpj(self):
        """Test for invalid cnpj sequential numbers validation"""
        invalid_cnpj = self.tools.validar(self.invalid_sequential_numbers_cnpj)
        self.assertFalse(invalid_cnpj)

    def test_invalid_missing_numbers_divided_cnpj(self):
        """Test for invalid cnpj missing divided numbers validation"""
        invalid_cnpj = self.tools.validar(self.invalid_missing_numbers_divided_cnpj)
        self.assertFalse(invalid_cnpj)

    def test_invalid_missing_numbers_numbers_cnpj(self):
        """Test for invalid cnpj missing numbers validation"""
        invalid_cnpj = self.tools.validar(self.invalid_missing_numbers_numbers_cnpj)
        self.assertFalse(invalid_cnpj)

    def test_invalid_exceed_numbers_divided_cnpj(self):
        """Test for invalid cnpj exceed divided numbers validation"""
        invalid_cnpj = self.tools.validar(self.invalid_exceed_numbers_divided_cnpj)
        self.assertFalse(invalid_cnpj)

    def test_invalid_exceed_numbers_numbers_cnpj(self):
        """Test for invalid cnpj exceed numbers validation"""
        invalid_cnpj = self.tools.validar(self.invalid_exceed_numbers_numbers_cnpj)
        self.assertFalse(invalid_cnpj)


if __name__ == "__main__":
    unittest.main()
