# Smoke test — proves the verify:fast gate wiring; real suites arrive with each D-task.
import dobra


def test_package_imports():
    assert dobra.__version__
