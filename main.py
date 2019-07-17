import time
import os

# import our modules
from display.menu import *
from display.show import *
from machine.std_mach import *
from dealer.mike import *

dsp_start()
time.sleep(1)  # 延迟两秒

game_type = dsp_choice_game()

deck = []
if(game_type == 1 or game_type == 2 or game_type == 3 or game_type == 4):
    make_deck_by_type(game_type, deck)
else:
    dsp_end()
    exit()

player_a = []
player_b = []
player_c = []
player_d = []
player_dumy = []

if game_type == 1:
    deal_to_multi_players(deck, player_a, player_b, player_c)
    record_deck(player_a, '争上游01的副牌.txt')
    record_deck(player_b, '争上游02的副牌.txt')
    record_deck(player_c, '争上游03的副牌.txt')
if game_type == 2:
    deal_to_multi_players(deck, player_a, player_b, player_c, player_d)
    record_deck(player_a, '桥牌01的副牌.txt')
    record_deck(player_b, '桥牌02的副牌.txt')
    record_deck(player_c, '桥牌03的副牌.txt')
    record_deck(player_d, '桥牌04的副牌.txt')
if game_type == 3:
    deal_to_multi_players_remain(
        deck, 3, player_dumy, player_a, player_b, player_c, player_d)
    record_deck(player_a, '三人斗地主01的副牌.txt')
    record_deck(player_b, '三人斗地主02的副牌.txt')
    record_deck(player_c, '三人斗地主03的副牌.txt')
    record_deck(player_d, '三人斗地主04的副牌.txt')
    record_deck(player_dumy, '三人斗地主-预留牌.txt')
if game_type == 4:
    deal_to_multi_players_remain(
        deck, 8, player_dumy, player_a, player_b, player_c, player_d)
    record_deck(player_a, '四人斗地主01的副牌.txt')
    record_deck(player_b, '四人斗地主02的副牌.txt')
    record_deck(player_c, '四人斗地主03的副牌.txt')
    record_deck(player_d, '四人斗地主04的副牌.txt')
    record_deck(player_dumy, '四人斗地主-预留牌.txt')
