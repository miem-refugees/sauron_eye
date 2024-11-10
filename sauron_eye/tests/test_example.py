from sauron_eye.dags.example_dag import test_func


def test_test_func():
    assert test_func() is None
