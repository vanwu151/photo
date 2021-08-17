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
            typewordlikelist = ['波','波次','波次图']
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

            # 建立JScript函数索引
            FunctionIndexSum = HaiBaoFunctionIndex + MJXFunctionIndex + PPDRTFunctionIndex + MTFunctionIndex + PingPuFunctionIndex + BociFunctionIndex + zhutuFunctionIndex + WMDRFunctionIndex
            FunctionIndexSumList = []
            for FunctionIndex in range(1, FunctionIndexSum + 1):
                FunctionIndexSumList.append(FunctionIndex)
            print('FunctionIndexSumList', len(FunctionIndexSumList))
            Allfileindexlist = HaiBaofileindexlist + MJXfileindexlist + PPDRTfileindexlist + MTfileindexlist + PingPufileindexlist + Bocifileindexlist + zhutufileindexlist + WMDRfileindexlist
            print('Allfileindexlist',len(Allfileindexlist))
            Allfileurllist = HaiBaofileurllist + MJXfileurllist + PPDRTfileurllist + MTfileurllist + PingPufileurllist + Bocifileurllist + zhutufileurllist +WMDRfileurllist
            print('Allfileurllist',len(Allfileurllist))
            Alltypewordlikeresaultslist = HaiBaotypewordlikeresaultslist + MJXtypewordlikeresaultslist + PPDRTtypewordlikeresaultslist + MTtypewordlikeresaultslist + PingPutypewordlikeresaultslist + Bocitypewordlikeresaultslist + zhututypewordlikeresaultslist + WMDRtypewordlikeresaultslist
            print('Alltypewordlikeresaultslist',len(Alltypewordlikeresaultslist))
            Allfnlist = HaiBaofnlist + MJXfnlist + PPDRTfnlist + MTfnlist + PingPufnlist + Bocifnlist + zhutufnlist + WMDRfnlist
            print('Allfnlist',len(Allfnlist))
            Allfiletypelist = HaiBaofiletypelist + MJXfiletypelist + PPDRTfiletypelist + MTfiletypelist + PingPufiletypelist + Bocifiletypelist + zhutufiletypelist + WMDRfiletypelist
            print('Allfiletypelist',len(Allfiletypelist))
            filetypeSet = list(set(Allfiletypelist))
            print('filetypeSet',filetypeSet)

            AllData = zip(Allfileindexlist, Allfileurllist, Alltypewordlikeresaultslist, Allfnlist, Allfiletypelist, FunctionIndexSumList)
            if HaiBaoresaultPD == 0 and MJXresaultPD == 0 and PPDRTresaultPD == 0 and MTresaultPD == 0 and PingPuresaultPD == 0 and zhuturesaultPD == 0 and WMDRresaultPD == 0:  # 后续用 and 关系加模特列表判断等等.....
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