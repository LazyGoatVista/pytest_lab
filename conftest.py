import pytest


class Runner:
    def __init__(self, name):
        pass

    def close(self):
        pass


@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}
    return _make_customer_record


@pytest.fixture
def runner_hub():
    ssh_runners = []
    def _runner_hub(name):
        runner = Runner(name)
        ssh_runners.append(runner)
        return runner

    yield _runner_hub

    for ssh_runner in ssh_runners:
        ssh_runner.close()