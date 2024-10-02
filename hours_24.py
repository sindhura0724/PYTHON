for hours in range(24):
    if hours == 0 or hours<4:
        print("Midnight")
    elif hours <12:
        print("AM")
    elif hours >15:
        print("PM")
    else:
        print("NOON")
        
        
    