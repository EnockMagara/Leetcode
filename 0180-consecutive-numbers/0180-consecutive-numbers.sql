/* Write your T-SQL query statement below */
SELECT DISTINCT L1.num AS ConsecutiveNums
FROM Logs L1
JOIN Logs L2 ON L2.id = L1.id + 1 AND L2.num = L1.num
JOIN Logs L3 ON L3.id = L2.id + 1 AND L3.num = L2.num;