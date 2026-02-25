import statistics

temperature = [30, 32, 31, 29, 33, 34, 32, 31, 30, 29]
humidity = [60, 65, 62, 58, 70, 68, 64, 61, 59, 63]

temp_mean = statistics.mean(temperature)
temp_median = statistics.median(temperature)
humidity_mean = statistics.mean(humidity)
humidity_median = statistics.median(humidity)

print(f"Temperature Mean: {temp_mean}")
print(f"Temperature Median: {temp_median}") 
print(f"Humidity Mean: {humidity_mean}")
print(f"Humidity Median: {humidity_median}")