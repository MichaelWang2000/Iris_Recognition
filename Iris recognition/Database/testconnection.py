import pymysql

def getDatabase():
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='wjy594792846',
                        database='IrisRecognition',
                        charset='utf8')
    return db

