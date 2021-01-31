#!/usr/bin/env python3

import re
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('questionfile')
    parser.add_argument('answerfiles', nargs='*')
    return parser.parse_args()


def parse_questions(file):
    lines = []
    with open(file) as f:
        lines = [line.rstrip() for line in f.readlines() if line.rstrip()]
    return lines


def find_answers(files, question, stopstr):
    answers = []
    for af in files:
        answers.append(find_answer(af, question, stopstr))
    return answers


def find_answer(file, question, stopstr):
    answer = []
    rec = False
    with open(file) as f:
        for line in f.readlines():
            if line.startswith(question):
                rec = True
                answer.append(file)
                continue
            if rec:
                if line.startswith(stopstr):
                    break
                answer.append(line.rstrip())
    return answer


def write_answers(num, question, answers):
    qname = question.replace(' ', '-').replace('?', '').replace("'", '')[0:15]
    with open(f"q-{num+1}_{qname}.txt", "w+") as f:
        f.write(question)
        f.write("\n\n")
        for a in answers:
            fname = a.pop(0)
            f.write(f"{fname}:\n")
            for aa in a:
                f.write(f"\t{aa}\n")
            f.write("\n")


def main():
    args = parse_args()
    questions = parse_questions(args.questionfile)
    for c,q in enumerate(questions):
        if c+1 >= len(questions):
            stopstr = 'XXXX'
        else:
            stopstr = questions[c+1]
        answers = find_answers(args.answerfiles, q, stopstr)
        write_answers(c, q, answers)


if __name__ == '__main__':
    main()
