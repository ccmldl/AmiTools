## 数据库中使用Zlog表
需要在创建Model的时候加上 `__table_args__ = {'implicit_returning':False}`

## 使用方法
```python
pip install amitools

ami = AmiTools(LogDir="./log", ConnString="", Host="127.0.0.1", PassWord="", Port=6379, db=10)  # 参数不用全填
logger = ami.loggers
logger.info("start session")
session = ami.initSession()
logger.info("start redis")
rs = ami.initRedis()
```