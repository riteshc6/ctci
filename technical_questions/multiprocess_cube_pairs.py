from multiprocessing import Process, Pool
# from concurrent.futures import ProcessPoolExecutor
RANGE = 1, 50000001


def print_int(RANGEL):
    count = 0
    for a in range(*RANGEL):
        # for b in range(*RANGE):
            # for c in range(*RANGE):
                # for d in range(*RANGE):
                    # if (a ** 3) + (b ** 3) == (c ** 3) + (d ** 3):
                        # print(a, b, c, d)
                        # break
        count += 1
    print(count)                    # print(count)


print_int(RANGE)
# if __name__ == "__main__":
#     procs = []
#     args = [(1, 51), (51, 101)]
#     for arg in args:
#         proc = Process(target=print_int, args=(arg,))
#         print("proc: ", proc)
#         procs.append(proc)
#         proc.start()

#     for proc in procs:
#         proc.join()

# p = Pool(4)
# list(p.map(print_int, range(*RANGE)))

# with ProcessPoolExecutor(max_workers=2) as executor:
#     res = executor.submit(print_int)
