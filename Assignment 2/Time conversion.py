#convert  the time entered in hh,min and sec into seconds

hh  = int(input("enter time in hh:"))
min = int(input("enter time in min:"))
sec = int(input('enter time seconds:'))

seconds = (hh*3600)+(min*60)+(sec)
print('Time in seconds:', seconds)