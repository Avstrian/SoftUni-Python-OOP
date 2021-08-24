import unittest
from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.student = Student("Test")

    def test_initialization(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_initialization_with_courses_appended(self):
        expected_courses = {"Test_key": "Test_value"}
        self.student.courses["Test_key"] = "Test_value"
        self.assertEqual("Test", self.student.name)
        self.assertEqual(expected_courses, self.student.courses)

    def test_successfull_enroll_working_properly(self):
        expected_courses = {"Test_course": "Test_note"}
        res = self.student.enroll("Test_course", "Test_note")
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual("Course and course notes have been added.", res)

    def test_successfull_enroll_working_properly_with_Y(self):
        expected_courses = {"Test_course": "Test_note"}
        res = self.student.enroll("Test_course", "Test_note", "Y")
        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual("Course and course notes have been added.", res)

    def test_enroll_with_existing_key(self):
        self.student.courses = {"Python": ["Test_note"]}
        res = self.student.enroll("Python", ["Test_note2"])
        self.assertEqual(["Test_note", "Test_note2"], self.student.courses["Python"])
        self.assertEqual(res, "Course already added. Notes have been updated.")

    def test_enroll_with_existing_key_with_adding_notes(self):
        self.student.enroll("Python", ["note0", "note1"], "Y")
        res = self.student.enroll("Python", ["note3"], "Y")
        self.assertEqual(res, "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses["Python"], ["note0", "note1", "note3"])

    def test_enroll_without_adding_notes(self):
        res = self.student.enroll("Python", "note1", "no")
        self.assertEqual(res, "Course has been added.")
        self.assertEqual(self.student.courses["Python"], [])

    def test_adding_notes_working(self):
        student = Student("Ivancho", {"Python": []})
        res = student.add_notes("Python", "note1")
        self.assertEqual(["note1"], student.courses["Python"])
        self.assertEqual(res, "Notes have been updated")

    def test_adding_notes_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Python", "note1")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leaving_course_working(self):
        self.student.courses["Python"] = []
        res = self.student.leave_course("Python")
        self.assertEqual({}, self.student.courses)
        self.assertEqual(res, "Course has been removed")

    def test_leaving_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Python")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()