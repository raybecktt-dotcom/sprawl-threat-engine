import re

class ThreatAnalyzer:
    @staticmethod
    def detect_sqli(payload: str) -> bool:
        """Detects common SQL injection patterns using Regular Expressions."""
        sqli_patterns = [
            r"(?i)\bOR\b\s+['\"]?\d+['\"]?\s*=\s*['\"]?\d+",
            r"(?i)\bDROP\b\s+\bTABLE\b",
            r"(?i)\bUNION\b\s+\bSELECT\b",
            r"--"
        ]
        for pattern in sqli_patterns:
            if re.search(pattern, payload):
                return True
        return False

    @staticmethod
    def sanitize_input(user_input: str) -> str:
        """Sanitizes user input for log printing."""
        return user_input.strip()
