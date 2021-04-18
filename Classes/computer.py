from .constants import HANDS
import random
'''
        self.win = win
        self.player_name = player_name
        self.player_num = player_num
        self.stack = start_amt
        self.hand = []
        self.board_cards = []
        self.buttons = []
        self.hand_num = 0 #your hand + board cards
        self.high_card = 0
'''

class Computer(Player):
    
    def takeATurn(self, curr_bet, prev_bet):
        amt_to_stay_in = curr_bet - prev_bet
        self.hand = [Card1, Card2]
        c1rank = self.hand[0].rank
        c2rank = self.hand[1].rank
        c1suit = self.hand[0].suit
        c2suit = self.hand[1].suit
        if len(self.board_cards) == 0: #preflop
            if ( not self.pre_flop_fold(curr_bet, prev_bet)): #not folding preflop
                if c1rank == c2rank: #pocket pair
                    if c1rank == 11 or c1rank == 12 or c1rank == 10:  #pocket queens, kings or aces
                        return self.stack
                    else:
                        return curr_bet
                else: 
                    if c1rank > 10 and c2rank > 10: #2 high cards
                        if amt_to_stay_in < self.stack / 8:
                            return amt_to_stay_in
                        else: 
                            return -1
                    else:
                        if (bluff()):  #bluff call
                            return amt_to_stay_in
                        else:
                            return -1 #fold
            else: 
                return -1
        else:
            if len(self.board_cards) == 3: #flop
                if (bluff()):
                    return amt_to_stay_in * 2.25
                else:
                    if self.hand_num == 0:
                        if amt_to_stay_in > 0:
                            return -1
                        else:
                            return 0 #check
                    if self.hand_num == 1:
                        if(bluff()):
                            return amt_to_stay_in * 2
                        else: 
                            if amt_to_stay_in > 0:
                                return -1
                            else:
                                return 0 
                    if self.hand_num == 2:
                        if(bluff()):
                            return self.stack
                        else:
                            if amt_to_stay_in > 0:
                                return amt_to_stay_in * 2
                            else: 
                                return amt_to_stay_in * 1.5
                    if self.hand_num == 3:
                        if(bluff()):
                            return amt_to_stay_in * 3
                        else:
                            if amt_to_stay_in > 0:
                                return amt_to_stay_in 
                            else:
                                return amt_to_stay_in * 1.5
                    if self.hand_num == 4:
                        if(bluff()):
                            return amt_to_stay_in * 2
                        else:
                            if amt_to_stay_in > 0:
                                return amt_to_stay_in
                            else:
                                return 0
                    if self.hand_num > 4:
                        return amt_to_stay_in
            
            if len(self.board_cards) == 4: #turn
                if self.hand_num == 0:
                    if amt_to_stay_in > 0:
                        return -1
                    else:
                        return 0
                if self.hand_num == 1:
                    if(bluff()):
                        return amt_to_stay_in * 2
                    else:
                        if amt_to_stay_in > 0:
                            if random.random() > .7:
                                return amt_to_stay_in
                            else:
                                return -1
                        else:
                            return 0
                if self.hand_num == 2:
                    if(bluff()):
                        return amt_to_stay_in * 2
                    else:
                        if amt_to_stay_in > 0:
                            return amt_to_stay_in
                        else:
                            return 0
                if self.hand_num == 3:
                    if(bluff()):
                        return amt_to_stay_in * 2.5
                    else:
                        if amt_to_stay_in > 0:
                            return amt_to_stay_in
                        else:
                            return 0
                if self.hand_num == 4:
                    if(bluff()):
                        return 0
                    else:
                        if amt_to_stay_in > 0:
                            return amt_to_stay_in * 2
                        else:
                            return amt_to_stay_in * 1.5
                if self.hand_num == 5:
                    if(bluff()):
                        return self.stack
                    else:
                        if amt_to_stay_in > 0:
                            return amt_to_stay_in * 2
                        else:
                            return 0
                if self.hand_num > 5:
                    if(bluff()):
                        return self.stack
                    else:
                        return 0
            if len(self.boad_cards) == 5:
                if self.hand_num == 0:
                    if(bluff()):
                        return self.stack
                    else:
                        if amt_to_stay_in > 0:
                            return -1
                        else:
                            return 0

                if self.hand_num == 1:
                    if(bluff()):
                        return amt_to_stay_in * 2
                    else:
                        if amt_to_stay_in > 0:
                            if random.random() > 0.6:
                                return amt_to_stay_in
                            else:
                                return -1
                        else:
                            return 0
                if self.hand_num == 2: 
                    if(bluff()):
                        return self.stack
                    else:
                        if amt_to_stay_in > 0:
                            return amt_to_stay_in
                        else:
                            return 0
                if self.hand_num == 3:
                    if(bluff()):
                        return amt_to_stay_in * 2
                    else:
                        if amt_to_stay_in > 0:
                            return amt_to_stay_in
                        else: 
                            return 0
                if self.hand_num == 4:
                    if(bluff()):
                        return self.stack
                    else:
                        if amt_to_stay_in > 0:
                            return amt_to_stay_in
                        else: 
                            return amt_to_stay_in * 3
                if self.hand_num == 5:
                    if(bluff()):
                        return self.stack
                    else:
                        if amt_to_stay_in > 0: 
                            return amt_to_stay_in * 3
                        else:
                            return amt_to_stay_in * 2
                if self.hand_num > 5:
                    if(bluff()):
                        return 0
                    else:
                        return self.stack
                        
    def pre_flop_fold(self, curr_bet, prev_bet):
        #returns true if folding
        #false if elsewise

        amt_to_stay_in = curr_bet - prev_bet

        if amt_to_stay_in <= BIG_BLIND:
            return False
        else:
            self.hand = [Card1, Card2]
            c1rank = self.hand[0].rank
            c2rank = self.hand[1].rank
            c1suit = self.hand[0].suit
            c2suit = self.hand[1].suit

            if c1rank > 10 and c2rank > 10: #2 high cards
                return False

            if c1rank == c2rank: #pocket pair
                return False
            
            if c2suit == c2suit: #suited
                if c1rank > 8 or c2rank > 8:
                    return False
                else:
                    return True
            
    '''
    def determineOutcome():
        cutoff = 0.5
        if self.hand_num > self.hand_num_board:
            cutoff = cutoff + 0.1
            if len(self.board_cards) < 4:
                cutoff = cutoff + 0.1
                '''

    def bluff():
        if random.random() > 0.7:
            return True
        else:
            return False

    