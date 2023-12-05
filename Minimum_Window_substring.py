"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length_of_s = len(s)
        min_length = length_of_s + 1
        min_length_substring = ''
        need_hash_map = Counter(t)
        have_hash_map = {key: 0 for key in list(set(t))}
        need = len(t)
        have = 0
        right = 0
        sub_str = ''
        while right < length_of_s:
            if have < need:
                sub_str += s[right]
                if s[right] in need_hash_map.keys():
                    have_hash_map[s[right]] += 1
                    if have_hash_map[s[right]] <= need_hash_map[s[right]]:
                        have += 1
                right += 1

            while have == need:
                if min_length > len(sub_str):
                    min_length_substring = sub_str
                    min_length = len(sub_str)
                if sub_str[0] in need_hash_map.keys():
                    have_hash_map[sub_str[0]] -= 1
                    if have_hash_map[sub_str[0]] < need_hash_map[sub_str[0]]:
                        have -= 1
                sub_str = sub_str[1: ]
        return min_length_substring
