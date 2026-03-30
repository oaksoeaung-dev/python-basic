from student_logic import StudentManager

if __name__ == "__main__":
    collector = StudentManager()
    collector.collect_all_data()
    collector.display_report()