class Group:
    def __init__(self, id, name, sem, count_students):
        self.id = id
        self.name = name
        self.sem = sem
        self.count_students = count_students


class Course:
    def __init__(self, id, id_group, title):
        self.id = id
        self.title = title
        self.id_group = id_group


class Group_Course:
    def __init__(self, id_group, id_course):
        self.id_group = id_group
        self.id_course = id_course


courses = [
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

groups = [
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

groups_courses = [
    Group_Course(1, 1),
    Group_Course(1, 2),
    Group_Course(1, 4),
    Group_Course(2, 1),
    Group_Course(3, 2),
    Group_Course(4, 4),
    Group_Course(5, 5),
    Group_Course(9, 3)
]


def main():
    print("Запрос № 1")
    data = [(c, g) for c in courses for g in groups if c.id_group == g.id and c.title.startswith("Курс")]
    for (c, g) in data:
        print(c.title, g.name, g.count_students)
    print()
    print("Запрос № 2")
    data = [(c, g) for c in courses for g in groups if c.id_group == g.id]
    sorted_data = sorted(data, key=lambda x: x[1].count_students, reverse=True)
    for (c, g) in sorted_data:
        print(c.title, g.id, g.name, g.count_students)
    print()
    print("Запрос № 3")
    letter = 'Р'
    filtered_data = [(g, c, gc) for gc in groups_courses for g in groups for c in courses if
                     gc.id_group == g.id and gc.id_course == c.id and letter in g.name]

    filtered_data.sort(key=lambda x: x[0].name)
    for (g, c, _) in filtered_data:
        print(g.name, c.title)


if __name__ == "__main__":
    main()
