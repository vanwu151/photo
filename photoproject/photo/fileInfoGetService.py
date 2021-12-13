import re, time, redis, json, os


class fileInfoGetService():
    def __init__(self, **kwds):
        try:
            self.SourceDir =  kwds['SourceDir']
        except Exception as E:
            print(E.args)
        try:
            self.RedisPoolNum = kwds['RedisPoolNum']
        except Exception as E:
            print(E.args)
        try:
            self.keyword = kwds['keyword']
        except Exception as E:
            print(E.args)
        try:
            self.typeword = kwds['typeword']
        except Exception as E:
            print(E.args)
        try:
            self.typewordlikelist = kwds['typewordlikelist']
        except Exception as E:
            print(E.args)
        try:
            self.serverRootPath = kwds['serverRootPath']
        except Exception as E:
            print(E.args)
        try:
            self.PcRootPath = kwds['PcRootPath']
        except Exception as E:
            print(E.args)

    def connRedis(self):
        """
        连接redis实例
        """
        EventPool = redis.ConnectionPool(host='172.18.99.116',
                                        port=6379,
                                        password='20**abAB',
                                        decode_responses=True,
                                        db=self.RedisPoolNum)
        EventPoolRedis = redis.StrictRedis(connection_pool=EventPool,
                                        charset='UTF-8',
                                        encoding='UTF-8')
        return EventPoolRedis


    def FilesDetails(self):
        """
        获取文件详细信息列表数据
        """
        RedisConn = self.connRedis()
        RedisConn.flushdb()
        for root, dirs, files in os.walk(r'{}'.format(self.SourceDir)):
            p0 = re.compile(r'~\$|\.db$|\.ini$|删|\.psd|\.tif|\.docx|\.xlsx|\.mp4|\.rar|\.pptx|\.ai|\.TIF|\.psb|\.tmp|\.CR2|\.pdf|\.xls')    # 过滤图片以外的格式 
            # p0 = re.compile(r'~\$|删|.*(?!jpg)|.*(?!png)|.*(?!jpeg)|.*(?!JPG)')          
            for File in files:
                filePath = os.path.join(root, File)
                b0 = p0.findall(filePath)
                try:
                    b0[0]
                except:                       
                    RedisConn.lpush(r'{}'.format(filePath),filePath,File)

    def serchKeywordsResaults(self):
        resaultsList = []
        connRedis = self.connRedis()
        resaultsGen = connRedis.scan_iter('*{}*'.format(self.keyword))
        for resault in resaultsGen:
            resaultsList.append(resault)
        return resaultsList

    def resaultsfiledata(self):
        conn = self.connRedis()
        typewordlikelist = self.typewordlikelist
        resaultsList = self.serchKeywordsResaults()
        typewordlikeresaultslist = []
        fileurllist = []
        fileindexlist = []
        fnlist = []
        index = 1
        functionIndex = 0
        filetypelist = []
        for resault in resaultsList:
            for typewordlike in typewordlikelist:
                pa = re.compile(r'{}'.format(typewordlike))
                ba = pa.findall(resault)
                try:
                    ba[0]
                    typewordlikeresaultslist.append(resault.replace(self.serverRootPath,self.PcRootPath).replace('/','\\'))  # 用户电脑中的文件访问具体路径列表
                    fileurllist.append(resault.replace(self.serverRootPath,''))                    
                    fileindexlist.append(index)
                    fnlist.append(conn.lindex(resault,0))  # 根据key 从redis列表中的索引获取第一个 文件名元素
                    filetypelist.append(self.typeword) 
                    index = index + 1
                    functionIndex = functionIndex + 1
                except:                   
                    pass
        filedata = {'fileindexlist':fileindexlist,'fileurllist': fileurllist,'typewordlikeresaultslist': typewordlikeresaultslist , 
                    'fnlist': fnlist,'filetypelist':  filetypelist,'functionIndex': functionIndex}
        return filedata
        





if __name__ == '__main__':
    BoCiSourceDir = "/mnt/images/ES/2021"
    BoCiRedisPoolNum = 15
    BociGetInfoService = fileInfoGetService(SourceDir = BoCiSourceDir, RedisPoolNum = BoCiRedisPoolNum)
    BociGetInfoService.FilesDetails()

    HBSourceDir = "/mnt/imageshaibao/海报/ES/2021" #海报图
    HBRedisPoolNum = 14
    HBGetInfoService = fileInfoGetService(SourceDir = HBSourceDir, RedisPoolNum = HBRedisPoolNum)
    HBGetInfoService.FilesDetails() 

    MJXSourceDir = "/mnt/imagesmaijiaxiu/ES天猫/推广部/❤❤❤❤❤2021内容营销❤❤❤❤/买家秀❤❤❤/买家秀"  #买家秀
    MJXRedisPoolNum = 13
    MJXGetInfoService = fileInfoGetService(SourceDir = MJXSourceDir, RedisPoolNum = MJXRedisPoolNum)
    MJXGetInfoService.FilesDetails()

    PPDRTSourceDir = "/mnt/imagespinpaidarentu/☆☆☆IP联名传播素材"  # 品牌达人图
    PPDRTRedisPoolNum = 12
    PPDRTGetInfoService = fileInfoGetService(SourceDir = PPDRTSourceDir, RedisPoolNum = PPDRTRedisPoolNum)
    PPDRTGetInfoService.FilesDetails()

    MTSourceDir = "/mnt/imageshaibao/修图组/妖精  修图临时存放点/OK/2021年"  # 模特图 
    MTRedisPoolNum = 11
    MTGetInfoService = fileInfoGetService(SourceDir = MTSourceDir, RedisPoolNum = MTRedisPoolNum)
    MTGetInfoService.FilesDetails()

    ZTSourceDir = "/mnt/imageszhutu/2021"  # 主图
    ZTRedisPoolNum = 10
    ZTGetInfoService = fileInfoGetService(SourceDir = ZTSourceDir, RedisPoolNum = ZTRedisPoolNum)
    ZTGetInfoService.FilesDetails()

    WMDRSourceDir = "/mnt/imagesmaijiaxiu/ES外贸/运营外贸/【SNS】/Lookbook"  #外贸达人
    WMDRRedisPoolNum = 9
    WMDRGetInfoService = fileInfoGetService(SourceDir = WMDRSourceDir, RedisPoolNum = WMDRRedisPoolNum)
    WMDRGetInfoService.FilesDetails()

    OtherSourceDir = "/mnt/imagesother"  #其他
    OtherRedisPoolNum = 8
    OtherGetInfoService = fileInfoGetService(SourceDir = OtherSourceDir, RedisPoolNum = OtherRedisPoolNum)
    OtherGetInfoService.FilesDetails()

    MTYPSourceDir = "/mnt/imageshaibao/原片/2021"  #模特原片
    MTYPRedisPoolNum = 7
    MTYPGetInfoService = fileInfoGetService(SourceDir = MTYPSourceDir, RedisPoolNum = MTYPRedisPoolNum)
    MTYPGetInfoService.FilesDetails()

    STDSourceDir = "/mnt/imagesshiti/4.实体设计素材"  #实体店图
    STDRedisPoolNum = 6
    STDGetInfoService = fileInfoGetService(SourceDir = STDSourceDir, RedisPoolNum = STDRedisPoolNum)
    STDGetInfoService.FilesDetails()

    SXHBSourceDir = "/mnt/shangxinhaibao"  #上新海报图周会用
    SXHBRedisPoolNum = 5
    SXHBGetInfoService = fileInfoGetService(SourceDir = SXHBSourceDir, RedisPoolNum = SXHBRedisPoolNum)
    SXHBGetInfoService.FilesDetails()

    # BoCiRedisPoolNum = 11 
    # keyword = '11108002'
    # typeword = '模特图'
    # typewordlikelist = ['模特']
    # serverRootPath = 'R:'
    # PcRootPath = '\\\\172.18.99.210\\6.模特图片库'
    # BociGetInfoService = fileInfoGetService(RedisPoolNum = BoCiRedisPoolNum, keyword = keyword, typeword = typeword,
    #                                     typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
    # resaultsData = BociGetInfoService.resaultsfiledata()
    # for i in resaultsData['fileinfolist']:
    #     print(i)
