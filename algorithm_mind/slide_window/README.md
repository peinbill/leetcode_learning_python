# 滑动窗格


框架：
只有java代码
```java
/* 滑动窗口算法框架 */
void slidingWindow(string s, string t) {
    unordered_map<char, int> need, window;
    for (char c : t) need[c]++;

    int left = 0, right = 0;
    int valid = 0;
    while (right < s.size()) {
        // c 是将移入窗口的字符
        char c = s[right];
        // 右移窗口
        right++;
        // 进行窗口内数据的一系列更新
        ...

        /*** debug 输出的位置 ***/
        printf("window: [%d, %d)\n", left, right);
        /********************/

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // d 是将移出窗口的字符
            char d = s[left];
            // 左移窗口
            left++;
            // 进行窗口内数据的一系列更新
            ...
        }
    }
}

```

需要变化的地方

    1、右指针右移之后窗口数据更新
    2、判断窗口是否要收缩
    3、左指针右移之后窗口数据更新
    4、根据题意计算结果


Solution76: 滑动窗格经典demo（做不出，看答案），但可以用该题作为一个经典入门

Solution567: Solution76的改进

