# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    def __init__(self):
        self.count = 0
        self.d = dict()
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.count += 1
        self.d[self.count] = longUrl
        return str(self.count)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[int(shortUrl)]
        

"""
Runtime: 32 ms, faster than 60.00% of Python3 online submissions for Encode and Decode TinyURL.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Encode and Decode TinyURL.
"""