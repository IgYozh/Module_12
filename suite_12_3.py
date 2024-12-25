import unittest
import tests_12_3



perem = unittest.TestSuite()
perem.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
perem.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(perem)