import unittest


class FuelTestCase(unittest.TestCase):
    def test_calculate_required(self):
        from day1.fuelrequired import calculate_required
        expected = 2
        given_mass = 12
        self.assertEqual(expected, calculate_required(given_mass))

    def test_calculate_required_large_number(self):
        from day1.fuelrequired import calculate_required
        expected = 966
        given_mass = 1969
        self.assertEqual(expected, calculate_required(given_mass))

    def test_calc_total_fuel(self):
        from day1.fuelrequired import calc_total_fuel
        expected = 5040874
        self.assertEqual(expected, calc_total_fuel(), "Not equal.")


if __name__ == '__main__':
    unittest.main()
