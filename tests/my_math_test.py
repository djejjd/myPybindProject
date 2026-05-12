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

"""
验证拷贝和非拷贝操作的耗时
"""
# 生成 NumPy 数组（float64，连续内存）
n = 10_000_000  # 亿级数据
np_data = np.random.random(n).astype(np.float64)  # 默认就是 float64，显式确保

# 从 NumPy 数组生成一份 list 副本，专门给拷贝版使用（模拟“原本只有 list”的情况）
list_data = np_data.tolist()
start_time = time.perf_counter()
nums_tuple = my_math.find_min_max(list_data)
end_time = time.perf_counter()
print(f"\n【需要拷贝】最小值：{nums_tuple[0]}, 最大值：{nums_tuple[1]}, 耗时：{end_time - start_time}")

# 测试非拷贝版性能
start_time = time.perf_counter()
# 这里传递的参数是np_data，不是list_data，这里采用numpy生成，是因为numpy数组分配的内存是一片连续的
nums_tuple = my_math.find_min_max_nocopy(np_data)
end_time = time.perf_counter()
print(f"\n【不需要拷贝】最小值：{nums_tuple[0]}, 最大值：{nums_tuple[1]}, 耗时：{end_time - start_time}")


"""
验证c++返回的list是否符合预期
"""
# 生成一个小型数组进行观察
arr = my_math.generate_random_numbers_new(10)

# 1. 类型确认
print("type:", type(arr))          # 必须是 <class 'numpy.ndarray'>
print("dtype:", arr.dtype)         # float64

# 2. 内存所有权确认
print("owndata:", arr.flags.owndata)  # 必须为 True！
# 这表示数组自己拥有数据内存，会自动释放。如果为 False，说明数据来自其他对象，我们无法管理生命周期。

# 3. 修改值，证明是真正的读写内存
before = arr[0]
arr[0] = 3.14159
print("修改后第一个元素是否为3.14159 :", arr[0])

# 4. 删除数组，触发释放
del arr
# 如果没有崩溃，且没有提示内存泄漏，说明 capsule 正常工作了。

# 5. 更大批量的测试：生成千万级数据，观察内存是否正常回落
import os, psutil, time
process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss
big_arr = my_math.generate_random_numbers_new(10_000_000)
mem_mid = process.memory_info().rss
print(f"分配前后内存差: {(mem_mid - mem_before) / 1024 / 1024:.2f} MB")
del big_arr
time.sleep(0.5)  # 等GC回收
mem_after = process.memory_info().rss
print(f"释放后内存差: {(mem_after - mem_mid) / 1024 / 1024:.2f} MB")
# 应看到内存基本回到原水平