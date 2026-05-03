from app.game import check_guess

def test_correct():
    assert check_guess("apple", "apple") == ["correct"]*5

def test_partial():
    result = check_guess("apple", "apron")
    assert result[0] == "correct"
