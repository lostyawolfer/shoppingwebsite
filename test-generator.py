import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def compute_heavy_load():
    tasks = [35, 36, 37, 38, 39, 40]
    with multiprocessing.Pool() as pool:
        results = pool.map(fibonacci, tasks) 
    print(results)

if __name__ == "__main__":
    compute_heavy_load()