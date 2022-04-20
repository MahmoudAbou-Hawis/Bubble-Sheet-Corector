class Degree:
    def __init__(self, Student_Answer, Correct_Answer):
        self.Student_Answer = Student_Answer
        self.Correct_Answer = Correct_Answer

    def get_degree(self):
        counter = 0
        for i in range(len(self.Student_Answer)):
            I_part_Student = self.Student_Answer[i]
            I_part_Correct = self.Correct_Answer[i]
            #print(I_part_Correct,I_part_Student)
            for r in range(len(I_part_Student)):
                if I_part_Correct[r] == I_part_Student[r]:
                    counter += 1
        return counter
