import threading, requests, time


def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread", total)


# 쓰레드가 실행 할 함수를 target 으로 지정
# 함수에 필요한 인자를 args 에 튜플로 전달
t = threading.Thread(target=sum, args=(1, 100000))
t.start()

print("Main Thread")


def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars 종료')


t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.start()
print("### End 1 ###")


# 파생 클래스로 사용 하는 방식
class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), ' chars')


t2 = HtmlGetter('http://google.com')
# HtmlGetter 클래스 내에서 재정의 한 run method 실행
t2.start()

print("### End 2 ###")


def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')


# 데몬 쓰레드
t3 = threading.Thread(target=getHtml, args=('http://google.com',))
t3.daemon = True
t3.start()

print("### End 3 ###")
