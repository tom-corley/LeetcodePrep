class Solution:
    # TC: O(n) since l, r loop through 1 to n forwards
    # SC: O(n) since set cointains in WC n elements
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()
        l, r = 0, 0
        ans = 0

        # Sliding window pattern
        while r < len(s):
            # If the character is not already in our window
            # we may extend right by 1, and possibly update answer
            if s[r] not in used:
                used.add(s[r])
                r += 1
                ans = max(ans, (r-l))
            # Otherwise, we must shrink the window in from the left
            # until the duplicate character is removed, and start again
            else:
                used.remove(s[l])
                l += 1
        return ans