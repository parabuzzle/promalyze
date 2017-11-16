from promalyze.vector import Vector


class TestVector:

    @staticmethod
    def meta():
        return {
            '__name__': 'test_metric',
            'tag1': 'value1'
        }

    @staticmethod
    def value():
        return [1234, 1]

    def mockvector(self):
        return {
            'metric': self.meta(),
            'value': self.value()
        }

    def setup(self):
        self.vector = Vector(self.mockvector())

    def teardown(self):
        self.vector = None

    def test_as_json(self):
        assert self.vector.as_json()['value'] == 1
        assert self.vector.as_json()['name'] == 'test_metric'
