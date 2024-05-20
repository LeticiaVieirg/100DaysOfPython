subscribers={}

def verified_registration(name):
  if regitration.get(name):
    print("Regitration is confirmed!")
  else:
    subscribers[name]=True
    print("No register. Register for the event!")
