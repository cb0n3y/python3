#!/usr/bin/python3
# _*_ coding: utf-8 _*_


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
