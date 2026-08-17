
#This is a simple physics calculator which is still in progress
print("   ---Welcome to physics calc (v:pocket)---")
#the loop
while True:
      
      #try error passing so your mistakes dont crash it
      try:
            
            #input block for your commands
            slct = int(input("\nChoose your equation\n0|0 for exit\n1|F=ma 2|v=√2gh 3|PE=mgh 4|v=d/t  5|a=(v-u)/t\n6|W=mg 7|p=mv   8|P=W/t  9|p=m/V 10|P=F/A\nselect using num: "))
            
            #if/elif/else code for your results
            if slct == 0:
                  break
            
            elif slct == 1:
                  
                  m = float(input("\nEnter the mass(kg): "))
                  
                  a = float(input("\nEnter the accelaration(m/s^2): "))
                  
                  print(f"\nYour force is {m*a:.4f}N or roughly {round(m*a)}N.")
                  
            elif slct == 2:
                  
                  g = float(input("\nEnter your gravity(m/s^2): "))
                  
                  h = float(input("\nEnter your height(m): "))
                  
                  print(f"\nYour velocity is {(2*g*h)**0.5:.4f}m/s or\nroughly {round((2*g*h)**0.5)}m/s.")
                  
            elif slct == 3:
                  
                  m = float(input("\nEnter your mass(kg): "))
                  
                  g = float(input("\nEnter your gravity(m/s^2): "))
                  
                  h = float(input("\nEnter your height(m): "))
                  
                  print(f"\nYour potential energy is {m*g*h:.4f}J or\nroughly {round(m*g*h)}J.")
            
            elif slct == 4:
                  
                  d = float(input("\nEnter your distance(m): "))
                  
                  t = float(input("\nEnter your time(s): "))
                  
                  print(f"\nYour velocity is {d/t:.4f}m/s or\nroughly {round(d/t)}m/s.")
           
            elif slct == 5:
                  
                  v = float(input("\nEnter your final velocity(m/s): "))
                  
                  u = float(input("\nEnter your initial velocity(m/s): "))
                  
                  t = float(input("\nEnter your time(s): "))
                  
                  print(f"\nYour accelaration is {(v-u)/t:.4f}m/s^2 or\nroughly {round((v-u)/t)}m/s^2.")
            
            elif slct == 6:
                  
                  m = float(input("\nEnter your mass(kg): "))
                  
                  g = float(input("\nEnter your gravity(m/s^2): "))
                  
                  print(f"\nYour weight is {m*g:.4f}N or\nroughly {round(m*g)}N")
            
      #the error handeler so your butter fingers dont crash my program
      except ValueError:
            
            #a very good error message
            print("\nError:[666]")
            
      except ZeroDivisionError:
            
            #a very bad error message
            print("\nError:[000]")
            
      #finally the finally block
      finally:
            pass

#the end message so it tells you, you are welcomed
print("\n            ---Thanks for using---\n                -Made by Mahir-")