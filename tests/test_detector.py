"""Unit tests for HallucinationDetector."""
import unittest
from hallucination_detector.detector import HallucinationDetector

class TestHallucinationDetector(unittest.TestCase):
    def test_detection(self):
        detector = HallucinationDetector(threshold=0.4)
        ref = "The Apollo program landed the first humans on the Moon in 1969."
        good = "The Moon landing happened in 1969."
        bad = "The Apollo mission visited Pluto and Jupiter."

        r1 = detector.verify(good, ref)
        self.assertTrue(r1["is_grounded"])

        r2 = detector.verify(bad, ref)
        self.assertFalse(r2["is_grounded"])

if __name__ == "__main__":
    unittest.main()
