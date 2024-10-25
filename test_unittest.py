import unittest
from reverse import my_reverse


class TestMyReverse(unittest.TestCase):
    def test_empty_string(self):
        # Тест для пустой строки.
        self.assertEqual(my_reverse(""), "")

    def test_single_character(self):
        # Тест для строки с одним символом.
        self.assertEqual(my_reverse("a"), "a")

    def test_two_characters(self):
        # Тест для строки с двумя символами
        self.assertEqual(my_reverse("ab"), "ba")

    def test_numbers(self):
        # Тест для строки с числами.
        self.assertEqual(my_reverse("10"), "01")

    def test_three_characters(self):
        # Тест для строки с тремя символами.
        self.assertEqual(my_reverse("abc"), "cba")

    def test_text_1(self):
        # Тест для строки с текстом.
        self.assertEqual(my_reverse("hello, world"), "dlrow ,olleh")

    def test_text_2(self):
        # Тест для строки с длинным текстом (100 символов).
        input_value = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in."
        result_value = ".ni tirerdneh ni rolod eruiri mue lev metua siuD .tauqesnoc odommoc ae xe piuqila tu lsin sitrobol tipicsus reprocmallu noitat icrexe durtson siuq ,mainev minim da mine isiw tU .taptulov tare mauqila angam erolod teeroal tu tnudicnit domsiue hbin ymmunon maid des ,tile gnicsipida reutetcesnoc ,tema tis rolod muspi meroL"
        self.assertEqual(my_reverse(input_value), result_value)


if __name__ == "__main__":
    unittest.main()
