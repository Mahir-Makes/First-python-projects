import random
win = 0
lose = 0
draw = 0

while True:
      #the input and the system
      
      a = random.randint(1,3)
      b = input("You: ").lower()
      #its the exit 
      
      if b == "exit":
            break
      #the bot mecanism
      if a == 1:
            print("Bot: Rock")
            
      elif a == 2:
            print("Bot: Paper")
            
      elif a == 3:
            print("Bot: Scissor")
            
      #the whole game with if/elif 
      #this cheks your input and makea the results
      if b == "rock" and a == 1:
            print("Its a draw.") 
            draw +=1
            
      elif b == "paper" and a == 1:
            print("You won.")
            win +=1
            
      elif b == "scissor" and a == 1:
            print("Bot wins.")
            lose += 1
            
      elif b == "rock" and a == 2:
            print("Bot wins.")
            lose += 1
            
      elif b == "scissor" and a == 2:
            print("You won.")
            win +=1
            
      elif b == "paper" and a == 2:
            print("Its a draw.")
            draw +=1
            
      elif b == "scissor" and a == 3:
            print("Its a draw.")
            draw +=1
            
      elif b == "paper" and a == 3:
            print("Bot wins.")
            lose += 1
            
      elif b == "rock" and a == 3:
            print("You won.")
            win +=1
            
print(f"Wins {win} | Lose {lose} | Draw {draw}")