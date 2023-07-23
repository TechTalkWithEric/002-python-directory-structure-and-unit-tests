import unittest
from models.avenger import Avenger

class AvengerTests(unittest.TestCase):
    def test_avenger_model(self):
        print('loading avenger model test')
        avenger: Avenger = Avenger()

        self.assertIsNotNone(avenger)


    def test_avenger_model_name(self):
        print('loading avenger model test')
        avenger: Avenger = Avenger()
        avenger.first_name = "Tony"
        avenger.last_name = "Stark"
        avenger.super_hero_name = "Iron Man"

        self.assertIsNotNone(avenger)
        self.assertEqual(avenger.first_name, "Tony")
        self.assertEqual(avenger.last_name, "Stark")
        self.assertEqual(avenger.super_hero_name, "Iron Man")


if __name__ == "__main__":
    unittest.main()