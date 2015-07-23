#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mugbya'


import xlsxwriter


def createFile(file):

    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()

    worksheet.title = "New Title"
    setTitle(worksheet)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    # worksheet.write('A1', 'Hello')

    # Text with formatting.
    # worksheet.write('A2', 'World', bold)

    # # Write some numbers, with row/column notation.
    # worksheet.write(2, 0, 123)

    # Insert an image.
    # worksheet.insert_image('B5', 'logo.png')

    workbook.close()


def setTitle(worksheet):
    # Widen the first column to make the text clearer.

    worksheet.set_column('C:C', 10)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 10)

    worksheet.write('C7', '主机')
    worksheet.write('D7', '操作系统')
    worksheet.write('E7', '设备类型')
    worksheet.write('F7', '端口')
    worksheet.write('G7', '端口状态')
    worksheet.write('H7', '服务名称')
    worksheet.write('I7', '域名')


if __name__=='__main__':
    createFile("test.xlsx")