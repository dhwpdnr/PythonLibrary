"""
Context Manager
원하는 타이밍에 자원을 할당하고 해제할 수 있도록 하는 기능
with 구문을 사용하여 사용할 수 있다.
"""

# Ex1 (Try - Finally)
file = open("./test.txt", "w")
try:
    file.write("Context Manager Tes1t\nContextlib Test1")
finally:
    file.close()

# Ex2 (with)
with open("./test2.txt", "w") as f:
    f.write("Context Manager Test2\nContextlib Test2")


# Ex3
# Use class > Context Manager with exception handling
class MyFileWriter:
    def __init__(self, file_name, method):
        print(
            "MyFileWriter started : __init__",
        )
        self.file_object = open(file_name, method)

    def __enter__(self):
        print("MyFileWriter started : __enter__")
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("MyFileWriter started : __exit__")
        if exc_type:
            print("Logging exception : {}".format((exc_type, exc_val, exc_tb)))
        self.file_object.close()


with MyFileWriter("./test3.txt", "w") as f:
    f.write("Context Manager Test3\nContextlib Test3")
