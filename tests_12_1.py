import unittest
import runner

Runner=runner.Runner
TestCase=unittest.TestCase

class RunnerTest(TestCase):
    def test_walk(self):
        wolker = Runner('Тихоня')
        for i in range(10):
            wolker.walk()
        self.assertEqual(wolker.distance, 50, 'test_walk: Test is filed!')
        # 1изменение параметра теста
        # for i in range(10): на for i in range(8):
        # 1. Вывод ниже

    def test_run(self):
        runner = Runner('Торопыжка')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100,'test_run: Test is filed!')

        # 2 изменение параметра теста
        # self.assertEqual(runner.distance, 100)
        # на self.assertEqual(runner.distance, 500)
        # 2. Вывод ниже

    def test_challenge(self):
        wolker = Runner('Александра')
        runner = Runner('Александр')

        for i in range(10):
            wolker.walk(), runner.run()
        self.assertNotEqual(wolker.distance, runner.distance,'test_challenge: Test is filed!')
        # 3 изменение параметра теста
        # runner.self.distance += 5 изменен на runner.self.distance += 5
        # 3. Вывод ниже


if __name__ == '__main__':
    unittest.main()




'''
**********Вывод1. изменение параметра теста***************
for i in range(10): на for i in range(8):

test_walk: Test is filed
50 != 40
Expected :40
Actual   :50
Ran 3 tests in 0.005s
FAILED (failures=1)


***********Вывод2. изменение параметра теста**************
self.assertEqual(runner.distance, 100)
на self.assertEqual(runner.distance, 500)   
   
test_run: Test is filed!
500 != 100
Expected :100
Actual   :500
Ran 3 tests in 0.005s
FAILED (failures=1)

***********Вывод3 изменение параметра теста**************   
runner.wolk.distance += 5 изменен на runner.wolk.distance += 10  

FAILED (failures=2)

Failure
Traceback (most recent call last):
  
    self.assertNotEqual(wolker.distance, runner.distance,'test_challenge: Test is filed!')

AssertionError: 100 == 100 : test_challenge: Test is filed!
 
 

test_walk: Test is filed!
50 != 100
Expected :100
Actual   :50
 
    
'''