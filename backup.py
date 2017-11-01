import os
import time
import tarfile
import sys
def backup(p1,p2):
    path1 = p1
    path2 = p2
    sourse = [path1]
    target_dir = path2
    today = target_dir + time.strftime('%Y%m%d') #备份文件路径+年月日
    now = time.strftime('%H%M%S')
    comment = ''
    if len(comment) == 0:
        target = today + os.sep + now + '.tar.gz' # os.sep为系统分隔符，此处为备份文件后文件路径和文件名
    else:
        target = today + os.sep + now + \
            comment.replace(' ','_') + '.tar.gz'
    if not os.path.exists(today):
        os.mkdir(today)
    try:
        start = time.time()
        tar = tarfile.open(target,'w:gz')#创建备份文件
        for root,dir,files in os.walk(sourse[0]):#检索要备份的文件夹下的所有文件
            for file in files:
                full = os.path.join(root,file)
                tar.add(full)#添加到备份文件中
        tar.close()#关闭备份文件
        endtime = time.time() - start
        if endtime > 60:#调试信息，正式运行不显示
            mis = int(endtime/60)
            sen = endtime - (mis * 60)
            print('\n 用时:%d m %.3f s' % (mis,sen))
            result = 'success'
            return result
        else:
            print('\n 用时:%.3f s' % endtime)
            result = 'success'
            return result
    except:
        print('发生了一个错误导致归档失败！')
        result = 'failed'
        print(sys.exc_info())#抛出异常信息
        return result