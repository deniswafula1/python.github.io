is_running = True


while is_running:
    marks = float(input("Enter marks Between 0 and 100: "))

    if 80 <= marks <= 100:
        print("Grade A")

    elif marks >= 70 and marks <=80:
         print("Grade B")

    elif marks >= 60 and marks <=70:
         print("Grade C")

    elif marks >= 50 and marks <=60:
         print("Grade D")

    elif marks >= 40 and marks <=50:
         print("Grade E")

    elif marks >= 0 and marks <=40:

          print("You have failed")
    else:
          print("Enter a value between 0 to 100")