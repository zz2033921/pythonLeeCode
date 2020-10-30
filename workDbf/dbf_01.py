import dbf

src_filename = 'zx .DBF'  # 原dbf的地址
# des_filename = 'xxxx\\template.DBF' #期望得到的dbf模板
# create an in-memory table
# table = dbf.Table(
#         filename=des_filename, #打开模板文件
#         codepage='cp936', #相当于gbk的方式打开
#         on_disk=True,     #是否在磁盘上保存修改
#         )
# table.open(mode=dbf.READ_WRITE)  #让内存中的table以可读写的方式打开，默认为只读

# 同上 以只读的方式打开原dbf
src_table = dbf.Table(
    filename=src_filename,
    codepage='cp936',
    on_disk=True,
)
src_table.open(dbf.READ_WRITE)
src_table.record_length
src_table.field_names

# print(src_table.record_length)
# print(src_table)
cclist = []
for cc in src_table.field_names:
    # print(cc)
    cclist.append(cc)
for i in src_table:
    # 这里的i并不是一个列表，而是一个数据结构，可以通过以下的方式转化为列表
    record_len = len(i)
    # print(i)
    print(i.__getattr__("ksh"))
    print(i.__getitem__("ksh"))

    # print(i.KSH)
    # print(record_len)
    # print(i)
    # print(len(i))
    one_data_list = i[0:record_len]
    one_data = list(one_data_list)
    # table.append(one_data)
    # print(one_data)
dbfDict = {}
for index, value in enumerate(one_data):
    # print(index,"--",value)
    print(index, "--", value, "---", len(value))
    # dbfDict[cclist[index]] = value

# print(dbfDict)
# #当然 你也可以自己添加新的一行数据 如下
# new_record = (1, '1', '测试', '20200831', '20200831', '1', '', '00', '')
# table.append(new_record)
# #可以用下面的方式，读取
# for record in table:
#     print(record)
#     print('--------')
#     print(record[0:9])
#     print([record.HGSQXH, record.HGZQZH, record.HGZHMC])
#     print('--------')
src_table.close()
# table.close() #关闭并保存到磁盘
