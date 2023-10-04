import numpy as np

m_3 = [
    [1, 2, 3],
    [4, 5, 6],
    [4, 5, 6]
]

m_4 = [
    [1, 2, 3],
    [4, 5, 6],
    [4, 5, 6]
]

m3_np = np.array(m_3)
m4_np = np.array(m_4)

m_total = m3_np + m4_np

data = np.arange(1, 5)
print(data)

data2 = np.linspace(2.0, 3.0)
print(data2)

data3 = np.eye(2)
print(data3)

data1 = np.array([10, 20, 30])
data2 = np.array([1, 2, 3])
data3 = data1 + data2
print(data3)
