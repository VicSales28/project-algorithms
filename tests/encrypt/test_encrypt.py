import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("abbcca", "4")

    with pytest.raises(TypeError):
        encrypt_message(112233, 3)

    assert encrypt_message("aabbcc", 3) == "baa_ccb"
    assert encrypt_message("abbcca", 4) == "ac_cbba"
    assert encrypt_message("word", 9) == "drow"
