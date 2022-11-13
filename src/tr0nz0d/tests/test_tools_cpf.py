import unittest
from tr0nz0d.tools.cpf import CPF


class TestCPFTools(unittest.TestCase):
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
        gen_cpf = self.tools.gerar()
        self.assertEqual(len(gen_cpf), 11)

    def test_cpf_formatting(self):
        gen_cpf = self.tools.gerar()
        formatted = self.tools.formatar(gen_cpf)
        self.assertEqual(len(formatted), 14)

    def test_cpf_generation_formatted(self):
        formatted_gen_cpf = self.tools.gerar_formatado()
        self.assertEqual(len(formatted_gen_cpf), 14)

    def test_valid_numbers_cpf(self):
        valid_cpf = self.tools.validar(self.numbers_cpf)
        self.assertEqual(valid_cpf, True)

    def test_valid_divided_cpf(self):
        valid_cpf = self.tools.validar(self.divided_cpf)
        self.assertEqual(valid_cpf, True)

    def test_invalid_divided_cpf(self):
        invalid_cpf = self.tools.validar(self.invalid_divided_cpf)
        self.assertEqual(invalid_cpf, False)

    def test_invalid_numbers_cpf(self):
        invalid_cpf = self.tools.validar(self.invalid_numbers_cpf)
        self.assertEqual(invalid_cpf, False)

    def test_invalid_sequential_divided_cpf(self):
        invalid_cpf = self.tools.validar(self.invalid_sequential_divided_cpf)
        self.assertEqual(invalid_cpf, False)

    def test_invalid_sequential_numbers_cpf(self):
        invalid_cpf = self.tools.validar(self.invalid_sequential_numbers_cpf)
        self.assertEqual(invalid_cpf, False)

    def test_invalid_missing_numbers_divided_cpf(self):
        invalid_cpf = self.tools.validar(self.invalid_missing_numbers_divided_cpf)
        self.assertEqual(invalid_cpf, False)

    def test_invalid_missing_numbers_numbers_cpf(self):
        invalid_cpf = self.tools.validar(self.invalid_missing_numbers_numbers_cpf)
        self.assertEqual(invalid_cpf, False)

    def test_invalid_exceed_numbers_divided_cpf(self):
        invalid_cpf = self.tools.validar(self.invalid_exceed_numbers_divided_cpf)
        self.assertEqual(invalid_cpf, False)


if __name__ == "__main__":
    unittest.main()
