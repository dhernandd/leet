# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# My solution
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        if len(s) == len(set(s)): return len(s)
        
        l = {} # maps a char to the last idx in s at which it appeared
        max_len = j = 0
        for i, ch in enumerate(s):
            if ch in l:
                # j stores the unique idx such that s[i:j] contains no repeated
                # character. Update j if the current character has already been
                # seen AND if the index of its previous occurrence is bigger
                # than the current j
                j = max(j, l[ch] + 1)  
            l[ch] = i # update l
            max_len = max(max_len, i - j + 1)
        return max_len
            
# ALTERNATIVES
class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        seen = []
        for i in s:
            if i in seen:
                m = max(m, len(seen))
                seen = seen[seen.index(i)+1:len(seen)]
            seen.append(i)
        return max(len(seen),m)
      
class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == len(set(s)):
            return len(s)
        
        last_pos = dict() # track last encountered position of each letter
        lengths_seen = list() # keep track of substring lengths
        start_pos = 0
        for pos, x in enumerate(s):
            if x in last_pos:
                # We've seen this letter before. Reset the starting
                # position to either the position after the previous
                # one for this letter, or else the current starting
                # position, whichever is later in the string.
                start_pos = max(start_pos, last_pos[x] + 1)
            lengths_seen.append(pos - start_pos + 1)
            # Update the last seen position
            last_pos[x] = pos
        # At this point we have walked through the entire string.
        # Return the longest length we encountered.
        return max(lengths_seen)