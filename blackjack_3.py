# blackjack na minimalkah 2
"""
1. туз всегда равен 1, а должно быть 1 или 11
"""

import random

class Player:

    def __init__(self, name, cash=100, bet=0, points=0, decision=False):
        self.name = name
        self.cash = cash
        self.bet = bet
        cards_pack = []
        self.cards_pack = cards_pack
        self.points = points
        self.decision = decision

    def give_card(self):
        # global deck
        self.cards_pack.append(deck.pop())

    def place_bet(self):
        while True:
            try:
                self.bet = int(input('Ваша ставка:'))
                if self.bet <= self.cash:
                    self.cash -= self.bet
                    break
                else:
                    print('Та де в тебе такі гроші?')
                    continue
            except:
                print('Ошибка, введите число!')
                continue

    def print_cards(self):
        print('%s cards:' % self.name, [str(card.suit) + str(card.rank) for card in self.cards_pack])

    def make_decision(self):
        while True:
            decision = str(input('Ваше решение (hit/pass):')[0].lower())
            if decision == 'h':
                self.decision = True
                break
            elif decision == 'p':
                self.decision = False
                break
            else:
                continue

    def make_move(self):
        # pick card or not
        while True:
            self.make_decision()
            if self.decision:
                self.give_card()
                self.print_cards()
                if self.check_for_max_points():
                    print('У {self.name} перебор'.format(**locals()))
                    break
                else:
                    continue
            elif not self.decision:
                print('Pass')
                break
            else:
                print('cerf')
                break

    def check_for_max_points(self):

        '''
        если очков больше чем 21. должен автоматически проиграть
        :return: True if self.points > 21 / False if self.points <= 21
        '''
        if self.count_points() > 21:
            return True
        return False

    def count_points(self):
        values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                  'K': 10}
        for card in self.cards_pack:
            card.value = values[card.rank]
        points = sum([card.value for card in self.cards_pack])
        # print('POINTS: ', points)
        return points


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


def first_deal():
    random.shuffle(deck)
    player1.cards_pack = []
    dealer.cards_pack = []

    player1.give_card()
    player1.give_card()
    dealer.give_card()
    dealer.give_card()
    print('Dealer cards:', [str(card.suit) + str(card.rank) for card in dealer.cards_pack[1:]])
    # print('Dealer cards:', map(lambda card: str(card.suit) + str(card.rank), player1.cards_pack))
    player1.print_cards()


def dealer_move():
    dealer.print_cards()
    while dealer.count_points() <= 16:
        dealer.give_card()
        dealer.print_cards()



def find_winner(player, dealer):
    if player.count_points() > dealer.count_points():
        player.cash += player.bet * 2
        print('Победил {player.name}, баланс {player.cash}'.format(**locals()))
    elif player.count_points() < dealer.count_points():
        print('Диллер победил! На счету осталось: %s' % player.cash)
    else:
        print('Поровну')
        player.cash += player.bet


def play_again():
    while True:
        decision = str(input('Играем снова? (yes/no):')[0].lower())
        if decision == 'y':
            return True
        elif decision == 'n':
            return False
        else:
            continue


def deck_shuffle():
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit, rank))


deck = []
suits = ['C', 'D', 'H', 'S']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def game_main():
    global player1, dealer

    deck_shuffle()
    player1 = Player(input('Введите имя:'))
    print('Ваш баланс: %s' % player1.cash)
    dealer = Player('dealer')

    while True:  # game loop
        player1.place_bet()
        first_deal()
        player1.make_move()
        if player1.check_for_max_points():
            print('На счету {} осталось {} грошей'.format(player1.name, player1.cash))
            continue
        dealer_move()
        find_winner(player1, dealer)

        if play_again():
            continue
        else:
            break


if __name__ == '__main__':
    game_main()
