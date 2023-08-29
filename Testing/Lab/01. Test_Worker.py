class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def test_is_object_is_initialized(self):
        worker = Worker("Test", 1000, 50)

        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(50, worker.energy)

    def test_is_worker_energy_is_increased(self):
        worker = Worker("Test", 1000, 50)

        expected_energy = worker.energy + 1

        worker.rest()

        self.assertEqual(expected_energy, worker.energy)

    def test_is_raise_energy(self):
        worker = Worker("Test", 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_is_money_increased(self):
        worker = Worker("Test", 1000, 50)

        expected_money = worker.money + worker.salary

        worker.work()

        self.assertEqual(expected_money, worker.money)

    def test_is_energy_decreased(self):
        worker = Worker("Test", 1000, 50)
        expected_energy = worker.energy - 1

        worker.work()

        self.assertEqual(expected_energy, worker.energy)

    def test_get_info_method_return(self):
        worker = Worker("Test", 1000, 50)
        expected = f"{worker.name} has saved {worker.money} money."
        actual = worker.get_info()
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()
