import unittest
from tr0nz0d.tools.cnpj import CNPJ


class TestCNPJTools(unittest.TestCase):
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
        gen_cnpj = self.tools.gerar()
        self.assertEqual(len(gen_cnpj), 14)

    def test_cnpj_formatting(self):
        gen_cnpj = self.tools.gerar()
        formatted = self.tools.formatar(gen_cnpj)
        self.assertEqual(len(formatted), 18)

    def test_cnpj_generation_formatted(self):
        formatted_gen_cnpj = self.tools.gerar_formatado()
        self.assertEqual(len(formatted_gen_cnpj), 18)

    def test_valid_numbers_cnpj(self):
        valid_cnpj = self.tools.validar(self.numbers_cnpj)
        self.assertEqual(valid_cnpj, True)

    def test_valid_divided_cnpj(self):
        valid_cnpj = self.tools.validar(self.divided_cnpj)
        self.assertEqual(valid_cnpj, True)

    def test_invalid_divided_cnpj(self):
        invalid_cnpj = self.tools.validar(self.invalid_divided_cnpj)
        self.assertEqual(invalid_cnpj, False)

    def test_invalid_numbers_cnpj(self):
        invalid_cnpj = self.tools.validar(self.invalid_numbers_cnpj)
        self.assertEqual(invalid_cnpj, False)

    def test_invalid_sequential_divided_cnpj(self):
        invalid_cnpj = self.tools.validar(self.invalid_sequential_divided_cnpj)
        self.assertEqual(invalid_cnpj, False)

    def test_invalid_sequential_numbers_cnpj(self):
        invalid_cnpj = self.tools.validar(self.invalid_sequential_numbers_cnpj)
        self.assertEqual(invalid_cnpj, False)

    def test_invalid_missing_numbers_divided_cnpj(self):
        invalid_cnpj = self.tools.validar(self.invalid_missing_numbers_divided_cnpj)
        self.assertEqual(invalid_cnpj, False)

    def test_invalid_missing_numbers_numbers_cnpj(self):
        invalid_cnpj = self.tools.validar(self.invalid_missing_numbers_numbers_cnpj)
        self.assertEqual(invalid_cnpj, False)

    def test_invalid_exceed_numbers_divided_cnpj(self):
        invalid_cnpj = self.tools.validar(self.invalid_exceed_numbers_divided_cnpj)
        self.assertEqual(invalid_cnpj, False)


if __name__ == "__main__":
    unittest.main()
