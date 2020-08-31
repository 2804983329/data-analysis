from weibo import APIClient
def weibo():
    APP_KEY='从微博 开发平台获取'
    APP_SECRETY='从微博 开发平台获取'
    CALLBACK_URL='从微博 开发平台获取 授权回调页'
    AUTH_URL = '从微博 开发平台获取 取消授权回调页'
    USERID=''#开发者微博ID
    PASSWD=''
    client=APIclient(app_key=APP_KEY,app_secret=APP_SECRET,redirect_url=CALLBACK_URL)#初始化client   refer_url未写
    refer_url=client.get_authorise_url() #通过什么网址输出
    print "refer_url:" + refer_url
