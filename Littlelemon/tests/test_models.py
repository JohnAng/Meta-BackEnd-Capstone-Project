from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):

    def get_test_cases(self):
        return [
            {
                "title": "IceCream",
                "price": 80,
                "inventory": 100,
                "expected_result": "IceCream : 80.00",
            },
            {
                "title": "Pizza",
                "price": 15.5,
                "inventory": 50,
                "expected_result": "Pizza : 15.50",
            },
            # Add more test cases as needed
        ]

    def test_get_item(self):
        for case in self.get_test_cases():
            with self.subTest(case=case):
                item = Menu.objects.create(
                    title=case["title"],
                    price=case["price"],
                    inventory=case["inventory"],
                )
                self.assertEqual(str(item), case["expected_result"])
