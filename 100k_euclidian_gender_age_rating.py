# Main file which calls MAD function for all folds and calculates final MAD
# MAD = 0.77755
from MAD_function_euclidian_gender_age_rating import mad_function
u1_base_file = 'C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u1.base'
u1_test_file = 'C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u1.test'

u2_base_file = 'C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u2.base'
u2_test_file = 'C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u2.test'

u3_base_file = 'C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u3.base'
u3_test_file = 'C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u3.test'

u4_base_file = 'C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u4.base'
u4_test_file = 'C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u4.test'

u5_base_file = 'C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u5.base'
u5_test_file = 'C:/Users/Aditya/Desktop/IUB/Data Mining/DM_Pedja/ml-100k/u5.test'

u_dict = {u1_base_file: u1_test_file, u2_base_file: u2_test_file, u3_base_file: u3_test_file, u4_base_file: u4_test_file, u5_base_file: u5_test_file}

# MAD = mad_function(u1_base_file, u1_test_file)
# print(MAD)

MAD_sum = 0
for base, test in u_dict.items():
    MAD_sum += mad_function(base, test)

MAD = MAD_sum/5
print(MAD)


