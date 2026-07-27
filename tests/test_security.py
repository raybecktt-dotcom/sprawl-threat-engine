import pytest
from src.security import ThreatAnalyzer

def test_sqli_detection():
    analyzer = ThreatAnalyzer()
    
    # Valid malicious payloads
    assert analyzer.detect_sqli("admin' OR '1'='1") == True
    assert analyzer.detect_sqli("SELECT * FROM users; DROP TABLE players; --") == True
    
    # Normal inputs
    assert analyzer.detect_sqli("NormalUser") == False
    assert analyzer.detect_sqli("I want to buy 5 health potions") == False

def test_input_sanitization():
    analyzer = ThreatAnalyzer()
    raw = "   decking_access_token \n "
    assert analyzer.sanitize_input(raw) == "decking_access_token"
