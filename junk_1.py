"""
Junk 
"""

import sqlite3
import re


STRING = "thiS Is an iSsue involving IsiS"


class MySum(object):
    def __init__(self):
        self.count = 0
        self.con = sqlite3.connect(":memory:")
        self.con.create_aggregate("mysum", 1, MySum)
        self.cur = self.con.cursor()

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

    def my_method(self):
        self.cur.execute("CREATE TABLE test(i)")
        self.cur.execute("INSERT INTO test(i) VALUES (1)")
        self.cur.execute("INSERT INTO test(i) VALUES (2)")
        self.cur.execute("SELECT mysum(i) FROM test")
        self.con.commit()

    def fetch_one(self):
        return self.cur.fetchone()[0]


def main():
    ms = MySum()

    for match in re.finditer("[iI][sS]", STRING):
        dog = match
        print dog.group()

    ms.my_method()
    one = ms.fetch_one()

    val = one
    print(val)

    dog = 1


if __name__ == '__main__':
    main()
