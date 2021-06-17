import pytest


@pytest.fixture(scope='session')
def session_scope(request):
    print("Hi session")

    def fin():
        print('This is finalizer session')

    request.addfinalizer(fin)


@pytest.fixture(scope='module', params='ab')
def module_scope(request):
    print('Hi module')
    return request.param


@pytest.fixture(scope='class')
def class_scope(request):
    print('Hi class')

    def fin():
        print('Fin class')

    request.addfinalizer(fin)


@pytest.fixture
def method_scope():
    print('Hi method')
    yield
    print('By method')


@pytest.fixture(autouse=True)
def aut_scope():
    print('=== Autouse ===')
