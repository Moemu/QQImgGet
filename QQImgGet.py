import os
import sys

download = 0

#GUI模式（PySimpleGUI）
def guimode():
    import PySimpleGUI as sg
    
    layout=[[sg.Text('请输入QQ号')],
        [sg.Input()],
        [sg.Button('提交')]]
    
    event, value = sg.Window('QQ头像获取', layout, icon=r'LOGO.ico').read()
    qq = value[0]

    img1 = 'https://q1.qlogo.cn/g?b=qq&nk='+qq+'&s=4'
    img2 = 'https://q1.qlogo.cn/g?b=qq&nk='+qq+'&s=5'

    if download==0:
        doc=open('download.txt','w')
        print('140x140: ',img1,file=doc)
        print('640x640:',img2,file=doc)
        doc.close()
        sg.popup('已在程序根目录存放download.txt，请前往查阅')
    if download==1:
        import requests
        img = requests.get(img1)
        open('140x140.jpg', 'wb').write(img.content)
        img = requests.get(img2)
        open('640x640.jpg', 'wb').write(img.content)
        sg.popup('已成功下载，请查看程序目录~', icon=r'LOGO.ico')

#无GUI模式
def cmdmode():
    print('已为您切换到无GUI模式')
    qq=input('请输入QQ号')
    img1 = 'https://q1.qlogo.cn/g?b=qq&nk='+qq+'&s=4'
    img2 = 'https://q1.qlogo.cn/g?b=qq&nk='+qq+'&s=5'
    if download==0:
        doc=open('download.txt','w')
        print('140x140: ',img1,file=doc)
        print('640x640:',img2,file=doc)
        doc.close()
        print('已在程序根目录存放download.txt，请前往查阅')
        input('按任意键退出')
        sys.exit()
    if download==1:
        import requests
        img = requests.get(img1)
        open('140x140.jpg', 'wb').write(img.content)
        img = requests.get(img2)
        open('640x640.jpg', 'wb').write(img.content)
        input('下载完成，头像在程序根目录中,按任意键退出~')

#判断PysimpleGUI是否存在
all = os.popen('pip list').read()
if 'PySimpleGUI' in all: #Temp
    print('PysimpleGUI已安装')
    #判断requests是否存在
    all = os.popen('pip list').read()
    if 'requests' in all:
        download = 1
    else:
        print('requests未检查到')
        print('您可能需要在控制台执行pip install requests以获得较高体验')
        print('当然您也可以选择继续运行，但需要您自行复制下载链接')
        con = input('要继续吗？(Y/N)')
        if con=='Y' or 'y':
            download = 0
        else:
            sys.exit()
    guimode() #切换到GUI模式
else:
    print('PysimpleGUI未检查到')
    #判断requests是否存在
    all = os.popen('pip list').read()
    if 'requests' in all:
        download = 1
    else:
        print('requests未检查到')
        print('您可能需要在控制台执行pip install requests以获得较高体验')
        print('当然您也可以选择继续运行，但需要您自行复制下载链接')
        con = input('要继续吗？(Y/N)')
    cmdmode() #切换到CMD模式