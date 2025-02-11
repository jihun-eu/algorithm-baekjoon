#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    hour, minute  = map(int, input().split())
    
    target_hour = hour
    target_minute = minute - 45

    if target_minute < 0:
        target_hour -= 1
        target_minute += 60

    if target_hour < 0:
        target_hour += 24

    print(target_hour, target_minute)


if __name__ == "__main__":
    main()