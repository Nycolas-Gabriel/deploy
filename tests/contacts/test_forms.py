from contacts.forms import NameForm


def teste_name_form_success():
    # Given
    data = {"your_name": "Nycolas"}
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result is True


def test_name_form_your_name_max_length():
    # Given
    data = {"your_name": "Godofredo" * 22 + "Go"}  # Gera exatamente 200 caracteres
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result is False
    assert form.errors == {
         "your_name": ["Certifique-se de que o valor tenha no máximo 100 caracteres (ele possui 200)."]
    }


def teste_name_form_fail():
    # Given
    data = {}
    form = NameForm(data=data)

    # When
    is_bound = form.is_bound
    result = form.is_valid()

    # Then
    assert result is False
    assert is_bound is True
