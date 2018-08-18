# 代码示例
def main():
    with MoApp(appid='wx01434b3ed0010d28', name='myButton'):
        myButtonPage()

class myButtonPage(Page):
    def UI():
        Button(text='支付测试' , type='primary', pos=['center', 50],onTap=onPay)

    def onPay():
        mo.wxpay.pay('测试支付',0.1, onPaySuccessed, onPayFail)

    def onPaySuccessed():
        mo.console('支付成功')
    def onPayFail():
        mo.console('支付失败')
