import backup
def yunxing():
    p = [r'',r'']
    i = 0
    for re in open('backupconfig.txt','r+'):
        p[i] = re
        i += 1
    p1 = p[0]
    p2 = p[1]
    p1 = p1.strip()
    p2 = p2.strip()
    try:
        backup.backup(p1,p2)
        result = '备份完成！'
        return result
    except:
        result = '备份出错！'
        return result