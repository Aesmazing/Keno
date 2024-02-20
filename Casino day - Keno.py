#In class Casino, group 13 : Keno 
#Aeslyn Broughton
#Cody Biesenbach
#Itzel Ortiz
#Aimika Saithong


import random
total_rewards= 0 


def new_player():
        print("Welcome to Keno for beginners (Easy Mode)!")
        while True:
            try:
                newp=input("Would you like the rules and instructions?(yes or no)").lower().strip()
                if newp== "no":
                    break
                elif newp== "yes":
                    print("Rules")
                    print("1) Typically, you  will be given a choice to select how many tickets you wish to play(Max 10 per game).")
                    print("For new players it is reccomended to start with only 1 ticket. So thats how we will play")
                    print("2) You will select how many entries per ticket (1-20) and choose numbers (1-80) for each entry.")
                    print("3) A random set of winning numbers (20 numbers) will be generated.")
                    print("4) If your chosen numbers match the winning numbers, you win!")
                    print("5) Your winnings depend on the number of matches and your bet (Min bet $5 . Max bet $50.")
                    print("6) Enjoy the game and good luck!")
                    print ()
                    print()
                    break
            except ValueError:
                print ("Answer is not regonized. Please try again.")
             
def number_of_entries():
    while True:
        try:
            x = int(input("How many numbers would you like to guess? (1-20): "))
            if x > 20:
                print("Invalid entry, please enter a number from the range 1-20")
            elif x < 1:
                print("Invalid entry, please enter a number from 1-20")
            else:
                return x
        except ValueError:
            print("Please only enter the numerical form of your entry, i.e., 1, 2, 3")

def player_number_entries(x, player_choices):
    for i in range(1, x + 1):
        while True:
            try:
                number = int(input(f"Please enter your number entry (1-80) {i}: "))
                if 1 <= number <= 80:
                    if number not in player_choices:
                        player_choices.append(number)
                        break
                    else:
                        print("Number already chosen. Please try to select a different one.")
                else:
                    print("That number is out of range. Please enter a number within the range (1-80).")
            except ValueError:
                print("Please only enter the numerical form of your entry, i.e., 1, 5, 46")
    return player_choices

def player_bets():
    while True:
        try:
            user_bet = int(input("Please enter your bet (Please keep bets between 5-50): $ "))
            if 5 <= user_bet <= 50:
                return user_bet
               
            else:
                print()
                print("Please enter a wager within the valid range (5-50)")
                print()
        except ValueError:
            print("Please only enter the numerical form of your entry, i.e., 1, 5, 46")

            

def generate_winning_numbers():
    winning_numbers= []
    for count in range(20):
        number = random.randint(1, 80)
        winning_numbers.append(number)
    return winning_numbers

def calculate_winning_bets(player_choices, winning_numbers,user_bet):
    winning_bets = 0
    common_numbers= []  
    for number in player_choices:
        if number in winning_numbers:
            common_numbers.append(number)
            winning_bets += user_bet
    return winning_bets, common_numbers
 

def dist_of_bets(winning_bets,user_bet):
    global total_rewards
    
    if winning_bets > 0:
        reward = winning_bets
        total_rewards  += reward  
        print(f'Congratulations! You have won $ {reward:.2f}!')
        print(f'Your total reward is now $ {total_rewards:.2f}!')
    else:
        total_rewards -= user_bet
        print(f'Aww shucks. You lost bet of $ {user_bet:.2f}. Your total payout is now $ {total_rewards:.2f}.')
    return total_rewards

# Define functions (new_player, number_of_tickets, etc.) as before


def main():
    global total_rewards
    new_player()
    while True:
        try:
            player_choices = []
            common_numbers = []
            x = number_of_entries()
            player_number_entries(x, player_choices)
            user_bet = player_bets()  # Move the bet input outside the game loop
            winning_numbers = generate_winning_numbers()
            winning_bets, common_numbers = calculate_winning_bets(player_choices, winning_numbers, user_bet)
            total_rewards += dist_of_bets(winning_bets, user_bet)
            print("Your numbers are", player_choices)
            print()
            print("The winning numbers are", winning_numbers)
            print("===============================================")

            again = input("Why not try again? Enter yes to continue or no to quit: ").lower().strip()
            if again == "no":
                print()
                print("Goodbye!")
                break
            elif again == "yes":
                print()
                print("May the odds be ever in your favor!")
                print()
            else:
                pprint("That answer isn't recognized. Please try again")

        except ValueError:
            print("That answer isn't recognized. Please try again")

    print(f"Your Total Payout Is $ {total_rewards:.2f}")

if __name__ == "__main__":
    main()
