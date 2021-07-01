import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--ya',
        action='store',
        default='https://www.google.ru/',
        help='This is url'
    )


@pytest.fixture(scope='session')
def url_fixt(request):
    return request.config.getoption('--ya')
