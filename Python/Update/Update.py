# coding=utf-8   #默认编码格式为utf-8
import os
import time

#全局变量

#用于存放每次运行update_all_dists期间的logs
logs = []


#读取txt中地址目录
def dirpathlist():
    data = []
    with open('Update\SVN地址.txt',
              'r',
              encoding='utf8') as f:
        for line in f:
            line_list = line.replace('\n', '')
            data.append(line_list)
        f.close()
    return data


#执行SVN更新
def SVNupdate():

    #执行前清空log文件内容
    # Clear_log=open('无双\测试脚本\SVN更新工具\logFile.txt','r+')
    # Clear_log=open('E:\Pyhton\Ws_test\脚本工具\SVN_update\logFile.txt','r+')
    with open('Update\logFile.log',
              'r+',

              encoding='utf8') as Clear_log:
        print("正在清空log日志内容……")
        Clear_log.truncate()

        for dist in dirpathlist():  
            cmd = 'TortoiseProc.exe /command:update /path:%s /closeonend:1' % dist
            #记录更新日志
            log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            log = '\n' + '执行：' + cmd + " --- 时间：" + log_time + '\n'
            print("记录log中……")
            logs.append(log)
            #执行更新
            print("正在更新:", dist)
            update_result = os.system(cmd)

            #更新完毕，添加成功与否的log
            if update_result == 0:
                log = '更新结果：成功  更新地址： ' + dist +  '\n'
                logs.append(log)

                #更新完毕打印数据
                print("更新完成:", dist)

                logs.append(
                    "******************************************************** 更新完成"
                    + '\n')
            else:
                log = '更新结果：失败  更新地址： ' + dist +  '\n'
                logs.append(log)

            #异常修复
            if update_result == 0:
                pass
            else:
                print(dist, "更新出现错误，正在检查中……")
                log = 'ERROR:' + dist + ' 更新失败, 执行修复...' + '\n'
                logs.append(log)

                cmd1 = 'TortoiseProc.exe /command:cleanup /path:%s /closeonend:1' % dist

                #执行清理
                print(dist, "正在执行清理功能,请手动点击OK进行下一步……")
                update_result1 = os.system(cmd1)

                #清理完毕，添加成功与否的log
                if update_result1 == 0:
                    log = '清理结果：成功  清理地址： ' + dist +  '\n'
                    logs.append(log)
                    print(dist, "清理已完成，正在重新更新……")
                    log = '重新获取更新……'+  '\n'
                    logs.append(log)

                    update_result = os.system(cmd)

                    #更新完毕，添加成功与否的log
                    if update_result == 0:
                        log = '更新结果：成功  更新地址： ' + dist +  '\n'
                        
                        logs.append(log)
                        #更新完毕打印数据
                        print("更新完成:", dist)
                        logs.append(
                            "******************************************************** 更新完成"
                            + '\n')
                    else:
                        log = '更新结果：失败  更新地址： ' + dist +  '\n'
                        logs.append(log)

                else:
                    log = '清理结果：失败  清理地址： ' + dist +  '\n'
                    print(dist, "清理失败，请手动检查问题……")
                    logs.append(log)
                    logs.append(
                        "******************************************************** 更新失败"
                        + '\n')

                    #更新完毕打印数据
                    print("更新失败:", dist)
        Clear_log.close()

        # with open('无双\测试脚本\SVN更新工具\logFile.txt','a') as y:
        with open('Update\logFile.log',
                  'a',
                  encoding='utf8') as y:
            for l in logs:
                y.write(l)

            y.close()
        logs.clear()
        print('Dong!')


#10秒倒计时
def countdown():
    time_new = 11
    for i in range(10):
        if time_new == 11:
            time.sleep(1)
            time_new -= 1
            print("%02d秒后关闭该程序！" % (time_new))
        elif time_new >= 3 and time_new <= 10:
            time.sleep(1)
            time_new -= 1
            print("还剩%02d秒关闭程序！" % (time_new))
        elif time_new == 2:
            time.sleep(1)
            time_new -= 1
            print("还剩%02d秒关闭程序！" % (time_new))
            time.sleep(1)
            print("脚本正在关闭……")
        else:
            print("倒计时出错……")
            time.sleep(3)


if __name__ == '__main__':
    SVNupdate()
    #countdown()
    #os.system('pause')
