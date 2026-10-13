
            # If character is seen and is within the current window, move the left pointer
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            # Update the character's latest index
            char_index_map[char] = right

            # Calculate the maximum length of the substring without repeating characters
            max_length = max(max_length, right - left + 1)

        return max_length


# Example usage:
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3 ("abc")
print(sol.lengthOfLongestSubstring("bbbbb"))  # Output: 1 ("b")
print(sol.lengthOfLongestSubstring("pwwkew"))  # Output: 3 ("wke")
