from morse import decode
import pytest


@pytest.mark.parametrize(
    "morse_msg,decoded_msg",
    [
        ('... --- ...', 'SOS'),  # Сработает
        ('.- .- .- -....- .- -.-. .- -.. . -- -.--',
         'AAA-ACADEMY'),  # Сработает
        ('.-. .. . -- .- -. -. .. .- -.   -- .- -. .. ..-. --- .-.. -..',
         'RIEMANNIAN MANIFOLD')  # Не сработает
    ]
)
def test_morse_decoder(morse_msg: str, decoded_msg: str) -> str:
    assert decode(morse_msg) == decoded_msg
