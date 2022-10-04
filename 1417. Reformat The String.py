class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        digits = ""
        letters = ""
        result = ""
        if len(s) == 1:
            return s
        for x in s:
            if x.isnumeric():
                digits += x
            else:
                letters += x
        if len(digits) == 0 or len(letters) == 0 or len(digits) - len(letters) < -1 or len(digits) - len(letters) > 1:
            return result
        if len(digits) > len(letters):
            for x in range(0, len(letters)):
                result += digits[x]
                result += letters[x]
            result += digits[len(digits)-1]
        elif len(letters) > len(digits):
            for x in range(0, len(digits)):
                result += letters[x]
                result += digits[x]
            result += letters[len(letters)-1]
        else:
            for x in range(0, len(letters)):
                result += letters[x]
                result += digits[x]
        return result
