from flask import Flask, render_template, request, jsonify
import sys
import os
from contextlib import redirect_stdout
import pygit2
import shutil


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def check_answer(answer, right_answer):
    return answer.strip() == right_answer.strip()


def check_solution(code):
    test_directory_name = 'tests'

    test_filenames = sorted([i for i in os.listdir(test_directory_name) if i.startswith('test')])

    answers_filenames = sorted([i for i in os.listdir(test_directory_name) if i.startswith('answer')])
    answers = []
    for answers_filename in answers_filenames:
        with open(f'{test_directory_name}/{answers_filename}', 'r', encoding='utf-8') as file:
            answers.append(file.read())

    test_info = []

    for i, test_filename in enumerate(test_filenames):
        input_filename = f'{test_directory_name}/{test_filename}'
        output_filename = 'output.txt'
        error_on_current_test = False
        with open(input_filename, 'r', encoding='utf-8') as file, open(output_filename, 'w',
                                                                       encoding='utf-8') as output_file:
            original_stdin = sys.stdin
            sys.stdin = file
            try:
                with redirect_stdout(output_file):
                    exec(code)
            except Exception as e:
                test_info.append([f'Test {i + 1}', 'RT'])
                error_on_current_test = True
            sys.stdin = original_stdin

        if not error_on_current_test:
            with open(output_filename, 'r', encoding='utf-8') as output_file:
                answer = output_file.read()
            if check_answer(answer, answers[i]):
                test_info.append([f'Test {i + 1}', 'OK'])
            else:
                test_info.append([f'Test {i + 1}', 'WA'])

    return jsonify(testing_data=test_info)


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    code = data.get('text')

    return check_solution(code)


@app.route('/check_solution_from_github', methods=['POST'])
def check_solution_from_github():
    local_path = './cloned_repository'

    if os.path.exists(local_path) and os.path.isdir(local_path):
        shutil.rmtree(local_path)

    repo_url = 'https://github.com/KonstBeliakov/test_repository.git'
    local_path = './cloned_repository'
    pygit2.clone_repository(repo_url, local_path)

    with open(f'./cloned_repository/main.py', 'r', encoding='utf-8') as f:
        code = f.read()

    return check_solution(code)


if __name__ == '__main__':
    app.run(debug=True)