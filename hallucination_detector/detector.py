"""Atomic claim extractor and context grounding verifier."""
import re
from typing import List, Dict, Any, Tuple

class HallucinationDetector:
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold

    def _split_sentences(self, text: str) -> List[str]:
        return [s.strip() for s in re.split(r"[.!?]\s+", text) if s.strip()]

    def _tokenize(self, text: str) -> set:
        return set(re.findall(r"\b\w+\b", text.lower()))

    def verify(self, response_text: str, reference_text: str) -> Dict[str, Any]:
        ref_tokens = self._tokenize(reference_text)
        sentences = self._split_sentences(response_text)
        if not sentences or not ref_tokens:
            return {"grounded_ratio": 1.0, "flagged_sentences": [], "is_grounded": True}

        results = []
        grounded_count = 0
        for sent in sentences:
            sent_tokens = self._tokenize(sent)
            overlap = sent_tokens.intersection(ref_tokens)
            score = len(overlap) / len(sent_tokens) if sent_tokens else 1.0
            is_supported = score >= self.threshold
            if is_supported:
                grounded_count += 1
            results.append({
                "sentence": sent,
                "overlap_score": round(score, 3),
                "is_supported": is_supported
            })

        ratio = grounded_count / len(sentences)
        return {
            "grounded_ratio": round(ratio, 3),
            "is_grounded": ratio >= 0.7,
            "claims": results
        }
