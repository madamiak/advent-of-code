class Captcha(object):
    def solve(self, digits, step=1):
        result = 0
        for index, digit in enumerate(digits):
            if digit is digits[(index + step) % len(digits)]:
                result += int(digit)
        return result
