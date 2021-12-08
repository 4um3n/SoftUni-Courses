from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.report_card = StudentReportCard("Name", 12)

    def test_initialization(self):
        self.assertEqual(f"Name", self.report_card.student_name)
        self.assertEqual(12, self.report_card.school_year)
        self.assertDictEqual({}, self.report_card.grades_by_subject)

    def test_student_name_cannot_be_an_empty_string_raises(self):
        expected = f"Student Name cannot be an empty string!"
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("", 12)
        self.assertEqual(expected, str(ex.exception))

    def test_school_year_must_be_between_1_and_12_raises(self):
        expected = f"School Year must be between 1 and 12!"
        with self.assertRaises(ValueError) as ex:
            self.report_card.school_year = 0
        self.assertEqual(expected, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.report_card.school_year = 13
        self.assertEqual(expected, str(ex.exception))

        self.report_card.school_year = 1
        self.assertEqual(1, self.report_card.school_year)

    def test_add_grade(self):
        self.assertDictEqual({}, self.report_card.grades_by_subject)
        expected = {"Test": [6]}
        self.report_card.add_grade("Test", 6)
        self.assertDictEqual(expected, self.report_card.grades_by_subject)
        expected = {"Test": [6, 5]}
        self.report_card.add_grade("Test", 5)
        self.assertDictEqual(expected, self.report_card.grades_by_subject)

    def test_average_grade_by_subject_report(self):
        self.assertDictEqual({}, self.report_card.grades_by_subject)
        self.report_card.add_grade("Test", 6)
        self.report_card.add_grade("Test", 5)
        expected = f"Test: 5.50"
        result = self.report_card.average_grade_by_subject()
        self.assertEqual(expected, result)

    def test_average_grade_for_all_subjects_report(self):
        self.report_card.add_grade("Test", 6)
        self.report_card.add_grade("Test1", 5)
        expected = f"Average Grade: 5.50"
        result = self.report_card.average_grade_for_all_subjects()
        self.assertEqual(expected, result)

    def test_report_card_representation(self):
        self.report_card.add_grade("Test", 6)
        self.report_card.add_grade("Test", 6)
        self.report_card.add_grade("Test1", 4)
        self.report_card.add_grade("Test1", 4)
        expected = f"Name: {self.report_card.student_name}\n" \
                 f"Year: {self.report_card.school_year}\n" \
                 f"----------\n" \
                 f"{self.report_card.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.report_card.average_grade_for_all_subjects()}"
        result = repr(self.report_card)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
