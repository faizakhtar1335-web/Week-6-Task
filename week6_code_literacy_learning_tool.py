#!/usr/bin/env python3
"""
CodeSteps – Beginner Code Literacy Learning Tool
=================================================
A small command-line capstone prototype for non-programmers.

Features:
- Plain-language explanations of core programming concepts
- Everyday analogies and small Python examples
- Multiple-choice practice with immediate explanations
- Session score and topic review
- Input validation and graceful exit

Requirements: Python 3.8+; standard library only.
Run: python week6_code_literacy_learning_tool.py

This is an educational prototype. It does not collect personal information
or save learner results to an external service.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Question:
    prompt: str
    choices: List[str]
    answer: int  # one-based choice number
    explanation: str


@dataclass
class Lesson:
    title: str
    concept: str
    analogy: str
    example: str
    questions: List[Question]


LESSONS = [
    Lesson(
        title="Algorithms",
        concept=(
            "An algorithm is a clear sequence of steps used to complete a task "
            "or solve a problem. The steps should be understandable and in a "
            "useful order."
        ),
        analogy=(
            "Think about a recipe. You gather ingredients, follow steps in "
            "order, and get a result. A computer program also follows instructions."
        ),
        example=(
            "1. Ask for two numbers.\\n"
            "2. Add the numbers.\\n"
            "3. Display the total."
        ),
        questions=[
            Question(
                "Which option best describes an algorithm?",
                ["A computer screen", "A sequence of steps", "A type of keyboard"],
                2,
                "An algorithm is a sequence of steps for completing a task."
            ),
            Question(
                "Why does the order of steps matter?",
                ["Steps can depend on earlier steps",
                 "Computers ignore order",
                 "It makes the screen brighter"],
                1,
                "Some steps rely on information created earlier, so order can change the result."
            ),
        ],
    ),
    Lesson(
        title="Variables and data",
        concept=(
            "A variable is a name that refers to a value stored by a program. "
            "The value might be text, a number, or another kind of information."
        ),
        analogy=(
            "Imagine a labelled box. The label is the variable name and the "
            "item inside the box is the value."
        ),
        example=(
            "learner_name = 'Asha'\\n"
            "points = 10\\n"
            "points = 12  # the stored value changes"
        ),
        questions=[
            Question(
                "In points = 10, what is points?",
                ["The variable name", "The computer monitor", "A loop"],
                1,
                "points is the variable name; 10 is the value stored in it."
            ),
            Question(
                "What happens after points = 12?",
                ["The value becomes 12", "The program is deleted", "A loop starts"],
                1,
                "Assigning 12 changes the value associated with points."
            ),
        ],
    ),
    Lesson(
        title="Input and output",
        concept=(
            "Input is information given to a program. Output is the information "
            "or result the program provides."
        ),
        analogy=(
            "A ticket machine receives your destination as input and displays "
            "a ticket or instruction as output."
        ),
        example=(
            "name = input('What is your name? ')\\n"
            "print('Hello, ' + name)"
        ),
        questions=[
            Question(
                "A person types their name into a program. This is:",
                ["Output", "Input", "A syntax error"],
                2,
                "The name is supplied to the program, so it is input."
            ),
            Question(
                "The program displays 'Hello'. This is:",
                ["Input", "Output", "A variable name"],
                2,
                "The displayed message is information produced by the program."
            ),
        ],
    ),
    Lesson(
        title="Conditions",
        concept=(
            "A condition is a test that helps a program choose what to do. "
            "A common structure is IF followed by an optional ELSE."
        ),
        analogy=(
            "If it is raining, take an umbrella. Otherwise, leave the umbrella "
            "at home. The weather is the condition."
        ),
        example=(
            "temperature = 30\\n"
            "if temperature > 25:\\n"
            "    print('It is warm')\\n"
            "else:\\n"
            "    print('It is not warm')"
        ),
        questions=[
            Question(
                "What does IF help a program do?",
                ["Repeat forever", "Make a decision", "Store a file"],
                2,
                "IF checks a condition and chooses which instructions to run."
            ),
            Question(
                "If the condition is false and an ELSE branch exists, what happens?",
                ["The ELSE branch can run", "The computer turns off", "The variable disappears"],
                1,
                "ELSE provides an alternative path when the IF condition is false."
            ),
        ],
    ),
    Lesson(
        title="Loops and debugging",
        concept=(
            "A loop repeats instructions. Debugging is the process of finding, "
            "understanding, and correcting a problem in a program."
        ),
        analogy=(
            "A repeated classroom checklist is like a loop. If one item is "
            "missed, checking the steps carefully is part of debugging."
        ),
        example=(
            "for number in range(3):\\n"
            "    print('Practice makes progress!')\\n\\n"
            "# This repeats the message three times."
        ),
        questions=[
            Question(
                "What is the main purpose of a loop?",
                ["Repeat instructions", "Rename a computer", "Delete all variables"],
                1,
                "A loop runs a set of instructions repeatedly."
            ),
            Question(
                "What is a sensible first debugging step?",
                ["Guess and change many lines", "Reproduce the problem", "Ignore the error"],
                2,
                "Reproducing the problem helps you observe it and investigate its cause."
            ),
        ],
    ),
]


def show_line() -> None:
    print("-" * 64)


def pause() -> None:
    input("\\nPress Enter to continue...")


def show_lesson(lesson: Lesson) -> None:
    show_line()
    print(f"TOPIC: {lesson.title}")
    show_line()
    print("\\nWHAT IT MEANS")
    print(lesson.concept)
    print("\\nEVERYDAY CONNECTION")
    print(lesson.analogy)
    print("\\nSMALL EXAMPLE")
    print(lesson.example.replace("\\n", "\n"))
    pause()


def ask_question(question: Question) -> bool:
    print("\\n" + question.prompt)
    for index, choice in enumerate(question.choices, start=1):
        print(f"  {index}. {choice}")

    while True:
        raw = input("Choose an option number: ").strip()
        if raw.isdigit():
            selected = int(raw)
            if 1 <= selected <= len(question.choices):
                break
        print(f"Please enter a number from 1 to {len(question.choices)}.")

    correct = selected == question.answer
    if correct:
        print("\\nCorrect! " + question.explanation)
    else:
        correct_text = question.choices[question.answer - 1]
        print("\\nNot quite. The best answer is: " + correct_text)
        print(question.explanation)
    return correct


def run_quiz(lesson: Lesson) -> tuple[int, int]:
    print(f"\\nPRACTICE: {lesson.title}")
    score = 0
    total = len(lesson.questions)
    for question in lesson.questions:
        if ask_question(question):
            score += 1
    percentage = (score / total * 100) if total else 0
    print(f"\\nTopic result: {score}/{total} correct ({percentage:.0f}%).")
    if score == total:
        print("Excellent work. Try explaining the concept in your own words.")
    elif score == 0:
        print("Keep practising. Review the example and try again when ready.")
    else:
        print("Good effort. Review the explanations for the questions you missed.")
    return score, total


def choose_lesson() -> Optional[Lesson]:
    print("\\nCHOOSE A TOPIC")
    for index, lesson in enumerate(LESSONS, start=1):
        print(f"  {index}. {lesson.title}")
    print("  0. Return to main menu")
    while True:
        raw = input("Your choice: ").strip()
        if raw == "0":
            return None
        if raw.isdigit() and 1 <= int(raw) <= len(LESSONS):
            return LESSONS[int(raw) - 1]
        print(f"Enter 0 or a number from 1 to {len(LESSONS)}.")


def display_summary(results: dict[str, tuple[int, int]]) -> None:
    show_line()
    print("YOUR SESSION SUMMARY")
    show_line()
    if not results:
        print("No topics completed yet. Choose a topic to begin.")
        return

    total_correct = sum(score for score, _ in results.values())
    total_questions = sum(total for _, total in results.values())
    for title, (score, total) in results.items():
        print(f"- {title}: {score}/{total} correct")
    overall = total_correct / total_questions * 100 if total_questions else 0
    print(f"\\nOverall: {total_correct}/{total_questions} correct ({overall:.0f}%).")
    print("A score is a learning signal, not a measure of your ability.")
    print("Review any topic that felt difficult and explain it in your own words.")


def main() -> None:
    results: dict[str, tuple[int, int]] = {}
    print("=" * 64)
    print("WELCOME TO CODESTEPS")
    print("A friendly introduction to code literacy for beginners.")
    print("=" * 64)

    while True:
        print("\\nMAIN MENU")
        print("  1. Learn and practise a topic")
        print("  2. View session summary")
        print("  3. View learning tips")
        print("  0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            lesson = choose_lesson()
            if lesson is None:
                continue
            show_lesson(lesson)
            score, total = run_quiz(lesson)
            previous = results.get(lesson.title, (0, 0))
            results[lesson.title] = (previous[0] + score, previous[1] + total)
            pause()
        elif choice == "2":
            display_summary(results)
            pause()
        elif choice == "3":
            show_line()
            print("LEARNING TIPS")
            print("1. Read the explanation before studying the code.")
            print("2. Predict what an example will do before running it.")
            print("3. Change one small thing and observe the result.")
            print("4. When something fails, reproduce it and investigate calmly.")
            print("5. Explain the idea in your own words.")
            pause()
        elif choice == "0":
            display_summary(results)
            print("\\nThank you for learning with CodeSteps. Keep asking questions!")
            break
        else:
            print("Please choose 0, 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\\n\\nSession ended. Thank you for trying CodeSteps.")
