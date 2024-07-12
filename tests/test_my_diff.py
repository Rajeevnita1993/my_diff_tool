import unittest
import sys
import os
from my_diff_tool.my_diff import lcs, lcs_lines_function, generate_diff

# Add the directory containing my_diff.py to the Python path
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../my_diff_tool')))

#from my_diff import lcs

class TestLCS(unittest.TestCase):

    def test_lcs(self):
        self.assertEqual(lcs("ABCDEF", "ABCDEF"), "ABCDEF")
        self.assertEqual(lcs("ABC", "XYZ"), "")
        self.assertEqual(lcs("AABCXY", "XYZ"), "XY")
        self.assertEqual(lcs("", ""), "")
        self.assertEqual(lcs("ABCD", "AC"), "AC")
        self.assertEqual(lcs("XMJYAUZ", "MZJAWXU"), "MJAU")
        self.assertEqual(lcs("ABAZDC", "BACBAD"), "ABAD")



class TestGenerateDiff(unittest.TestCase):
    
    def test_generate_diff(self):
        lines1 = [
            "Coding Challenges helps you become a better software engineer through that build real applications.",
            "I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
            "I’ve used or am using these coding challenges as exercise to learn a new programming language or technology.",
            "Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."
        ]
        lines2 = [
            "Helping you become a better software engineer through coding challenges that build real applications.",
            "I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
            "These are challenges that I’ve used or am using as exercises to learn a new programming language or technology.",
            "Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."
        ]
        expected_diff = [
            "< Coding Challenges helps you become a better software engineer through that build real applications.",
            "> Helping you become a better software engineer through coding challenges that build real applications.",
            "  I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
            "< I’ve used or am using these coding challenges as exercise to learn a new programming language or technology.",
            "> These are challenges that I’ve used or am using as exercises to learn a new programming language or technology.",
            "  Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."
        ]
        self.assertEqual(generate_diff(lines1, lines2), expected_diff)

        # Additional test cases
        self.assertEqual(
            generate_diff(
                ["a", "b", "c", "d"],
                ["a", "x", "c", "d"]
            ),
            ["  a", "< b", "> x", "  c", "  d"]
        )
        
        self.assertEqual(
            generate_diff(
                ["a", "b", "c"],
                ["x", "y", "z"]
            ),
            ["< a", "< b", "< c", "> x", "> y", "> z"]
        )


if __name__ == "__main__":
    unittest.main()