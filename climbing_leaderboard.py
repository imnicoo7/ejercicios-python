# Ejercicio Climbing the Leaderboard prueba técnica
# Nicolas Gutierrez
# ------------------------------------------------------------------------------------------------------------
def climbing_leaderboard(ranked, player):
    unique_ranks = sorted(set(ranked), reverse=True)  # Obtener las puntuaciones únicas ordenadas en orden descendente
    total_ranks = len(unique_ranks)
    player_ranks = []

    j = total_ranks - 1  # Índice para recorrer la tabla de clasificación
    for score in player:
        # Avanzar en la tabla de clasificación hasta encontrar una puntuación que sea menor o igual a la del jugador actual
        while j >= 0 and score >= unique_ranks[j]:
            j -= 1

        if j == -1:
            # Si llegamos al principio de la tabla de clasificación, el jugador ocupa el primer lugar
            player_ranks.append(1)
        else:
            # Si la puntuación del jugador es igual a la de algún jugador en la tabla, ocupa el mismo rango que ese jugador
            if score == unique_ranks[j]:
                player_ranks.append(j + 1)
            else:
                # Si la puntuación del jugador es menor que la de algún jugador en la tabla, ocupa el siguiente rango
                player_ranks.append(j + 2)

    return player_ranks
# ------------------------------------------------------------------------------------------------------------
ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]
result = climbing_leaderboard(ranked, player)
print(result)
