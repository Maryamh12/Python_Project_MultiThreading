import multiprocessing
import time
from multiprocessing import Pool




q = multiprocessing.Queue()

for i in range(5):
    q.put(i)

def worker(number):
    while  True:
        job_id = q.get()
        start = time.time()
        time.sleep(2)
        print(f"worker {number} job {job_id} started {start} finished {time.time()}")
        if q.empty():
            break

def multi_process():



    # process_list = list()
    # for i in range(15):
    #     p =multiprocessing.Process(target= worker, args= (i, ))
    #
    #     p.start()
    #     process_list.append(p)
    #     # p.join()
    #
    # for pr in process_list:
    #     pr.join()

    pool = Pool(4)

    with pool:
        pool.map(worker, q )
    print("All processes finished")




