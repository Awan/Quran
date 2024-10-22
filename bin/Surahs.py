#!/usr/bin/env python

# A python script to feed metadata into verses
# Usage:
# path/to/this/script Surah_number
# ./Surahs.py 17

import sys

surahs_names = {
        1: '001 - Fateha',
        2: '002 - Baqara',
        3: '003 - Al Imran',
        4: '004 - Nisaa',
        5: '005 - Mayedah',
        6: '006 - Anaam',
        7: '007 - Araaf',
        8: '008 - Anfaal',
        9: '009 - Tauba',
        10: '010 - Yunus',
        11: '011 - Hud',
        12: '012 - Yusuf',
        13: '013 - Raad',
        14: '014 - Ibrahim',
        15: '015 - Hajr',
        16: '016 - Nahl',
        17: '017 - Israa',
        18: '018 - Kahf',
        19: '019 - Maryam',
        20: '020 - Taha',
        21: '021 - Ambiya',
        22: '022 - Hajj',
        23: '023 - Mominoon',
        24: '024 - Noor',
        25: '025 - Furqan',
        26: '026 - Shuaraa',
        27: '027 - Naml',
        28: '028 - Qassas',
        29: '029 - Ankaboot',
        30: '030 - Room',
        31: '031 - Luqman',
        32: '032 - Sajdah',
        33: '033 - Ahzaab',
        34: '034 - Saba',
        35: '035 - Faatir',
        36: '036 - Yaseen',
        37: '037 - Saaffaat',
        38: '038 - Suaad',
        39: '039 - Zumar',
        40: '040 - Ghaafir',
        41: '041 - Fussilat',
        42: '042 - Shoora',
        43: '043 - Zukhruf',
        44: '044 - Dukhaan',
        45: '045 - Jaasiya',
        46: '046 - Ahqaaf',
        47: '047 - Muhammad',
        48: '048 - Fateh',
        49: '049 - Hujraat',
        50: '050 - Qaaf',
        51: '051 - Zaariyaat',
        52: '052 - Toor',
        53: '053 - Najm',
        54: '054 - Qamar',
        55: '055 - Rahman',
        56: '056 - Waqeaa',
        57: '057 - Hadeed',
        58: '058 - Mujaadilah',
        59: '059 - Hashr',
        60: '060 - Mumtahinah',
        61: '061 - Saff',
        62: '062 - Jummah',
        63: '063 - Munaafiqoon',
        64: '064 - Taghaabun',
        65: '065 - Talaaq',
        66: '066 - Tahreem',
        67: '067 - Mulk',
        68: '068 - Qalam',
        69: '069 - Haaqa',
        70: "070 - Ma'aarij",
        71: '071 - Nooh',
        72: '072 - Jinn',
        73: '073 - Muzzammil',
        74: '074 - Muddassir',
        75: '075 - Qayamat',
        76: '076 - Insan',
        77: '077 - Mursalaat',
        78: '078 - Nabaa',
        79: '079 - Naaziyaat',
        80: '080 - Abbas',
        81: '081 - Takveer',
        82: '082 - Infitaar',
        83: '083 - Mutaffiffeen',
        84: '084 - Inshiqaaq',
        85: '085 - Burooj',
        86: '086 - Taariq',
        87: '087 - Aalaa',
        88: '088 - Ghaashiya',
        89: '089 - Fajr',
        90: '090 - Balad',
        91: '091 - Shams',
        92: '092 - Lail',
        93: '093 - Duhaa',
        94: '094 - Inshirah',
        95: '095 - Teen',
        96: '096 - Alaq',
        97: '097 - Qaddar',
        98: '098 - Bayyennah',
        99: '099 - Zalzalah',
        100: '100 - Aadiyaat',
        101: '101 - Qaareya',
        102: '102 - Takaasur',
        103: '103 - Asr',
        104: '104 - Hummaza',
        105: '105 - Feel',
        106: '106 - Quraish',
        107: "107 - Maa'oon",
        108: '108 - Kosar',
        109: '109 - Kaafiroon',
        110: '110 - Nasr',
        111: '111 - Lahab',
        112: '112 - Ikhlaas',
        113: '113 - Falaq',
        114: '114 - Naas'
        }

surah = int(sys.argv[1])

def get_Surah_name(surah):
    return surahs_names[surah]

print(get_Surah_name(surah))
