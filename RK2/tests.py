import unittest
from unittest.mock import patch
from main import get_courses_by_group, get_sorted_courses_by_group, get_filtered_data, Group, Course, GroupCourse


class TestProgram(unittest.TestCase):
    def setUp(self):
        self.groups = [
            Group(1, "ИУ5", 2, 23),
            Group(2, "ИУ5", 1, 22),
            Group(3, "ИУ5", 1, 21),
            Group(4, "ИУ5", 3, 25),
            Group(5, "ИУ5", 4, 21),
            Group(6, "ФН3", 3, 24),
            Group(7, "СГН3", 5, 24),
            Group(8, "ИБМ5", 7, 21),
            Group(9, "РК6", 9, 26)
        ]

        self.courses = [
            Course(1, 1, "Курс 1"),
            Course(1, 2, "Курс 1"),
            Course(1, 3, "Курс 1"),
            Course(2, 4, "Курс 2"),
            Course(2, 5, "Курс 2"),
            Course(2, 6, "Курс 2"),
            Course(3, 7, "Курс 3"),
            Course(4, 8, "Курс 4"),
            Course(5, 9, "Курс 5")
        ]

        self.groups_courses = [
            GroupCourse(1, 1),
            GroupCourse(1, 2),
            GroupCourse(1, 4),
            GroupCourse(2, 1),
            GroupCourse(3, 2),
            GroupCourse(4, 4),
            GroupCourse(5, 5),
            GroupCourse(9, 3)
        ]

    def test_get_courses_by_group(self):
        result = get_courses_by_group(self.groups, self.courses, "ИУ5")
        self.assertEqual(result, [
            (self.courses[0], self.groups[0]),
            (self.courses[1], self.groups[1]),
            (self.courses[2], self.groups[2]),
            (self.courses[3], self.groups[3]),
            (self.courses[4], self.groups[4])
        ])

    def test_get_sorted_courses_by_group(self):
        result = get_sorted_courses_by_group(self.groups, self.courses)
        self.assertEqual(result, [
            (self.courses[3], self.groups[4]),
            (self.courses[4], self.groups[3]),
            (self.courses[5], self.groups[0]),
            (self.courses[6], self.groups[5]),
            (self.courses[7], self.groups[6]),
            (self.courses[8], self.groups[8]),
            (self.courses[0], self.groups[1]),
            (self.courses[1], self.groups[2]),
            (self.courses[2], self.groups[7])
        ])

    def test_get_filtered_data(self):
        result = get_filtered_data(self.groups, self.courses, self.groups_courses, 'Р')
        self.assertEqual(result, [
            (self.groups[8], self.courses[6], self.groups_courses[7])
        ])


if __name__ == '__main__':
    unittest.main()
