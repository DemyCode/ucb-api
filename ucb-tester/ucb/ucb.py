import numpy as np


# UCB algorithm
def restaurant_picker(
    restaurants_mean: list[float],
    restaurants_number_of_visit: list[int],
    time_step: int,
):
    restaurants_ucb_score = np.array(restaurants_mean) + np.sqrt(
        2 * np.log(time_step) / np.array(restaurants_number_of_visit)
    )
    return restaurants_ucb_score.argmax()
