from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        sorted_deck = sorted(deck)  # Sort in ascending order
        
        result = [0] * n
        queue = deque(range(n))  # Queue of indices 0 to n-1
        
        for number in sorted_deck:
            # Place the number at the front index
            result[queue[0]] = number
            queue.popleft()
            if queue:
                # Move the next index to the end
                queue.append(queue.popleft())
        
        return result