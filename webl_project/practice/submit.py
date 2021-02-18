import subprocess
import os


class Code:
    # constructor
    def __init__(self, code, problem_title):
        self.code = code
        self.problem_title = problem_title
    # checks the code against test cases

    def check(self):
        def testCode(solution_array, submissions_path):
            print(solution_array)
            #subprocess.run(['gcc', '-lm', submissions_path + self.code])
            #output = subprocess.run(['./a.out', '<', 'input0.txt'], capture_output=True)
            compile_code = os.popen('gcc -lm ' + self.code)
            execute_code = os.popen('./a.out < ' + submissions_path + '/practice/input0.txt').read().split('\n')
            print(execute_code)
            #print(output.stdout.decode().split('\n'))
            if solution_array[0] == execute_code[0]:
                print('same')
                print(solution_array[0])
                print(execute_code[0])
                
            else:
                print(solution_array[0])
                print(execute_code[0])
                print('different')
            
        # initilize an empty array
        solution_array = []
        path = os.getcwd()
        parent_path = os.path.abspath(os.path.join(path, os.pardir))
        submissions_path = parent_path + '/webl_project/'
        #print(type(self.problem_title))
        with open(submissions_path+'/practice/solutions/'+self.problem_title+'/solution.txt', 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                solution_array.append(line)
            testCode(solution_array, submissions_path)
        

        #print(self.code)
        #print(parent_path)
        #print(submissions_path)