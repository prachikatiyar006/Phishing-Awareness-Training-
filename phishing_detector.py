# phishing_detector.py

"""
A basic script to demonstrate how one might detect potential phishing URLs
based on common suspicious patterns.
"""

def is_phishing_url(url):
    suspicious_keywords = ["login", "verify", "update", "secure", "account"]
    suspicious_extensions = [".zip", ".exe"]

    # Check for suspicious keywords
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            return True

    # Check for suspicious file extensions
    for ext in suspicious_extensions:
        if url.lower().endswith(ext):
            return True

    # Example of suspicious domain pattern
    if "-" in url.split("//")[-1].split("/")[0]:
        return True

    return False

# Example usage
if __name__ == "__main__":
    test_urls = [
        "http://example.com/login",
        "https://secure-update.info",
        "http://goodsite.com/profile",
        "http://malicious-site.com/download.zip"
    ]

    for url in test_urls:
        if is_phishing_url(url):
            print(f"[ALERT] Potential phishing URL detected: {url}")
        else:
            print(f"[SAFE] {url}")
