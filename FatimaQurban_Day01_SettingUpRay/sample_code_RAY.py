# import time
# import ray

# # Initialize Ray
# ray.init()

# @ray.remote
# def factorial_ray(start, end):
#     result = 1
#     for i in range(start, end + 1):
#         result *= i
#     return result

# def parallel_factorial(n, num_chunks=10):
#     chunk_size = n // num_chunks
#     tasks = []

#     for i in range(num_chunks):
#         start = i * chunk_size + 1
#         end = (i + 1) * chunk_size if i != num_chunks - 1 else n
#         tasks.append(factorial_ray.remote(start, end))

#     results = ray.get(tasks)
#     final_result = 1
#     for res in results:
#         final_result *= res

#     return final_result

# # Example usage
# if __name__ == "__main__":
#     number = 120  # You can change this number to test different inputs

#     # Measure time for the entire Ray version
#     start_time = time.time()
#     result_ray = parallel_factorial(number)
#     end_time = time.time()
#     ray_time = end_time - start_time

#     print(f"Factorial of {number} with Ray is {result_ray}")
#     print(f"Execution time with Ray: {ray_time} seconds")

#     # Shutdown Ray
#     ray.shutdown()





import time
import ray

# Initialize Ray with the dashboard enabled
ray.init(include_dashboard=True)

@ray.remote
def factorial_ray(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def parallel_factorial(n, num_chunks=10):
    chunk_size = n // num_chunks
    tasks = []

    for i in range(num_chunks):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != num_chunks - 1 else n
        tasks.append(factorial_ray.remote(start, end))

    results = ray.get(tasks)
    final_result = 1
    for res in results:
        final_result *= res

    return final_result

# Example usage
if __name__ == "__main__":
    number = 120  # You can change this number to test different inputs

    # Measure time for the entire Ray version
    start_time = time.time()
    result_ray = parallel_factorial(number)
    end_time = time.time()
    ray_time = end_time - start_time

    print(f"Factorial of {number} with Ray is {result_ray}")
    print(f"Execution time with Ray: {ray_time} seconds")

    # Keep the script running to view the dashboard
    input("Press Enter to shutdown Ray and exit...")

    # Shutdown Ray
    ray.shutdown()
