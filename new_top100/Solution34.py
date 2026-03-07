#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/3/7 07:49
# @Author      : Jim
# @File        : Solution34.py
# @Software    : PyCharm
# @Description :
class Solution:

    def find_index(self,nums,target)->int:
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left += 1

        return -1

    def find_left(self,nums,left,right,target)->int:
        while left+1<right:
            mid = (left+right)//2
            if nums[mid] == target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        else:
            return right


    def find_right(self,nums,left,right,target)->int:
        while left+1<right:
            mid = (left+right)//2
            if nums[mid] == target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            return right
        else:
            return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        find_index_result = self.find_index(nums,target)
        if self.find_index == -1:
            return [-1,-1]
        left = self.find_left(nums,0,find_index_result,target)
        right = self.find_right(nums,find_index_result,len(nums)-1,target)

        return [left,right]