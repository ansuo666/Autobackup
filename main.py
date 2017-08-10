import time
import backup
import os
start = time.strftime('%Y%m%d')
endtime = time.strftime('%Y%m%d')
n = 1
i = 0
p = [r'',r'']
if not os.path.exists('backupconfig.txt'):
    wj = open('backupconfig.txt','w+')
    wj.write(r'c:\data')
    wj.write('\n')
    wj.write(r'z:\backup')
    wj.close()
else:
    for re in open('backupconfig.txt','r+'):
        p[i] = re
        i += 1
p1 = p[0]
p2 = p[1]
p1 = p1.strip()
p2 = p2.strip()
print('程序初始化中...\n')
print('程序已经启动！\n')
print('当前日期为：' + start)
while n:
    dd = int(endtime) - int(start)
    if dd == 1:
        try:
            result = backup.backup(p1,p2)
            start = endtime
            endtime = time.strftime('%Y%m%d')
            print(result)
        except:
            print('自动备份错误，请检查备份路径是否已经改变！')
    else:
        endtime = time.strftime('%Y%m%d')