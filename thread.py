import threading, requests, time


def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread", total)


t = threading.Thread(target=sum, args=(1, 100000))
t.start()

print("Main Thread")


def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')


t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.start()

print("### End ###")
