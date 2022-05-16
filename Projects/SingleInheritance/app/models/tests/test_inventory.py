import pytest
import sys
sys.path.insert(0, 'd:\\Study\\Projects\\SingleInheritance\\app\\models')
from inventory import Resource, HDD, SSD

def test_resource_creation():
    test_resource = Resource('Test', 'AMD', 10, 3)
    assert test_resource.name == 'Test'
    assert test_resource.total == 10


def test_invalid_parameters():
    with pytest.raises(ValueError):
        test_resource = Resource('Test', 'AMD', '10', 3)
    with pytest.raises(ValueError):
        test_resource = Resource('Test', 'AMD', 10, 11)
    with pytest.raises(ValueError):
        test_resource = Resource('Test', 'AMD', -1, -1)


def test_methods():
    test_resource = Resource('Test', 'AMD', 10, 3)
    test_resource.claim(2)
    assert test_resource.total == 10
    assert test_resource.allocated == 5

    test_resource.freeup(2)
    assert test_resource.total == 10
    assert test_resource.allocated == 3

    test_resource.died()
    assert test_resource.total == 9
    assert test_resource.allocated == 2

    test_resource.purchased(3)
    assert test_resource.total == 12
    assert test_resource.allocated == 2


def test_invalid_methods():
    test_resource = Resource('Test', 'AMD', 1, 0)
    with pytest.raises(ValueError):
        test_resource.freeup(1)
    with pytest.raises(ValueError):
        test_resource.claim(2)
    test_resource.died()
    with pytest.raises(AttributeError):
        test_resource.died()


def test_category():
    test_resource = Resource('Test', 'AMD', 1, 0)
    assert test_resource.category == 'resource'


def test_HDD_creation():
    test_resource = HDD('Test', 'AMD', 1, 0, 120, 2.5, 7200)


def test_SSD_creation():
    test_resource = SSD('Test', 'AMD', 1, 0, 120, 'PCI-E')
