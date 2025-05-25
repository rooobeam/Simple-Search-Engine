import pickle
import re
from django.shortcuts import render
from firstWEB import cal_p_multi


# Create your views here.


def start(request):
    return render(request, 'start.html')


def cal(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']
    result = int(num1) + int(num2)
    return render(request, 'back.html', context={'data': result})


def search(request):
    return render(request, 'index.html')


def service(request):
    query = request.POST['query']

    content, acc, prec, recal, f1_s = cal_p_multi.func(query)

    paths = []
    pattern = re.compile(r'(N\d{2}[^.]+?)(?=\.pkl)')
    for i in content[0]:
        match = pattern.search(i)
        if match:
            paths.append(match.group(0))

    for i in range(len(paths)):
        paths[i] = r"D:\PyProject\STNO-UNICODE\\" + paths[i] + r".txt"

    text = [''] * 20
    title = [''] * 20

    for i in range(len(paths)):
        if i > 19:  # 页面最多显示20篇
            break
        with open(paths[i], 'r', encoding='utf-8') as file:  # 'r' 表示读取模式，'utf-8' 是文件的编码方式
            text[i] = file.read()
        lines = text[i].split("\n")
        if lines[0] == '\ufeff':
            title[i] = (lines[1])
        else:
            title[i] = (lines[0])

    context = {'query': query,
               'acc': acc,
               'prec': prec,
               'recal': recal,
               'f1_s': f1_s,
               't1': title[0], 'c1': text[0],
               't2': title[1], 'c2': text[1],
               't3': title[2], 'c3': text[2],
               't4': title[3], 'c4': text[3],
               't5': title[4], 'c5': text[4],
               't6': title[5], 'c6': text[5],
               't7': title[6], 'c7': text[6],
               't8': title[7], 'c8': text[7],
               't9': title[8], 'c9': text[8],
               't10': title[9], 'c10': text[9],
               't11': title[10], 'c11': text[10],
               't12': title[11], 'c12': text[11],
               't13': title[12], 'c13': text[12],
               't14': title[13], 'c14': text[13],
               't15': title[14], 'c15': text[14],
               't16': title[15], 'c16': text[15],
               't17': title[16], 'c17': text[16],
               't18': title[17], 'c18': text[17],
               't19': title[18], 'c19': text[18],
               't20': title[19], 'c20': text[19],
               }

    return render(request, 'service.html', context)
