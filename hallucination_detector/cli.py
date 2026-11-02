"""Command line interface for hallucination-detector."""
from .detector import HallucinationDetector

def main():
    detector = HallucinationDetector()
    ref = "Antigravity was released in 2026 as an agentic AI coding companion."
    gen = "Antigravity was released in 2026. It flies on Mars."
    res = detector.verify(gen, ref)
    print("Hallucination check complete. Grounded ratio:", res["grounded_ratio"])

if __name__ == "__main__":
    main()
