
# msg= input("say something")
# i= 1
# while msg!= ("stop copying me"):
#     if i<3:
#         msg= input(f"{msg}\n")
#         i=i+1
#     else:
#         print("time out")
#         break
# else:
#     print("UGH FINE YOU WIN, BROTHER")



value = 5
g_r = 4
print("you have four guess attempts")
keep_playing="true"
while keep_playing == "true":
      guess = int(input("enter a number:"))
      g_r = g_r - 1
      if guess == value:
          print("you win")
          keep_playing = "false"
      else:
           if g_r == 0:
              print("you lose") 
              keep_playing= "false"
           elif guess != value:
                print("oops")     

      
