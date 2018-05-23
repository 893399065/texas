import os
def rankKickers(ranks, noOfCards):

    kickerRank = 0.0000
    myRanks = []
    rank = ''

    for i in range(0, noOfCards):

        rank = ranks[i]

        if (rank == 'A') :
            myRanks.append(0.2048)
        
        if (rank == 'K') :
            myRanks.append(0.1024)
        
        if (rank == 'Q') :
            myRanks.append(0.0512)
        
        if (rank == 'J') :
            myRanks.append(0.0256)
        
        if (rank == 'T') :
            myRanks.append(0.0128)
        
        if (rank == '9') :
            myRanks.append(0.0064)
        
        if (rank == '8') :
            myRanks.append(0.0032)
        
        if (rank == '7') :
            myRanks.append(0.0016)
        
        if (rank == '6') :
            myRanks.append(0.0008)
        
        if (rank == '5') :
            myRanks.append(0.0004)
        
        if (rank == '4') :
            myRanks.append(0.0002)
        
        if (rank == '3') :
            myRanks.append(0.0001)
        
        if (rank == '2') :
            myRanks.append(0.0000)
        
    
    for i in range(0, noOfCards):
        kickerRank += myRanks[i]

    return kickerRank




def rankHandInt(hand) :
    # 此时hand为列表
    rank = 0.0000
    message = ""
    handRanks = ""
    handSuits = ""
    for i in range(0, 5):
        if(len(hand[i]) == 2):
            handRanks += hand[i][0]
            handSuits += hand[i][1]
        else:
            print (hand[i])

    handRanks = list(handRanks)
    handRanks.sort()
    s1 = "".join(handRanks)
    handSuits = list(handSuits)
    handSuits.sort()
    s2 = "".join(handSuits)
    ranks = s1
    suits = s2
    cards = hand

    # Four of a kind
    if (rank == 0) :
        if "AAAA" in ranks :
            rank = 292 + rankKickers(ranks.replace('AAAA', ''), 1)
        
        if "KKKK" in ranks and rank == 0:
            rank = 291 + rankKickers(ranks.replace('KKKK', ''), 1)
        
        if "QQQQ" in ranks and rank == 0:
            rank = 290 + rankKickers(ranks.replace('QQQQ', ''), 1)
        
        if "JJJJ" in ranks and rank == 0:
            rank = 289 + rankKickers(ranks.replace('JJJJ', ''), 1);
        
        if "TTTT" in ranks and rank == 0:
            rank = 288 + rankKickers(ranks.replace('TTTT', ''), 1);
        
        if "9999" in ranks and rank == 0:
            rank = 287 + rankKickers(ranks.replace('9999', ''), 1);
        
        if "8888" in ranks and rank == 0:
            rank = 286 + rankKickers(ranks.replace('8888', ''), 1);
        
        if "7777" in ranks and rank == 0:
            rank = 285 + rankKickers(ranks.replace('7777', ''), 1);
        
        if "6666" in ranks and rank == 0:
            rank = 284 + rankKickers(ranks.replace('6666', ''), 1);
        
        if "5555" in ranks and rank == 0:
            rank = 283 + rankKickers(ranks.replace('5555', ''), 1);
        
        if "4444" in ranks and rank == 0:
            rank = 282 + rankKickers(ranks.replace('4444', ''), 1);
        
        if "3333" in ranks and rank == 0:
            rank = 281 + rankKickers(ranks.replace('3333', ''), 1);
        
        if "2222" in ranks and rank == 0:
            rank = 280 + rankKickers(ranks.replace('2222', ''), 1);
                

        
        if (rank != 0) :
            message = 'Four of a kind'
        
    

    # Full House
    if (rank == 0) :
        if "AAA" in ranks and "KK" in ranks and rank == 0:
            rank = 279
        
        if "AAA" in ranks and "QQ" in ranks and rank == 0:
            rank = 278
        
        if "AAA" in ranks and "JJ" in ranks and rank == 0:
            rank = 277
        
        if "AAA" in ranks and "TT" in ranks and rank == 0:
            rank = 276
        
        if "AAA" in ranks and "99" in ranks and rank == 0:
            rank = 275
        
        if "AAA" in ranks and "88" in ranks and rank == 0:
            rank = 274
        
        if "AAA" in ranks and "77" in ranks and rank == 0:
            rank = 273
        
        if "AAA" in ranks and "66" in ranks and rank == 0:
            rank = 272
        
        if "AAA" in ranks and "55" in ranks and rank == 0:
            rank = 271
        
        if "AAA" in ranks and "44" in ranks and rank == 0:
            rank = 270
        
        if "AAA" in ranks and "33" in ranks and rank == 0:
            rank = 269
        
        if "AAA" in ranks and "22" in ranks and rank == 0:
            rank = 268
        
        if "KKK" in ranks and "AA" in ranks and rank == 0:
            rank = 267
        
        if "KKK" in ranks and "QQ" in ranks and rank == 0:
            rank = 266
        
        if "KKK" in ranks and "JJ" in ranks and rank == 0:
            rank = 265
        
        if "KKK" in ranks and "TT" in ranks and rank == 0:
            rank = 264
        
        if "KKK" in ranks and "99" in ranks and rank == 0:
            rank = 263
        
        if "KKK" in ranks and "88" in ranks and rank == 0:
            rank = 262
        
        if "KKK" in ranks and "77" in ranks and rank == 0:
            rank = 261
        
        if "KKK" in ranks and "66" in ranks and rank == 0:
            rank = 260
        
        if "KKK" in ranks and "55" in ranks and rank == 0:
            rank = 259
        
        if "KKK" in ranks and "44" in ranks and rank == 0:
            rank = 258
        
        if "KKK" in ranks and "33" in ranks and rank == 0:
            rank = 257
        
        if "KKK" in ranks and "22" in ranks and rank == 0:
            rank = 256
        
        if "QQQ" in ranks and "AA" in ranks and rank == 0:
            rank = 255
        
        if "QQQ" in ranks and "KK" in ranks and rank == 0:
            rank = 254
        
        if "QQQ" in ranks and "JJ" in ranks and rank == 0:
            rank = 253
        
        if "QQQ" in ranks and "TT" in ranks and rank == 0:
            rank = 252
        
        if "QQQ" in ranks and "99" in ranks and rank == 0:
            rank = 251
        
        if "QQQ" in ranks and "88" in ranks and rank == 0:
            rank = 250
        
        if "QQQ" in ranks and "77" in ranks and rank == 0:
            rank = 249
        
        if "QQQ" in ranks and "66" in ranks and rank == 0:
            rank = 248
        
        if "QQQ" in ranks and "55" in ranks and rank == 0:
            rank = 247
        
        if "QQQ" in ranks and "44" in ranks and rank == 0:
            rank = 246
        
        if "QQQ" in ranks and "33" in ranks and rank == 0:
            rank = 245
        
        if "QQQ" in ranks and "22" in ranks and rank == 0:
            rank = 244
        
        if "JJJ" in ranks and "AA" in ranks and rank == 0:
            rank = 243
        
        if "JJJ" in ranks and "KK" in ranks and rank == 0:
            rank = 242
        
        if "JJJ" in ranks and "QQ" in ranks and rank == 0:
            rank = 241
        
        if "JJJ" in ranks and "TT" in ranks and rank == 0:
            rank = 240
        
        if "JJJ" in ranks and "99" in ranks and rank == 0:
            rank = 239
        
        if "JJJ" in ranks and "88" in ranks and rank == 0:
            rank = 238
        
        if "JJJ" in ranks and "77" in ranks and rank == 0:
            rank = 237
        
        if "JJJ" in ranks and "66" in ranks and rank == 0:
            rank = 236
        
        if "JJJ" in ranks and "55" in ranks and rank == 0:
            rank = 235
        
        if "JJJ" in ranks and "44" in ranks and rank == 0:
            rank = 234
        
        if "JJJ" in ranks and "33" in ranks and rank == 0:
            rank = 233
        
        if "JJJ" in ranks and "22" in ranks and rank == 0:
            rank = 232
        
        if "TTT" in ranks and "AA" in ranks and rank == 0:
            rank = 231
        
        if "TTT" in ranks and "KK" in ranks and rank == 0:
            rank = 230
        
        if "TTT" in ranks and "QQ" in ranks and rank == 0:
            rank = 229
        
        if "TTT" in ranks and "JJ" in ranks and rank == 0:
            rank = 228
        
        if "TTT" in ranks and "99" in ranks and rank == 0:
            rank = 227
        
        if "TTT" in ranks and "88" in ranks and rank == 0:
            rank = 226
        
        if "TTT" in ranks and "77" in ranks and rank == 0:
            rank = 225
        
        if "TTT" in ranks and "66" in ranks and rank == 0:
            rank = 224
        
        if "TTT" in ranks and "55" in ranks and rank == 0:
            rank = 223
        
        if "TTT" in ranks and "44" in ranks and rank == 0:
            rank = 222
        
        if "TTT" in ranks and "33" in ranks and rank == 0:
            rank = 221
        
        if "TTT" in ranks and "22" in ranks and rank == 0:
            rank = 220
        
        if "999" in ranks and "AA" in ranks and rank == 0:
            rank = 219
        
        if "999" in ranks and "KK" in ranks and rank == 0:
            rank = 218
        
        if "999" in ranks and "QQ" in ranks and rank == 0:
            rank = 217
        
        if "999" in ranks and "JJ" in ranks and rank == 0:
            rank = 216
        
        if "999" in ranks and "TT" in ranks and rank == 0:
            rank = 215
        
        if "999" in ranks and "88" in ranks and rank == 0:
            rank = 214
        
        if "999" in ranks and "77" in ranks and rank == 0:
            rank = 213
        
        if "999" in ranks and "66" in ranks and rank == 0:
            rank = 212
        
        if "999" in ranks and "55" in ranks and rank == 0:
            rank = 211
        
        if "999" in ranks and "44" in ranks and rank == 0:
            rank = 210
        
        if "999" in ranks and "33" in ranks and rank == 0:
            rank = 209
        
        if "999" in ranks and "22" in ranks and rank == 0:
            rank = 208
        
        if "888" in ranks and "AA" in ranks and rank == 0:
            rank = 207
        
        if "888" in ranks and "KK" in ranks and rank == 0:
            rank = 206
        
        if "888" in ranks and "QQ" in ranks and rank == 0:
            rank = 205
        
        if "888" in ranks and "JJ" in ranks and rank == 0:
            rank = 204
        
        if "888" in ranks and "TT" in ranks and rank == 0:
            rank = 203
        
        if "888" in ranks and "99" in ranks and rank == 0:
            rank = 202
        
        if "888" in ranks and "77" in ranks and rank == 0:
            rank = 201
        
        if "888" in ranks and "66" in ranks and rank == 0:
            rank = 200
        
        if "888" in ranks and "55" in ranks and rank == 0:
            rank = 199
        
        if "888" in ranks and "44" in ranks and rank == 0:
            rank = 198
        
        if "888" in ranks and "33" in ranks and rank == 0:
            rank = 197
        
        if "888" in ranks and "22" in ranks and rank == 0:
            rank = 196
        
        if "777" in ranks and "AA" in ranks and rank == 0:
            rank = 195
        
        if "777" in ranks and "KK" in ranks and rank == 0:
            rank = 194
        
        if "777" in ranks and "QQ" in ranks and rank == 0:
            rank = 193
        
        if "777" in ranks and "JJ" in ranks and rank == 0:
            rank = 192
        
        if "777" in ranks and "TT" in ranks and rank == 0:
            rank = 191
        
        if "777" in ranks and "99" in ranks and rank == 0:
            rank = 190
        
        if "777" in ranks and "88" in ranks and rank == 0:
            rank = 189
        
        if "777" in ranks and "66" in ranks and rank == 0:
            rank = 188
        
        if "777" in ranks and "55" in ranks and rank == 0:
            rank = 187
        
        if "777" in ranks and "44" in ranks and rank == 0:
            rank = 186
        
        if "777" in ranks and "33" in ranks and rank == 0:
            rank = 185
        
        if "777" in ranks and "22" in ranks and rank == 0:
            rank = 184
        
        if "666" in ranks and "AA" in ranks and rank == 0:
            rank = 183
        
        if "666" in ranks and "KK" in ranks and rank == 0:
            rank = 182
        
        if "666" in ranks and "QQ" in ranks and rank == 0:
            rank = 181
        
        if "666" in ranks and "JJ" in ranks and rank == 0:
            rank = 180
        
        if "666" in ranks and "TT" in ranks and rank == 0:
            rank = 179
        
        if "666" in ranks and "99" in ranks and rank == 0:
            rank = 178
        
        if "666" in ranks and "88" in ranks and rank == 0:
            rank = 177
        
        if "666" in ranks and "77" in ranks and rank == 0:
            rank = 176
        
        if "666" in ranks and "55" in ranks and rank == 0:
            rank = 175
        
        if "666" in ranks and "44" in ranks and rank == 0:
            rank = 174
        
        if "666" in ranks and "33" in ranks and rank == 0:
            rank = 173
        
        if "666" in ranks and "22" in ranks and rank == 0:
            rank = 172
        
        if "555" in ranks and "AA" in ranks and rank == 0:
            rank = 171
        
        if "555" in ranks and "KK" in ranks and rank == 0:
            rank = 170
        
        if "555" in ranks and "QQ" in ranks and rank == 0:
            rank = 169
        
        if "555" in ranks and "JJ" in ranks and rank == 0:
            rank = 168
        
        if "555" in ranks and "TT" in ranks and rank == 0:
            rank = 167
        
        if "555" in ranks and "99" in ranks and rank == 0:
            rank = 166
        
        if "555" in ranks and "88" in ranks and rank == 0:
            rank = 165
        
        if "555" in ranks and "77" in ranks and rank == 0:
            rank = 164
        
        if "555" in ranks and "66" in ranks and rank == 0:
            rank = 163
        
        if "555" in ranks and "44" in ranks and rank == 0:
            rank = 162
        
        if "555" in ranks and "33" in ranks and rank == 0:
            rank = 161
        
        if "555" in ranks and "22" in ranks and rank == 0:
            rank = 160
        
        if "444" in ranks and "AA" in ranks and rank == 0:
            rank = 159
        
        if "444" in ranks and "KK" in ranks and rank == 0:
            rank = 158
        
        if "444" in ranks and "QQ" in ranks and rank == 0:
            rank = 157
        
        if "444" in ranks and "JJ" in ranks and rank == 0:
            rank = 156
        
        if "444" in ranks and "TT" in ranks and rank == 0:
            rank = 155
        
        if "444" in ranks and "99" in ranks and rank == 0:
            rank = 154
        
        if "444" in ranks and "88" in ranks and rank == 0:
            rank = 153
        
        if "444" in ranks and "77" in ranks and rank == 0:
            rank = 152
        
        if "444" in ranks and "66" in ranks and rank == 0:
            rank = 151
        
        if "444" in ranks and "55" in ranks and rank == 0:
            rank = 150
        
        if "444" in ranks and "33" in ranks and rank == 0:
            rank = 149
        
        if "444" in ranks and "22" in ranks and rank == 0:
            rank = 148
        
        if "333" in ranks and "AA" in ranks and rank == 0:
            rank = 147
        
        if "333" in ranks and "KK" in ranks and rank == 0:
            rank = 146
        
        if "333" in ranks and "QQ" in ranks and rank == 0:
            rank = 145
        
        if "333" in ranks and "JJ" in ranks and rank == 0:
            rank = 144
        
        if "333" in ranks and "TT" in ranks and rank == 0:
            rank = 143
        
        if "333" in ranks and "99" in ranks and rank == 0:
            rank = 142
        
        if "333" in ranks and "88" in ranks and rank == 0:
            rank = 141
        
        if "333" in ranks and "77" in ranks and rank == 0:
            rank = 140
        
        if "333" in ranks and "66" in ranks and rank == 0:
            rank = 139
        
        if "333" in ranks and "55" in ranks and rank == 0:
            rank = 138
        
        if "333" in ranks and "44" in ranks and rank == 0:
            rank = 137
        
        if "333" in ranks and "22" in ranks and rank == 0:
            rank = 136
        
        if "222" in ranks and "AA" in ranks and rank == 0:
            rank = 135
        
        if "222" in ranks and "KK" in ranks and rank == 0:
            rank = 134
        
        if "222" in ranks and "QQ" in ranks and rank == 0:
            rank = 133
        
        if "222" in ranks and "JJ" in ranks and rank == 0:
            rank = 132
        
        if "222" in ranks and "TT" in ranks and rank == 0:
            rank = 131
        
        if "222" in ranks and "99" in ranks and rank == 0:
            rank = 130
        
        if "222" in ranks and "88" in ranks and rank == 0:
            rank = 129
        
        if "222" in ranks and "77" in ranks and rank == 0:
            rank = 128
        
        if "222" in ranks and "66" in ranks and rank == 0:
            rank = 127
        
        if "222" in ranks and "55" in ranks and rank == 0:
            rank = 126
        
        if "222" in ranks and "44" in ranks and rank == 0:
            rank = 125
        
        if "222" in ranks and "33" in ranks and rank == 0:
            rank = 124
        
        if (rank != 0) :
            message = 'Full House'
        
    

    # Flush
    if (rank == 0) :
        if ("CCCCC" in suits or "DDDDD" in suits or "HHHHH" in suits or "SSSSS" in suits):
            rank = 123
            message = 'Flush'
        

        # Straight flush
        if (("TC" in cards) and ("JC" in cards) and ("QC" in cards) and ("KC" in cards) and ("AC" in cards) and (rank == 123) and rank == 0):
            rank = 302
            message = 'Royal Flush'
        
        if (("TD" in cards) and ("JD" in cards) and ("QD" in cards) and ("KD" in cards) and ("AD" in cards) and (rank == 123) and rank == 0):
            rank = 302
            message = 'Royal Flush'
        
        if (("TH" in cards) and ("JH" in cards) and ("QH" in cards) and ("KH" in cards) and ("AH" in cards) and (rank == 123) and rank == 0):
            rank = 302
            message = 'Royal Flush'
        
        if (("TS" in cards) and ("JS" in cards) and ("QS" in cards) and ("KS" in cards) and ("AS" in cards) and (rank == 123) and rank == 0):
            rank = 302
            message = 'Royal Flush'
        
        if (("TC" in cards) and ("JC" in cards) and ("QC" in cards) and ("KC" in cards) and ("9C" in cards) and (rank == 123) and rank == 0):
            rank = 301
            message = 'Straight Flush'
        
        if (("TD" in cards) and ("JD" in cards) and ("QD" in cards) and ("KD" in cards) and ("9D" in cards) and (rank == 123) and rank == 0):
            rank = 301
            message = 'Straight Flush'
        
        if (("TH" in cards) and ("JH" in cards) and ("QH" in cards) and ("KH" in cards) and ("9H" in cards) and (rank == 123) and rank == 0):
            rank = 301
            message = 'Straight Flush'
        
        if (("TS" in cards) and ("JS" in cards) and ("QS" in cards) and ("KS" in cards) and ("9S" in cards) and (rank == 123) and rank == 0):
            rank = 301
            message = 'Straight Flush'
        
        if (("TC" in cards) and ("JC" in cards) and ("QC" in cards) and ("8C" in cards) and ("9C" in cards) and (rank == 123) and rank == 0):
            rank = 301
            message = 'Straight Flush'
        if (("TD" in cards) and ("JD" in cards) and ("QD" in cards) and ("8D" in cards) and ("9D" in cards) and (rank == 123) and rank == 0):
            rank = 300
            message = 'Straight Flush'
        
        if (("TH" in cards) and ("JH" in cards) and ("QH" in cards) and ("8H" in cards) and ("9H" in cards) and (rank == 123) and rank == 0):
            rank = 300
            message = 'Straight Flush'
        
        if (("TS" in cards) and ("JS" in cards) and ("QS" in cards) and ("8S" in cards) and ("9S" in cards) and (rank == 123) and rank == 0):
            rank = 300
            message = 'Straight Flush'
        
        if (("TC" in cards) and ("JC" in cards) and ("7C" in cards) and ("8C" in cards) and ("9C" in cards) and (rank == 123) and rank == 0):
            rank = 299
            message = 'Straight Flush'
        
        if (("TD" in cards) and ("JD" in cards) and ("7D" in cards) and ("8D" in cards) and ("9D" in cards) and (rank == 123) and rank == 0):
            rank = 299
            message = 'Straight Flush'
        
        if (("TH" in cards) and ("JH" in cards) and ("7H" in cards) and ("8H" in cards) and ("9H" in cards) and (rank == 123) and rank == 0):
            rank = 299
            message = 'Straight Flush'
        
        if (("TS" in cards) and ("JS" in cards) and ("7S" in cards) and ("8S" in cards) and ("9S" in cards) and (rank == 123) and rank == 0):
            rank = 299
            message = 'Straight Flush'
        
        if (("TC" in cards) and ("6C" in cards) and ("7C" in cards) and ("8C" in cards) and ("9C" in cards) and (rank == 123) and rank == 0):
            rank = 298
            message = 'Straight Flush'
        
        if (("TD" in cards) and ("6D" in cards) and ("7D" in cards) and ("8D" in cards) and ("9D" in cards) and (rank == 123) and rank == 0):
            rank = 298
            message = 'Straight Flush'
        
        if (("TH" in cards) and ("6H" in cards) and ("7H" in cards) and ("8H" in cards) and ("9H" in cards) and (rank == 123) and rank == 0):
            rank = 298
            message = 'Straight Flush'
        
        if (("TS" in cards) and ("6S" in cards) and ("7S" in cards) and ("8S" in cards) and ("9S" in cards) and (rank == 123) and rank == 0):
            rank = 298
            message = 'Straight Flush'
        
        if (("5C" in cards) and ("6C" in cards) and ("7C" in cards) and ("8C" in cards) and ("9C" in cards) and (rank == 123) and rank == 0):
            rank = 297
            message = 'Straight Flush'
        
        if (("5D" in cards) and ("6D" in cards) and ("7D" in cards) and ("8D" in cards) and ("9D" in cards) and (rank == 123) and rank == 0):
            rank = 297
            message = 'Straight Flush'
        
        if (("5H" in cards) and ("6H" in cards) and ("7H" in cards) and ("8H" in cards) and ("9H" in cards) and (rank == 123) and rank == 0):
            rank = 297
            message = 'Straight Flush'
        
        if (("5S" in cards) and ("6S" in cards) and ("7S" in cards) and ("8S" in cards) and ("9S" in cards) and (rank == 123) and rank == 0):
            rank = 297
            message = 'Straight Flush'
        
        if (("5C" in cards) and ("6C" in cards) and ("7C" in cards) and ("8C" in cards) and ("4C" in cards) and (rank == 123) and rank == 0):
            rank = 296
            message = 'Straight Flush'
        
        if (("5D" in cards) and ("6D" in cards) and ("7D" in cards) and ("8D" in cards) and ("4D" in cards) and (rank == 123) and rank == 0):
            rank = 296
            message = 'Straight Flush'
        
        if (("5H" in cards) and ("6H" in cards) and ("7H" in cards) and ("8H" in cards) and ("4H" in cards) and (rank == 123) and rank == 0):
            rank = 296
            message = 'Straight Flush'
        
        if (("5S" in cards) and ("6S" in cards) and ("7S" in cards) and ("8S" in cards) and ("4S" in cards) and (rank == 123) and rank == 0):
            rank = 296
            message = 'Straight Flush'
        
        if (("5C" in cards) and ("6C" in cards) and ("7C" in cards) and ("3C" in cards) and ("4C" in cards) and (rank == 123) and rank == 0):
            rank = 295
            message = 'Straight Flush'
        
        if (("5D" in cards) and ("6D" in cards) and ("7D" in cards) and ("3D" in cards) and ("4D" in cards) and (rank == 123) and rank == 0):
            rank = 295
            message = 'Straight Flush'
        
        if (("5H" in cards) and ("6H" in cards) and ("7H" in cards) and ("3H" in cards) and ("4H" in cards) and (rank == 123) and rank == 0):
            rank = 295
            message = 'Straight Flush'
        
        if (("5S" in cards) and ("6S" in cards) and ("7S" in cards) and ("3S" in cards) and ("4S" in cards) and (rank == 123) and rank == 0):
            rank = 295
            message = 'Straight Flush'
        
        if (("5C" in cards) and ("6C" in cards) and ("2C" in cards) and ("3C" in cards) and ("4C" in cards) and (rank == 123) and rank == 0):
            rank = 294
            message = 'Straight Flush'
        
        if (("5D" in cards) and ("6D" in cards) and ("2D" in cards) and ("3D" in cards) and ("4D" in cards) and (rank == 123) and rank == 0):
            rank = 294
            message = 'Straight Flush'
        
        if (("5H" in cards) and ("6H" in cards) and ("2H" in cards) and ("3H" in cards) and ("4H" in cards) and (rank == 123) and rank == 0):
            rank = 294
            message = 'Straight Flush'
        
        if (("5S" in cards) and ("6S" in cards) and ("2S" in cards) and ("3S" in cards) and ("4S" in cards) and (rank == 123) and rank == 0):
            rank = 294
            message = 'Straight Flush'
        
        if (("5C" in cards) and ("AC" in cards) and ("2C" in cards) and ("3C" in cards) and ("4C" in cards) and (rank == 123) and rank == 0):
            rank = 293
            message = 'Straight Flush'
        
        if (("5S" in cards) and ("AS" in cards) and ("2S" in cards) and ("3S" in cards) and ("4S" in cards) and (rank == 123) and rank == 0):
            rank = 293
            message = 'Straight Flush'
        
        if (("5H" in cards) and ("AH" in cards) and ("2H" in cards) and ("3H" in cards) and ("4H" in cards) and (rank == 123) and rank == 0):
            rank = 293
            message = 'Straight Flush'
        
        if (("5D" in cards) and ("AD" in cards) and ("2D" in cards) and ("3D" in cards) and ("4D" in cards) and (rank == 123) and rank == 0):
            rank = 293
            message = 'Straight Flush'
        
        if (rank == 123) :
            rank = rank + rankKickers(ranks, 5)
        

    

    # Straight
    if (rank == 0) :
        if (("T" in ranks) and ("J" in ranks) and ("Q" in ranks) and ("K" in ranks) and("A" in ranks) and rank == 0):
            rank = 122
        
        if (("T" in ranks) and ("J" in ranks) and ("Q" in ranks) and ("K" in ranks) and("9" in ranks) and rank == 0):
            rank = 121
        
        if (("T" in ranks) and ("J" in ranks) and ("Q" in ranks) and ("8" in ranks) and("9" in ranks) and rank == 0):
            rank = 120
        
        if (("T" in ranks) and ("J" in ranks) and ("7" in ranks) and ("8" in ranks) and("9" in ranks) and rank == 0):
            rank = 119
        
        if (("T" in ranks) and ("6" in ranks) and ("7" in ranks) and ("8" in ranks) and("9" in ranks) and rank == 0):
            rank = 118
        
        if (("5" in ranks) and ("6" in ranks) and ("7" in ranks) and ("8" in ranks) and("9" in ranks) and rank == 0):
            rank = 117
        
        if (("5" in ranks) and ("6" in ranks) and ("7" in ranks) and ("8" in ranks) and("4" in ranks) and rank == 0):
            rank = 116
        
        if (("5" in ranks) and ("6" in ranks) and ("7" in ranks) and ("3" in ranks) and("4" in ranks) and rank == 0):
            rank = 115
        
        if (("5" in ranks) and ("6" in ranks) and ("2" in ranks) and ("3" in ranks) and("4" in ranks) and rank == 0):
            rank = 114
        
        if (("5" in ranks) and ("A" in ranks) and ("2" in ranks) and ("3" in ranks) and("4" in ranks) and rank == 0):
            rank = 113
        
        if (rank != 0) :
            message = 'Straight'

    

    # Three of a kind
    if (rank == 0) :
        if ("AAA" in ranks and rank == 0):
            rank = 112 + rankKickers(ranks.replace('AAA', ''), 2)
        
        if ("kkk" in ranks and rank == 0):
            rank = 111 + rankKickers(ranks.replace('KKK', ''), 2)
        
        if ("QQQ" in ranks and rank == 0):
            rank = 110 + rankKickers(ranks.replace('QQQ', ''), 2)
        
        if ("JJJ" in ranks and rank == 0):
            rank = 109 + rankKickers(ranks.replace('JJJ', ''), 2)
        
        if ("TTT" in ranks and rank == 0):
            rank = 108 + rankKickers(ranks.replace('TTT', ''), 2)
        
        if ("999" in ranks and rank == 0):
            rank = 107 + rankKickers(ranks.replace('999', ''), 2)
        
        if ("888" in ranks and rank == 0):
            rank = 106 + rankKickers(ranks.replace('888', ''), 2)
        
        if ("777" in ranks and rank == 0):
            rank = 105 + rankKickers(ranks.replace('777', ''), 2)
        
        if ("666" in ranks and rank == 0):
            rank = 104 + rankKickers(ranks.replace('666', ''), 2)
        
        if ("555" in ranks and rank == 0):
            rank = 103 + rankKickers(ranks.replace('555', ''), 2)
        
        if ("444" in ranks and rank == 0):
            rank = 102 + rankKickers(ranks.replace('444', ''), 2)
        
        if ("333" in ranks and rank == 0):
            rank = 101 + rankKickers(ranks.replace('333', ''), 2)
        
        if ("222" in ranks and rank == 0):
            rank = 100 + rankKickers(ranks.replace('222', ''), 2)
        
        if (rank != 0) :
            message = 'Three of a Kind'
        
    

    # Two pair
    if (rank == 0) :
        if (("AA" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 99 + rankKickers(ranks.replace('AA', '').replace('KK', ''), 1)
        
        if (("AA" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 98 + rankKickers(ranks.replace('AA', '').replace('QQ', ''), 1)
        
        if (("AA" in ranks) and ("JJ" in ranks) and rank == 0):
            rank = 97 + rankKickers(ranks.replace('AA', '').replace('JJ', ''), 1)
        
        if (("AA" in ranks) and ("TT" in ranks) and rank == 0):
            rank = 96 + rankKickers(ranks.replace('AA', '').replace('TT', ''), 1)
        
        if (("AA" in ranks) and ("99" in ranks) and rank == 0):
            rank = 95 + rankKickers(ranks.replace('AA', '').replace('99', ''), 1)
        
        if (("AA" in ranks) and ("88" in ranks) and rank == 0):
            rank = 94 + rankKickers(ranks.replace('AA', '').replace('88', ''), 1)
        
        if (("AA" in ranks) and ("77" in ranks) and rank == 0):
            rank = 93 + rankKickers(ranks.replace('AA', '').replace('77', ''), 1)
        
        if (("AA" in ranks) and ("66" in ranks) and rank == 0):
            rank = 92 + rankKickers(ranks.replace('AA', '').replace('66', ''), 1)
        
        if (("AA" in ranks) and ("55" in ranks) and rank == 0):
            rank = 91 + rankKickers(ranks.replace('AA', '').replace('55', ''), 1)
        
        if (("AA" in ranks) and ("44" in ranks) and rank == 0):
            rank = 90 + rankKickers(ranks.replace('AA', '').replace('44', ''), 1)
        
        if (("AA" in ranks) and ("33" in ranks) and rank == 0):
            rank = 89 + rankKickers(ranks.replace('AA', '').replace('33', ''), 1)
        
        if (("AA" in ranks) and ("22" in ranks) and rank == 0):
            rank = 88 + rankKickers(ranks.replace('AA', '').replace('22', ''), 1)
        
        if (("QQ" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 87 + rankKickers(ranks.replace('KK', '').replace('QQ', ''), 1)
        
        if (("JJ" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 86 + rankKickers(ranks.replace('KK', '').replace('JJ', ''), 1)
        
        if (("TT" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 85 + rankKickers(ranks.replace('KK', '').replace('TT', ''), 1)
        
        if (("99" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 84 + rankKickers(ranks.replace('KK', '').replace('99', ''), 1)
        
        if (("88" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 83 + rankKickers(ranks.replace('KK', '').replace('88', ''), 1)
        
        if (("77" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 82 + rankKickers(ranks.replace('KK', '').replace('77', ''), 1)
        
        if (("66" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 81 + rankKickers(ranks.replace('KK', '').replace('66', ''), 1)
        
        if (("55" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 80 + rankKickers(ranks.replace('KK', '').replace('55', ''), 1)
        
        if (("44" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 79 + rankKickers(ranks.replace('KK', '').replace('44', ''), 1)
        
        if (("33" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 78 + rankKickers(ranks.replace('KK', '').replace('33', ''), 1)
        
        if (("22" in ranks) and ("KK" in ranks) and rank == 0):
            rank = 77 + rankKickers(ranks.replace('KK', '').replace('22', ''), 1)
        
        if (("JJ" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 76 + rankKickers(ranks.replace('QQ', '').replace('JJ', ''), 1)
        
        if (("TT" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 75 + rankKickers(ranks.replace('QQ', '').replace('TT', ''), 1)
        
        if (("99" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 74 + rankKickers(ranks.replace('QQ', '').replace('99', ''), 1)
        
        if (("88" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 73 + rankKickers(ranks.replace('QQ', '').replace('88', ''), 1)
        
        if (("77" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 72 + rankKickers(ranks.replace('QQ', '').replace('77', ''), 1)
        
        if (("66" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 71 + rankKickers(ranks.replace('QQ', '').replace('66', ''), 1)
    
        if (("55" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 70 + rankKickers(ranks.replace('QQ', '').replace('55', ''), 1)

        if (("44" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 69 + rankKickers(ranks.replace('QQ', '').replace('44', ''), 1)
        
        if (("33" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 68 + rankKickers(ranks.replace('QQ', '').replace('33', ''), 1)
        
        if (("22" in ranks) and ("QQ" in ranks) and rank == 0):
            rank = 67 + rankKickers(ranks.replace('QQ', '').replace('22', ''), 1)
        
        if (("TT" in ranks) and ("JJ" in ranks) and rank == 0):
            rank = 66 + rankKickers(ranks.replace('JJ', '').replace('TT', ''), 1)
        
        if (("99" in ranks) and ("JJ" in ranks) and rank == 0):
            rank = 65 + rankKickers(ranks.replace('JJ', '').replace('99', ''), 1)
        
        if (("88" in ranks) and ("JJ" in ranks) and rank == 0):
            rank = 64 + rankKickers(ranks.replace('JJ', '').replace('88', ''), 1)
        
        if (("77" in ranks) and ("JJ" in ranks) and rank == 0):
            rank = 63 + rankKickers(ranks.replace('JJ', '').replace('77', ''), 1)
        
        if (("66" in ranks) and ("JJ" in ranks) and rank == 0):
            rank = 62 + rankKickers(ranks.replace('JJ', '').replace('66', ''), 1)
        
        if (("55" in ranks) and ("JJ" in ranks) and rank == 0):
            rank = 61 + rankKickers(ranks.replace('JJ', '').replace('55', ''), 1)
        
        if (("44" in ranks) and ("JJ" in ranks) and rank == 0):
            rank = 60 + rankKickers(ranks.replace('JJ', '').replace('44', ''), 1)
        
        if (("33" in ranks) and ("JJ" in ranks) and rank == 0):
            rank = 59 + rankKickers(ranks.replace('JJ', '').replace('33', ''), 1)
        
        if (("22" in ranks) and ("JJ" in ranks) and rank == 0):
            rank = 58 + rankKickers(ranks.replace('JJ', '').replace('22', ''), 1)
        
        if (("99" in ranks) and ("TT" in ranks) and rank == 0):
            rank = 57 + rankKickers(ranks.replace('TT', '').replace('99', ''), 1)
        
        if (("88" in ranks) and ("TT" in ranks) and rank == 0):
            rank = 56 + rankKickers(ranks.replace('TT', '').replace('88', ''), 1)
        
        if (("77" in ranks) and ("TT" in ranks) and rank == 0):
            rank = 55 + rankKickers(ranks.replace('TT', '').replace('77', ''), 1)
        
        if (("66" in ranks) and ("TT" in ranks) and rank == 0):
            rank = 54 + rankKickers(ranks.replace('TT', '').replace('66', ''), 1)
        
        if (("55" in ranks) and ("TT" in ranks) and rank == 0):
            rank = 53 + rankKickers(ranks.replace('TT', '').replace('55', ''), 1)
        
        if (("44" in ranks) and ("TT" in ranks) and rank == 0):
            rank = 52 + rankKickers(ranks.replace('TT', '').replace('44', ''), 1)
        
        if (("33" in ranks) and ("TT" in ranks) and rank == 0):
            rank = 51 + rankKickers(ranks.replace('TT', '').replace('33', ''), 1)
        
        if (("22" in ranks) and ("TT" in ranks) and rank == 0):
            rank = 50 + rankKickers(ranks.replace('TT', '').replace('22', ''), 1)
        
        if (("88" in ranks) and ("99" in ranks) and rank == 0):
            rank = 49 + rankKickers(ranks.replace('99', '').replace('88', ''), 1)
        
        if (("77" in ranks) and ("99" in ranks) and rank == 0):
            rank = 48 + rankKickers(ranks.replace('99', '').replace('77', ''), 1)
        
        if (("66" in ranks) and ("99" in ranks) and rank == 0):
            rank = 47 + rankKickers(ranks.replace('99', '').replace('66', ''), 1)
        
        if (("55" in ranks) and ("99" in ranks) and rank == 0):
            rank = 46 + rankKickers(ranks.replace('99', '').replace('55', ''), 1)
        
        if (("44" in ranks) and ("99" in ranks) and rank == 0):
            rank = 45 + rankKickers(ranks.replace('99', '').replace('44', ''), 1)
        
        if (("33" in ranks) and ("99" in ranks) and rank == 0):
            rank = 44 + rankKickers(ranks.replace('99', '').replace('33', ''), 1)
        
        if (("22" in ranks) and ("99" in ranks) and rank == 0):
            rank = 43 + rankKickers(ranks.replace('99', '').replace('22', ''), 1)
        
        if (("77" in ranks) and ("88" in ranks) and rank == 0):
            rank = 42 + rankKickers(ranks.replace('88', '').replace('77', ''), 1)
        
        if (("66" in ranks) and ("88" in ranks) and rank == 0):
            rank = 41 + rankKickers(ranks.replace('88', '').replace('66', ''), 1)
        
        if (("55" in ranks) and ("88" in ranks) and rank == 0):
            rank = 40 + rankKickers(ranks.replace('88', '').replace('55', ''), 1)
        
        if (("44" in ranks) and ("88" in ranks) and rank == 0):
            rank = 39 + rankKickers(ranks.replace('88', '').replace('44', ''), 1)
        
        if (("33" in ranks) and ("88" in ranks) and rank == 0):
            rank = 38 + rankKickers(ranks.replace('88', '').replace('33', ''), 1)
        
        if (("22" in ranks) and ("88" in ranks) and rank == 0):
            rank = 37 + rankKickers(ranks.replace('88', '').replace('22', ''), 1)
        
        if (("66" in ranks) and ("77" in ranks) and rank == 0):
            rank = 36 + rankKickers(ranks.replace('77', '').replace('66', ''), 1)
        
        if (("55" in ranks) and ("77" in ranks) and rank == 0):
            rank = 35 + rankKickers(ranks.replace('77', '').replace('55', ''), 1)
        
        if (("44" in ranks) and ("77" in ranks) and rank == 0):
            rank = 34 + rankKickers(ranks.replace('77', '').replace('44', ''), 1)
        
        if (("33" in ranks) and ("77" in ranks) and rank == 0):
            rank = 33 + rankKickers(ranks.replace('77', '').replace('33', ''), 1)
        
        if (("22" in ranks) and ("77" in ranks) and rank == 0):
            rank = 32 + rankKickers(ranks.replace('77', '').replace('22', ''), 1)
        
        if (("55" in ranks) and ("66" in ranks) and rank == 0):
            rank = 31 + rankKickers(ranks.replace('66', '').replace('55', ''), 1)
        
        if (("44" in ranks) and ("66" in ranks) and rank == 0):
            rank = 30 + rankKickers(ranks.replace('66', '').replace('44', ''), 1)
        
        if (("33" in ranks) and ("66" in ranks) and rank == 0):
            rank = 29 + rankKickers(ranks.replace('66', '').replace('33', ''), 1)
        
        if (("22" in ranks) and ("66" in ranks) and rank == 0):
            rank = 28 + rankKickers(ranks.replace('66', '').replace('22', ''), 1)
        
        if (("44" in ranks) and ("55" in ranks) and rank == 0):
            rank = 27 + rankKickers(ranks.replace('55', '').replace('44', ''), 1)
        
        if (("33" in ranks) and ("55" in ranks) and rank == 0):
            rank = 26 + rankKickers(ranks.replace('55', '').replace('33', ''), 1)
        
        if (("22" in ranks) and ("55" in ranks) and rank == 0):
            rank = 25 + rankKickers(ranks.replace('55', '').replace('22', ''), 1)
        
        if (("33" in ranks) and ("44" in ranks) and rank == 0):
            rank = 24 + rankKickers(ranks.replace('44', '').replace('33', ''), 1)
        
        if (("22" in ranks) and ("44" in ranks) and rank == 0):
            rank = 23 + rankKickers(ranks.replace('44', '').replace('22', ''), 1)
        
        if (("22" in ranks) and ("33" in ranks) and rank == 0):
            rank = 22 + rankKickers(ranks.replace('33', '').replace('22', ''), 1)
        
        if (rank != 0) :
            message = 'Two Pair'
        
    

    # One Pair
    if (rank == 0) :
        if ("AA" in ranks):
            rank = 21 + rankKickers(ranks.replace('AA', ''), 3)
        
        if ("KK" in ranks and rank == 0):
            rank = 20 + rankKickers(ranks.replace('KK', ''), 3)
        
        if ("QQ" in ranks and rank == 0):
            rank = 19 + rankKickers(ranks.replace('QQ', ''), 3)
        
        if ("JJ" in ranks and rank == 0):
            rank = 18 + rankKickers(ranks.replace('JJ', ''), 3)
        
        if ("TT" in ranks and rank == 0):
            rank = 17 + rankKickers(ranks.replace('TT', ''), 3)
        
        if ("99" in ranks and rank == 0):
            rank = 16 + rankKickers(ranks.replace('99', ''), 3)
        
        if ("88" in ranks and rank == 0):
            rank = 15 + rankKickers(ranks.replace('88', ''), 3)
        
        if ("77" in ranks and rank == 0):
            rank = 14 + rankKickers(ranks.replace('77', ''), 3)
        
        if ("66" in ranks and rank == 0):
            rank = 13 + rankKickers(ranks.replace('66', ''), 3)
        
        if ("55" in ranks and rank == 0):
            rank = 12 + rankKickers(ranks.replace('55', ''), 3)
        
        if ("44" in ranks and rank == 0):
            rank = 11 + rankKickers(ranks.replace('44', ''), 3)
        
        if ("33" in ranks and rank == 0):
            rank = 10 + rankKickers(ranks.replace('33', ''), 3)
        
        if ("22" in ranks and rank == 0):
            rank = 9 + rankKickers(ranks.replace('22', ''), 3)
        
        if (rank != 0) :
            message = 'Pair'
        
    

    # High Card
    if (rank == 0) :
        if ("A" in ranks and rank == 0):
            rank = 8 + rankKickers(ranks.replace('A', ''), 4)
        
        if ("K" in ranks and rank == 0):
            rank = 7 + rankKickers(ranks.replace('K', ''), 4)
        
        if ("Q" in ranks and rank == 0):
            rank = 6 + rankKickers(ranks.replace('Q', ''), 4)
        
        if ("J" in ranks and rank == 0):
            rank = 5 + rankKickers(ranks.replace('J', ''), 4)
        
        if ("T" in ranks and rank == 0):
            rank = 4 + rankKickers(ranks.replace('T', ''), 4)
        
        if ("9" in ranks and rank == 0):
            rank = 3 + rankKickers(ranks.replace('9', ''), 4)
        
        if ("8" in ranks and rank == 0):
            rank = 2 + rankKickers(ranks.replace('8', ''), 4)
        
        if ("7" in ranks and rank == 0):
            rank = 1 + rankKickers(ranks.replace('7', ''), 4)
        
        if (rank != 0 ) :
            message = 'High Card'
        
    

    result = {"rank": rank, "message":message}

    return result
