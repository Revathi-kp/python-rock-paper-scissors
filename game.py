import random

options = ("rock", "paper", "scissors")

player_wins = 0
computer_wins = 0
ties = 0

running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        # .strip() removes accidental spaces, .lower() fixes capital letters
        player = input("\nEnter a choice (rock, paper, scissors): ").strip().lower()
        if player not in options:
            print("❌ That is not a valid choice. Try again!")
        
    print(f"\n🧑 Player: {player}")
    print(f"🤖 Computer: {computer}")
    
    # Win / Loss / Tie Logic
    if player == computer:
        print("🤝 It's a tie!")
        ties = ties + 1
    elif player == "rock" and computer == "scissors":
        print("🎉 You win!")
        player_wins = player_wins + 1
    elif player == "paper" and computer == "rock":
        print("🎉 You win!")
        player_wins = player_wins + 1
    elif player == "scissors" and computer == "paper":
        print("🎉 You win!")
        player_wins = player_wins + 1
    else:
        print("💥 You lose!")
        computer_wins = computer_wins + 1
        
    # --- Project Feature: Live Scoreboard ---
    print("-" * 30)
    print(f"📊 CURRENT SCORE -> Wins: {player_wins} | Losses: {computer_wins} | Ties: {ties}")
    print("-" * 30)
    
    # Clean play again prompt
    play_again = input("Do you want to play another round? (y/n): ").strip().lower()
    if play_again != "y" and play_again != "yes":
        running = False

# This prints ONLY when the player exits the game completely
print("\n" + "=" * 35)
print("✨ Thanks for playing! Final Game Stats: ✨")
print(f"🏆 Total Wins: {player_wins} | Total Losses: {computer_wins} | Total Ties: {ties}")
print("=" * 35)