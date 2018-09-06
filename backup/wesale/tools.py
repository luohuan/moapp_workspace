from goods_db import *



def get_publisher_info(publisher_id, user, mo):
    goods = Goods_db(user.openid, mo.db)
    items = goods.get_goodsinfo(publisher_id)
    publisher_id = items.get('publisher')
    publisher_info = user.getInfo(publisher_id)
    return publisher_info

def reverse_list(arr, start, end):
    if end < start:
        return
    for i in range(0, (end - start + 1) // 2):
        arr[start + i], arr[end - i] = arr[end - i], arr[start + i]

def reverse_list_mid(arr, mid):
    assert(mid < len(arr))
    end = len(arr) - 1
    reverse_list(arr, 0, mid - 1)
    reverse_list(arr, mid + 1, end)
    reverse_list(arr, 0, end)

def sortlist(listdata):
    list1 =[]
    list2 = []
    i = 0
    for item in listdata:
        if i%2 == 0:
            list1.append(item)
        else:
            list2.append(item)
        i += 1
    lastlist = list1 + list2
    return lastlist