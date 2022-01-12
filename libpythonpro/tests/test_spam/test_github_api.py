from unittest.mock import Mock

import pytest

from libpythonpro import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('renzo')
    assert avatar_url == url

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/402714v=4'
    resp_mock.json.return_value = {
        'login': 'renzo', 'id': 6402714,
        'avatar_url': url,
    }
    get_mock=mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value=resp_mock
    return url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('JosemarBrito')
    assert 'https://avatars.githubusercontent.com/u/65689172?v=4' == url


