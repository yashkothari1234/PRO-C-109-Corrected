import pandas as pd 
import statistics 
import csv 

df = pd.read_csv("StudentsPerformance.csv")

math_list = df["math score"].to_list()


math_std_deviation = statistics.stdev(math_list)


math_mean = statistics.mean(math_list)


math_median=statistics.median(math_list)
 

#math_mode = statistics.mode(math_list)


print("Mean,Median,Standard Deviation of Math Score is{}, {} and {} respectively".format(math_mean, math_median,math_std_deviation))



math_first_std_deviation_start, math_first_std_deviation_end = math_mean - math_std_deviation, math_mean + math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean - (2*math_std_deviation), math_mean + (2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean - (3*math_std_deviation), math_mean + (3*math_std_deviation)



math_list_of_data_within_1_std_deviation = [result for result in math_list if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_list if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_list if result > math_third_std_deviation_start and result < math_third_std_deviation_end]



print("{}% of data for Math Scores lie within 1 Standard Deviation".format(len(math_list_of_data_within_1_std_deviation)*100/len(math_list)))
print("{}% of data for Math Scores lie within 2 Standard Deviation".format(len(math_list_of_data_within_2_std_deviation)*100/len(math_list)))
print("{}% of data for Math Scores lie within 3 Standard Deviation".format(len(math_list_of_data_within_3_std_deviation)*100/len(math_list)))

