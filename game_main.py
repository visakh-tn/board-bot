import random

titan_pos=0
nimbus_pos=0
venus_pos=0
phantom_pos=0

titan_moves=0
nimbus_moves=0
venus_moves=0
phantom_moves=0

# -- ABIITIES --
venus_dig_ability=False
phantom_portal_ability=False
phantom_teleport_ability=False
nimbus_sprint_ability=False
nimbus_sprint_rolls=0

won_players=[]

dig_pos=[]
in_ditch=[]
phantom_trap=[]
in_p_trap=[]

def get_portal_end(pos):
    if pos <20:
        prob=random.randint(-15,10)
        return prob
    elif pos < 50:
        prob = random.randint(-20,10)
        return prob
    elif pos < 75:
        prob = random.randint(-25,15)
        return prob
    elif pos < 90:        
        prob = random.randint(-5,95-pos)
        return prob
    else:
        prob=random.randint(-5,99-pos)
        return prob

def nimbus_tackle(pos):
    #TODO4 : As of now doing with move number, later have to add EXP of each champion for attack and defense intensity
    if pos < 6:
        return 0
    if nimbus_moves < 5:
        prob= random.randint(0,100)
        if prob<50:
            return random.randint(-5,-1)
        else:
            return random.randint(1,5)
    if nimbus_moves < 10:
        prob=random.randint(0,100)
        if prob < 70:
            return random.randint(-3,-1)
        else: 
            return random.randint(1,2)
    else: 
        prob=random.randint(0,100)
        if prob <80:
            return random.randint(-3,-1)
        else:
            return random.randint(1,2)

def check_champ_clash(attacker_pos,ignore_champ):
    if attacker_pos == titan_pos and ignore_champ != 'T':
        return 'T'
    if attacker_pos == nimbus_pos and ignore_champ != 'N':
        return 'N'
    if attacker_pos == venus_pos and ignore_champ != 'V':
        return 'V'
    if attacker_pos == phantom_pos and ignore_champ != 'P':
        return 'P'
    else:
        return None

def direction_dice(precision=0):
    if precision == 0:
        return random.randint(1,4)
    else:
        probability = random.randint(0,100)
        if precision == 25:
            if probability <=50:
                return 3
            if probability <= 65:
                return 1
            if probability <= 80:
                return 4
            else:
                return 2
        if precision == 50:
            if probability <=50:
                return 3
            if probability <= 75:
                return 2
            if probability <= 87:
                return 4
            else:
                return 1
        if precision == 75:
            if probability <=50:
                return 3
            if probability <= 84:
                return 2
            if probability <= 92:
                return 4
            else:
                return 1

def titan_throw(pos):
    if pos<10:
        if titan_moves < 5 :
            dir = random.choice([-1,1])         #-1 is for 3 or for negetive dir and +1
            return random.choice([1,2,3]) * dir
        else:
            return  random.choice([1,2,3]) * -1
    elif pos < 25:
        dir = direction_dice(75)
        if dir == 1:
            return random.randint(10,15)
        if dir == 2:
            return random.randint(-15,-10)      
        if dir == 3:
            return random.randint(-5,-1) 
        if dir == 4:
            return random.randint(1,5)
    elif pos < 50:
        dir = direction_dice(50)
        if dir == 1:
            return random.randint(10,25)
        if dir == 2:
            return random.randint(-25,-10)      
        if dir == 3:
            return random.randint(-8,-1) 
        if dir == 4:
            return random.randint(1,8)
        
    else:
        dir = direction_dice(75)
        if dir == 1:
            distance = random.randint(8,12)
            if pos+distance >= 100:
                return random.randint(1,100-pos)
            else:
                return distance
        if dir == 2:
            return random.randint(-12,-8)      
        if dir == 3:
            return random.randint(-3,-1) 
        if dir == 4:
            distance = random.randint(1,3)
            if pos+distance >= 100:
                return random.randint(1,100-pos)
            else:
                return distance

def venus_throw(pos):
    if pos<13:
        if titan_moves < 5 :
            dir = random.choice([-1,1])         #-1 is for 3 or for negetive dir and +1 for 4 or for +ve
            return random.choice([1,2,3]) * dir
        else:
            return  random.choice([1,2,3]) * -1
    else:
        dir = direction_dice(0)
        if dir == 1:
            distance = random.randint(8,12)
            if pos+distance >= 100:
                return random.randint(1,100-pos)
            else:
                return distance
            
        if dir == 2:
            return random.randint(-12,-8)
        
        if dir == 3:
            return random.randint(-3,-1)
        
        if dir == 4:
            distance = random.randint(1,3)
            if pos+distance >= 100:
                return random.randint(1,100-pos)
            else:
                return distance


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

    if len(phantom_trap) != 0:
        for pps in phantom_trap:
            if isinstance(board[pps - 1],str):
                board[pps - 1]+='Q'
            else:
                board[pps - 1]='Q'

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
            if titan_pos in dig_pos: 
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

        if titan_pos in phantom_trap:
            titan_pos+=get_portal_end(titan_pos)
            print("you fell in portal and teleported to ",titan_pos)
        
        #TODO2 ✅ : Add a function for titan throw based on moves or EXP for throw intensity
        throw_champ = check_champ_clash(titan_pos,'T')
        if throw_champ == 'N':
            print("throwing  N at ",nimbus_pos)
            nimbus_pos+=titan_throw(titan_pos)

        if throw_champ == 'V':
            print("throwing V at ",venus_pos)
            venus_pos+=titan_throw(titan_pos)

        if throw_champ == 'P':
            print("throwing P at ",phantom_pos)
            phantom_pos += titan_throw(titan_pos)


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
            if nimbus_pos in dig_pos: 
                dig_pos.remove(nimbus_pos)
            next_player='V'
            continue

        if nimbus_moves >=10 and nimbus_moves%5 and nimbus_sprint_rolls==False:     # checking if nimbus' sprint mode is ON
            nimbus_sprint_ability=True
            nimbus_sprint_rolls=4

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
        #TODO3 : check nimbus's SPRINT ability and increase speed on each dice roll
        if nimbus_sprint_ability == True:
            print(" nimbus sprinting SPRINT ON ")
            if nimbus_roll == 6:
                nimbus_sprint_rolls = nimbus_sprint_rolls - 2
            else:
                nimbus_sprint_rolls = nimbus_sprint_rolls - 1
            if nimbus_sprint_rolls <= 0:
                nimbus_sprint_ability = False
            nimbus_roll=nimbus_roll+ int(nimbus_roll*0.5)

        nimbus_pos += nimbus_roll

        if check_ditch(nimbus_pos):         # ------- CHECKING IF FALLING IN DITCH AND ADDING CHARACTER TO DITCH
            in_ditch.append('N')
            print("Fell in ditch. You will lose next Rolling")

        if nimbus_pos in phantom_trap:      #----- CHECKING IF FELL IN PORTAL ------
            nimbus_pos+=get_portal_end(nimbus_pos)
            print("you fell in portal and teleported to ",nimbus_pos)
        #TODO1 ✅ : check if there is any champion in the new nimbus_pos and then call tackle function, it should change tackled champion's pos
        
        tackle_champ =check_champ_clash(nimbus_pos,'N')
        if tackle_champ == 'T':
            print("tackling T at ",nimbus_pos)
            titan_pos+=nimbus_tackle(nimbus_pos)
        if tackle_champ == 'V':
            print("tackling V at ",nimbus_pos)
            venus_pos += nimbus_tackle(nimbus_pos)
        if tackle_champ == 'P':
            print("tackling P at ",nimbus_pos)
            phantom_pos += nimbus_tackle(nimbus_pos)
        


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

        if venus_pos in phantom_trap:       #---- CHECKING IF VENUS FELL IN PORTAL-----------
            venus_pos+=get_portal_end(venus_pos)
            print("you fell in portal and teleported to ",venus_pos)
        
        throw_champ = check_champ_clash(venus_pos,'V')      # venus throw same as titans but precision is 0
        if throw_champ == 'N':
            print("throwing  N at ",nimbus_pos)
            nimbus_pos+=venus_throw(venus_pos)

        if throw_champ == 'T':
            print("throwing T at ",venus_pos)
            titan_pos+=venus_throw(venus_pos)

        if throw_champ == 'P':
            print("throwing P at ",phantom_pos)
            phantom_pos += venus_throw(venus_pos)

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
            if phantom_pos in dig_pos: 
                dig_pos.remove(phantom_pos)
            continue

        if phantom_moves >10 :   #--- CHECKING IF PHANTOM CAN MAKE TRAP PORTAL
            if  phantom_moves%5==0:
                phantom_portal_ability=True
            if phantom_moves % 11 == 0:
                phantom_teleport_ability = True


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
        elif phantom_portal_ability:
                p_trap=input("you have unlocked TRAP PORTAL. Do you want to plant it here? (y/n)")
                if p_trap == 'y':
                    phantom_trap.append(phantom_pos)
                    phantom_portal_ability=False
        elif phantom_teleport_ability:
            teleport_champ = input("You have enabled teleport, near which champion do u wish to teleport? (T,N,V,P)")
            if teleport_champ == "t" or teleport_champ == 'T':
                phantom_pos = titan_pos - 1
            elif teleport_champ == 'n' or teleport_champ == 'N':
                phantom_pos = nimbus_pos -1
            elif teleport_champ == 'v' or teleport_champ == 'V':
                phantom_pos == venus_pos -1
            else :
                phantom_pos == max(titan_pos, nimbus_pos,venus_pos)-1
            phantom_teleport_ability = False


        phantom_moves+=1
        next_player = 'T'
        print(phantom_pos)
        show_board()
print("GAME OVER")
print(F"TITAN MOVES = {titan_moves},  NIMBUS {nimbus_moves}")
