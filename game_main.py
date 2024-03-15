import random

titan_pos=0
nimbus_pos=0
venus_pos=0
phantom_pos=0

titan_moves=0
nimbus_moves=0
venus_moves=0
phantom_moves=0

venus_dig_ability=False

won_players=[]

dig_pos=[]
in_ditch=[]

def check_ditch(pos):
    if pos in dig_pos:
        return True
    else:
        return False

def show_board():
    board=[]
    for i in range(1,101):
        board.append(i)
    if titan_pos != 0:
        if isinstance(board[titan_pos-1], str):
            board[titan_pos-1]+="T"
        else:
            board[titan_pos-1]="T"
    if nimbus_pos != 0:
        if isinstance(board[nimbus_pos-1], str):
            board[nimbus_pos-1]+="N"
        else:
            board[nimbus_pos-1]="N"
    if venus_pos != 0:
        if isinstance(board[venus_pos-1], str):
            board[venus_pos-1]+="V"
        else:
            board[venus_pos-1]="V"
    if phantom_pos != 0:
        if isinstance(board[phantom_pos-1], str):
            board[phantom_pos-1]+="P"
        else:
            board[phantom_pos-1]="P"
    if len(dig_pos) !=0:
        for dps in dig_pos:
            if isinstance(board[dps - 1],str):
                board[dps - 1]+='D'
            else:
                board[dps - 1] = 'D'
    for i in range(len(board)):
        print(board[i]," ",end="")
        if i>0 and (i+1) % 10==0:
            print("\n")

    print("---------------------------------")
    return 0

def roll_dice():
    return random.randint(1,6)

next_player = 'T'

while(True):
    if len(won_players) == 3:    #To check if more than 1 players are in game
        print(" GAME OVER ")
        print(f"1. {won_players[0]}, 2. {won_players[1]}, 3. {won_players[2]}")
        break

#----- TITAN TURN ---------------------------------------------
    
    if next_player == 'T':      #to check turn
        if 'T' in won_players:
            next_player = 'N'   #to assign next turn player
            continue
        if 'T' in in_ditch:         # ----- CHECKNG IF IN DITCH AND SKIPPING THE DICE ROLL 
            in_ditch.remove('T')
            dig_pos.remove(titan_pos)
            next_player='N'
            continue
        titan_roll = roll_dice()
        if titan_pos + titan_roll == 100:   #to check if winning condition is reached
            titan_pos += titan_roll
            titan_moves+=1
            print(titan_pos)
            show_board()
            print("TITAN won")
            next_player = 'N'
            won_players.append('T') #adding to winnes list so that turns can be skipped
            continue
        if titan_pos + titan_roll >100: #If the rolled number exceeds the postion beyond board, roll has to be separate variable bcoz of this
            print(f"You win if u roll {100 - titan_pos}")
            next_player = 'N'
            print(titan_pos)
            show_board()
            continue

        titan_pos += titan_roll     #normal game condtion

        if check_ditch(titan_pos):      # ------- CHECKING IF FALLING IN DITCH AND ADDING CHARACTER TO DITCH
            in_ditch.append('T')
            print("Fell in ditch. You will lose next Rolling")

        titan_moves+=1
        next_player = 'N'
        print(titan_pos)
        show_board()
    #------------------------------------------

#------ NIMBUS TURN ---------------------------
        
    if next_player == 'N':
        if 'N' in won_players:
            next_player = 'V'
            continue
        if 'N' in in_ditch:             # -------- CHECKNG IF IN DITCH AND SKIPPING THE DICE ROLL 
            in_ditch.remove('N')
            dig_pos.remove(nimbus_pos)
            next_player='V'
            continue

        nimbus_roll = roll_dice()
        if nimbus_pos + nimbus_roll == 100:
            nimbus_pos += nimbus_roll
            nimbus_moves+=1
            print(nimbus_pos)
            show_board()
            print("NIMBUS won")
            next_player = 'V'
            won_players.append('N')
            continue
        if nimbus_pos + nimbus_roll >100:
            print(f"You win if u roll {100 - nimbus_pos}")
            next_player = 'V'
            print(nimbus_pos)
            show_board()
            continue
        nimbus_pos += nimbus_roll

        if check_ditch(nimbus_pos):         # ------- CHECKING IF FALLING IN DITCH AND ADDING CHARACTER TO DITCH
            in_ditch.append('N')
            print("Fell in ditch. You will lose next Rolling")

        nimbus_moves+=1
        next_player = 'V'
        print(nimbus_pos)
        show_board()
        #----------------------------------

#----- VENUS TURN -------------------------
        
    if next_player == 'V':
        if 'V' in won_players:
            next_player='P'
            continue

        if venus_moves >= 5 and venus_moves%5==0:       #----- CHECKING IF VENUS CAN DIG DITCH
            venus_dig_ability = True

        venus_roll = roll_dice()
        if venus_pos + venus_roll == 100:
            venus_pos += venus_roll
            venus_moves+=1
            print(venus_pos)
            show_board()
            print("VENUS won")
            next_player = 'P'
            won_players.append('V')
            continue
        if venus_pos + venus_roll >100:
            print(f"You win if u roll {100 - venus_pos}")
            next_player = 'P'
            print(venus_pos)
            show_board()
            continue
        if venus_dig_ability:
            dig = input(" you have unlocked DIG, do u want to dig a ditch here?(y/n)")
            if dig == 'y':
                dig_pos.append(venus_pos)
                venus_dig_ability=False
            else:
                pass
        venus_pos += venus_roll
        venus_moves+=1
        next_player = 'P'
        print(venus_pos)
        show_board()
        #----------------------------------

#------ PHANTOM TURN ---------------------
        
    if next_player == 'P':
        if 'P' in won_players:
            next_player = 'T'
            continue

        if 'P' in in_ditch:       # ----- CHECKNG IF IN DITCH AND SKIPPING THE DICE ROLL 
            in_ditch.remove('P')
            next_player='T'
            dig_pos.remove(phantom_pos)
            continue

        phantom_roll = roll_dice()
        if phantom_pos + phantom_roll == 100:
            phantom_pos += phantom_roll
            phantom_moves+=1
            print(phantom_pos)
            show_board()
            print("PHANTOM won")
            next_player = 'T'
            won_players.append('P')
            continue
        if phantom_pos + phantom_roll >100:
            print(f"You win if u roll {100 - phantom_pos}")
            next_player = 'T'
            print(phantom_pos)
            show_board()
            continue
        phantom_pos += phantom_roll

        if check_ditch(phantom_pos):        # ------- CHECKING IF FALLING IN DITCH AND ADDING CHARACTER TO DITCH
            in_ditch.append('P')
            print("Fell in ditch. You will lose next Rolling")

        phantom_moves+=1
        next_player = 'T'
        print(phantom_pos)
        show_board()
print("GAME OVER")
print(F"TITAN MOVES = {titan_moves},  NIMBUS {nimbus_moves}")

#to check if the changes are reflecting on the local repo or the remote repo
# this part will be appended at remote repo