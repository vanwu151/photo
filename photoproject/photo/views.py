from django.shortcuts import render
import os, re, time, json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from . import fileInfoGetService as fs

# Create your views here.


def searchfile(request):
    if request.method == "GET":
        return render(request, 'photo/searchfile.html')


def serchfileinfo(request):
    if request.method == "POST":
        keyword = request.POST.get('search')
        if keyword == '':
            return redirect('/')
        else:
            #  主图
            zhutuPoolNum = 10
            typeword = '主图'
            typewordlikelist = ['导购页', '主图', '2021']
            serverRootPath = '/mnt/imageszhutu'
            PcRootPath = '\\\\172.18.99.210\\导购页'
            zhutuGetInfoService = fs.fileInfoGetService(RedisPoolNum = zhutuPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            zhuturesaultsData = zhutuGetInfoService.resaultsfiledata()
            try:
                zhuturesaultPD = len(zhuturesaultsData['fileurllist'])
            except:
                zhuturesaultPD = 'OK Getch It'
            zhutufileindexlist = zhuturesaultsData['fileindexlist']
            zhutufileurllist = zhuturesaultsData['fileurllist']
            zhututypewordlikeresaultslist = zhuturesaultsData['typewordlikeresaultslist']                
            zhutufnlist = zhuturesaultsData['fnlist']
            zhutufiletypelist = zhuturesaultsData['filetypelist']
            zhuturesaultsData['resaultPD'] = zhuturesaultPD
            zhutuFunctionIndex = zhuturesaultsData['functionIndex']

            # 海报图查询
            HBPoolNum = 14
            typeword = '海报图'
            typewordlikelist = ['海报']
            serverRootPath = '/mnt/imageshaibao'
            PcRootPath = '\\\\172.18.99.210\\6.模特图片库'
            HaiBaoGetInfoService = fs.fileInfoGetService(RedisPoolNum = HBPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            HaiBaoresaultsData = HaiBaoGetInfoService.resaultsfiledata()
            try:
                HaiBaoresaultPD = len(HaiBaoresaultsData['fileurllist'])
            except:
                HaiBaoresaultPD = 'OK Getch It'
            HaiBaofileindexlist = HaiBaoresaultsData['fileindexlist']
            HaiBaofileurllist = HaiBaoresaultsData['fileurllist']
            HaiBaotypewordlikeresaultslist = HaiBaoresaultsData['typewordlikeresaultslist']                 
            HaiBaofnlist = HaiBaoresaultsData['fnlist']
            HaiBaofiletypelist = HaiBaoresaultsData['filetypelist']
            HaiBaoresaultsData['resaultPD'] = HaiBaoresaultPD
            HaiBaoFunctionIndex = HaiBaoresaultsData['functionIndex']

            # 买家秀查询
            MJXPoolNum = 13
            typeword = '买家秀'
            typewordlikelist = ['买家秀']
            serverRootPath = '/mnt/imagesmaijiaxiu'
            PcRootPath = '\\\\172.18.99.211\\运营部'
            MJXGetInfoService = fs.fileInfoGetService(RedisPoolNum = MJXPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            MJXresaultsData = MJXGetInfoService.resaultsfiledata()
            try:
                MJXresaultPD = len(MJXresaultsData['fileurllist'])
            except:
                MJXresaultPD = 'OK Getch It'
            MJXfileindexlist = MJXresaultsData['fileindexlist']
            MJXfileurllist = MJXresaultsData['fileurllist']
            MJXtypewordlikeresaultslist = MJXresaultsData['typewordlikeresaultslist']                 
            MJXfnlist = MJXresaultsData['fnlist']
            MJXfiletypelist = MJXresaultsData['filetypelist']
            MJXresaultsData['resaultPD'] = MJXresaultPD
            MJXFunctionIndex = MJXresaultsData['functionIndex']

            # 品牌达人图查询
            PPDRTPoolNum = 12
            typeword = '达人图'
            typewordlikelist = ['IP联名传播素材']
            serverRootPath = '/mnt/imagespinpaidarentu'
            PcRootPath = '\\\\172.18.99.210\\自媒体（共享-线框）'
            PPDRTGetInfoService = fs.fileInfoGetService(RedisPoolNum = PPDRTPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            PPDRTresaultsData = PPDRTGetInfoService.resaultsfiledata()
            try:
                PPDRTresaultPD = len(PPDRTresaultsData['fileurllist'])
            except:
                PPDRTresaultPD = 'OK Getch It'
            PPDRTfileindexlist = PPDRTresaultsData['fileindexlist']
            PPDRTfileurllist = PPDRTresaultsData['fileurllist']
            PPDRTtypewordlikeresaultslist = PPDRTresaultsData['typewordlikeresaultslist']                 
            PPDRTfnlist = PPDRTresaultsData['fnlist']
            PPDRTfiletypelist = PPDRTresaultsData['filetypelist']
            PPDRTresaultsData['resaultPD'] = PPDRTresaultPD
            PPDRTFunctionIndex = PPDRTresaultsData['functionIndex']

            #  模特图
            MTPoolNum = 11
            typeword = '模特图'
            typewordlikelist = ['模特']
            serverRootPath = '/mnt/imageshaibao'
            PcRootPath = '\\\\172.18.99.210\\6.模特图片库'
            MTGetInfoService = fs.fileInfoGetService(RedisPoolNum = MTPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            MTresaultsData = MTGetInfoService.resaultsfiledata()
            try:
                MTresaultPD = len(MTresaultsData['fileurllist'])
            except:
                MTresaultPD = 'OK Getch It'
            MTfileindexlist = MTresaultsData['fileindexlist']
            MTfileurllist = MTresaultsData['fileurllist']
            MTtypewordlikeresaultslist = MTresaultsData['typewordlikeresaultslist']                 
            MTfnlist = MTresaultsData['fnlist']
            MTfiletypelist = MTresaultsData['filetypelist']
            MTresaultsData['resaultPD'] = MTresaultPD
            MTFunctionIndex = MTresaultsData['functionIndex']
            

            #  平铺图
            PingPuPoolNum = 11
            typeword = '平铺图'
            typewordlikelist = ['平铺']
            serverRootPath = '/mnt/imageshaibao'
            PcRootPath = '\\\\172.18.99.210\\6.模特图片库'
            PingPuGetInfoService = fs.fileInfoGetService(RedisPoolNum = PingPuPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            PingPuresaultsData = PingPuGetInfoService.resaultsfiledata()
            try:
                PingPuresaultPD = len(PingPuresaultsData['fileurllist'])
            except:
                PingPuresaultPD = 'OK Getch It'
            PingPufileindexlist = PingPuresaultsData['fileindexlist']
            PingPufileurllist = PingPuresaultsData['fileurllist']
            PingPutypewordlikeresaultslist = PingPuresaultsData['typewordlikeresaultslist']                 
            PingPufnlist = PingPuresaultsData['fnlist']
            PingPufiletypelist = PingPuresaultsData['filetypelist']
            PingPuresaultsData['resaultPD'] = PingPuresaultPD
            PingPuFunctionIndex = PingPuresaultsData['functionIndex']


            # 波次图查询
            BociPoolNum = 15
            typeword = '波次图'
            typewordlikelist = ['波','波次','波次图','月']
            serverRootPath = '/mnt/images'
            PcRootPath = '\\\\172.18.99.210\\分图'
            BociGetInfoService = fs.fileInfoGetService(RedisPoolNum = BociPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            BociresaultsData = BociGetInfoService.resaultsfiledata()
            try:
                BociresaultPD = len(BociresaultsData['fileurllist'])
            except:
                BociresaultPD = 'OK Getch It'
            Bocifileindexlist = BociresaultsData['fileindexlist']
            Bocifileurllist = BociresaultsData['fileurllist']
            Bocitypewordlikeresaultslist = BociresaultsData['typewordlikeresaultslist']                 
            Bocifnlist = BociresaultsData['fnlist']
            Bocifiletypelist = BociresaultsData['filetypelist']
            BociresaultsData['resaultPD'] = BociresaultPD
            BociFunctionIndex = BociresaultsData['functionIndex']

            # 外贸达人查询
            WMDRPoolNum = 9
            typeword = '外贸达人'
            typewordlikelist = ['外贸','SNS']
            serverRootPath = '/mnt/imagesmaijiaxiu'
            PcRootPath = '\\\\172.18.99.211\\运营部'
            WMDRGetInfoService = fs.fileInfoGetService(RedisPoolNum = WMDRPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            WMDRresaultsData = WMDRGetInfoService.resaultsfiledata()
            try:
                WMDRresaultPD = len(WMDRresaultsData['fileurllist'])
            except:
                WMDRresaultPD = 'OK Getch It'
            WMDRfileindexlist = WMDRresaultsData['fileindexlist']
            WMDRfileurllist = WMDRresaultsData['fileurllist']
            WMDRtypewordlikeresaultslist = WMDRresaultsData['typewordlikeresaultslist']                 
            WMDRfnlist = WMDRresaultsData['fnlist']
            WMDRfiletypelist = WMDRresaultsData['filetypelist']
            WMDRresaultsData['resaultPD'] = WMDRresaultPD
            WMDRFunctionIndex = WMDRresaultsData['functionIndex']

            # 其他照片查询
            OtherPoolNum = 8
            typeword = '照片'
            typewordlikelist = ['211backup','date']
            serverRootPath = '/mnt/imagesother'
            PcRootPath = '\\\\172.18.99.211\\SQLbak-temp'
            OtherGetInfoService = fs.fileInfoGetService(RedisPoolNum = OtherPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            OtherresaultsData = OtherGetInfoService.resaultsfiledata()
            try:
                OtherresaultPD = len(OtherresaultsData['fileurllist'])
            except:
                OtherresaultPD = 'OK Getch It'
            Otherfileindexlist = OtherresaultsData['fileindexlist']
            Otherfileurllist = OtherresaultsData['fileurllist']
            Othertypewordlikeresaultslist = OtherresaultsData['typewordlikeresaultslist']                 
            Otherfnlist = OtherresaultsData['fnlist']
            Otherfiletypelist = OtherresaultsData['filetypelist']
            OtherresaultsData['resaultPD'] = OtherresaultPD
            OtherFunctionIndex = OtherresaultsData['functionIndex']

            #  模特原片图
            MTYPPoolNum = 7
            typeword = '原片'
            typewordlikelist = ['原片']
            serverRootPath = '/mnt/imageshaibao'
            PcRootPath = '\\\\172.18.99.210\\6.模特图片库'
            MTYPGetInfoService = fs.fileInfoGetService(RedisPoolNum = MTYPPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            MTYPresaultsData = MTYPGetInfoService.resaultsfiledata()
            try:
                MTYPresaultPD = len(MTYPresaultsData['fileurllist'])
            except:
                MTYPresaultPD = 'OK Getch It'
            MTYPfileindexlist = MTYPresaultsData['fileindexlist']
            MTYPfileurllist = MTYPresaultsData['fileurllist']
            MTYPtypewordlikeresaultslist = MTYPresaultsData['typewordlikeresaultslist']                 
            MTYPfnlist = MTYPresaultsData['fnlist']
            MTYPfiletypelist = MTYPresaultsData['filetypelist']
            MTYPresaultsData['resaultPD'] = MTYPresaultPD
            MTYPFunctionIndex = MTYPresaultsData['functionIndex']

            #  实体照片
            STDPoolNum = 6
            typeword = '实体照片'
            typewordlikelist = ['实体设计素材','实体']
            serverRootPath = '/mnt/imagesshiti'
            PcRootPath = '\\\\172.18.99.210\\品牌部'
            STDGetInfoService = fs.fileInfoGetService(RedisPoolNum = STDPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            STDresaultsData = STDGetInfoService.resaultsfiledata()
            try:
                STDresaultPD = len(STDresaultsData['fileurllist'])
            except:
                STDresaultPD = 'OK Getch It'
            STDfileindexlist = STDresaultsData['fileindexlist']
            STDfileurllist = STDresaultsData['fileurllist']
            STDtypewordlikeresaultslist = STDresaultsData['typewordlikeresaultslist']                 
            STDfnlist = STDresaultsData['fnlist']
            STDfiletypelist = STDresaultsData['filetypelist']
            STDresaultsData['resaultPD'] = STDresaultPD
            STDFunctionIndex = STDresaultsData['functionIndex']

            # 周例会海报上新图片
            SXHBPoolNum = 5
            typeword = '上新海报'
            typewordlikelist = ['shangxinhaibao']
            serverRootPath = '/mnt/shangxinhaibao'
            PcRootPath = '\\\\172.18.99.210\\品牌部\\5.淘系上新设计\\上新开屏海报+周一例会海报\\周一例会海报'
            SXHBGetInfoService = fs.fileInfoGetService(RedisPoolNum = SXHBPoolNum, keyword = keyword, typeword = typeword,
                                                typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
            SXHBresaultsData = SXHBGetInfoService.resaultsfiledata()
            try:
                SXHBresaultPD = len(SXHBresaultsData['fileurllist'])
            except:
                SXHBresaultPD = 'OK Getch It'
            SXHBfileindexlist = SXHBresaultsData['fileindexlist']
            SXHBfileurllist = SXHBresaultsData['fileurllist']
            SXHBtypewordlikeresaultslist = SXHBresaultsData['typewordlikeresaultslist']                 
            SXHBfnlist = SXHBresaultsData['fnlist']
            SXHBfiletypelist = SXHBresaultsData['filetypelist']
            SXHBresaultsData['resaultPD'] = SXHBresaultPD
            SXHBFunctionIndex = SXHBresaultsData['functionIndex']

            # 建立JScript函数索引
            FunctionIndexSum = HaiBaoFunctionIndex + MJXFunctionIndex + PPDRTFunctionIndex + MTFunctionIndex + PingPuFunctionIndex + BociFunctionIndex + zhutuFunctionIndex + WMDRFunctionIndex + OtherFunctionIndex + MTYPFunctionIndex + STDFunctionIndex + SXHBFunctionIndex
            FunctionIndexSumList = []
            for FunctionIndex in range(1, FunctionIndexSum + 1):
                FunctionIndexSumList.append(FunctionIndex)
            print('FunctionIndexSumList', len(FunctionIndexSumList))
            Allfileindexlist = HaiBaofileindexlist + MJXfileindexlist + PPDRTfileindexlist + MTfileindexlist + PingPufileindexlist + Bocifileindexlist + zhutufileindexlist + WMDRfileindexlist + Otherfileindexlist + MTYPfileindexlist + STDfileindexlist + SXHBfileindexlist
            print('Allfileindexlist',len(Allfileindexlist))
            Allfileurllist = HaiBaofileurllist + MJXfileurllist + PPDRTfileurllist + MTfileurllist + PingPufileurllist + Bocifileurllist + zhutufileurllist +WMDRfileurllist + Otherfileurllist + MTYPfileurllist + STDfileurllist + SXHBfileurllist
            print('Allfileurllist',len(Allfileurllist))
            Alltypewordlikeresaultslist = HaiBaotypewordlikeresaultslist + MJXtypewordlikeresaultslist + PPDRTtypewordlikeresaultslist + MTtypewordlikeresaultslist + PingPutypewordlikeresaultslist + Bocitypewordlikeresaultslist + zhututypewordlikeresaultslist + WMDRtypewordlikeresaultslist + Othertypewordlikeresaultslist + MTYPtypewordlikeresaultslist + STDtypewordlikeresaultslist + SXHBtypewordlikeresaultslist
            print('Alltypewordlikeresaultslist',len(Alltypewordlikeresaultslist))
            Allfnlist = HaiBaofnlist + MJXfnlist + PPDRTfnlist + MTfnlist + PingPufnlist + Bocifnlist + zhutufnlist + WMDRfnlist + Otherfnlist + MTYPfnlist + STDfnlist + SXHBfnlist
            print('Allfnlist',len(Allfnlist))
            Allfiletypelist = HaiBaofiletypelist + MJXfiletypelist + PPDRTfiletypelist + MTfiletypelist + PingPufiletypelist + Bocifiletypelist + zhutufiletypelist + WMDRfiletypelist + Otherfiletypelist + MTYPfiletypelist + STDfiletypelist + SXHBfiletypelist
            print('Allfiletypelist',len(Allfiletypelist))
            filetypeSet = list(set(Allfiletypelist))
            print('filetypeSet',filetypeSet)

            AllData = zip(Allfileindexlist, Allfileurllist, Alltypewordlikeresaultslist, Allfnlist, Allfiletypelist, FunctionIndexSumList)
            if HaiBaoresaultPD == 0 and MJXresaultPD == 0 and PPDRTresaultPD == 0 and MTresaultPD == 0 and PingPuresaultPD == 0 and zhuturesaultPD == 0 and WMDRresaultPD == 0 and OtherresaultPD == 0 and MTYPresaultPD == 0 and STDresaultPD == 0 and SXHBresaultPD == 0:  # 后续用 and 关系加模特列表判断等等.....
                info = '未查询到 “{}” 相关的图片！'.format(keyword)
                Pic404 = "photo/img/404.png"
                infoData = {'info': info, 'resault': 0, 'Pic404': Pic404, 'keyword': keyword}
                return render(request, 'photo/showserchfileinfo.html', infoData )
            else:
                # AllData = [HaiBaoresaultsData, MJXresaultsData, PPDRTresaultsData, MTresaultsData,  PingPuresaultsData]
                # serchfileinfoData = {'AllData': AllData, 'FunctionIndexSumList': FunctionIndexSumList}
                serchfileinfoData = {'AllData': AllData, 'keyword': keyword, 'filetypeSet':filetypeSet}
                keys=['fileindex','fileurl','filename','fn','filetype','functionindex']
                AllDataLi = list(zip(Allfileindexlist, Allfileurllist, Alltypewordlikeresaultslist, Allfnlist, Allfiletypelist, FunctionIndexSumList))
                list_json=[dict(zip(keys,item)) for item in AllDataLi]   # zip类型 转为可json化的列表格式
                str_json=json.dumps(list_json,indent=2, ensure_ascii=False)  # 将列表化后的zip类型转为json格式
                # print(str_json)
                serchfileinfoDataJson = {"AllData": str_json, "keyword": keyword, "filetypeSet":filetypeSet}   # 打包成json串，在下一步存入session中
                request.session['serchfileinfoDataJson'] = serchfileinfoDataJson
                # print(serchfileinfoData)
                # print(request.session['serchfileinfoDataJson'])
                return render(request, 'photo/showserchfileinfo.html', serchfileinfoData )
        

def searchSXHB(request):  #查询上新海报系列二维码链接
    haibaoSearchName = request.GET.get('haibao_name')
    print(haibaoSearchName)
    if request.method == "GET":
        getsearchSXHB = getSXHB( haibaoSearchName )
        getsearchSXHBData = { 'AllData': getsearchSXHB }
        try:
            return render(request, 'photo/showsearchhaibao.html', getsearchSXHBData)
        except:
            pass


def getSXHB(haibao_name):  #查询上新海报海报内容数据
    haibao_name = haibao_name
    SXHBPoolNum = 5
    typeword = '上新海报'
    typewordlikelist = ['shangxinhaibao']
    serverRootPath = '/mnt/shangxinhaibao'
    PcRootPath = '\\\\172.18.99.210\\品牌部\\5.淘系上新设计\\上新开屏海报+周一例会海报\\周一例会海报'
    SXHBGetInfoService = fs.fileInfoGetService(RedisPoolNum = SXHBPoolNum, keyword = haibao_name, typeword = typeword,
                                        typewordlikelist = typewordlikelist, serverRootPath = serverRootPath, PcRootPath = PcRootPath)
    SXHBresaultsData = SXHBGetInfoService.resaultsfiledata()
    try:
        SXHBresaultPD = len(SXHBresaultsData['fileurllist'])
    except:
        SXHBresaultPD = 'OK Getch It'
    SXHBfileindexlist = SXHBresaultsData['fileindexlist']
    SXHBfileurllist = SXHBresaultsData['fileurllist']
    SXHBtypewordlikeresaultslist = SXHBresaultsData['typewordlikeresaultslist']                 
    SXHBfnlist = SXHBresaultsData['fnlist']
    SXHBfiletypelist = SXHBresaultsData['filetypelist']
    SXHBresaultsData['resaultPD'] = SXHBresaultPD
    SXHBFunctionIndex = SXHBresaultsData['functionIndex']
    FunctionIndexSum = SXHBFunctionIndex
    FunctionIndexSumList = []
    for FunctionIndex in range(1, FunctionIndexSum + 1):
        FunctionIndexSumList.append(FunctionIndex)
    print('FunctionIndexSumList', len(FunctionIndexSumList))
    Allfileindexlist = SXHBfileindexlist
    print('Allfileindexlist',len(Allfileindexlist))
    Allfileurllist = SXHBfileurllist
    print('Allfileurllist',len(Allfileurllist))
    Alltypewordlikeresaultslist = SXHBtypewordlikeresaultslist
    print('Alltypewordlikeresaultslist',len(Alltypewordlikeresaultslist))
    Allfnlist = SXHBfnlist
    print('Allfnlist',len(Allfnlist))
    Allfiletypelist = SXHBfiletypelist
    print('Allfiletypelist',len(Allfiletypelist))
    filetypeSet = list(set(Allfiletypelist))
    print('filetypeSet',filetypeSet)
    AllData = zip(Allfileindexlist, Allfileurllist, Alltypewordlikeresaultslist, Allfnlist, Allfiletypelist, FunctionIndexSumList)
    return AllData

def selectfiletype(request):
    if request.method == "POST":
        selfiletype = request.POST.get('selectfiletype')
        # print(selfiletype)
        serchfileinfoDataJson = request.session['serchfileinfoDataJson']
        # print(serchfileinfoDataJson['AllData'])
        AllDataJsonLoads = json.loads(serchfileinfoDataJson['AllData'])
        selectfileData = []
        # print(AllDataJsonLoads) selectfiletypeinfo.html
        for i in range(0, len(AllDataJsonLoads), 1):
            filetype = AllDataJsonLoads[i]['filetype']
            if filetype == selfiletype:
                selectfileData.append(AllDataJsonLoads[i])
        print(selectfileData)
        keyword = serchfileinfoDataJson['keyword']
        filetypeSet = serchfileinfoDataJson['filetypeSet']
        selectfiletypeData = {'selectfileData': selectfileData, 'keyword': keyword, 'filetypeSet':filetypeSet}
        return render(request, 'photo/selectfiletypeinfo.html', selectfiletypeData )