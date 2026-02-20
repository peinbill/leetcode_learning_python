#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/18 23:31
# @Author      : Jim
# @File        : Solution33.py
# @Software    : PyCharm
# @Description :
class Solution:

    def find_split_index(self,nums):
        left,right = 0,len(nums)-1
        if nums[left] <= nums[right]:
            return -1

        while left+1<right:
            mid = (left+right)//2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid

        if nums[right] > nums[left]:
            return right
        else:
            return left


    def search_new(self,nums,left,right,target):
        while left+1<right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        return -1