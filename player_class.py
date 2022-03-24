


class Player:
    def __init__(self):
        self.wins = 0
        # Where we can have a default choose gesture method
        # when ai inherits player the method can change to random
        # when human inferits player the method can be default
        self.gestures_list = ['Scissor', 'Spock','Paper','Lizard','Rock']
    
    def choose_gesture(self):
        index = 0
        for gestures in self.gestures_list:
            print(f" Type {index} for {gestures}")
            index += 1

        while True:
         user_gesture_index = int(input('Pick a gesture: '))
         if user_gesture_index not in [0,1,2,3,4]:
             continue
         else: 
             break

        return self.gestures_list[user_gesture_index]
        
        


        


