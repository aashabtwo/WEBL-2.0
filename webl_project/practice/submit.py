import subprocess
import os


class Code:
    # constructor
    def __init__(self, code, problem_title):
        self.code = code
        self.problem_title = problem_title.replace(" ", "")
    # checks the code against test cases

    # method to run code against test cases
    
    # initilize an empty array
    # configure the path
    # read the contents of the solution
    # call the testCode() function
    
    # inside testCode():
    # test the code against test cases
    # 
    def check(self):
        # this number will change to 1 if any of the test cases fail
        def testCode(solution_array, submissions_path):
            num = 0
            """
                THIS IS INCOMPLETE!
            """
            print(solution_array)
            #subprocess.run(['gcc', '-lm', submissions_path + self.code])
            #output = subprocess.run(['./a.out', '<', 'input0.txt'], capture_output=True)
            # attempt to compile the code
            # if any compilation error occurs
            # the error message will be sent back
            try:
                compile_code = os.popen('gcc -lm ' + self.code)
                # now attempting to execute the code
                # any occuring errors will returned as error messages
                try:
                    # in a loop
                    # and run the test cases
                    print('entering loop')
                    #p = submissions_path + '/practice/solutions/'+self.problem_title+'/input' + '1' + '.txt'
                    #print(p)
                    j = 0
                    for i in range(5):
                        # solution path
                        print(j)
                        path_solution = './a.out < ' + submissions_path + 'practice/solutions/'+self.problem_title+'/input' + str(i) + '.txt'
                        #print(path_solution)
                        #print(i)
                        execute_code = os.popen(path_solution).read().split('\n')
                        print(execute_code)
                        print(execute_code[0] + '\t' + solution_array[j])
                        #print(solution_array[j])
                        print(execute_code[1] + '\t' + solution_array[j+1])
                        if execute_code[0] != solution_array[j] or execute_code[1] != solution_array[j+1]:
                            num += 1
                            print('Worng. Breaking...')
                            break
                        else:
                            print('Passed!')

                        j=j+2
                    if num == 0:
                        return "SUCCESS!"
                    else:
                        return "Error bluh bluh"
                except Exception as error:
                    return error
            except Exception as e:
                return e
            
        solution_array = []
        path = os.getcwd()
        parent_path = os.path.abspath(os.path.join(path, os.pardir)) # path upto /WEBL
        submissions_path = parent_path + '/webl_project/'
        #print(type(self.problem_title))
        with open(submissions_path+'/practice/solutions/'+self.problem_title+'/solution.txt', 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                solution_array.append(line)
            result = testCode(solution_array, submissions_path)
        return result

        #print(self.code)
        #print(parent_path)
        #print(submissions_path)