from django.db import models

class Result(models.Model):
    GRADE_CHOICES = [
        ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'),
        ('C+', 'C+'), ('C', 'C'), ('D', 'D'), ('F', 'F'),
    ]

    student_name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)

    def __str__(self):
        return self.student_name

    def get_grade_color(self):
        if self.marks >= 90:
            return 'grade-a-plus'
        elif self.marks >= 80:
            return 'grade-a'
        elif self.marks >= 70:
            return 'grade-b'
        elif self.marks >= 60:
            return 'grade-c'
        else:
            return 'grade-f'
