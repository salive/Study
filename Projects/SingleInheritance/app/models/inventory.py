

class Resource():
    '''
    Base class for resourse with following parameters:
    - `name` : user-friendly name of resource instance (e.g.` Intel Core i9-9900K`)
    - `manufacturer` - resource instance manufacturer (e.g. `Nvidia`)
    - `total` : inventory total (how many are in the inventory pool)
    - `allocated` : number allocated (how many are already in use)
    - a `__str__` representation that just returns the resource name
    - a mode detailed `__repr__` implementation
    - `claim(n)` : method to take n resources from the pool (as long as inventory is available)
    - `freeup(n)` : method to return n resources to the pool (e.g. disassembled some builds)
    - `died(n)` : method to return and permanently remove inventory from the pool (e.g. they broke something) - as long as total available allows it
    - `purchased(n)` - method to add inventory to the pool (e.g. they purchased a new CPU)
    - `category` - computed property that returns a lower case version of the class name
    '''

    def __init__(self, name, manufacturer, total, allocated):
        __slots__ = 'name, manufacturer, total, allocated'
        self._name = name
        self._manufacturer = manufacturer
        self.check_valid_type(total)
        self.check_valid_type(allocated)
        if allocated > total:
            raise ValueError('Allocated could not exeed total')
        self._total = total
        self._allocated = allocated

    @property
    def category(self):
        return f'{self.__class__.__name__.lower()}'

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    def check_valid_type(self, n, type=int, default_value=0):
        if not isinstance(n, int) or n < default_value:
            raise ValueError('Value must be integer number > 0')
        return True

    def __repr__(self):
        return f'{self.__class__.__name__}: {vars(self)}'

    def claim(self, amount):
        self.check_valid_type(amount, default_value=0)
        if amount > self.total - self.allocated:
            raise ValueError('Amount exeeds total')
        self._allocated += amount
        return f' {amount} {self.name} successfully claimed'

    def freeup(self, amount):
        self.check_valid_type(amount, default_value=0)
        if amount > self.allocated:
            raise ValueError('Amount exeeds allocated units')
        self._allocated -= amount
        return f' {amount} {self.name} successfully freeup'

    def died(self):
        if self.allocated > 0:
            self._allocated -= 1
            self._total -= 1
        elif self.total > 0:
            self._total -= 1
        else:
            raise AttributeError('There is nothing to die')
        return f'Press F for {self.name}'

    def purchased(self, amount):
        self.check_valid_type(amount, default_value=0)
        self._total += amount


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity):
        super().__init__(name, manufacturer, total, allocated)
        self.check_valid_type(capacity)
        self._capacity = capacity

    @property
    def capacity(self):
        return self._capacity


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity)
        self.check_valid_type(rpm)
        self._rpm = rpm
        if size not in [2.5, 3.5]:
            raise ValueError('Size must be 2.5 or 3.5')
        self._size = size

    @property
    def rpm(self):
        return self._rpm

    @property
    def size(self):
        return self._size


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity, interface):
        super().__init__(name, manufacturer, total, allocated, capacity)
        self._interface = interface

    @property
    def interface(self):
        return self._interface


if __name__ == '__main__':
    pass
