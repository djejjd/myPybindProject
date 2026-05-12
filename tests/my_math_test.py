import my_math
import numpy as np
import time

result = my_math.add(10, 20)
print(f"结果是: {result}") # 输出: 结果是: 30

result = my_math.mul(10, 20)
print(f"结果是: {result}") # 输出: 结果是: 200

result = my_math.sub(30, 20)
print(f"结果是: {result}") # 输出: 结果是: 10

result = my_math.fibonacci(10);
print(f"结果是: {result}")

print("结果是: ", end="")
my_math.print_float()

# 生成 NumPy 数组（float64，连续内存）
n = 100_000_000  # 亿级数据
np_data = np.random.random(n).astype(np.float64)  # 默认就是 float64，显式确保

# 2. 从 NumPy 数组生成一份 list 副本，专门给拷贝版使用（模拟“原本只有 list”的情况）
list_data = np_data.tolist()
start_time = time.perf_counter()
nums_tuple = my_math.find_min_max(list_data)
end_time = time.perf_counter()
print(f"\n【需要拷贝】最小值：{nums_tuple[0]}, 最大值：{nums_tuple[1]}, 耗时：{end_time - start_time}")

# 3. 测试非拷贝版性能
start_time = time.perf_counter()
# 这里传递的参数是np_data，不是list_data，这里采用numpy生成，是因为numpy数组分配的内存是一片连续的
nums_tuple = my_math.find_min_max_nocopy(np_data)
end_time = time.perf_counter()
print(f"\n【不需要拷贝】最小值：{nums_tuple[0]}, 最大值：{nums_tuple[1]}, 耗时：{end_time - start_time}")