from reverse import my_reverse


def main() -> None:
    # Проверяем на итоговый результат.
    assert my_reverse("") == ""
    assert my_reverse("a") == "a"
    assert my_reverse("ab") == "ba"
    assert my_reverse("10") == "01"
    assert my_reverse("abc") == "cba"
    assert my_reverse("hello, world") == "dlrow ,olleh"

    result = my_reverse("Привет")
    print(result)


if __name__ == "__main__":
    main()
