###### Description:

python爬虫，获取糗百8小时热门动态,使用scrapy框架，快速抓取糗百短文、发布者、阅读数、，生成csv文件。


###### 用法：

配置生成文件的地址：settings.py 文件下

     FEED_URI=u'file:///D://qiubai-hot.csv'
     FEED_FORMAT='CSV'
    
下载源代码，根目录下直接运行` scrapy crawl Qiubai `

D盘根目录生成 qiubai-hot.csv 文件，大概2400条数据...
