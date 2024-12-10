import unittest
from main import linkedlist

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = linkedlist()

    def test_add_package(self):
        self.linked_list.add_package(10, 5, 15, "Hanoi", 200)
        self.linked_list.add_package(20, 10, 20, "Da Nang", 500)
        result = self.linked_list.to_list()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['id'], 1)
        self.assertEqual(result[1]['id'], 2)

    def test_add_package_invalid_inputs(self):
        with self.assertRaises(ValueError):
            self.linked_list.add_package(-10, 5, 15, "Hanoi", 200)  
        with self.assertRaises(ValueError):
            self.linked_list.add_package(10, -5, 15, "Hanoi", 200)  
        with self.assertRaises(ValueError):
            self.linked_list.add_package(10, 5, -15, "Hanoi", 200)  
        with self.assertRaises(ValueError):
            self.linked_list.add_package(10, 5, 15, "Hanoi", -200)  
        with self.assertRaises(TypeError):
            self.linked_list.add_package(10, 5, 15, 123, 200)  

    def test_sort_packages(self):
        self.linked_list.add_package(10, 5, 15, "Hanoi", 200)
        self.linked_list.add_package(20, 10, 20, "Da Nang", 500)
        self.linked_list.add_package(15, 8, 40, "HCMC", 300)
        self.linked_list.add_package(5, 3, 60, "Nha Trang", 1000)
        self.linked_list.add_package(25, 15, 70, "Hai Phong", 700)
        self.linked_list.sort()

        sorted_list = self.linked_list.to_list()
        self.assertEqual(sorted_list[0]['destination'], "Hanoi")
        self.assertEqual(sorted_list[1]['destination'], "HCMC")
        self.assertEqual(sorted_list[2]['destination'], "Da Nang")
        self.assertEqual(sorted_list[3]['destination'], "Hai Phong")
        self.assertEqual(sorted_list[4]['destination'], "Nha Trang")

    def test_duplicate_destinations(self):
        self.linked_list.add_package(10, 5, 15, "Hanoi", 200)
        self.linked_list.add_package(15, 8, 40, "Hanoi", 300)
        self.linked_list.add_package(5, 3, 60, "Hanoi", 100)

        self.linked_list.sort()
        sorted_list = self.linked_list.to_list()
        self.assertEqual(sorted_list[0]['distance'], 100)  
        self.assertEqual(sorted_list[1]['distance'], 200)
        self.assertEqual(sorted_list[2]['distance'], 300)

    def test_empty_list(self):
        self.linked_list.sort()
        sorted_list = self.linked_list.to_list()
        self.assertEqual(len(sorted_list), 0)

    def test_display_empty_list(self):
        self.linked_list.display()  

    def test_display(self):
        self.linked_list.add_package(10, 5, 15, "Hanoi", 200)
        self.linked_list.add_package(20, 10, 20, "Da Nang", 500)
        self.linked_list.add_package(15, 8, 40, "HCMC", 300)
        self.linked_list.sort()

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.linked_list.display()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Hanoi", output)
        self.assertIn("HCMC", output)
        self.assertIn("Da Nang", output)

if __name__ == "__main__":
    unittest.main()
