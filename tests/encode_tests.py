import pytest
import main
import re

four_letter_words = [
    ('Word', 'Wrod'),
    ('test', 'tset'),
    ('moje', 'mjoe'),
]

sentences = [
    ('This is a long looong test sentence,\n with some big (biiiiig) words!'),
]

no_words = [
    (''),
]

@pytest.mark.parametrize('word, expected_word', four_letter_words)
def test_four_letter_word(word, expected_word):
    assert main.encode(word) == main.separator + expected_word + main.separator + word


@pytest.mark.parametrize('sentence', sentences)
def test_letters_in_words(sentence):
    tokenize_re = re.compile(r'(\w+)', re.U)
    original_words = tokenize_re.findall(sentence)
    encoded_sentence = main.encode(sentence)
    _, encoded_sentence, _ = encoded_sentence.split(main.separator)
    encoded_words = tokenize_re.findall(encoded_sentence)
    assert len(original_words) == len(encoded_words)
    for i in range(len(original_words)):
        assert sorted(original_words[i]) == sorted(encoded_words[i])

