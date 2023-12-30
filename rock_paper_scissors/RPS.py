# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_opponent_play, opponent_history=[], play_order={}):
  if not prev_opponent_play:
      prev_opponent_play = 'R'

  opponent_history.append(prev_opponent_play)

  prediction = 'P'

  if len(opponent_history) > 4:
      last_five = "".join(opponent_history[-5:])

      play_order[last_five] = play_order.get(last_five, 0) + 1
      potential_next_plays = [
          last_five[1:] + next_play for next_play in ['R', 'P', 'S']
      ]

      filtered_play_order = {
          play: play_order[play] for play in potential_next_plays if play in play_order
      }

      if filtered_play_order:
          prediction = max(filtered_play_order,key=filtered_play_order.get)[-1]

  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  return ideal_response[prediction]


