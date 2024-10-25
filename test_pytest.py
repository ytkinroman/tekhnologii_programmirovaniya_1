import pytest
from reverse import my_reverse


def test_empty_string():
    # Тест для пустой строки.
    assert my_reverse("") == ""


def test_single_character():
    # Тест для строки с одним символом.
    assert my_reverse("a") == "a"


def test_two_characters():
    # Тест для строки с двумя символами
    assert my_reverse("ab") == "ba"


def test_numbers():
    # Тест для строки с числами.
    assert my_reverse("10") == "01"


def test_three_characters():
    # Тест для строки с тремя символами.
    assert my_reverse("abc") == "cba"


def test_text_1():
    # Тест для строки с текстом.
    assert my_reverse("hello, world") == "dlrow ,olleh"


def test_text_2():
    # Тест для строки с длинным текстом (100 символов).
    input_value = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in."
    result_value = ".ni tirerdneh ni rolod eruiri mue lev metua siuD .tauqesnoc odommoc ae xe piuqila tu lsin sitrobol tipicsus reprocmallu noitat icrexe durtson siuq ,mainev minim da mine isiw tU .taptulov tare mauqila angam erolod teeroal tu tnudicnit domsiue hbin ymmunon maid des ,tile gnicsipida reutetcesnoc ,tema tis rolod muspi meroL"
    assert my_reverse(input_value) == result_value


if __name__ == "__main__":
    pytest.main()
