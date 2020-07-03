import time
import csv
import os


class MetricManager:

    @staticmethod
    def timeCall(call, input, iterations, times):
        results = []
        for _ in range(times):
            start = time.time()
            call(input, iterations)
            end = time.time()
            results.append(end - start)
        return results
    
    @staticmethod
    def writeResultsToCSV(fileName, results):
        with open(f'{os.path.dirname(os.path.abspath(__file__))}/{fileName}.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(map(lambda x: [x], results))
