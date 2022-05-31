import pytest
import main
import re

four_letter_words = [
    ('Word', 'Wrod'),
    ('test', 'tset'),
    ('moje', 'mjoe'),
    ('4567', '4657'),
]

sentences = [
    ('This is a long looong test sentence,\n with some big (biiiiig) words!'),
    ('I don not &62 43 know 7&2@# anything,'),
]

no_words = [
    (''),
    ('$%%%%%%'),
]

short_words = [
    ('a'),
    ('cs'),
    ('G'),
    ('sDf'),
    ('123'),
]


@pytest.mark.parametrize('word, expected_word', four_letter_words)
def test_four_letter_word(word, expected_word):
    assert main.encode(word) == main.separator + expected_word + main.separator + word


@pytest.mark.parametrize('word', short_words)
def test_short_words(word):
    assert main.encode(word) == main.separator + word + main.separator


@pytest.mark.parametrize('word', no_words)
def test_no_words(word):
    assert main.encode(word) == main.separator + word + main.separator


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


@pytest.mark.parametrize('sentence', sentences)
def test_words_in_sentence(sentence):
    tokenize_re = re.compile(r'(\w+)', re.U)
    original_words = tokenize_re.findall(sentence)
    test_words = []
    encoded_sentence = main.encode(sentence)
    _, _, words = encoded_sentence.split(main.separator)
    for word in original_words:
        if len(word) > 3:
            if word[1:-1] != word[1] * len(word[1:-1]):
                test_words.append(word)
    assert ' '.join(sorted(test_words, key=str.lower)) == words
