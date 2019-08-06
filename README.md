# Gensis.py 开发及使用文档
A distributed crawler framework for Steam

# 介绍

### Gensis.py是什么

Gensis(读音/dʒɛn’sis/)是一套用于爬取Steam上所有合法数据的分布式爬虫框架。与市面上其他的Steam数据获取的框架和程式不同的是，Gensis被设计为Master-Worker形式，由主节点负责分发任务和任意数量的子节点抓取任务执行。不仅易于使用，还给予了用户抓取Steam上巨型大数据的能力，并且便于进行任意功能的扩展。Gensis完全能够满足游戏公司对于Steam上任意类型和数量的公开数据进行抓取和大数据分析的需求。

### 起步 - 安装

安装Gensis.py不需要耗费太多的精力，只需要简单的访问其Github界面
https://github.com/Ramonywangziyao/Gensis.py

在安装Gensis.py前：

如您的电脑未安装Git，在使用Gensis.py前请移步https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
来安装Git工具及库，也可选择安装Github Desktop桌面应用方便管理
https://desktop.github.com/

如您的电脑未安装Python, 在使用Gensis.py前请移步
https://www.python.org/downloads/
下载最新版本的Python（推荐使用Python3）

如您身在中国，您或许需要一个VPN来使用Gensis.py（因为Steam的部分功能在中国受到访问限制）

如只需爬取万级以下的数据，则可直接使用Gensis.py。如您需爬取大量数据，您或许需要一个IP轮换软件来防止单一IP访问过度被禁止的反爬虫情况。因为Gensis.py面向企业或组织级使用，本机的IP轮换功能的IP数量和可用性都受到限制和重复的影响，所以不提供该功能，推荐使用MyIpHide
https://myiphide.com/
来进行搭配使用

在安装好所需的所有内容后：

使用以下三种方式进行安装1.（推荐）导航到您想下载Gensis.py的文件夹，在Windows的CMD命令提示符界面或Mac OS的Terminal下输入

git clone https://github.com/Ramonywangziyao/Gensis.py.git

2.下载Gensis.py Github界面的Zip打包文件到本地，并解压

3. 点击界面上的Open in Desktop进行下载（如已安装Github Desktop桌面应用）

！官方指南假设您已经了解Python，分布式编程和多线程编程。如果您刚开始学习Python或者编程，建议您先阅读有关数据结构，分布式应用，线程以及爬虫等相关基础知识再来使用本框架。


### 起步 - 框架结构

Gensis.py是整个框架的总称，在其内部拥有Gensis-Master和Gensis-Worker两个相对独立的程式。Gensis-Master为主节点，用于执行指定的服务，负责监听用于接收子节点结果的端口，启动分发/接受/分析/储存数据的通道以及主节点所用的爬虫管理和启动。而Gensis-Worker在执行对应的服务后，则负责从主节点所映射的任务池里抓取任务，在完成后负责把结果上传到结果池，以供主节点进行进一步分析和其他动作。对于主节点和子节点的详解请查看组件部分的主/子节点对应段落。

# 起步 - 运行

Gensis.py的运行十分的简单，无论是主节点还是子节点，都可在Windows的CMD命令提示符或Mac OS的Terminal输入以下指令执行：

python x.py servicename ip port   

Servicename：您想执行的已开发的服务的指定名称，具体内容将在‘添加一个新服务’部分进行详解。但是请注意，Servicename是必须输入的一个执行参数。如果不输入该执行参数或输入了错误或不存在的服务名称，将导致Gensis无法执行。您必须选用一个服务来执行Gensis。

IP：您主节点运行的本机IP。如子节点是运行在您的局域网内，则可输入您主机的局域网内IP地址，如果子节点是运行在外网，则需输入您的外网IP地址。

PORT：您主节点运行的本机端口。一般是在XXXX-XXXX之间。

对于主节点，执行程序名为
Gensis.py

对于子节点，执行程序名为
GensisWorker.py

以上程序名用于替换执行指令中的x.py。
在使用Gensis时，如需使用分布式功能，可将子节点程序可复制到多台主机，在指定好主节点的IP地址以及端口后独立运行。

参考运行实例：
主节点
python Gensis.py serviceName

子节点
python GensisWorker.py serviceName

以上两个服务的具体使用流程将其对应板块进行详解。

### 起步 - 组件

#### 通用组件

Constants：该组件为枚举组件。在Gensis中所需要的任何枚举值都存在于该组件所包含的类中。目前包含了以下枚举类
ServiceNames.py：用于枚举所有的服务名称
DataKeyNames.py：用于枚举所有接口字典类所需要用到键值（Key）

Interfaces：该组件为接口组件。在Gensis中对于分析，日志，爬虫组件的统一接口都存在于该组件中，来规定新添加服务所对应组件必须实现的方程（Function）。目前包含了以下接口
	AnalyzerInterface.py： 分析类需继承的接口
	LoggerInterface.py：日志类需继承的接口
	SpiderInterface.py：爬虫类需继承的接口

Managers：该组件为管理组件。Gensis的各项功能是由不同的服务所引导的。每一个服务都包含了不同的爬虫类，日志类，分析类等。而管理组件的作用是作为中间件，用于根据所选择的服务动态的创建该服务所需要的功能类，并且根据该功能所需进行配置，运行。目前包含了以下管理类
GensisManager.py：	Gensis的核心管理类，用于配置主节点IP地址，端口，认证密钥，数据流                                                        操作通道的包的发布和管理还有上一次的断点数据的读取。由外部主程序Gensis.py进行启动。
AnalyzeManager.py：分析类的管理类，用于抽象分析的具体操作，根据服务动态的创建具体服务对应的分析类，并且命令执行。
	DataManager.py：数据储存类的管理类，用于抽象数据储存的具体操作，根据服务动态的创建具体服务对应的数据储存类，并命令其跟数据库进行交互。
	LogManager.py：日志类的管理类，用于抽象日志的具体操作，根据服务动态的创建具体服务对应的日志类，并命令其进行日志的读写操作。
	PackageManager.py：包裹类的管理类，用于抽象包的具体操作，负责维护新建包的列队和旧包的记录，对包进行储存，检查，删除。
	SpiderManager.py：爬虫类的管理类，用于抽象爬虫的具体操作，根据服务动态的创建对应的爬虫类，并对其进行配置，执行。
	StatManager.py：统计工具类的管理类，用于根据服务动态的分发统计工具类。

Packages:：该组件为包组件。Gensis分布式功能得力于自定义包的使用。一个包指的是主节点分发给子节点的一个任务或子节点上传至主节点的结果的抽象，其中包括了url, ID等子节点进行任务所需的或子节点完成任务后封装过的数据和信息。 

Tools：该组件为工具组件，其包括了一切Gensis需要用到的辅助工具，如以下现有工具
	PackageFactory.py：包的工厂。用于根据不同的服务，动态的生产所需要的包。

#### 主节点组件

Spiders：该组件为主节点的爬虫组件，其只会在主节点运行时全局的运行一次（内部可进行翻页，循环等），根据您的自定义为导向来获取对应的数据或信息。如需配合子节点分布式的使用，则需其他组件的配合，会在稍后为您讲解。
Analyzers：该组件为主节点的分析组件，其主要负责对爬取数据或信息的分析，包括对统计工具的使用。
Loggers：该组件为主节点的日志组件，其主要负责对爬取数据或信息的日志导出或读取。
StatTools：该组件为主节点的统计工具组件，其主要负责在分析组件中进行统计相关的计算任务。
Tools：该组件为主节点的工具组件，其包括了一切主节点需要用到的共有工具和私有辅助工具，包括以下私有工具
	DataWrapper.py：数据封装类，用于对Gensis内对内，内对外的一切数据流进行差别化的封装，形成统一数据接口。

#### 子节点组件

Spiders：该组件为子节点的爬虫组件。该爬虫组件需服务于主节点所发布的任务，在功能上进行对应，根据您的自定义为导向来获取对应的数据或信息。
Managers：该组件为子节点的管理组件，包含了子节点所需的共有和私有的管理中间件，如以下私有管理类
	GensisWorkerManager.py：子节点的核心管理类，负责建立于主节点的连接，并且与之进行通讯。同时负责维护数据流的任务和结果的双向通道的映射。
	PackageManager.py：子节点的包的管理类，负责包的下载和上传任务。
Tools：该组件为子节点的工具组件，其包括了一切子节点需要用到的共有工具和私有辅助工具。
	


### 准备好了吗？
相信到目前为止，您已经对Gensis的所有组件有所了解。那么接下来我们将进入开发的环节，一起探索如何使用Gensis框架来扩展出能满足您对Steam数据各种需求的服务。您准备好了吗？

# 开发

### 添加一个新的服务
在Gensis中，一个服务（Service）意味着一个您所期望的功能模块。一个服务中通常包含了以下主要组件：
Spider
Package
Analyzer
Logger
StatTool

首先您要做的是在枚举类Constants组件中的ServiceTypeNames.py内定义您所想要添加的服务：
'''python
serviceName = 'newService'
'''
这一步可以让您给您想要添加的功能起一个统一的名称来全局调用。同时在启动Gensis.py的时候，您需要将引号内的名称作为启动参数填入：
Python Gensis.py newService
否则Gensis.py将无法运行。所以请确保启动时输入的名称与在该枚举类内输入的名称一致。

### 添加一个新的爬虫组件
爬虫组件为一项服务的主要组件，所有其他的组件都是围绕起爬虫组件来执行的。
首先，在Managers组件中的SpiderManager.py的crwal()方法内定义一个执行入口
'''python
if self.service == self.serviceConstants.newServiceName:
  return self.runNewSpider()
'''
该入口确保了SpiderManager.py能够根据您所指向的服务来执行对应的爬虫。

其次，在Spiders组件中添加一个您自定义的Spider类。该类应该继承SpiderInterface这个接口，并且实现其中的方法。而Spider类返回值的格式，将由开发者自行定义。

### 添加一个新的包裹
一个包裹指的是在使用Gensis分布式功能的时候，主节点发布的任务包裹和子节点在完成任务后所上传的结果包裹。包裹的形式完全由开发者在Packages组件中自行定义，并且进行封装。通常一个任务包裹包含了以下几个属性：
Status：包裹的状态
URL：包裹所包含的单个URL
Flag：包裹所需要执行相关任务的标记
Others：其他自定义属性

一个结果包裹包含了以下几个属性：
Status：包裹的状态
Content：子节点抓取的结果，可以是数据，也可以是一个新的URL或者URLSET
Others：其他自定义属性

在Package组件中定义后，还需要在Tools组件中的PackageFactory.py内添加两个包裹的生产情况：
在producePacakge()方法内添加
'''python
if service == self.serviceConstants.newService:
  return newPackage()
'''
来新增一个创建新任务包裹的方法

在regeneratePackageFromResultPackage()方法内添加
'''python
if service == self.serviceConstants.newService:
  return newPackage(resultPackage)
'''
来新增一个从结果包裹创建任务包裹的方法

### 添加一个新服务的数据分析组件

### 添加一个新服务的日志管理组件

### 添加一个新的接口

### 添加一个新的统计工具

### 分布化 - 添加子节点


# 更多

### 对比其他Steam数据获取框架
#### Steam DB

# 加入Gensis开发社区

# 认识开发者

Gensis的研发出自于重庆帕斯亚科技有限公司的团队。这里展示其主要研发者信息

Ziyao Wang
Creator @ Gensis.py
Location: New York, NY, USA
Language: 中文 - English
Blog: https://www.ziyaowang.com/
Github: https://github.com/Ramonywangziyao
Email: zw593@nyu.edu



