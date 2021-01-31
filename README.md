# collect-answers

This collects answers from multiple files based on question source file and
outputs answers to separate question files.

This a tool to help to assemble answers from assessment interviews.

## Usage

```shell

$ ./collect-answers.py questions.txt person1.txt person2.txt ...

```

Answers are split into separate files based on the questions. Name of the files
are starting with character 'q' and then numeber in the question file and
15 first characters of the question separated by a dash.
f.ex. 'q-1-what-do-you-do.txt'

### Question file format

Only single line questions are accepted.

### Answer files

The answers to questions have to be in the same order as in the questions file.
Answers between subsequent questions are copied to the files. Matching is done
by matching the exact question as in questions file.
