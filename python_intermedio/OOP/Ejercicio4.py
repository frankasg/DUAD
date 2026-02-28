class Head:
    def __init__(self, hair, eyes, ears, mouth):
        self.hair = hair
        self.eyes = eyes
        self.ears = ears
        self.mouth = mouth
    


class Hand:
    def __init__(self, side):
        self.side = side

class Arm:
    def __init__(self, side, hand:Hand):
        self.side = side
        self.hand = hand

class Feet:
    def __init__(self, side):
        self.side = side

class Leg:
    def __init__(self, side, feet:Feet):
        self.side = side
        self.feet = feet


class Torso:
    def __init__(self, left_arm:Arm, right_arm:Arm):        
        self.left_arm = left_arm
        self.right_arm = right_arm

class Human:
    def __init__(self, head:Head, torso:Torso, left_leg:Leg, right_leg:Leg):
        self.head = head
        self.torso = torso
        self.left_leg = left_leg
        self.right_leg = right_leg

head = Head("black", "brows", "big", "small")

left_hand = Hand("left")
right_hand = Hand("right")
left_arm = Arm("left", left_hand)
right_arm = Arm("left", right_hand)

torso = Torso(left_arm, right_arm)

left_feet = Feet("left")
right_feet = Feet("right")
left_leg = Leg("left", left_feet)
right_leg = Leg("left", right_feet)

human = Human(head, torso, left_leg, right_leg)

#Example
print(human.head.ears)
