#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-18 21:17:00
# @Author  : sober (wangshaobo08@gmail.com)
# @Link    : https://www.jianshu.com/u/b2d5110e9a57
# @Version : $Id$


class Queue():
    '''Queue'''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        '''into queue'''
        self.items.insert(0, item)

    def dequeue(self):
        '''output queue'''
        return self.items.pop()

    def size(self):
        '''return size'''
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue('hello')
    q.enqueue('world')
    q.enqueue('test')
    print(q.size())
