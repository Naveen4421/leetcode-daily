def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flips = 0

        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1

            if bit_c == 1:
                # both a and b are 0 → need 1 flip
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            else:
                # bit_c == 0 → flip all 1s in a and b
                flips += bit_a + bit_b

        return flips
