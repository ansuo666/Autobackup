import backup
import time
def yunxing():
    start = time.strftime('%Y%m%d')
    endtime = time.strftime('%Y%m%d')
    n = 1
    i = 0
    p = [r'',r'']
    for re in open('backupconfig.txt','r+'):
        p[i] = re
        i += 1
    p1 = p[0]
    p2 = p[1]
    p1 = p1.strip()
    p2 = p2.strip()
    while n:
        dd = int(endtime) - int(start)
        if dd == 1:
            try:
                backup.backup(p1,p2)
                start = endtime
                endtime = time.strftime('%Y%m%d')
                jieguo()
            except:
                result = '备份出错！请检查路径是否有误！'
                return result
        else:
            endtime = time.strftime('%Y%m%d')
def jieguo():
    result = '备份完成！'
    return result