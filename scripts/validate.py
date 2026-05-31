#!/usr/bin/env python3
"""Validate legal citation format and extract components."""
import json, sys, re

def validate_citation(data):
    citation = data.get("citation", "")
    # Common patterns: "123 U.S. 456 (1890)", "[2020] UKSC 5", "Case C-123/19"
    patterns = [
        (r"(\d+)\s+([A-Z][A-Za-z.]+(?:\s+[A-Za-z.]+)*)\s+(\d+)\s*\((\d{4})\)", "us_reporter"),
        (r"\[(\d{4})\]\s+([A-Z]+)\s+(\d+)", "uk_neutral"),
        (r"Case\s+([CT])-(\d+)/(\d{2,4})", "eu_case"),
    ]
    for pattern, fmt in patterns:
        m = re.match(pattern, citation)
        if m:
            return {"valid": True, "format": fmt, "citation": citation, "components": m.groups()}

    return {
        "valid": False,
        "citation": citation,
        "suggestion": "Expected format: '123 U.S. 456 (1890)' or '[2020] UKSC 5' or 'Case C-123/19'"
    }

if __name__ == "__main__":
    print(json.dumps(validate_citation(json.loads(sys.argv[1])), indent=2))
