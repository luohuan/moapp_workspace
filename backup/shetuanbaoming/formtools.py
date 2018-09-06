import time

class form():
	def __init__(self, openid, mo):
        self.openid = openid
        self.mo = mo

    def addform(self, detail):  #创建报名
    	mo = self.mo
    	detail['createtime'] = time.time()
    	detail['state'] = 0
    	mo.db.form.insert(detail)

    def addformdata(self, detail):  #新的报名
		mo = self.mo
		detail['createtime'] = time.time()
		detail['state'] = 1
		mo.db.formdata.insert(detail)

	def deleteformdata(self, formid): #删除报名信息
		openid = self.openid
		myformdata = mo.db.formdata.find({'formid':formid, 'openid':openid})
		mo.db.formdata.update(myformdata[0]['id'], {'state':0})

	def get_formdata(self, formid):  #根据formid返回某场活动的表单信息
		mo = self.mo
		formdata = mo.db.form.find({'id':formid})
		return formdata
	
class manager():
	def __init__(self, openid, mo):
		self.openid = openid
		self.mo = mo

	def addmanager(self, formid): #新增管理员
		openid = self.openid
		mo = self.mo
		mo.db.manager.insert({'formid':formid, 'managerid':openid})

	def deletemanager(self, formid):  #删除管理员
		openid =self.openid
		mo = self.mo
		manager = mo.db.manager.find({'managerid':openid})
		mo.db.manager.delete(manager[0]['id'])

	def is_manager(self, formid):  #判断是否是管理员
		openid = self.openid
		mo = self.mo
		manager = mo.db.manager.find({'managerid':openid})
		if manager:
			return True
		else:
			return False

class person():
	def __init__(self, openid, mo):
		self.openid = openid
		self.mo = mo
	def is_newuser(self):  #判断是否新用户
		openid = self.openid
		mo = self.mo
		personinfo = mo.db.person.find({'openid':openid})
		if personinfo:
			return False
		else:
			return True
	def addpersoninfo(self, detail):  #新增用户信息
		openid = self.openid
		mo = self.mo
		mo.db.person.insert({detail})

	def updatepersoninfo(self, detail):  #更新用户信息
		openid = self.openid
		mo = self.mo
		personinfo = mo.db.person.find({'openid':openid})
		for item in detail:
			if item['nickname'] != personinfo[0]['nickname']:
				item['nickname'] = personinfo[0]['nickname']
			elif item['headpic'] != personinfo[0]['headpic']:
				item['headpic'] = personinfo[0]['headpic']
			else:
				pass
		mo.db.person.update(personinfo[0]['id'], detail)		
























