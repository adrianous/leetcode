class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        ret = ''
        index = 0
        one_place = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        two_place = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                     'Nineteen']
        two_place_m = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        more_place = ['Thousand', 'Million', 'Billion']
        while num != 0:
            index += 1
            r = num % 10
            num //= 10
            if index % 3 == 1:
                if index // 3 != 0:
                    if r != 0 or num % 100 != 0:
                        ret = more_place[index // 3 - 1] + ' ' + ret

                if num % 10 == 1:
                    ret = two_place[r] + ' ' + ret
                    num //= 10
                    index += 1
                    continue

                elif r != 0:
                    ret = one_place[r - 1] + ' ' + ret

            elif index % 3 == 2:
                if r != 0:
                    ret = two_place_m[r - 2] + ' ' + ret

            elif index % 3 == 0:
                if r != 0:
                    ret = one_place[r - 1] + ' Hundred ' + ret

        return ret[:-1:]


print(Solution().numberToWords(1000000))