#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/7 01:03
# @Author      : Jim
# @File        : all.py
# @Software    : PyCharm
# @Description :

# 作者：好文摘读 https://www.bilibili.com/read/cv23519599/ 出处：bilibili


def add(num1, num2):
    result = ""
    carry = 0
    len1, len2 = len(num1), len(num2)
    for i in range(max(len1, len2)):
        digit1 = int(num1[len1-1-i]) if i < len1 else 0
        digit2 = int(num2[len2-1-i]) if i < len2 else 0
        digit = digit1 + digit2 + carry
        carry = digit // 10
        digit %= 10
        result = str(digit) + result
    if carry:
        result = str(carry) + result
    return result

def subtract(num1, num2):
    result = ""
    borrow = 0
    len1, len2 = len(num1), len(num2)
    if len1 < len2:
        num1, num2 = num2, num1
        len1, len2 = len2, len1
        result = "-"
    elif len1 == len2 and num1 < num2:
        num1, num2 = num2, num1
        len1, len2 = len2, len1
        result = "-"
    for i in range(len1):
        digit1 = int(num1[len1-1-i])
        digit2 = int(num2[len2-1-i]) if i < len2 else 0
        digit = digit1 - digit2 - borrow
        borrow = 0
        if digit < 0:
            digit += 10
            borrow = 1
        result = str(digit) + result
    result = result.lstrip("0")
    if not result:
        result = "0"
    return result

def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    result = "0"
    for i in range(len(num2)-1, -1, -1):
        carry = 0
        sub_result = ""
        for j in range(len(num1)-1, -1, -1):
            digit = int(num1[j]) * int(num2[i]) + carry
            carry = digit // 10
            digit %= 10
            sub_result = str(digit) + sub_result
        if carry:
            sub_result = str(carry) + sub_result
        sub_result += "0" * (len(num2)-1-i)
        result = add(result, sub_result)
    return result

def divide(num1, num2):
    if num2 == "0":
        return "Undefined"
    if num1 == "0":
        return "0"
    result = ""
    remainder = ""
    for i in range(len(num1)):
        remainder += num1[i]
        quotient = 0
        while compare(remainder, num2) >= 0:
            remainder = subtract(remainder, num2)
            quotient = add(quotient, "1")
        result += quotient
    result = result.lstrip("0")
    if not result:
        result = "0"
    return result, remainder

def power(num, exponent):
    if exponent == 0:
        return "1"
    if exponent == 1:
        return num
    if exponent % 2 == 0:
        half_power = power(num, exponent // 2)
        return multiply(half_power, half_power)
    else:
        half_power = power(num, (exponent-1) // 2)
        return multiply(num, multiply(half_power, half_power))

def compare(num1, num2):
	len1, len2 = len(num1), len(num2)
	if len1 < len2:
		return -1
	elif len1 > len2:
		return 1
	else:
		for i in range(len1):
			if num1[i] < num2[i]:
				return -1
			elif num1[i] > num2[i]:
				return 1
		return 0

num1 = "123456789012345678901234567890"
num2 = "987654321098765432109876543210"
print("num1 = ", num1)
print("num2 = ", num2)

print("num1 + num2 = ", add(num1, num2))
print("num1 - num2 = ", subtract(num1, num2))
print("num1 * num2 = ", multiply(num1, num2))
# print("num1 / num2 = ", divide(num1, num2))

# num3 = "123"
# exponent = 45
# print("num3 = ", num3)
# print("num3^exponent = ", power(num3, exponent))