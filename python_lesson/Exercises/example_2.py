from typing import Final


MidtermExam = float(input("Write your midter mexam: "))
FinalExam = float(input("Write your final exam: "))

result = (MidtermExam * 0.4) + (FinalExam * 0.6)

if result >= 60:
    print("Passed the exam")
else:
    print("Failed the exam")

