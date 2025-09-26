class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        columns = len(matrix[0])

        new_matrix = []
        for _ in range(columns):
            row = [0] * rows
            new_matrix.append(row)

        for i in range(rows):
            for j in range(columns):
                new_matrix[j][i] = matrix[i][j]
    
        return new_matrix