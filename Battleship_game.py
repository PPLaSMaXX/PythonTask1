import os
import time


class Player:

    def __init__(self, name: str):
        self.Name = name
        self.fleet_health_point = 31
        self.play_field = [[0 for x in range(10)] for y in range(10)]
        self.hit_and_miss_field = [[0 for x in range(10)] for y in range(10)]
        self.available_ships = [6, 4, 4, 3, 3, 3, 2, 2, 2, 2]

    def get_play_field(self, x: int, y: int):
        cell = self.play_field[x][y]
        match cell:
            case 0:
                return "░"
            case 1:
                return "█"
            case 2:
                return "Ⅹ"
            case 3:
                return "〇"
            case 4:
                return "▓"
            case _:
                return "?"

    def get_hit_and_miss_field(self, x: int, y: int):
        cell = self.hit_and_miss_field[x][y]
        match cell:
            case 0:
                return "░"
            case 1:
                return "Ⅹ"
            case 2:
                return "〇"
            case 3:
                return "〷"
            case _:
                return "?"

alphabet = "abcdefghij"


def draw_player_screen(player: Player):
    print("PLAYER NAME: ", player.Name)
    print("# # # MAIN BOARD # # #")
    print(" ", end=" ")
    for i in range(10):
        print(alphabet[i], end=" ")
    print()
    for i in range(10):
        for j in range(10):
            if j == 0:
                print(i, end=" ")
            print(player.get_play_field(i, j), end=" ")
        print()

    print("\n\n# # #SHOTS RECORD# # #")
    print(" ", end=" ")
    for i in range(10):
        print(alphabet[i], end=" ")
    print()
    for i in range(10):
        for j in range(10):
            if j == 0:
                print(i, end=" ")
            print(player.get_hit_and_miss_field(i, j), end=" ")
        print()


def convert_coordinate(coordinate: str):
    coordinate = coordinate.lower()
    return (int(coordinate[1]), alphabet.index(coordinate[0]))


def check_position(i: int, numeric_coordinate: tuple, player: Player):

    if not player.play_field[numeric_coordinate[0]][numeric_coordinate[1]] == 0:
        return []

    check_top = True
    check_bottom = True
    check_left = True
    check_right = True

    for j in range(i):
        if j + numeric_coordinate[0] + 1 < 10:
            if (
                check_bottom
                and not player.play_field[numeric_coordinate[0] + j + 1][
                    numeric_coordinate[1]
                ]
                == 0
            ):
                check_bottom = False
        else:
            check_bottom = False
        if j + numeric_coordinate[1] + 1 < 10:
            if (
                check_right
                and not player.play_field[numeric_coordinate[0]][
                    numeric_coordinate[1] + j + 1
                ]
                == 0
            ):
                check_right = False
        else:
            check_right = False
        if numeric_coordinate[0] - j - 1 >= 0:
            if (
                check_top
                and not player.play_field[numeric_coordinate[0] - j - 1][
                    numeric_coordinate[1]
                ]
                == 0
            ):
                check_top = False
        else:
            check_top = False
        if numeric_coordinate[1] - j - 1 >= 0:
            if (
                check_left
                and not player.play_field[numeric_coordinate[0]][
                    numeric_coordinate[1] - j - 1
                ]
                == 0
            ):
                check_left = False
        else:
            check_left = False

    possible_directions = []

    if check_right:
        possible_directions.append(0)
    if check_bottom:
        possible_directions.append(1)
    if check_left:
        possible_directions.append(2)
    if check_top:
        possible_directions.append(3)

    return possible_directions


def place_ships(player: Player):
    for i in player.available_ships:

        numeric_coordinate = (0, 0)
        possible_directions = []
        while True:
            coordinate = input("Enter coordinate, where you want to place a nose of your ship (for e.g. A0, B7, etc)")
            if len(coordinate) != 2:
                print("incorrect input!")
                continue
            else:
                if len(check_position(i, convert_coordinate(coordinate), player)) == 0:
                    print("This position is too tight, choose another!")
                else:
                    numeric_coordinate = convert_coordinate(coordinate)
                    possible_directions = check_position(
                        i, convert_coordinate(coordinate), player
                    )
                    break
        print(
            "Choose direction in which you want to rotate your ship from available(0 - right, 1 - down, 2 - left, 3 - up): ",
            possible_directions,
        )
        direction = int(input())

        for j in range(i):
            if direction == 0:
                player.play_field[numeric_coordinate[0]][numeric_coordinate[1] + j] = 1
            if direction == 1:
                player.play_field[numeric_coordinate[0] + j][numeric_coordinate[1]] = 1
            if direction == 2:
                player.play_field[numeric_coordinate[0]][numeric_coordinate[1] - j] = 1
            if direction == 3:
                player.play_field[numeric_coordinate[0] - j][numeric_coordinate[1]] = 1

        for n in range(10):
            for m in range(10):
                if player.play_field[n][m] == 1:
                    if n >= 1 and player.play_field[n - 1][m] != 1:
                        player.play_field[n - 1][m] = 4

                if player.play_field[n][m] == 1:
                    if n <= 8 and player.play_field[n + 1][m] != 1:
                        player.play_field[n + 1][m] = 4

                if player.play_field[n][m] == 1:
                    if m >= 1 and player.play_field[n][m - 1] != 1:
                        player.play_field[n][m - 1] = 4

                if player.play_field[n][m] == 1:
                    if m <= 8 and player.play_field[n][m + 1] != 1:
                        player.play_field[n][m + 1] = 4

                if player.play_field[n][m] == 1:
                    if (
                        n <= 8
                        and m <= 8
                        and player.play_field[n][m + 1] != 1
                        and player.play_field[n + 1][m] != 1
                    ):
                        player.play_field[n + 1][m + 1] = 4

                if player.play_field[n][m] == 1:
                    if (
                        n >= 1
                        and m <= 8
                        and player.play_field[n][m + 1] != 1
                        and player.play_field[n - 1][m] != 1
                    ):
                        player.play_field[n - 1][m + 1] = 4

                if player.play_field[n][m] == 1:
                    if (
                        n >= 1
                        and m >= 1
                        and player.play_field[n][m - 1] != 1
                        and player.play_field[n - 1][m] != 1
                    ):
                        player.play_field[n - 1][m - 1] = 4

                if player.play_field[n][m] == 1:
                    if (
                        n <= 8
                        and m >= 1
                        and player.play_field[n][m - 1] != 1
                        and player.play_field[n + 1][m] != 1
                    ):
                        player.play_field[n + 1][m - 1] = 4

        os.system("cls")
        draw_player_screen(player)


def shoot(first_player: Player, second_player: Player):
    numeric_coordinate = (0, 0)

    while True:
        coordinate = input("Enter coordinate that you wanna to attack (for e.g. A0, h7, etc)")
        if len(coordinate) != 2:
            print("incorrect input!")
            continue
        else:
            numeric_coordinate = convert_coordinate(coordinate)
            if (
                numeric_coordinate[0] < 0
                or numeric_coordinate[0] > 9
                or numeric_coordinate[1] < 0
                or numeric_coordinate[1] > 9
            ):
                continue
            else:
                if (
                    second_player.play_field[numeric_coordinate[0]][
                        numeric_coordinate[1]
                    ]
                    == 1
                ):
                    second_player.play_field[numeric_coordinate[0]][
                        numeric_coordinate[1]
                    ] = 2
                    first_player.hit_and_miss_field[numeric_coordinate[0]][
                        numeric_coordinate[1]
                    ] = 1
                    second_player.fleet_health_point -= 1
                    print("HIT!")
                else:
                    second_player.play_field[numeric_coordinate[0]][
                        numeric_coordinate[1]
                    ] = 3
                    first_player.hit_and_miss_field[numeric_coordinate[0]][
                        numeric_coordinate[1]
                    ] = 2
                    print("MISS!")
                break

    draw_player_screen(first_player)


name1 = input("Enter Name of the first player ")
name2 = input("Enter Name of the second player ")
print("GOOD LUCK, HAVE FUN")
time.sleep(1)
os.system("cls")
player1 = Player(name1)
player2 = Player(name2)
draw_player_screen(player1)
place_ships(player1)
os.system("cls")
input(
    "Press ENTER to give control to other player, for him to place his ships. It`ll be shown in 5 second after pressing"
)
time.sleep(5)
os.system("cls")
draw_player_screen(player2)
place_ships(player2)
os.system("cls")

while player1.fleet_health_point != 0 or player2.fleet_health_point != 0:

    draw_player_screen(player1)
    shoot(player1, player2)
    if player2.fleet_health_point == 0:
        break
    input(
        "Press ENTER to give control to other player, his playboard will be shown in 5 second after pressing"
    )
    time.sleep(5)
    os.system("cls")
    draw_player_screen(player2)
    shoot(player2, player1)
    if player1.fleet_health_point == 0:
        break
    input(
        "Press ANY BUTTON to give control to other player, his playboard will be shown in 5 second"
    )
    time.sleep(5)
    os.system("cls")

print(
    "GOOD GAME!!!! VICTORY FOR ",
    (
        player1.Name
        if player1.fleet_health_point > player2.fleet_health_point
        else player2.Name
    ),
)
