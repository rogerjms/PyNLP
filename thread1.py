import time, threading



def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name


# ������CPU����������ͬ��N���̣߳���4��CPU�Ͽ��Լ�ص�CPUռ���ʽ���160%��Ҳ����ʹ�ò������ˡ�

# ��ʹ����100���̣߳�ʹ����Ҳ��170%���ң���Ȼ�������ˡ�

# ������C��C++��Java����д��ͬ����ѭ����ֱ�ӿ��԰�ȫ������������4�˾��ܵ�400%��8�˾��ܵ�800%��ΪʲôPython�����أ�

# ��ΪPython���߳���Ȼ���������̣߳���������ִ�д���ʱ����һ��GIL����Global Interpreter Lock���κ�Python�߳�ִ��ǰ�������Ȼ��GIL����Ȼ��ÿִ��100���ֽ��룬���������Զ��ͷ�GIL�����ñ���߳��л���ִ�С����GILȫ����ʵ���ϰ������̵߳�ִ�д��붼�������������ԣ����߳���Python��ֻ�ܽ���ִ�У���ʹ100���߳�����100��CPU�ϣ�Ҳֻ���õ�1���ˡ�

# GIL��Python��������Ƶ���ʷ�������⣬ͨ�������õĽ������ǹٷ�ʵ�ֵ�CPython��Ҫ�������ö�ˣ�������дһ������GIL�Ľ�������

# ���ԣ���Python�У�����ʹ�ö��̣߳�����Ҫָ������Ч���ö�ˡ����һ��Ҫͨ�����߳����ö�ˣ���ֻ��ͨ��C��չ��ʵ�֣�����������ʧȥ��Python�����õ��ص㡣

# ������Ҳ���ù��ڵ��ģ�Python��Ȼ�������ö��߳�ʵ�ֶ�����񣬵�����ͨ�������ʵ�ֶ�����񡣶��Python�����и��Զ�����GIL��������Ӱ�졣

# С��