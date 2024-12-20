import main
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = main.Runner('Аркана')
        for walk in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = main.Runner('Мэл')
        for run in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = main.Runner('Виктор')
        runner_4 = main.Runner('Джейс')
        for run in range(10):
            runner_3.run()
        for walk in range(10):
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)

if __name__ == "__main__":
    unittest.main()