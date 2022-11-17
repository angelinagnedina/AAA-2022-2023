from morse import encode


def check_morse_encoder(message: str) -> str:
    r"""
    >>> encode('SOS')
    '... --- ...'
    >>> encode('@@@ ACADEMY') # Будет ошибка из-за отсутствия кодировки для "@"
    '.. --. .   .. -.. -.'
    """
    return encode(message)
