import my_math
import random
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

list_data = [random.random() for _ in range(1_000_000_00)]
start_time = time.perf_counter()
nums_tuple = my_math.find_min_max(list_data)
end_time = time.perf_counter()
print(f"\n最小值：{nums_tuple[0]}, 最大值：{nums_tuple[1]}, 耗时：{end_time - start_time}")

