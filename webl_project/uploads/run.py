import subprocess
import os


class Code:
    
    def __init__(self, code):
        self.code = code
    
    def check(self):
        print(type(self.code))
        #path = os.getcwd()
        #parent_path = os.path.abspath(os.path.join(path, os.pardir))
        #submissions_path = parent_path + '/webl_project/uploads/'
        #subprocess.run(['gcc', '-lm', self.code])
        #output = subprocess.run('./a.out', stdout=subprocess.PIPE, text=True)
        #print(output.stdout)

        #print(self.code)
        #print(parent_path)
        #print(submissions_path)