import os
from datetime import datetime
from student_model import StudentProfile

class StudentManager:
    def __init__(self):
        self.student = StudentProfile()

    def ask_input(self, prompt, error_msg="Input cannot be empty!"):
        while True:
            value = input(prompt).strip()
            if value == "":
                print(error_msg)
            else:
                return value

    def ask_score(self, subject_name):
        while True:
            score_str = input(f"What is your {subject_name} Score? ")
            if score_str == "":
                print("Score cannot be empty!")
                continue
            try:
                score = int(score_str)
                if 0 <= score <= 100:
                    return score
                else:
                    print("Score must be between 0 and 100!")
            except ValueError:
                print("Score must be a valid integer!")

    def collect_all_data(self):
        s = self.student
        s.name = self.ask_input("What is your name? ")
        s.birthday = self.ask_input("What's your birthday? [dd/MM/yyyy] ")
        s.uni = self.ask_input("Which university are you studying in right now? ")
        s.enroll_date = self.ask_input("When did you join your university? [dd/MM/yyyy] ")
        s.major = self.ask_input("What is your major? ")

        print("\n--- Please enter your scores ---")
        for full_name, short_name in s.subjects:
            s.scores[short_name] = self.ask_score(full_name)

    def calculate_stats(self):
        s = self.student
        bd_date = datetime.strptime(s.birthday, "%d/%m/%Y")
        age = datetime.now().year - bd_date.year
        
        en_date = datetime.strptime(s.enroll_date, "%d/%m/%Y")
        study_year = datetime.now().year - en_date.year
        
        total_score = sum(s.scores.values())
        average = total_score / len(s.subjects)
        gpa = average / 25
        
        return age, study_year, average, gpa

    def display_report(self):
        age, study_year, average, gpa = self.calculate_stats()
        s = self.student
        
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "Personal Information Collector".upper())
        print("-" * 35)
        
        print(f"Name          : {s.name}")
        print(f"Birthday      : {s.birthday} ({age} years old)")
        print(f"University    : {s.uni}")
        print(f"Entry Date    : {s.enroll_date} ({study_year}th year)")
        print(f"Major         : {s.major}")
        print("-" * 35)
        
        for full_name, short_name in s.subjects:
            print(f"{full_name.ljust(25)}: {s.scores[short_name]}")
            
        print("-" * 35)
        print(f"Average Score : {average:.2f}")
        print(f"GPA           : {gpa:.2f}")
        print("\n" + "end".upper())