from project.team import Team
from unittest import TestCase, main


class TeamTests(TestCase):
    __TEAM_NAME = "TestName"
    __TEAM_NAME1 = "TestNameFirst"
    __MEMBERS = {
        "First": 5,
        "Second": 6,
    }
    __MEMBERS1 = {
        "Third": 7,
        "Fourth": 8,
        "Fifth": 9,
    }

    def setUp(self) -> None:
        self.team = Team(self.__TEAM_NAME)
        self.team1 = Team(self.__TEAM_NAME1)
        self.team.add_member(**self.__MEMBERS)
        self.team1.add_member(**self.__MEMBERS1)

    def test_structure_initialization(self):
        team = Team(self.__TEAM_NAME)
        self.assertEqual(self.__TEAM_NAME, self.team.name)
        self.assertDictEqual({}, team.members)
        with self.assertRaises(ValueError) as ex:
            Team("T3stNam3")
        expected = f"Team Name can contain only letters!"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_member(self):
        expected = f"Member with name Zero does not exist"
        result = self.team.remove_member("Zero")
        self.assertDictEqual(self.__MEMBERS, self.team.members)
        self.assertEqual(expected, result)

        expected = f"Member First removed"
        result = self.team.remove_member("First")
        self.assertDictEqual({"Second": 6}, self.team.members)
        self.assertEqual(expected, result)

    def test_greater_than_between_two_instances_of_team(self):
        expected = True
        result = self.team1 > self.team
        self.assertEqual(expected, result)

        expected = False
        result = self.team > self.team1
        self.assertEqual(expected, result)

    def test_len_method_on_team_instance(self):
        self.assertEqual(2, len(self.team))

    def test_adding_two_instances_of_team(self):
        expected = Team(f"{self.__TEAM_NAME}{self.__TEAM_NAME1}")
        expected.add_member(**self.__MEMBERS)
        expected.add_member(**self.__MEMBERS1)
        result = self.team + self.team1
        self.assertEqual(expected.name, result.name)
        self.assertDictEqual(expected.members, result.members)

    def test_team_string_representation(self):
        expected = [f"Team name: {self.team.name}"]
        members = list(sorted(self.team.members.items(), key=lambda x: (-x[1], x[0])))
        expected.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        expected = '\n'.join(expected)
        result = str(self.team)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
