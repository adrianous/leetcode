class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a = int(num1.split('+')[0])
        b = int(num1.split('+')[1][:-1])
        c = int(num2.split('+')[0])
        d = int(num2.split('+')[1][:-1])
        return str(a*c - b*d) + '+' + str(a*d + b*c) + 'i'


if __name__ == '__main__':
    num1 = "1+-1i"
    num2 = "1+-1i"
    print(Solution().complexNumberMultiply(num1,num2))