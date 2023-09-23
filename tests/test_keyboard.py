from src.keyboard import Keyboard


kb = Keyboard('keyboard1', 25, 1)


def test_mixin():
    assert kb.language == 'EN'

    kb.change_lang()
    assert kb.language == 'RU'
