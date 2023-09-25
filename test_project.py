from project import get_word, check_guess,give_explanation

def test__word_length():
    assert len(get_word()) == 8
    assert len(get_word()) != 0

def test_check_guess(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _:"correct")
    assert check_guess("correct") == True
    monkeypatch.setattr("builtins.input", lambda _:"incorrect")
    assert check_guess("gibberish") == False

def test_give_explanation(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _:"b")
    assert give_explanation() == True
    monkeypatch.setattr("builtins.input", lambda _:"B")
    assert give_explanation() == True


