sec = int(input("Enter the number of seconds: "))
hours=0
if sec>=3600: 
    hours = sec // 3600
minutes=0
if sec>=60:
    minutes = (sec % 3600) // 60    
seconds = (sec % 3600) % 60
print(f"{hours}:{minutes}:{seconds}")