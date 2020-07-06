from student_data_abstraction import Student


class Devops(Student):
    def __init__(self, first_name, last_name, stream): # This adds an attribute "stream" to the devops sub class.
        self.first_name = first_name
        self.last_name = last_name
        self.stream = stream

    def full_name(self):
        print(self.first_name, " ", self.last_name)

    def roll_call(self):
        print("I am a Devops Student")

    def test_question(self):
        print("Your test today will be on CI/CD!")



