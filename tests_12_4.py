import logging
import unittest
from module12_log import Runner



class RunnerTest(unittest.TestCase):

    def test_walk(self):
       try:
           runner1 = Runner('Nik', -8)
           runner1.walk()
           logging.info('"test_walk" выполнен успешно')

       except Exception:
           logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner2 = Runner(33)
            runner2.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

if __name__ == '__main__':
    unittest.main()

logging.basicConfig(filename="runner_tests.log", filemode="w", level=logging.INFO,
                    encoding="utf-8", format='%(asctime)s | %(levelname)s | %(message)s')



