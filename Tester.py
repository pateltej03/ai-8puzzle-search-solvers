#!/usr/bin/env python
# coding: utf-8

# In[21]:


import re
import io
import sys
from IPython.display import display, HTML

class PuzzleState:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move

def run_solution(solution_file, input_file):
    with open(input_file, 'r') as f:
        input_content = f.read().strip()

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    with open(solution_file, 'r') as file:
        exec(file.read(), {'__name__': '__main__'})
    
    sys.stdout = old_stdout
    
    return new_stdout.getvalue()

def parse_output(output):
    solutions = {}
    current_question = None
    for line in output.split('\n'):
        line = line.strip()
        if "solution of Q" in line:
            match = re.search(r'Q(\d+\.\d+[a-e]?)', line)
            if match:
                current_question = match.group(1)
                solutions[current_question] = ""
        elif current_question and line:
            solutions[current_question] = line.strip()
    return solutions


def grade_solution(solution_file, input_file):
    with open(input_file, 'r') as f:
        initial_state = f.read().strip()

    output = run_solution(solution_file, input_file)
    parsed_output = parse_output(output)
    
    feedback = []

    if "q2" in solution_file.lower():
        expected_questions = ["2.1a", "2.1b", "2.1c", "2.1d", "2.1e"]
        # goal_test = goal_test_q2
    else:
        expected_questions = ["1.1a", "1.1b", "1.1c", "1.1d", "1.1e"]
        # goal_test = goal_test_q1
    
    for question in expected_questions:
        if question in parsed_output:
            feedback.append(f"Q{question}: Valid solution")
        else:
            feedback.append(f"Q{question}: Invalid/Missing solution")

    return feedback

def display_feedback(feedback):
    print("Feedback:")
    print("Question\tFeedback")
    for fb in feedback:
        question, result = fb.split(': ', 1)
        status = "Valid" if "Valid solution" in result else "Invalid/Missing"
        print(f"{question}\t{status}")


solution_file = "solution_q2.py"
input_file = "input.txt"

feedback = grade_solution(solution_file, input_file)
display_feedback(feedback)


# In[ ]:




