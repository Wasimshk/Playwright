#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    try:
        if n < 1 or n > 100:
            raise Exception("Please enter value between 1 to 100!")
        else:
            if n%2 == 1 or 6 <= n <= 20 :
                print("Weird")
            else:
                print("Not Weird")
    except Exception as e:
        print(e)
