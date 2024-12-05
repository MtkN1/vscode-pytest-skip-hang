import pytest


@pytest.fixture
def docker_client() -> object:
    try:
        # NOTE: Actually connect with the docker sdk
        raise Exception("Docker client not available")
    except Exception:
        pytest.skip("Docker client not available")

    return object()


def test_hang(docker_client):
    # Running the test in VS Code will hang.
    assert ...
