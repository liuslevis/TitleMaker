#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

PUBG 絕地求生 爆笑精華&精彩操作合輯 EP1 (playerunknown's battlegrounds)

【絕地求生 - 精彩鏡頭#1】PUBG 最強實力玩家：Shroud

30殺 Shroud SOLO FPP － PUBG 精華#1 －【 絕地求生 PUBG 】

絕地求生 精彩擊殺 -Kar98特輯- PUBG Highlights Ep.3


景三求生精彩時刻 (PlayerUnknown's Battlegrounds)

絕地求生PUBG精彩moment # 1【仲HOW精華】

【絕地求生PUBG】精彩重播XD

絕地求生 精彩時刻 SaiHoPUBG Highlight #6

11/4 PUBG精彩時刻-2

DOUYU QQQ 娱乐LYB精彩集錦 绝地求生 PUBG
TIMBK PUBG

絕地求生|PUBG【CAM11111111】 M16&S12K 行雲流水般的精彩作戰 FPP 四排吃雞 with TreadstoneTW iangood PizzK3 2017/9/27


PUBG精彩击杀集锦！

【絕地求生PUBG】精彩重播5 又遇到BUG...

絕地求生 | PUBG 21殺精彩吃雞 !! SniperSR直播精華

PUBG精彩誤殺

绝地求生大逃杀PUBG_ 欢乐时刻Ep. 11

播单 【逍遥小枫】双排吃鸡, 简直惊心动魄啊! | 绝地求生大逃杀

PUBG绝对求生教学：最详细的绝地求生教程，新手必看 - 吃鸡专

★绝地求生 PUBG★想做黄雀的蝉 #G22★酷爱娱乐解说

绝地求生大逃杀PUBG集锦# 1 -难以置信的1000m镜头


17《绝地求生大逃杀》（吃鸡）国外玩家精..集锦-07-PUBG


绝地求生大逃杀pubg WTF搞笑瞬间集锦132

T.N.T PUBG 个人集锦


绝地求..北美职业玩家Shroud最强的PUBG玩家之一精彩集锦

PUBG WTF 绝地求生搞笑集锦第70期：天降正义

[寒霜】PUBG精彩时刻 P1


绝地..pubg精彩操作&搞笑视频集锦ep107五车连环相撞事故

PUBG绝地求生精彩操作

【绝地求生：大逃杀（PUBG）】twitch直播精彩瞬间


《绝地求生》大逃杀 PUBG 吃鸡 精彩视频集锦02

'''
import random

def gen_huya_pubg_titles():
    mat = [
        ['PUBG ', 'PUBG: ', '绝地求生 ', '绝地求生：', '绝地求生：大逃杀 '],
        ['直播', '主播', ''],
        ['精彩'],# '搞笑''
        ['击杀', ''],
        ['时刻', '瞬间', ' moment ', '集锦', '一刻', '操作', '镜头', '回放', '剪辑', '片段', '合集'],
    ]
    ret = []
    for i in mat[0]:
        for j in mat[1]:
            for k in mat[2]:
                for l in mat[3]:
                    for m in mat[4]:
                        title = i + j + k + l + m
                        ret.append(title)
    return ret

titles = gen_huya_pubg_titles()
random.shuffle(titles)
print('\n'.join(titles))
print('num:', len(titles))
print(random.choice(titles))
