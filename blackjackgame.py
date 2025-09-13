
'''
    turtle_BJ.py (aka. version 1.1) brewed by KunToto@MikeLabDotNet [August 2024]
'''
import random, time
#import turtle

class Card():
    ''' Card(): create a card object. To create a deck, try \\Card.test_Card()\\! '''
    symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def __repr__(self):
        return f"{self.name}{Card.symbols[self.suit]}"
    def test_Card():
        Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
        Suits = ['D','C','H','S']
        deck = [Card(str(n), s) for s in Suits for n in Names]
        random.shuffle(deck)
        res = [str(card) for card in deck]
        return ' '.join(res)
    #---------------------------------------------------------------------
    def render(self, x, y, color='blue', RENDER=False):
        ''' วาดไพ่ด้วยเต่า '''
        if not RENDER:
            return None
        # Draw border
        pen.penup()
        pen.color(color)
        pen.goto(x+50, y+75)
        xy = ((x+50, y+75), (x+50, y-75), (x-50, y-75), (x-50, y+75))
        pen.begin_fill()
        pen.pendown()
        for pos in xy:
            pen.goto(pos)
        pen.end_fill()
        pen.penup()
        # Draw card info
        if self.name not in ['','O']:
            # Draw suit in the middle
            pen.color('white')
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
            # Draw top left
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
        pen.penup()
    #---------------------------------------------------------------------

class Deck:
    ''' Deck(): สร้างสำรับไพ่ '''
    Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    Suits = ['D','C','H','S']
    def __init__(self):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
    def shuffle(self):
        random.shuffle(self.cards)
    def get_card(self):
        return self.cards.pop()
    def set_cards(self, cards):
        self.cards = cards
    def reset(self, n=1):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
        for i in range(n):
            self.shuffle()
    def __repr__(self):
        res = [str(x) for x in self.cards]
        return ' '.join(res)

def preamble(RENDER=False):
    ''' จัดการ environment ในการวาดเต่า '''
    if not RENDER:
        return None
    #--------------------------------------------------------------------------------------
    global wn, pen
    wn, pen = turtle.Screen(), turtle.Turtle()
    wn.bgcolor('black')
    wn.setup(800, 600)
    wn.title('Deck of Cards Simulator by @TokyoEdtech, rebrewed by KunTotoNaMikeLabDotNet')
    pen.speed(0)
    pen.hideturtle()
    #--------------------------------------------------------------------------------------


def createVirtualDeck(s='K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'):
    dd = s.split()
    res = []
    suit = {'♦':'D','♣':'C','♥':'H','♠':'S'}
    for d in dd:
        card = Card(d[0], suit[d[1]])
        res.append(card)
    deck = Deck()
    deck.set_cards(res)
    return deck

def get_value(card):
    if card.get_name()=='J' or card.get_name()=='Q' or card.get_name()=='K' or card.get_name()=='T':
        return 10
    elif card.get_name()=='A':
        return 11
    else:
        return int(card.get_name())
        

class mycard:
    def __init__(self):
        self.cards=[]
    def pick_card(self,deck):
        self.cards.append(deck.get_card())
    def cal_card(self):
        points=0
        aces=0
        for card in self.cards:
            if card.get_name()=='J' or card.get_name()=='Q' or card.get_name()=='K' or card.get_name()=='T':
                points+=10
            elif card.get_name()=='A':
                aces+=1
                points+=11
            else:
                points+=int(card.get_name())
        while points>21 and aces>0:
             points-=10
             aces-=1
        return points
    def isBlackjack(self):
        if self.cal_card()==21 or len(self.cards)==5:
            return True
        return False
    
def show_hand_com(computer,name,hidden_card=True,):
    if hidden_card:
        print(f"{name:>9}: O{computer.cards[0].symbols[computer.cards[0].suit]} {' '.join([str(card) for card in computer.cards[1:]]):<13}-> {computer.cal_card()-get_value(computer.cards[0])}")
    else:
        print(f"{name:>9}: {' '.join([str(card) for card in computer.cards]):<16}-> {computer.cal_card()}")

def show_hand_player(player,name):
    print(f"{name:>9}: {' '.join([str(card) for card in player.cards]):<16}-> {player.cal_card()}")

def computer_play(computer,player,deck,name):
    
    while True:

        if len(computer.cards)==5:
            break
        #player reaches five card and point reaches 21. com picks
        elif player.isBlackjack() and computer.cal_card()<21:
            computer.pick_card(deck)
        
        elif computer.cal_card()<=16  or computer.cal_card()<player.cal_card() and player.cal_card()<=21 :
            computer.pick_card(deck)
        elif computer.cal_card()>=16 and player.cal_card()>21:
            break
        else:
            break

    show_hand_com(computer,name,hidden_card=False)
 

def play(player1='Computer', player2='Player', d=None, RENDER=False):
    print('Welcome to WinWut BlackJack Casino.')
    preamble(RENDER)
    # create a deck of cards
    if d==None:
        deck = Deck()
        deck.reset()
    else:
        #----------------------------- virtual deck
        #d = 'A♦ A♥ 3♥ 4♣ 4♥ 7♣ 5♣ 6♦ A♠'
        deck = createVirtualDeck(d)
    #----------------------
#     print(deck) # for DEBUG
    #----------------------
    player=mycard()
    computer=mycard()
        
    computer.pick_card(deck)
    player.pick_card(deck)
    computer.pick_card(deck)
    player.pick_card(deck)
    
    show_hand_com(computer,player1,hidden_card=True)
    show_hand_player(player,player2)
    global playercount
    playercount=0
    while True:
        if playercount ==3 or player.cal_card()>=21:
            break
        draw_ch=input("Draw another card (y/n): ")
        
        if draw_ch == 'y' or draw_ch=='Y':
            player.pick_card(deck)
            show_hand_player(player,player2)
            playercount+=1
            
        else:
            break
    print("+++++++++++++++++++++++++++++++++")

    computer_play(computer,player,deck,player1)
    show_hand_player(player,player2)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    p = player.cal_card()
    c = computer.cal_card()
    pc = len(player.cards)
    cc = len(computer.cards)
    
    #natural blackjack vs 5 cards
    if (pc== 2 and p==21 and cc==5) or (cc==2 and c==21 and pc==5):
        result = "Draw!"
    #both five cards without busts
    elif pc == 5 and p <= 21 and cc == 5 and c <= 21:
        result = "Draw!"
    #five card only
    elif pc == 5 and p <= 21:
        result = f"{player2} wins."
    elif cc == 5 and c <= 21:
        result = f"{player1} wins."
    #bust
    elif p > 21 and c > 21:
        result = "Draw!"
    elif p > 21:
        result = f"{player1} wins."
    elif c > 21:
        result = f"{player2} wins."
        
    #normal
    elif p > c:
        result = f"{player2} wins."
    elif p < c:
        result = f"{player1} wins."
    else:
        result = "Draw!"

    print(result)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
   


def testcase01():
    random.seed(2)
    play()
def testcase02():
    random.seed(16)
    play()
def testcase03():
    random.seed(30)
    play()
def testcase04():
    s = 'K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'
    play('Toto', 'Tutu', d=s)

def testcase05():
    s = 'A♣ 3♥ 2♠ T♥ 8♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase06():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase07():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ T♠'
    play(d=s)
def testcase08():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ Q♥ 3♠'
    play(d=s)
def testcase09():
    s = '5♠ A♥ A♣ 8♥ J♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase10():
    s = 'A♣ 3♦ A♦ A♥ 3♥ 4♣ 4♥ 7♣ 3♣ 2♦ A♠'
    play(d=s)
#------------------------------------------
q = int(input())
if q==1:
    testcase01()
elif q==2:
    testcase02()
elif q==3:
    testcase03()
elif q==4:
    testcase04()
elif q==5:
    testcase05()
elif q==6:
    testcase06()
elif q==7:
    testcase07()
elif q==8:
    testcase08()
elif q==9:
    testcase09()
elif q==10:
    testcase10()