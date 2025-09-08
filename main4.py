def find_team_place(team_name, team_score, teams_data):
    """
    Визначає місце нової команди та повертає список команд з меншою кількістю очок.

    Args:
        team_name (str): Назва нової команди.
        team_score (int): Кількість очок, набраних новою командою.
        teams_data (dict): Словник з даними існуючих 9 команд.

    Returns:
        tuple: Кортеж, що містить:
               - int: Місце нової команди.
               - list: Список назв команд, які набрали менше очок.
    """
    
    all_teams = list(teams_data.items())
    all_teams.append((team_name, team_score))

    all_teams.sort(key=lambda x: x[1], reverse=True)
    
    place = 0
    less_score_teams = []

    for i, (name, score) in enumerate(all_teams):
        if name == team_name:
            place = i + 1
        elif place > 0 and i >= place - 1:
            less_score_teams.append(name)

    return place, less_score_teams

n = 9
current_teams = {
    'Динамо': 25,
    'Шахтар': 23,
    'Дніпро-1': 22,
    'Зоря': 20,
    'Ворскла': 18,
    'Олександрія': 16,
    'Кривбас': 15,
    'Рух': 13,
    'Чорноморець': 12
}

new_team_name = 'Металіст'
new_team_score = 17

team_place, teams_with_less_score = find_team_place(new_team_name, new_team_score, current_teams)


print(f"Нова команда '{new_team_name}' зайняла {team_place}-е місце.")
print("Назви команд, які набрали менше очок, ніж ця команда:")
for team in teams_with_less_score:
    print(f"- {team}")