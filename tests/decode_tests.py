import pytest
import main
import re

sentences = [
    ('This is a long looong test sentence,\n with some big (biiiiig) words!'),
    ('I don not &62 43 know 7&2@# anything,'),
]

encoded_sentences = [
    (
        main.separator + 'Tihs is a lnog lonoog tset stneecne,\n wtih smoe big (biiiiig) wdors!' + main.separator + 'long looong sentence some test This with words',
        'This is a long looong test sentence,\n with some big (biiiiig) words!'),
    (
        main.separator + 'Abbba Bruta Csess DDDes Efg F' + main.separator + 'Butra Cesss DeDDs',
        'Abbba Butra Cesss DeDDs Efg F'),

    (
        main.separator + 'A$b^C2=h' + main.separator,
        'A$b^C2=h'
    ),
]


@pytest.mark.parametrize('sentence', sentences)
def test_encode_decode(sentence):
    encoded_sentence = main.encode(sentence)
    decoded_sentence = main.decode(encoded_sentence)
    assert sentence == decoded_sentence


@pytest.mark.parametrize('encoded_sentence,original_sentence', encoded_sentences)
def test_decode(encoded_sentence, original_sentence):
    decoded_sentence = main.decode(encoded_sentence)
    assert original_sentence == decoded_sentence


@pytest.mark.parametrize('sentence', sentences)
def test_exception(sentence):
    with pytest.raises(ValueError, match='Error: Text is not valid'):
        main.decode(sentence)
