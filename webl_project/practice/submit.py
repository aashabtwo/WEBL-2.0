import subprocess
import os


class Code:
    # constructor
    def __init__(self, code):
        self.code = code
    # checks the code against test cases
    def check(self):
        path = os.getcwd()
        parent_path = os.path.abspath(os.path.join(path, os.pardir))
        submissions_path = parent_path + '/webl_project/'
        subprocess.run(['gcc', '-lm', submissions_path + self.code])
        output = subprocess.run('./a.out', stdout=subprocess.PIPE, text=True)
        print(output.stdout.split('\n'))

        #print(self.code)
        #print(parent_path)
        #print(submissions_path)