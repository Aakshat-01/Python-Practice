#LeetCode Problem 904 Fruit Into Baskets

class Solution:
    def totalFruit(self, fruits):
        basket = set()
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            basket.add(fruits[right])

            while len(basket) > 2:
                # remove left fruit if it doesn't exist later in window
                if fruits[left] not in fruits[left+1:right+1]:
                    basket.remove(fruits[left])
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
