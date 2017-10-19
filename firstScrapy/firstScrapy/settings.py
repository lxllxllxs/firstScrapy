BOT_NAME = 'firstScrapy'
SPIDER_MODULES = ['firstScrapy.spiders']
NEWSPIDER_MODULE = 'firstScrapy.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'
ROBOTSTXT_OBEY = False
# COOKIES_ENABLED = True

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Cookie':"SINAGLOBAL=993218899238.8546.1491390950748; UM_distinctid=15c61216062274-02d9cb18def1a5-314b7b5f-13c680-15c6121606319b; login_sid_t=fdf7d53696cab26efe4821c7194069db; _s_tentry=-; Apache=860073820780.5004.1508128876895; ULV=1508128876908:96:2:1:860073820780.5004.1508128876895:1507521162167; UOR=baike.baidu.com,widget.weibo.com,www.baidu.com; un=774785161@qq.com; TC-Page-G0=9183dd4bc08eff0c7e422b0d2f4eeaec; WBtopGlobal_register_version=015f00677046c229; SCF=AigEEUe9YTOi-CXvQmto3B92OW3pRumlXQkIk2086aBs_-lrAN0BmNv-LInDiUwhBExOe-o4gRGO2By_-V1o0LI.; SUB=_2A2507BPBDeRhGeRH7lAW8yfNzDmIHXVXmAIJrDV8PUNbmtANLRb8kW8osfYmXP503kS2zoFiV5bL87F37Q..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh4jxo.IPIdKkPoSYe09De55JpX5K2hUgL.Foz4SKzNe0.pS0-2dJLoIpRLxK-LBKBLBK.LxKBLB.2LB--LxKBLB.2L1h9eg27t; SUHB=0sqBKZ2OmO_MdK; ALF=1509006864; SSOLoginState=1508402065; un=774785161@qq.com"

}
