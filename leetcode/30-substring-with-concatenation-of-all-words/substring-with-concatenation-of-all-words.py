class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = Counter(words)
        result_indices = []

        # Iterate over each possible starting point within the first word_length characters
        for i in range(word_length):
            left = i
            right = i
            seen_words = defaultdict(int)
            count = 0
            
            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length

                if word in word_count:
                    seen_words[word] += 1
                    count += 1
                    
                    while seen_words[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        seen_words[left_word] -= 1
                        count -= 1
                        left += word_length

                    if count == num_words:
                        result_indices.append(left)
                else:
                    seen_words.clear()
                    count = 0
                    left = right

        return result_indices