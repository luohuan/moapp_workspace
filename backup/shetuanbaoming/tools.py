import time
import operator

FORMDATAID = ['input_1', 'input_2', 'input_3', 'input_4', 'input_5', 'input_6', 'input_7', 'input_8', 'input_9', 'input_10', 'input_11', 'input_12', 'input_13', 'input_14', 'input_15']
INPUTID = ['input1', 'input2', 'input3', 'input4', 'input5', 'input6', 'input7', 'input8', 'input9', 'input10', 'input11', 'input12', 'input13', 'input14', 'input15']
BOX = ['box1', 'box2', 'box3', 'box4', 'box5', 'box6', 'box7', 'box8', 'box9', 'box10', 'box11', 'box12', 'box13', 'box14', 'box15']

options_template = [
    {
    'option':'姓名',
    'icon':'http://material.motimaster.com/ywjiang/ceshiyong/demo/30a7f7ed0235065a17c2d6a4bbf6ba60.png',
    'label':'realname'
    },

    {
    'option':'性别',
    'icon':'http://material.motimaster.com/ywjiang/ceshiyong/demo/b9ddafd0760dc25c3bb3c133bcd166d3.png',
    'label':'gender'
    },

    {
    'option':'学号',
    'icon':'http://material.motimaster.com/ywjiang/ceshiyong/demo/2abfa3f5e098b7d0a4df1b35f26930ec.png',
    'label':'studentid'
    },

    {
    'option':'院系',
    'icon':'http://material.motimaster.com/ywjiang/ceshiyong/demo/361a3d0ad6c31add1328f92ca100791b.png',
    'label':'department'
    },

    {
    'option':'联系电话',
    'icon':'http://material.motimaster.com/ywjiang/ceshiyong/demo/c048df6a346309cf266b787347b4cf72.png',
    'label':'phonenumber'
    },

    {
    'option':'邮箱',
    'icon':'http://material.motimaster.com/ywjiang/ceshiyong/demo/bd130f545a3ff5ee6166621ded6e84f5.png',
    'label':'email'
    },

    {
    'option':'qq',
    'icon':'http://material.motimaster.com/ywjiang/ceshiyong/demo/db1e820d007bb50c853893749854d49f.png',
    'label':'qq'
    },

    {
    'option':'意向部门',
    'icon':'http://material.motimaster.com/ywjiang/ceshiyong/demo/3969a38f025eac342004fa9fbfd2e849.png',
    'label':'intentiondepartment'
    },

    {
    'option':'兴趣爱好',
    'icon':'http://material.motimaster.com/ywjiang/ceshiyong/demo/3969a38f025eac342004fa9fbfd2e849.png',
    'label':'interest'
    },

    {
    'option':'微信',
    'icon':'http://material.motimaster.com/ywjiang/ceshiyong/demo/2e77bb69601f2a5e3bc201536e899c71.png',
    'label':'weixin'
    }
]

TEMPLATE = ['invate', 'result']
invate = ['姓名', '面试时间', '面试地点', '温馨提醒']
invateid = '8sItDq7aN7ADpIprTBYlYA5UeJhe1xNeQ28HrDFrPOg'
result = ['姓名', '面试部门', '面试结果', '备注']
resultid = '_hCk_6Z9R5yNn79USQDFGE7VUdoBUbV7zlZ72nN74IA'
createlistid = 'zZU7PFDiKJF0IbR_IImaiozqjSce0xN_kpPwaP4in6Q'
entryid = 'aZON8Kw6FDty3KNM21iKbnmxCDVYUDCnG4qD_6l2iFE'

navicolor = '#256DF2'
MANAGEID = ['oIkUc5ATjFE9G7xbpKQzkNh2IWJo']

whitebackground = '#ffffff'
greybackground = '#f4f4f4'

right_arrow = 'http://material.motimaster.com/ywjiang/ceshiyong/demo/a15eb4750f4a80ebf64514d3c50a7fd7.png'

banner_image = [
    {
    'id':1,
    'pic':'http://material.motimaster.com/suyu1996/hi/main/aab8cc5f4da054429c04b1058486470e.png'
    },

    {
    'id':2,
    'pic':'http://material.motimaster.com/suyu1996/hi/main/a62bf7adc3591995df5e7cef564267af.png'
    }
]

functionlist = [
    {
    'function':'查看',
    'pic':'http://material.motimaster.com/ywjiang/ceshiyong/demo/9e5b347aaedb40f719e79356f9f284f5.png'
    },

    {
    'function':'邀请报名',
    'pic':'http://material.motimaster.com/ywjiang/ceshiyong/demo/cb5e784d0390cb2cfd4fffa496ad5281.png'
    },

    {
    'function':'查看结果',
    'pic':'http://material.motimaster.com/ywjiang/ceshiyong/demo/f37449fa75da116ac6853a5c7c2ef554.png'
    },

    {
    'function':'权限管理',
    'pic':'http://material.motimaster.com/ywjiang/ceshiyong/demo/1cb7315cbd3b4f00e77126b170f330de.png'
    },

    {
    'function':'删除',
    'pic':'http://material.motimaster.com/ywjiang/ceshiyong/demo/f30ad661c72778b57db5f4d489f759e3.png'
    }
]


class form():
    def __init__(self, openid, mo):
        self.openid = openid
        self.mo = mo

    def addform(self, detail):  #创建报名
        mo = self.mo
        detail['createtime'] = time.time()
        detail['state'] = 0
        mo.db.form.insert(detail)

    def get_formdata(self, formid):  #根据formid返回某场活动的表单信息
        mo = self.mo
        formdata = mo.db.form.find({'id':formid})
        return formdata

    def get_all_formdata(self):  #返回报名列表里的所有信息
        mo = self.mo
        formdata = mo.db.form.find()
        formdata.reverse()
        return formdata

    def update_form_state(self, formid):  #更改活动审核状态
        mo = self.mo
        formdata = mo.db.form.find({'id':formid})
        if formdata[0]['state']:
            mo.db.form.update(formdata[0]['id'], {'state':0})    
            return False
        else:
            mo.db.form.update(formdata[0]['id'], {'state':1})    
            return True
            
    def get_pass_formdata(self):  #获取审核通过的活动信息
        mo = self.mo
        formdata = mo.db.form.find({'state':1})
        formdata.reverse()
        return formdata
        

class formdata():
    def __init__(self, openid, mo):
        self.openid = openid
        self.mo = mo

    def addformdata(self, detail):  #新的报名
        mo = self.mo
        openid = self.openid

        detail['createtime'] = time.time()
        detail['state'] = 1
        detail['openid'] = openid
        mo.db.formdata.insert(detail)

    def deleteformdata(self, formid): #删除报名信息
        openid = self.openid
        mo = self.mo
        myformdata = mo.db.formdata.find({'formid':formid, 'openid':openid})
        mo.db.formdata.update(myformdata[0]['id'], {'state':0})

    def clearformdata(self):  #清空所有报名信息，谨慎用
        mo = self.mo
        alldata = mo.db.formdata.find()
        for item in alldata:
            mo.db.formdata.delete(item['id'])
        return True

    def get_formdata_detail(self, formid):  #根据openid和formid返回这个人的某场活动的报名信息
        openid = self.openid
        mo = self.mo

        formdata = mo.db.formdata.find({'openid':openid, 'formid':formid})
        return formdata

    def get_thisform_allopenid(self, formid):  #根据formid返回这场活动的所有openid，以[openid1, openid2, openid3, ...]形式
        mo = self.mo
        allformfdata = mo.db.formdata.find({'formid':formid})
        
        allopenid = []
        allformfdata.reverse()
        for item in allformfdata:
            allopenid.append(item['openid'])
        return allopenid

    def haveformdata(self, formid): #判断openid是否已经报名了这场比赛
        openid = self.openid
        mo = self.mo
        formdata = mo.db.formdata.find({'openid':openid, 'formid':formid})
        if formdata:
            return True
        else:
            return False



    
class manager():
    def __init__(self, openid, mo):
        self.openid = openid
        self.mo = mo

    def addmanager(self, formid): #新增管理员
        openid = self.openid
        mo = self.mo
        mo.db.manager.insert({'formid':formid, 'managerid':openid})

    def deletemanager(self):  #删除管理员
        mo = self.mo
        openid = self.openid
        manager = mo.db.manager.find({'managerid':openid})
        mo.db.manager.delete(manager[0]['id'])

    def is_manager(self, formid):  #判断是否是管理员
        openid = self.openid
        mo = self.mo
        manager = mo.db.manager.find({'managerid':openid, 'formid':formid})
        if manager:
            return True
        else:
            return False
    def get_form_manager(self, formid):  #根据formid查找所有的管理员openid
        mo = self.mo
        all_manager_openid = mo.db.manager.find({'formid':formid})
        return all_manager_openid

class person():
    def __init__(self, user, mo):
        self.user = user
        self.mo = mo
        self.detail = {
            'openid':user.openid,
            'nickname':user.nickname,
            'headpic':user.avatarUrl,
            'gender':user.gender,
            'province':user.province,
            'city':user.city,
            'realname':'',
            'weixin':'',
            'phonenumber':'',
            'department':'',
            'studentid':'',
            'qq':'',
            'email':''
        }

    def is_newuser(self):  #判断是否新用户
        user = self.user
        mo = self.mo

        personinfo = mo.db.person.find({'openid':user.openid})
        if personinfo:
            return False
        else:
            return True

    def addpersoninfo(self):  #新增用户信息
        user = self.user
        mo = self.mo
        detail = self.detail

        mo.db.person.insert(detail)

    def get_person_info(self, openid):  #根据openid当前用户个人信息
        mo = self.mo
        personinfo = mo.db.person.find({'openid':openid})
        return personinfo
    # def updatepersoninfo(self):  #更新用户信息
    #     openid = self.openid
    #     mo = self.mo
    #     detail = self.detail
        
    #     personinfo = mo.db.person.find({'openid':user.openid})
        
    #     for item in detail:
    #         if item['nickname'] != personinfo[0]['nickname']:
    #             item['nickname'] = personinfo[0]['nickname']
    #         elif item['headpic'] != personinfo[0]['headpic']:
    #             item['headpic'] = personinfo[0]['headpic']
    #         else:
    #             pass
    #     mo.db.person.update(personinfo[0]['id'], detail)        

    def showpersoninfo(self):  #根据openid返回某个用户的所有个人信息
        user = self.user
        mo = self.mo
        personinfo = mo.db.person.find({'openid':user.openid})
        return personinfo

def get_my_formdata(user, mo):  #获取个人报名的所有活动信息
    formdata = mo.db.formdata.find({'openid':user.openid})
    alldata = []
    for item in formdata:
        thisform = mo.db.form.find({'id':item['formid']})
        formdict = {
            'id':thisform[0]['id'],
            'formid':item['formid'],
            'title':thisform[0]['title'],
            'intro':thisform[0]['intro']
        }
        alldata.append(formdict)
    alldata.reverse()
    return alldata

def get_my_all_createform(user, mo):
    formdata = mo.db.form.find({'openid':user.openid})
    managerdata = mo.db.manager.find({'managerid':user.openid})
    #将管理员的表单添加进去
    for item in managerdata:
        managerlist = mo.db.form.find({'id':item['formid']})
        formdata += managerlist
    
    for item in formdata:
        item['count'] = len(mo.db.formdata.find({'formid':item['id']}))
    
    formdata = sorted(formdata, key=operator.itemgetter('createtime'), reverse=True) 
    return formdata    
    

    
    


#返回某一场比赛的报名名单
def showformdata(mo, formid):
    formdata3 = []
    formdata1 = mo.db.form.find({'id':formid})
    formdata2 = mo.db.formdata.find({'formid':formid})
    formdata2.reverse()

    for item in formdata2:
        formdata3.append({'openid':item['openid'],
            'formid':item['formid'], 
            'keyword1':formdata1[0]['input1']+':'+item['input1'], 
            'keyword2':formdata1[0]['input2']+':'+item['input2'], 
            'keyword3':formdata1[0]['input3']+':'+item['input3'],
            'keyword4':item['createtime']
            })

    
    return formdata3

#根据openid和formid返回某个人某场比赛的所有报名信息，并且按顺序排列好
def showformdatadetail(mo, openid, formid):
    thisform = form(openid, mo)
    thisformdata = thisform.get_formdata(formid)
    thisforminfo = formdata(openid, mo)
    thisforminfo_detail = thisforminfo.get_formdata_detail(formid)

    formdatadetail = []
    for k in thisformdata[0].keys():
        if k in INPUTID:
            formdatadetail.append({'keyword1':str(INPUTID.index(k)+1)+'.'+thisformdata[0][k], 'keyword2':thisforminfo_detail[0][k], 'index':INPUTID.index(k)})
        else:
            pass
    sorted_formdatadetail = sorted(formdatadetail, key=operator.itemgetter('index'), reverse=False)
    return thisformdata[0]['title'], sorted_formdatadetail



























