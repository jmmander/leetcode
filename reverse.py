class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        length = len(x)
        rev_int = x[length::-1]
        if rev_int[-1] == "-":
            new = rev_int[0:length-1]
            if new.count("0") == length-1:
                num =  "-" + "0"
            else:
                num = new.lstrip("0")
                num = "-" + num
        else:
            new = rev_int
            if new.count("0") == length:
                num = "0"
            else:
                num = new.lstrip("0")
        num = int(num)
        if -2147483648 <= num <= 2147483647:
            return num
        else:
            return 0
