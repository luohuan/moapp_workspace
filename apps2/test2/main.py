scoreData = [   
    {   
        'name': 'Alice',    
        'score': 87,    
        'portrait': 'https://wx.qlogo.cn/mmopen/vi_32/w1FCduEibtUaib0dhRpUkqDABa5rflJmsvuMITJMcwa7254CkbR6zIst5XicNInVt1ZvTw6XWiaxS9P0icdOGJicUCzg/132'   
    },  
    {   
        'name': 'Bob',  
        'score': 81,    
        'portrait': 'https://wx.qlogo.cn/mmopen/vi_32/w1FCduEibtUaib0dhRpUkqDABa5rflJmsvuMITJMcwa7254CkbR6zIst5XicNInVt1ZvTw6XWiaxS9P0icdOGJicUCzg/132'   
    },  
    {   
        'name': 'Charles',  
        'score': 91,    
        'portrait': 'https://wx.qlogo.cn/mmopen/vi_32/w1FCduEibtUaib0dhRpUkqDABa5rflJmsvuMITJMcwa7254CkbR6zIst5XicNInVt1ZvTw6XWiaxS9P0icdOGJicUCzg/132'   
    },          
    {   
        'name': 'Diana',    
        'score': 96,    
        'portrait': 'https://wx.qlogo.cn/mmopen/vi_32/w1FCduEibtUaib0dhRpUkqDABa5rflJmsvuMITJMcwa7254CkbR6zIst5XicNInVt1ZvTw6XWiaxS9P0icdOGJicUCzg/132'   
    }   
]   


def main():     
    with MoApp(appid='wx263b9c72fc87b39c', name='List sample'):   
        index()     

class index(Page):  

    def UI():   
        Input(name='input1', pos=['center', 5], border='1px solid #eeeeee', placeholder='Name',width=500)   
        Button(text='Search', pos=['center', 100], type='plainDefault', openType='getUserInfo',onTap=searchInfo)   
        Text(name='searchResult', pos=[240, 200], text='', color='green')   
        Text(pos=[5,300], text='List sorted by:')   

        with Box(pos=[5, 380]):     
            with List(name='list1'):    
                with Box(size=[600,150], margin='0 10% 10px 10%', fontSize=35, border='1px solid #cccccc'):     
                    Text(text='Name: {item.name}', pos=[10,20])     
                    Text(text='Score: {item.score}', pos=[10,75]) 
                    Image(src='{item.portrait}',mode='widthFix',position='relative',width=300,onTap=moui.goto('goods_info',goods_id='{item.goods_id}'))
                    Image(src='{item.portrait}',size=[200,200], pos=[-54,-48])

    def onInit():   
        mo.console(user.avatarUrl)
        page.list1.data = scoreData     

    def searchInfo():   
        # 列表中寻找对应人名，并返回结果   
        searchName = page.input1.value.strip().lower()  
        if searchName:  
            searchRes = 0   
            for x in scoreData:     
                if x['name'].lower() == searchName:     
                    searchRes = '%s     :     %s' %(x['name'], x['score'])  
                    break   
                else: pass  
            if searchRes:   
                page.searchResult.text = searchRes  
            else:   
                mo.showAlert('No match','')