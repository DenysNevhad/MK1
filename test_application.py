import pytest
from application import find_top_words, write_to_file

@pytest.fixture
def sample_text_file(tmpdir):
    sample_text = """This is a sample text file for testing purposes.
    It contains some repeated words like sample, text, and testing."""
    file_path = tmpdir.join("sample.txt")
    with open(file_path, "w") as file:
        file.write(sample_text)
    return file_path

def test_find_top_words(sample_text_file):
    top_words = find_top_words(sample_text_file)
    expected_top_words = [('sample', 2), ('text', 2), ('testing', 2), ('this', 1), ('is', 1), ('a', 1), ('file', 1), ('for', 1), ('purposes', 1), ('it', 1)]

    assert top_words == expected_top_words

@pytest.mark.parametrize("words_count, expected_result", [
    ([('sample', 2), ('text', 2), ('testing', 1), ('this', 1), ('is', 1), ('a', 1), ('file', 1), ('for', 1), ('purposes', 1), ('it', 1)], "sample-2\ntext-2\ntesting-1\nthis-1\nis-1\na-1\nfile-1\nfor-1\npurposes-1\nit-1\n"),
    ([('word1', 3), ('word2', 2), ('word3', 1)], "word1-3\nword2-2\nword3-1\n"),
    ([], ""),
])
def test_write_to_file(tmpdir, words_count, expected_result):
    output_file_path = tmpdir.join("output.txt")
    write_to_file(words_count, str(output_file_path))
    assert output_file_path.read() == expected_result
