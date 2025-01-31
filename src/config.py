"""
Config file. Change these if you want to change paths etc.
"""

# Define the directory where the Piper models are stored
MODEL_DIR = "/home/glick/Desktop/reader-app/piper_voices"
DATA_DIR = "/home/glick/Desktop/reader-app/piper_voices"
DOWNLOAD_DIR = "/home/glick/Desktop/reader-app/piper_voices"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

def get_cookies():
    """
    The function for getting cookies.
    This is in config.py because you may want to change both the domain and the browser as needed
    """
    return {cookie.name: cookie.value for cookie in browser_cookie3.firefox(domain_name="newyorker.com")}

