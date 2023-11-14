import unittest
from day9.day9 import Head, Tail, directions, distance_between_two_points

p1 = {"x": 0, "y": 0}
p2 = {"x": 0, "y": 1}
p3 = {"x": 4, "y": 0}
p4 = {"x": 1, "y": 1}
p5 = {"x": 0, "y": 2}

test_initial_coordinates_1 = [
    [
        {"x": 0, "y": 0}, {"x": -1, "y": 1}, "U",
    ],
    [
        {"x": 0, "y": 0}, {"x": 1, "y": 1}, "R"
    ],
    [
        {"x": 0, "y": 0}, {"x": 1, "y": -1}, "D"
    ],
    [
        {"x": 0, "y": 0}, {"x": -1, "y": -1}, "L"
    ],

]

test_initial_coordinates_2 = [
    [
        {"x": 0, "y": 0}, {"x": 0, "y": 1}, "L"
    ],
    [
        {"x": 0, "y": 0}, {"x": 1, "y": 1}, "D"
    ],
    [
        {"x": 0, "y": 0}, {"x": -1, "y": -1}, "U"
    ],
    [
        {"x": 0, "y": 0}, {"x": 1, "y": 0}, "D"
    ],

]
test_initial_coordinates_3 =[
    [
        {"x": 0, "y": 0}, {"x": 0, "y": 1}, "U"
    ],
    [
        {"x": 0, "y": 0}, {"x": 0, "y": -1}, "D"
    ],
    [
        {"x": 0, "y": 0}, {"x": -1, "y": 0}, "L"
    ],
    [
        {"x": 0, "y": 0}, {"x": 1, "y": 0}, "R"
    ],

]
class Test_Motion(unittest.TestCase):

    def test_head_and_tail_coordinates_greater_than_2(self):
    
        for coordinates in test_initial_coordinates_1:
            with self.subTest(coordinates = coordinates):
                tail_coordinates, head_coordinates, dir1 = coordinates
                head = Head(head_coordinates)
                tail = Tail(tail_coordinates)
                
                head.move_to(directions[dir1])
                tail.follow(head)

                self.assertEqual(tail._current_position, head._previous_position)                
                self.assertNotEqual(tail._current_position, tail._previous_position)
    def test_head_and_tail_coordinates_greater_smaller_than_2(self):
        for coordinates in test_initial_coordinates_2:
            with self.subTest(coordinates = coordinates):
                tail_coordinates, head_coordinates, dir1 = coordinates
                head = Head(head_coordinates)
                tail = Tail(tail_coordinates)
                
                head.move_to(directions[dir1])
                tail.follow(head)

                self.assertEqual(tail._current_position, tail._previous_position)                
        
    def test_head_and_tail_coordinates_greater_equal_to_2(self):
        for coordinates in test_initial_coordinates_3:
            with self.subTest(coordinates = coordinates):
                tail_coordinates, head_coordinates, dir1 = coordinates
                head = Head(head_coordinates)
                tail = Tail(tail_coordinates)
                
                head.move_to(directions[dir1])
                tail.follow(head)


if __name__ == '__main__':
    unittest.main()
