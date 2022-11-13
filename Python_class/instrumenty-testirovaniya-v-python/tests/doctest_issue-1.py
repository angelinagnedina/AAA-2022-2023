from morse import encode


def check_morse_encoder(message: str) -> str:
    r"""
    >>> encode('SOS')
    '... --- ...'
    >>> encode('AAA ACADEMY')
    '.. --. .   .. -.. -.'
    """
    return encode(message)
