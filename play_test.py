"""
Test for Rock Paper Scissors
"""
import unittest
from play import play

class RockPaperScissorsTest(unittest.TestCase):
    """
    Tests
    """
    def test_it_works(self):
        """
        Test it works
        """

    def test_rock_beats_scissors(self):
        """
        When rock and scissors are played
        Then rock wins
        """
        # Arrange
        play1 = "r"
        play2 = "s"

        # Act
        winner = play(play1, play2)

        # Assert
        assert winner == "r"
    
    def test_rock_beats_scissors_if_reversed(self):
        """
        When scissors and rock are played
        Then rock wins
        """
        # Arrange
        play1 = "s"
        play2 = "r"

        # Act
        winner = play(play1, play2)

        # Assert
        assert winner == "r"
    
    def test_scissors_beats_paper(self):
        """
        When scissors and paper are played
        Then scissors wins
        """
        # Arrange
        play1 = "s"
        play2 = "p"

        # Act
        winner = play(play1, play2)

        # Assert
        assert winner == "s"
    
    def test_scissors_beats_paper_reversed(self):
        """
        When paper and scissors are played
        Then scissors wins
        """
        # Arrange
        play1 = "p"
        play2 = "s"

        # Act
        winner = play(play1, play2)

        # Assert
        assert winner == "s"
    
    def test_paper_beats_rock(self):
        """
        When paper and rock are played
        Then paper wins
        """
        # Arrange
        play1 = "p"
        play2 = "r"

        # Act
        winner = play(play1, play2)

        # Assert
        assert winner == "p"

    def test_paper_beats_rock_reversed(self):
        """
        When rock and paper are played
        Then paper wins
        """
        # Arrange
        play1 = "r"
        play2 = "p"

        # Act
        winner = play(play1, play2)

        # Assert
        assert winner == "p"