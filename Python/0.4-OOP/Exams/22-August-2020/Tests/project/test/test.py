from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.student_card = StudentReportCard("student_name", 12)

    def test_init_student_report_card(self):
        self.assertEqual("student_name", self.student_card.student_name)
        self.assertEqual(12, self.student_card.school_year)
        self.assertDictEqual({}, self.student_card.grades_by_subject)

    def test_student_name_cannot_be_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("", 12)
        self.assertEqual(f"Student Name cannot be an empty string!", str(ex.exception))

        self.student_card.student_name = "new_name"
        self.assertEqual("new_name", self.student_card.student_name)

    def test_school_year_not_in_range_1_to_12_raises(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("student", 0)
        self.assertEqual(f"School Year must be between 1 and 12!", str(ex.exception))

        self.student_card.school_year = 1
        self.assertEqual(1, self.student_card.school_year)

    def test_add_grade(self):
        self.assertDictEqual({}, self.student_card.grades_by_subject)
        result = self.student_card.add_grade("subject", 5)
        self.assertDictEqual({"subject": [5]}, self.student_card.grades_by_subject)
        self.assertIsNone(result)

        self.student_card.grades_by_subject = {"subject": [5]}
        self.student_card.add_grade("subject", 6)
        expected = {"subject": [5, 6]}
        self.assertDictEqual(expected, self.student_card.grades_by_subject)

        self.student_card.add_grade("subject1", 5)
        expected = {"subject": [5, 6], "subject1": [5]}
        self.assertDictEqual(expected, self.student_card.grades_by_subject)

    def test_report_for_average_grade_by_subject(self):
        self.assertDictEqual({}, self.student_card.grades_by_subject)
        result = self.student_card.average_grade_by_subject()
        self.assertEqual("", result)

        self.student_card.grades_by_subject = {"subject": [5, 6], "subject1": [6, 6]}
        expected = f"subject: 5.50\n" \
                   f"subject1: 6.00"
        result = self.student_card.average_grade_by_subject()
        self.assertEqual(expected, result)

    def test_report_average_grade_for_all_subjects(self):
        self.student_card.grades_by_subject = {"subject": [5, 5], "subject1": [6, 6]}
        expected = f"Average Grade: 5.50"
        result = self.student_card.average_grade_for_all_subjects()
        self.assertEqual(expected, result)

    def test_student_card_represent(self):
        self.student_card.grades_by_subject = {"subject": [5, 5], "subject1": [6, 6]}
        expected = f"Name: student_name\n" \
                   f"Year: 12\n" \
                   f"----------\n" \
                   f"subject: 5.00\n" \
                   f"subject1: 6.00\n" \
                   f"----------\n" \
                   f"Average Grade: 5.50"
        result = repr(self.student_card)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
