import time


def stopwatch():  
    input('Hit enter start laps.')
    index = 1
    prev_time = time.time()
    while True:
        print(f'Beginning beginning lap {index}.')
        input()
        index += 1
        delta = time.time() - prev_time
        prev_time = time.time()
        lap_times.append(delta)
        
        
try:
    lap_times = []
    stopwatch()
except KeyboardInterrupt:
    for i, lap in enumerate(lap_times):
        print(f'Lap {i}: {round(lap, 2)} seconds')
    print(f'Total time: {sum(lap_times)}')
        
        