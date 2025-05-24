class Dictionary:
    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):

        #1. Helper function to calculate the edit distance (number of changes needed) between two words.
        def edit_distance(word1, word2):
            m = len(word1)
            n = len(word2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]

            # Initialize the first row and column of the DP table
            for i in range(m + 1):
                dp[i][0] = i
            for j in range(n + 1):
                dp[0][j] = j

            # Fill the DP table using dynamic programming
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            return dp[m][n]


        # 2. Find the word with the minimum edit distance:
        min_distance = float('inf')  # Initialize with infinity
        most_similar_word = ""

        for word in self.words:
            distance = edit_distance(term, word)
            if distance < min_distance:
                min_distance = distance
                most_similar_word = word

        # 3. Return the most similar word.
        return most_similar_word