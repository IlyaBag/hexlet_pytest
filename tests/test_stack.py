import pytest


def test_normal_behavior():  # позитивный сценарий
    stack = []

    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_emptiness():  # тест на доп. функции стека
    stack = []
    assert not stack

    stack.append('one')
    assert bool(stack)

    stack.pop()
    assert not stack


def test_pop_with_empty_stack():  # пограничные случаи
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
