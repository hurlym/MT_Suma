import pytest
import suma

@pytest.mark.parametrize("w", [
"abcc",
"aabbcccc",
"abbccc",
"aaabbbcccccc"
])
def test_acepta(w):
    assert suma.evaluar(w)

@pytest.mark.parametrize("w", [
"abc",
"aabbcc",
"aaccbb",
"aabbbcccccc",
"hola"
])
def test_rechaza(w):
    assert not suma.evaluar(w)