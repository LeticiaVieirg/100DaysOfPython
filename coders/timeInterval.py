def seconds(hours, minutes, seconds):
  hours%=12
  totalSeconds=hours*3600+minutes*60+seconds
  return totalSeconds

def timeDiference(hours1, hours2, minutes1, minutes2, seconds1, seconds2):
  time1seconds= seconds(hour1, minutes1, seconds1)
  time2seconds=seconds(hour2, minutes2, seconds2)
  diferenceSeconds=times2seconds-times1seconds

  if diferenceSeconds<0:
    diferenceSeconds+=12*3600
  return diferenceSeconds

def requestTime(time):
  print(f"Enter a {time}time (hour, minutes and seconds: ")
  hours, minutes, seconds=map(int, input().split())
  return hours, minutes, seconds

def main():
  hour1, minutes1, seconds1=requestTime("first")
  hour2, minutes2, seconds2=requestTime("second")

  diference=diferenceTime(hours1, hours2, minutes1, minutes2, seconds1, seconds2)
  print(f"The diference is: {diference} seconds")
  return hours, minutes, seconds

if __name__=="__main__":
  main()
