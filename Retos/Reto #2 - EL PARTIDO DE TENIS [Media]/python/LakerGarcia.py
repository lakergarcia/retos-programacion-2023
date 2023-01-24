def play_tennis(points):
  scores = {"P1": 0, "P2": 0}
  scores_translate = {0: "Love", 1: "15", 2: "30", 3: "40"}
  for point in points:
    scores[point] += 1
  if scores["P1"] == scores["P2"]:
    score = "Deuce"
  else:
    score = scores_translate[scores["P1"]] + " - " + scores_translate[scores["P2"]]
  return score

def who_won(points):
  scores = {"P1": 0, "P2": 0}
  for point in points:
    scores[point] += 1
  if scores["P1"] >= 4 and scores["P1"] - scores["P2"] >= 2:
    return "Ha ganado el P1"
  elif scores["P2"] >= 4 and scores["P2"] - scores["P1"] >= 2:
    return "Ha ganado el P2"
  else:
    return None

def play(points):
  for point in points:
    score = play_tennis(points[:points.index(point)+1])
    print(score)
    winner = who_won(points[:points.index(point)+1])
    if winner:
      return winner

points = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
play(points)
