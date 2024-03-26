#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/15 23:04
# @Author      : Jim
# @File        : Solution15.py
# @Software    : PyCharm
# @Description :


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()
        for i in range(len(nums)):
            if i>=1 and nums[i]==nums[i-1]:
                continue

            rtn = self.twoSum(nums,i+1,len(nums)-1,0-nums[i])


            if rtn:
                for rtn_1,rtn_2 in rtn:
                    tmp_result = [nums[i],rtn_1,rtn_2]
                    result.append(tmp_result)

        return list(result)

    def twoSum(self,nums,start,end,target):
        result_set = set()
        result = []
        while start< end:
            if nums[start]+nums[end] == target:
                if (nums[start],nums[end]) not in result_set:
                    result.append((nums[start],nums[end]))
                    result_set.add((nums[start],nums[end]))
                start += 1
                end -= 1
            elif nums[start]+nums[end] > target:
                end-=1
            else:
                start+=1

        return result


