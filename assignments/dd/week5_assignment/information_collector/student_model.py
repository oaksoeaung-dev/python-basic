class StudentProfile:
    def __init__(self):
        self.name = ""
        self.birthday = ""
        self.uni = ""
        self.enroll_date = ""
        self.major = ""
        self.scores = {}
        self.subjects = [
            ("English", "eng"), 
            ("Mathematics", "math"), 
            ("Operating System", "ops"), 
            ("Control System", "cns"), 
            ("Advanced Control Network", "acn"), 
            ("Computer Architecture", "cao"), 
            ("ADMT", "admt")
        ]