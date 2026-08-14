for i in range(0,21):
    print(i)
    if (i == 11):
        break #cancel the execution of this loop now

for i in range(1,21):
    if i %2== 0:
        continue  #skips this part when i%2==0...sends back to loop and below part dosent get printed for this condition
    print(i)
  
for i in range (5):   #(i goes from 1 to 4)
    if i==3:
        pass   #does nothing....ye isliye lagte hai taaki agar hume future me kuch add krna ho but abhi kuch nhi dalna ho....isliye
    print(i)
