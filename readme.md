# QQ头像获取器

## 背景

一天某推销员加我来推销游戏，因为对面是企业账号的原因，无法查看其头像，故作此程序

## 使用

使用前请确保您配置好Python环境

点击`QQImgGet.py`即可开始使用

注意:

本程序拥有GUI界面，GUI使用库`PySimpleGUI`，您需要安装此库来使用GUI模式:

```powershell
pip install PySimpleGUI
```

当然您也选择不安装，我们也准备了无GUI模式，若您没有此库则会切换到无GUI模式

本程序拥有自动下载图片的功能，需要安装库`requests`才可使用：

```powershell
pip install requests
```

当然您也选择不安装，我们也准备了离线模式，若您没有此库则会切换到离线模式，需要您自行使用链接下载

## 输出

本程序一共输出两个版本的图片:

140x140: 兼容模式，适用于全部用户

640x640: 高清模式，对企业用户不适用

## 后话

本仓库遵守`Apache License 2.0`协议，未经允许不可转载

WhitemuTeam