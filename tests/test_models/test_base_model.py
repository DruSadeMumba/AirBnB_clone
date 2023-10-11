import unittest


class TestBaseModel(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()

    def id(self) -> str:
        return super().id()

    def test_save(self):
        self.fail()

    def test_to_dict(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
