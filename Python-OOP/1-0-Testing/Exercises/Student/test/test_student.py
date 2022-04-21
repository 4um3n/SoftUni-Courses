from project.student import Student
from unittest import TestCase, main


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student("student_name", {"course": ["note", "note1"]})

    def test_init_without_courses(self):
        student = Student("student_name")
        self.assertEqual("student_name", student.name)
        self.assertDictEqual({}, student.courses)

    def test_init_with_courses(self):
        self.assertEqual("student_name", self.student.name)
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)

    def test_enroll_course_already_in_courses(self):
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)
        result = self.student.enroll("course", ["note2"])
        self.assertDictEqual({"course": ["note", "note1", "note2"]}, self.student.courses)
        self.assertEqual(f"Course already added. Notes have been updated.", result)

    def test_enrol_add_course_notes(self):
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)
        result = self.student.enroll("new_course", ["note"], "Y")
        self.assertDictEqual({"course": ["note", "note1"], "new_course": ["note"]}, self.student.courses)
        self.assertEqual(f"Course and course notes have been added.", result)

        result = self.student.enroll("third_course", ["note"])
        self.assertDictEqual(
            {"course": ["note", "note1"], "new_course": ["note"], "third_course": ["note"]}, self.student.courses)
        self.assertEqual(f"Course and course notes have been added.", result)

    def test_enrol_dont_add_course_notes(self):
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)
        result = self.student.enroll("new_course", ["note"], "N")
        self.assertDictEqual({"course": ["note", "note1"], "new_course": []}, self.student.courses)
        self.assertEqual(f"Course has been added.", result)

    def test_add_notes_course_not_found_raises(self):
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("new_course", ["note", "note1"])

        self.assertEqual(f"Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_success(self):
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)
        self.student.add_notes("course", "note2")
        self.assertDictEqual({"course": ["note", "note1", "note2"]}, self.student.courses)

    def test_leave_course_not_found_course_raises(self):
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("new_course")

        self.assertEqual(f"Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_success(self):
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)
        result = self.student.leave_course("course")
        self.assertDictEqual({}, self.student.courses)
        self.assertEqual(f"Course has been removed", result)


if __name__ == '__main__':
    main()
