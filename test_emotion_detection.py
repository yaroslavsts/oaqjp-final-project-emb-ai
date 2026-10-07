"""Integration tests for the five required Watson emotion classifications."""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Check the dominant emotion for each required example."""

    def test_joy(self):
        """Recognize joy."""
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

    def test_anger(self):
        """Recognize anger."""
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")

    def test_disgust(self):
        """Recognize disgust."""
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Recognize sadness."""
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")

    def test_fear(self):
        """Recognize fear."""
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
