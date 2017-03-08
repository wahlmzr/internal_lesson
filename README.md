# internal_lesson
这是内部分享材料，由于公司内部网络的限制，很多东西无法在Internet上分享，故在此建项目，希望大家可以找到自己的快乐。  

所有材料请扫这里
<img src="./我的github.jpg" width = "300" height = "200" alt="图片名称" align=center />


> 国内的blog关于selenium写得很少，虫师算是比较好的一位了，大家可以去拜访一下他的博客，觉得麻烦可以买一本看看。

言归正传，怎么布置Windows下的selenium环境。
大致步骤如下：
1. python环境 推荐anaconda环境  
2. 安装selenium  
3. 安装firefox  
4. 设置path  
5. geckodriver for firefox  
6. test  


------  

1. python环境，anaconda，一步步next就可以了（记得勾选path的选项）  
2. 联网环境可以运行cmd，到命令行界面后运行  
   pip install selenium  
   即可  
   在内网，可以下载selenium_xx.rar ,解压后命令行cd到这个文件夹，运行  
   python setup.py install   
   最后可以看到selenium install successfully字样  
3. firefox，这个不用说了，一步步next就可以了  
4. 将firefox的路径，一般都是 C:\Users\user\AppData\Local\Mozilla Firefox  （user为自己用户的名字）  
   之后将这个复制后，打开我的电脑邮件属性，高级系统设置，环境变量，找到path ，在变量值最后添加 分号（英文的），将复制的值写入最后。 或者在自己的用户上新建path，将路径复制到变量值。  
5. 下载geckodriver驱动  
   内网中可以从本人或栗子的firefox路径中找到后复制到自己的firefox文件夹中。  
   
