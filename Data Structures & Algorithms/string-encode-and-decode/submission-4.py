class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        while i < len(s):
            # Find the '#' separator
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # Extract the string of that length
            res.append(s[j + 1 : j + 1 + length])
            # Move to the next segment
            i = j + 1 + length
        return res
