# the basic settings about the host
BASE = {
    'host': 'localhost',
    'port': 1121,
    'headers': {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 "
            "Safari/537.36 "
    }
}

# the settings about MongoDB database
DATABASE = {
    'host': 'localhost',
    'port': 27017,
    'database': 'AppCrawler'
}

# the settings about the target market sites
TARGET = {
    'tencent': {
        'url': 'https://sj.qq.com/myapp/',
        'core': 'sj.qq.com/myapp'
    },
    '360': {
        'url': 'http://zhushou.360.cn/',
        'core': 'zhushou.360.cn'
    },
    'mi': {
        'url': 'http://app.mi.com/',
        'core': 'app.mi.com'
    }
}
