import time


def printn(text, t=0.1):
    print(text)
    time.sleep(t)


def draw_tour(players, round_wins=[]):
    rounds_winner = ["", "", "", "", "", "", "", "", "", "", "", "",
                     "", "", ""]
    round_count = 0
    line_len = 15
    name_len = []

    for player in players:
        name_len.append(15 - len(player))
    for winner in round_wins:
        rounds_winner[round_count] = winner
        round_count += 1

    printn(players[0]+name_len[0]*"-")
    printn(line_len*" "+"|")
    printn(line_len*" "+"|"+line_len*"-"+rounds_winner[0])
    printn(line_len*" "+"|"+line_len*" "+"|")
    printn(players[1]+name_len[1]*"-"+(line_len+1)*" "+"|")
    printn(line_len*" "+(line_len+1)*" "+"|"+line_len*"-"+rounds_winner[8])
    printn(line_len*" "+(line_len+1)*" "+"|"+line_len*" "+"|")
    printn(players[2]+name_len[2]*"-"+(line_len+1)*" "+"|"+line_len*" "+"|")
    printn(line_len*" "+"|"+line_len*" "+"|"+line_len*" "+"|")
    printn(line_len*" "+"|"+line_len*"-"+rounds_winner[1] +
           (line_len-len(rounds_winner[1])+1)*" "+"|")
    printn(line_len*" "+"|"+31*" "+"|")
    printn(players[3]+name_len[3]*"-"+32*" "+"|")
    printn(47*" "+"|"+line_len*"-"+rounds_winner[12])
    printn(47*" "+"|"+line_len*" "+"|")
    printn(players[4]+name_len[4]*"-"+32*" "+"|"+line_len*" "+"|")
    printn(line_len*" "+"|"+31*" "+"|"+line_len*" "+"|")
    printn(line_len*" "+"|"+line_len*"-"+rounds_winner[2] +
           (line_len-len(rounds_winner[2])+1)*" "+"|"+line_len*" "+"|")
    printn(line_len*" "+"|"+line_len*" "+"|"+line_len*" "+"|"+line_len*" "+"|")
    printn(players[5]+name_len[5]*"-"+(line_len+1)*" "+"|"+line_len*" " +
           "|"+line_len*" "+"|")
    printn(line_len*" "+(line_len+1)*" "+"|"+line_len*"-"+rounds_winner[9] +
           (line_len-len(rounds_winner[9])+1)*" "+"|")
    printn(line_len*" "+(line_len+1)*" "+"|"+31*" "+"|")
    printn(players[6]+name_len[6]*"-"+(line_len+1)*" "+"|"+31*" "+"|")
    printn(line_len*" "+"|"+line_len*" "+"|"+31*" "+"|")
    printn(line_len*" "+"|"+line_len*"-"+rounds_winner[3] +
           (32-len(rounds_winner[3]))*" "+"|")
    printn(line_len*" "+"|"+47*" "+"|")
    printn(players[7]+name_len[7]*"-"+48*" "+"|")
    printn(63*" "+"|"+line_len*"-"+rounds_winner[14])
    printn(63*" "+"|")
    printn(players[8]+name_len[8]*"-"+48*" "+"|")
    printn(line_len*" "+"|"+47*" "+"|")
    printn(line_len*" "+"|"+line_len*"-"+rounds_winner[4] +
           (32-len(rounds_winner[4]))*" "+"|")
    printn(line_len*" "+"|"+line_len*" "+"|"+31*" "+"|")
    printn(players[9]+name_len[9]*"-"+(line_len+1)*" "+"|"+31*" "+"|")
    printn(line_len*" "+(line_len+1)*" "+"|"+line_len*"-"+rounds_winner[10] +
           (line_len-len(rounds_winner[10])+1)*" "+"|")
    printn(line_len*" "+(line_len+1)*" "+"|"+line_len*" "+"|"+line_len*" "+"|")
    printn(players[10]+name_len[10]*"-"+(line_len+1)*" "+"|"+line_len*" " +
           "|"+line_len*" "+"|")
    printn(line_len*" "+"|"+line_len*" "+"|"+line_len*" "+"|"+line_len*" "+"|")
    printn(line_len*" "+"|"+line_len*"-"+rounds_winner[5] +
           (line_len-len(rounds_winner[5])+1)*" "+"|"+line_len*" "+"|")
    printn(line_len*" "+"|"+31*" "+"|"+line_len*" "+"|")
    printn(players[11]+name_len[11]*"-"+32*" "+"|"+line_len*" "+"|")
    printn(47*" "+"|"+line_len*"-"+rounds_winner[13])
    printn(47*" "+"|")
    printn(players[12]+name_len[12]*"-"+32*" "+"|")
    printn(line_len*" "+"|"+31*" "+"|")
    printn(line_len*" "+"|"+line_len*"-"+rounds_winner[6] +
           (line_len-len(rounds_winner[6])+1)*" "+"|")
    printn(line_len*" "+"|"+line_len*" "+"|"+line_len*" "+"|")
    printn(players[13]+name_len[13]*"-"+(line_len+1)*" "+"|"+line_len*" "+"|")
    printn(line_len*" "+(line_len+1)*" "+"|"+line_len*"-"+rounds_winner[11])
    printn(line_len*" "+(line_len+1)*" "+"|")
    printn(players[14]+name_len[14]*"-"+(line_len+1)*" "+"|")
    printn(line_len*" "+"|"+line_len*" "+"|")
    printn(line_len*" "+"|"+line_len*"-"+rounds_winner[7])
    printn(line_len*" "+"|")
    printn(players[15]+name_len[15]*"-")
    input("\nPress enter to continue")


if __name__ == '__main__':
    pass
