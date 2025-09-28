import json
import time
from datetime import datetime


class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer.upper()


def load_questions_from_json(filename):
    """Load questions from a JSON file."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            questions = []
            for q in data:
                questions.append(Question(q['prompt'], q['options'], q['answer']))
            return questions
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print("❌ Error decoding JSON.")
        exit(1)


def ask_question(question, index, total, time_limit=20):
    """Ask a single question with a time limit."""
    print(f"\nQ{index}/{total}: {question.prompt}")
    for i, opt in zip(['A', 'B', 'C', 'D'], question.options):
        print(f"  {i}. {opt}")

    start = time.time()
    user_answer = input(f"⏳ Answer (A/B/C/D) [You have {time_limit} sec]: ").strip().upper()
    end = time.time()

    elapsed = end - start
    if elapsed > time_limit:
        print(f"⏰ Time's up! You took {int(elapsed)} seconds.")
        return False
    elif user_answer == question.answer:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! Correct answer: {question.answer}")
        return False


def run_quiz(questions, time_limit=20):
    """Run the quiz."""
    print("\n🎉 Welcome to the Advanced Python Quiz! 🎉")
    print("You will have", time_limit, "seconds per question.\n")

    score = 0
    total = len(questions)

    for idx, question in enumerate(questions, 1):
        if ask_question(question, idx, total, time_limit):
            score += 1

    percentage = (score / total) * 100
    print("\n📊 Quiz Completed!")
    print(f"✅ Correct Answers: {score}/{total}")
    print(f"📈 Score Percentage: {percentage:.2f}%")

    if percentage == 100:
        print("🏆 Outstanding! Perfect score!")
    elif percentage >= 75:
        print("🎉 Great job!")
    elif percentage >= 50:
        print("👍 Good effort. Keep practicing.")
    else:
        print("📚 Don't give up! Try again.")

    log_results(score, total, percentage)


def log_results(score, total, percentage):
    """Log quiz result to a file."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_line = f"[{now}] Score: {score}/{total} ({percentage:.2f}%)\n"

    with open("results.log", "a") as log_file:
        log_file.write(result_line)


if __name__ == "__main__":
    questions = load_questions_from_json("questions.json")
    run_quiz(questions, time_limit=20)
