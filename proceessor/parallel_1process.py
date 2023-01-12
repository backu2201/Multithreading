from time import sleep,perf_counter
def task():
    print("Task started")
    sleep(1)
    print("Task done")
start_time = perf_counter()
task()

end_time = perf_counter()
print(f' {end_time-start_time}sec taken')
#depend on task(time differs)