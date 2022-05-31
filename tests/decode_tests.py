import pytest
import main
import re

sentences = [
    ('This is a long looong test sentence,\n with some big (biiiiig) words!'),
]


@pytest.mark.parametrize('sentence', sentences)
def test_encode_decode(sentence):
    encoded_sentence = main.encode(sentence)
    decoded_sentence = main.decode(encoded_sentence)
    assert sentence == decoded_sentence
