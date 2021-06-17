import pytest
import random


class TestDigit:
    def test_numbers(self, module_scope, class_scope, method_scope, session_scope):
        c = random.randint(-100, 100)

        assert c > 0, 'c < 0'

    def test_sum(self, session_scope):
        a = 5 + 7
        assert a == 12


class TestParams:
    @pytest.mark.parametrize('par', "bc")
    def test_params(self, module_scope, par):
        print(par, module_scope)
