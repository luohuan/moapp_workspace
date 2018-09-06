import time


img_type ={
            '出售':'http://material.motimaster.com/suyu1535094894000/微信图片_20180824151443.png',
            '求购':'http://material.motimaster.com/suyu1535094892000/微信图片_20180824151440.png',
            '赠送':'http://material.motimaster.com/suyu1535094889000/微信图片_20180824151424.png',
            }


class Goods_db:
    def __init__(self, openid, modb):
        self.openid = openid
        self.db = modb

    def pub_goods(self, detail): #商品发布需要信息
        db = self.db

        detail['creat_time'] = time.time()
        detail['update_time'] = time.time()
        detail['subcriber'] = ''
        detail['condition'] = '待接'
        detail['pv'] = 0
        return db.goods.insert(detail)

    def del_all_goods(self):#危险勿用
        db = self.db
        list_goods = db.goods.find()
        for item in list_goods:
            db.goods.delete(item['id'])


    def all_goods(self):#首页需要的商品信息列表
        db = self.db
        list_goods = db.goods.find({'condition':'待接'})
        ans = []
        need = ['title','type','cover','pv','price','goods_id']
        for item in list_goods:
            ans_one = {}
            for i in need:
                if i == 'cover':
                    ans_one[i] = item['pic_list'][0]
                    continue
                if i == 'goods_id':
                    ans_one[i] = item['id']
                    continue
                if i == 'type':
                    ans_one['img_type'] = img_type[item['type']]
                ans_one[i] = item[i]
            ans.append(ans_one)
        return ans

    def get_goodsinfo(self, goods_id): #商品详情页需要信息
        db = self.db

        list_goods = db.goods.find({'id':goods_id})    
        goods = list_goods[0]
        need = ['publisher','title','price','description','pic_list','deliver_type','type','pv','newness']
        ans = {}
        for item in need:
            ans[item] = goods[item]
        db.goods.update(goods_id,{'pv':goods['pv']+1})
        return goods

    def sub_goods(self, goods_id): #商品详情页接受信息
        db = self.db

        list_goods = db.goods.find({'id': goods_id})
        if list_goods[0]['condition'] != '待接':
            return False
        db.goods.update(goods_id,{'subcriber':self.openid})
        db.goods.update(goods_id,{'condition':'被接受'})
        db.goods.update(goods_id,{'update_time':time.time()})
        return True


    def get_pub_orderlist(self): #订单列表页-我发布的商品订单
        db = self.db

        list_goods = db.goods.find({'publisher':self.openid})

        ans = []
        need = ['publisher','subcriber','condition','cover','update_time','price','deliver_type','description','goods_id','title','newness', 'pv','type']
        for item in list_goods:
            ans_one = {}
            for i in need:
                if i == 'cover':
                    ans_one[i] = item['pic_list'][0]
                    continue
                if i == 'goods_id':
                    ans_one[i] = item['id']
                    continue
                ans_one[i] = item[i]
            ans.append(ans_one)
        return ans

    def get_sub_orderlist(self): #订单列表页-我接收的商品订单
        db = self.db

        list_goods = db.goods.find({'subcriber':self.openid})

        ans = []
        need = ['publisher','subcriber','condition','cover','update_time','price','deliver_type','description','goods_id','title','newness']
        for item in list_goods:
            ans_one = {}
            for i in need:
                if i == 'cover':
                    ans_one[i] = item['pic_list'][0]
                    continue
                if i == 'goods_id':
                    ans_one[i] = item['id']
                    continue
                ans_one[i] = item[i]
            ans.append(ans_one)
        return ans

    def confirm_order(self,goods_id):  # 订单确认
        db = self.db

        db.goods.update(goods_id,{'update_time':time.time()})
        return db.goods.update(goods_id,{'condition':'已完成'})


    def cancel_order(self,goods_id):  # 订单取消
        db = self.db
        db.goods.update(goods_id,{'subcriber':''})
        db.goods.update(goods_id,{'condition':'待接'})
        db.goods.update(goods_id,{'update_time':time.time()})

    def delete_order(self,goods_id):  # 订单删除
        db = self.db
        db.goods.update(goods_id,{'subcriber':''})
        db.goods.update(goods_id,{'condition':'取消'})
        db.goods.update(goods_id,{'update_time':time.time()})

    def match(self, title):  #匹配求购和出售相似度
        db = self.db
        allgoods = db.goods.find({'condition':'待接', 'type':'出售'})
        matchgoods = []
        for item in title:
            for item1 in allgoods:
                if item in item1['title']:
                    if title.index(item) != len(title)-1:
                        num = title.index(item)
                        if title[num:num+2] in item1['title']:
                            matchgoods.append(item1)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        return matchgoods



    def searchgoods(self, inputtext):  #首页商品搜索
        db = self.db
        allgoods = db.goods.find({'condition':'待接'})
        searchdata = []
        for item in allgoods:
            if inputtext in item['title']:
                searchdata.append(item)
            else:
                pass
        for item in inputtext:
            for item1 in allgoods:
                if item in item1['title']:
                    if inputtext.index(item) != len(inputtext)-1:
                        num = inputtext.index(item)
                        if inputtext[num:num+2] in item1['title']:
                            if item1 not in searchdata:
                                searchdata.append(item1)
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass        
        ans = []
        need = ['title','type','cover','pv','price','goods_id']
        for item in searchdata:
            ans_one = {}
            for i in need:
                if i == 'cover':
                    ans_one[i] = item['pic_list'][0]
                    continue
                if i == 'goods_id':
                    ans_one[i] = item['id']
                    continue
                if i == 'type':
                    ans_one['img_type'] = img_type[item['type']]
                ans_one[i] = item[i]
            ans.append(ans_one)
        return ans


















