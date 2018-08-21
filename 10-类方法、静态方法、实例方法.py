# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/21 19:29'


class Date(object):
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    def tomorrow(self):
        self.date += 1

    @staticmethod
    def date_string(date_str):
        year, month, date = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(date))

    @classmethod
    def cls_date_string(cls, date_str):
        year, month, date = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(date))

    def __str__(self):
        return "{year}/{month}/{date}".format(year=self.year, month=self.month, date=self.date)


if __name__ == '__main__':
    new_date = Date(2018, 10, 11)
    print(new_date)

    new_date1 = Date.date_string('2018-6-5')
    print(new_date1)

    new_date2 = Date.cls_date_string('2018-8-20')
    print(new_date2)

