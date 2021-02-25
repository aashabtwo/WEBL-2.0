import subprocess
import os


class Code:
    # constructor
    def __init__(self, code, problem_title):
        self.code = code
        self.problem_title = problem_title.replace(" ", "")

    # Create an empty solution array
    # Read the solution text using the second argument
    # and append to the solution array
    # Now start the testCode() function which
    # has arguments 'solution_array' and submissions path
    # Start with num = 0 and empty "test_results" array
    # Compile the code in a try-catch block
    # Open another try-catch block and run a loop of execute commands
    # the loop represents the number of test cases
    # Append the passed test cases to the test_results array
    # If a test case fails, break the loop, and set num = 1
    # Append a False or True element at the end of the test_results
    # array depending whether a test case fails or not
    def check(self):
        def testCode(solution_array, submissions_path):
            num = 0
            test_results = []
            """
                THIS IS INCOMPLETE!
            """
            print(solution_array)
            try:
                compile_code = os.popen('gcc -lm ' + self.code)
                try:
                    print('entering loop')
                    p = submissions_path + ('/practice/solutions/'+self.problem_title+'/input' + '1' + '.txt')
                    j = 0
                    for i in range(5):
                        path_solution = ('./a.out < ' + submissions_path + 'practice/solutions/'+self.problem_title+'/input' + str(i) + '.txt')
                        execute_code = os.popen(path_solution).read().split('\n')
                        print(execute_code)
                        print(execute_code[0] + '\t' + solution_array[j])
                        print(execute_code[1] + '\t' + solution_array[j+1])
                        if execute_code[0] != solution_array[j] or execute_code[1] != solution_array[j+1]:
                            num += 1
                            test_results.append('Failed')
                            print('Wrong. Breaking...')
                            break
                        else:
                            test_results.append('Passed')
                            print('Passed!')
                        j=j+2
                    if num == 0:
                        test_results.append(True)
                        return test_results
                    else:
                        test_results.append(False)
                        return test_results
                except Exception as error:
                    return error
            except Exception as e:
                return e
            
        solution_array = []
        path = os.getcwd()
        parent_path = os.path.abspath(os.path.join(path, os.pardir)) # path upto /WEBL
        submissions_path = (parent_path + '/webl_project/')
        with open(submissions_path+'/practice/solutions/'+self.problem_title+'/solution.txt', 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                solution_array.append(line)
            result = testCode(solution_array, submissions_path)
        return result
"""
    JUNK
    #subprocess.run(['gcc', '-lm', submissions_path + self.code])
            #output = subprocess.run(['./a.out', '<', 'input0.txt'], capture_output=True)

"""