import unittest
import subprocess

def create_tester(i):
    def tester(self):
        with open(f'./testcases/{i:02d}.in', 'r') as input:
            process = subprocess.run(["python3", "hw07.py"], stdin=input, capture_output=True)
        with open(f'./testcases/{i:02d}.out', 'r') as output:
            self.assertEqual(
                output.read().strip(),
                process.stdout.decode("utf-8").strip()
            )
    return tester

class TestHW07(unittest.TestCase):
    pass

for i in range(1, 101):
    setattr(TestHW07, f'test_case_{i:02d}', create_tester(i))

if __name__ == '__main__':
    unittest.main()
