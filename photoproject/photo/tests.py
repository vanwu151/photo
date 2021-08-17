from django.test import TestCase
import os, re, time, json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage

# Create your test here.

# fileindexlist = []
# for i in range(1, 5+1):
#     fileindexlist.append(i)
# print(fileindexlist)

# def searchfile(request):
#     if request.method == "GET":
#         return render(request, 'photo/searchfile.html')


# def serchfileinfo(request):
#     if request.method == "POST":
#         kewWord = request.POST.get('search')
#         print(kewWord)
#         filetype = '波次图'
#         fileindex = [1,2,3,4,5]
#         # fileurl = ["\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00560.jpg","\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00590.JPG",
#         # "\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00602.JPG","\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00620.JPG",
#         # "\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00695.JPG" ]
#         fileurl = ["\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00560.jpg","\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00590.JPG",
#         "\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00602.JPG","\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00620.JPG",
#         "\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00695.JPG" ]
#         filenamelist = ["\\\\172.18.99.210\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00560.jpg","\\\\172.18.99.210\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00590.JPG",
#         "\\\\172.18.99.210\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00602.JPG","\\\\172.18.99.210\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00620.JPG",
#         "\\\\172.18.99.210\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋00695.JPG" ]
#         filenames = ['7.7妖精的口袋00560.jpg','7.7妖精的口袋00590.JPG','7.7妖精的口袋00602.JPG','7.7妖精的口袋00620.JPG','7.7妖精的口袋00695.JPG']
#         fileinfolistBC = zip( fileindex, fileurl, filenamelist, filenames)
#         BCdata = {'filetype': filetype, 'fileinfolist':fileinfolistBC}

#         filetype = '模特图'
#         fileindex = [1,2,3,4,5]
#         fileurl = ["\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋01336.jpg","\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋01478.JPG",
#         "\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋01491.JPG","\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋01631.JPG",
#         "\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋01671.JPG" ]
#         filenamelist = ["\\\\172.18.99.210\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋01336.jpg","\\\\172.18.99.210\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋01478.JPG",
#         "\\\\172.18.99.210\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋01491.JPG","\\\\172.18.99.210\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋01631.JPG",
#         "\\\\172.18.99.210\\分图\\ES\\2021\\7月\\7.4\\11205390-2T恤\\7.7妖精的口袋01671.JPG" ]
#         filenames = ['7.7妖精的口袋01336.jpg','7.7妖精的口袋01478.JPG','7.7妖精的口袋01491.JPG','7.7妖精的口袋01631.JPG','7.7妖精的口袋01671.JPG']
#         fileinfolistMT = zip(fileindex, fileurl, filenamelist, filenames)
#         MTdata = {'filetype': filetype, 'fileinfolist':fileinfolistMT} 
#         # filetypelist = [filetypeBC, filetypeMT]
#         AllData =[BCdata, MTdata]
#         serchfileinfoData = {'AllData': AllData}
#         print(serchfileinfoData)
#         return render(request, 'photo/showserchfileinfo.html', serchfileinfoData )

# def serchfileinfo(request):
#     if request.method == "POST":
#         kewWord = request.POST.get('search')
# Create your tests here.
# s = '\\172.18.99.210\分图\ES\2021\7月\7.1波 11200420-2连衣裙\删\9.7.2021-dx08333.jpg'
# p0 = re.compile(r'~\$|\.db$|\.ini$|删')
# b0 = p0.findall(s)
# print(b0[0])
a= []
b = ['b', 'c']
c = [1,2]
d = [32,12]
p = [9,0]
q = [7,8]
# for i in range(1,60,1):
#     a.append(i)
# print(a+b)
l = zip(c ,d)
m = zip(p , q)
s = list(l) + list(m)
l2 = [1 ,2 ,3 ,4]
print(s)
print(zip(*l))
l3 = zip(s,l2)
for i in zip(*m):
    print(i)
