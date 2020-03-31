#!/usr/bin/python
# -*- coding: utf-8 -*-

num = 10


# 一个数据节点
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def set_next(self, node):
        self.next_node = node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data

    def if_data_equals(self, data):
        return self.data == data


class HashTable(object):
    def __init__(self):
        self.value = [None] * num

    def search(self, data):
        i = data % num
        if self.value[i] is None:
            return False
        else:
            head = self.value[i]
            while head and not head.if_data_equals(data):
                head = head.get_next()
            if head:
                return head
            else:
                return False

    def insert(self, data):
        if self.search(data):
            return True

        i = data % num
        node = Node(data)
        if self.value[i] is None:
            self.value[i] = node
            return True
        else:
            head = self.value[i]
            while head.get_next() is not None:
                head = head.get_next()
            head.set_next(node)
            return True

    def delete(self, data):
        if self.search(data):
            i = data % num
            if self.value[i].if_data_equals(data):
                self.value[i] = self.value[i].get_next()
            else:
                head = self.value[i]
                while not head.get_next().if_data_equals(data):
                    head = head.get_next()
                head.set_next(head.get_next().get_next())
            return True
        else:
            return False

    def echo(self):
        i = 0
        for head in self.value:
            print(str(i) + ':\t')
            if head is None:
                print("None")
            else:
                while head is not None:
                    print(str(head.get_data()) + ' ->')
                    head = head.get_next()
                print("None")
            print('')
            i += 1
        print('')


if __name__ == '__main__':
    hashTable = HashTable()
    hashTable.insert(10)
    hashTable.insert(11)
    hashTable.insert(1)
    hashTable.echo()
    hashTable.delete(1)
    hashTable.echo()