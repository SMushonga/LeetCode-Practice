class Solution(object):
    def romanToInt(self, s):
        current_value = 0
        last_value = 0
        numbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for letter in reversed(s):
            if last_value>numbers[letter]:
                current_value -= numbers[letter]
            else :
                current_value += numbers[letter]
            last_value = numbers[letter]
        return current_value
