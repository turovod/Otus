import allure
import pytest

@allure.feature('Тестовый')
#@allure.story('Разные тесты')
def test_success_():
    """this test succeeds"""
    assert True

@allure.feature('Не тестовый')
#@allure.story('Одинаковые тесты тесты')
def test_failure_():
    """this test fails"""
    assert False

@allure.feature('По мылу')
def test_skip_():
    """this test is skipped"""
    pytest.skip('for a reason!')

@allure.feature('Тестовый')
def test_broken_():
    raise Exception('oops')
