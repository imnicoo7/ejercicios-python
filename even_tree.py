# Ejercicio Even Tree
# Nicolas Gutierrez

# ------------------------------------------------------------------------------------------------------------
def climbingLeaderboard(ranked, player):
    unique_ranks = sorted(set(ranked), reverse=True)  # Get the unique scores in descending order

    total_ranks = len(unique_ranks)
    player_ranks = []

    j = total_ranks - 1  # Index to traverse the leaderboard
    for score in player:
        # Move through the leaderboard until finding a score that is less than or equal to the current player's score
        
        while j >= 0 and score >= unique_ranks[j]:
            j -= 1

        if j == -1:
            # If we reach the beginning of the leaderboard, the player is in the first place
            player_ranks.append(1)
            
        else:
            # If the player's score matches a score in the leaderboard, they share the same rank as that player
            if score == unique_ranks[j]:
                player_ranks.append(j + 1)
            else:
                # If the player's score is lower than a score in the leaderboard, they take the next rank
                player_ranks.append(j + 2)

    return player_ranks
# ------------------------------------------------------------------------------------------------------------
print(climbingLeaderboard([100, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
