class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        （1）思路：中心扩展法
                这是一个比较巧妙的方法，实质的思路和动态规划的思路类似。比如对一个字符串ababa，选择最中间的a作为中心点，
            往两边扩散，第一次扩散发现left指向的是b，right指向的也是b，所以是回文串，继续扩散，同理ababa也是回文串。这个
            是确定了一个中心点后的寻找的路径，然后我们只要寻找到所有的中心点，问题就解决了。中心点一共有多少个呢？看起来
            像是和字符串长度相等，但你会发现，如果是这样，上面的例子永远也搜不到abab，想象一下单个字符的哪个中心点扩
            展可以得到这个子串？似乎不可能。所以中心点不能只有单个字符构成，还要包括两个字符，比如上面这个子串abab，
            就可以有中心点ba扩展一次得到
        （2）复杂度：
            - 时间复杂度：O（N^2）
            - 空间复杂度：O（1）
        """
        # 处理特殊情况
        str_len = len(s)
        if str_len == 0 or s is None:
            return 0
        # 定义变量储存结果，初始化时直接考虑单字符回文的情况，所以直接赋值为字符串长度
        res = str_len
        # 遍历所有的中心点，第一类，遍历所有的单中心点
        for center in range(1, str_len-1):
            # 初始定义left和right和中心点不同，因为单字符已经在res初始化时考虑了
            left, right = center-1, center+1
            while left >= 0 and right < str_len and s[left] == s[right]:
                res += 1
                left, right = left-1, right+1
        # 遍历所有的中心点，第二类，遍历所有的双中心点
        # 注意考虑两个问题，一个是双中心点本身需要考虑是否是回文，另一个是边界条件，需要考虑
        for center in range(0, str_len - 1):
            # 考虑双中心点本身是否是回文子串
            if s[center] == s[center+1]:
                res += 1
            # 初始定义left和right和中心点不同
            left, right = center-1, center+2
            while left >= 0 and right < str_len and s[left] == s[right] and s[center] == s[center+1]:
                res += 1
                left, right = left-1, right+1

        return res

