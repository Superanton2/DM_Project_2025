from time import perf_counter
# import time
#
# def sleeper():
#     time.sleep(1.75)
#
#
# def spinlock():
#     for _ in range(100_000_000):
#         pass
#
#
# for function in sleeper, spinlock:
#     t1 = time.perf_counter(), time.process_time()
#     function()
#     t2 = time.perf_counter(), time.process_time()
#     # print(f"{function.__name__}()")
#     print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
#     # print(f" CPU time: {t2[0] - t1[0]} seconds")
#     print("t1", t1)
#     print("t2", t2)
#     print()
#
# # sleeper()
# #  Real time: 1.75 seconds
# #  CPU time: 0.00 seconds
# #
# # spinlock()
# #  Real time: 1.77 seconds
# #  CPU time: 1.77 seconds

# Python program to show time by perf_counter()


# Start the stopwatch / counter
t1_start = perf_counter()

# функція

# Stop the stopwatch / counter
t1_stop = perf_counter()