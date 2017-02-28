# Function to calculate MAD for each fold

from global_module import movie_dict
from global_module import user_dict
from math import sqrt
from math import pow


def mad_function(base_file, test_file):

    for user in user_dict:
        user_dict[user].movies_watched.clear()

    for movie in movie_dict:
        movie_dict[movie].watched_by.clear()

    file = open(base_file, 'r')
    for line in file:
        items = line.split()
        user = int(items[0])
        movie = int(items[1])
        rating = int(items[2])

        user_obj = user_dict[user]
        user_obj.movies_watched[movie] = rating

        movie_obj = movie_dict[movie]
        movie_obj.watched_by[user] = rating

    file = open(test_file, 'r')
    predicted_rating_list = {}
    true_rating_list = {}

    for line in file:
        line = ' '.join(line.split())
        items = line.split(' ')
        test_user = int(items[0])
        test_movie = int(items[1])
        true_rating = int(items[2])
        test_user_age_group = user_dict[test_user].age_group
        test_user_gender = user_dict[test_user].gender

        if test_user not in true_rating_list:
            true_rating_list[test_user] = {}
        true_rating_list[test_user][test_movie] = true_rating

        test_user_movies_watched = user_dict[test_user].movies_watched.keys()
        no_of_movies_watched_by_test_user = len(test_user_movies_watched)
        test_movie_watched_by = movie_dict[test_movie].watched_by.keys()
        if test_user not in predicted_rating_list:
            predicted_rating_list[test_user] = {}
        users_ranking = {}

        for user in test_movie_watched_by:
            user_movies_watched = user_dict[user].movies_watched.keys()
            user_age_group = user_dict[user].age_group
            user_gender = user_dict[user].gender
            no_of_common_movies = 0
            euclidian = 0

            for movie in test_user_movies_watched:
                if movie in user_movies_watched:
                    no_of_common_movies += 1
                    test_user_rating = user_dict[test_user].movies_watched[movie]
                    user_rating = user_dict[user].movies_watched[movie]
                    euclidian += (pow((test_user_rating - user_rating), 2))

            if no_of_common_movies != 0:
                common_movies_coeff = no_of_common_movies / no_of_movies_watched_by_test_user
                euclidian_coeff = 1 / (1 + sqrt(euclidian))
                age_coeff = 1-(abs((test_user_age_group - user_age_group))/6)
                if test_user_gender == user_gender:
                    gender_coeff = 1
                else:
                    gender_coeff = 0.5
                weight = common_movies_coeff * euclidian_coeff * age_coeff * gender_coeff
                users_ranking[user] = weight

        users_ranking_sorted = sorted(users_ranking.items(), key=lambda x: x[1], reverse=True)[:100]
        length = len(users_ranking_sorted)
        users_ranking_sorted_1 = users_ranking_sorted[:int(round(length / 4))]
        users_ranking_sorted_2 = users_ranking_sorted[int(round(length / 4)) + 1: int(round(length / 2))]
        users_ranking_sorted_3 = users_ranking_sorted[int(round(length / 2)) + 1: int(round(3 * length / 4))]
        users_ranking_sorted_4 = users_ranking_sorted[int(round(3 * length / 4)) + 1: length]
        avg_predicted_rating = 0

        test_movie_rating_sum = 0
        for user, weight in users_ranking_sorted_1:
            test_movie_rating = user_dict[user].movies_watched[test_movie]
            test_movie_rating_sum += test_movie_rating
        if len(users_ranking_sorted_1) != 0:
            avg_predicted_rating += 0.7 * test_movie_rating_sum / len(users_ranking_sorted_1)

        test_movie_rating_sum = 0
        for user, weight in users_ranking_sorted_2:
            test_movie_rating = user_dict[user].movies_watched[test_movie]
            test_movie_rating_sum += test_movie_rating
        if len(users_ranking_sorted_2) != 0:
            avg_predicted_rating += 0.2 * test_movie_rating_sum / len(users_ranking_sorted_2)

        test_movie_rating_sum = 0
        for user, weight in users_ranking_sorted_3:
            test_movie_rating = user_dict[user].movies_watched[test_movie]
            test_movie_rating_sum += test_movie_rating
        if len(users_ranking_sorted_3) != 0:
            avg_predicted_rating += 0.07 * test_movie_rating_sum / len(users_ranking_sorted_3)

        test_movie_rating_sum = 0
        for user, weight in users_ranking_sorted_4:
            test_movie_rating = user_dict[user].movies_watched[test_movie]
            test_movie_rating_sum += test_movie_rating
        if len(users_ranking_sorted_4) != 0:
            avg_predicted_rating += 0.03 * test_movie_rating_sum / len(users_ranking_sorted_4)

        if length == 0:
            avg_predicted_rating = 0

        predicted_rating_list[test_user][test_movie] = round(avg_predicted_rating)
        # print(test_movie)
        # print(predicted_rating_list[test_user])
        # input("Check")

    print((predicted_rating_list.items()))
    print((true_rating_list.items()))

    # MAD
    sum_of_diff = 0
    for user in true_rating_list:
        for movie in true_rating_list[user]:
            sum_of_diff += abs(true_rating_list[user][movie] - predicted_rating_list[user][movie])

    MAD = sum_of_diff / 20000

    return MAD


