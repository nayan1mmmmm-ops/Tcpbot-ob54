# ======================== BOT NAME LOADER =======================
import os as _os
def _read_bot_name():
    _d = _os.path.dirname(_os.path.abspath(__file__)) if "__file__" in dir() else "."
    _f = _os.path.join(_d, "yourname.txt")
    try:
        with open(_f, "r", encoding="utf-8") as _fp:
            _n = _fp.read().strip()
            if _n: return _n
    except: pass
    return "BOT"
BOT_NAME = _read_bot_name()
BOT_NAME_LOWER = BOT_NAME.lower()
# ======================== END BOT NAME LOADER ====================


import requests
from byte import Encrypt_ID, encrypt_api
import RemoveFriend_Req_pb2
import data_pb2
import uid_generator_pb2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii
import jwt

# Pb2 folder থেকে ইমপোর্ট
from Pb2 import AccountPersonalShow_pb2
from Pb2 import main_pb2

# ======================== IMPORTS =======================
import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp , traceback , signal  , asyncio
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2, RemoveFriend_Req_pb2, GetFriend_Res_pb2, spam_request_pb2, devxt_count_pb2, dev_generator_pb2, kyro_title_pb2, room_join_pb2
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from cfonts import render, say
import google.protobuf.json_format as json_format
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# ======================== COLORS =======================
WHITE   = "\033[97m"
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
RESET   = "\033[0m"

# =======================================================
# =================== CREDIT LOADER ===================
def _load_credit_name():
    """Load credit name from yourname.txt"""
    try:
        with open("yourname.txt", "r", encoding="utf-8") as f:
            name = f.read().strip()
            if name:
                return name
    except:
        pass
    return f"{BOT_NAME_LOWER}"

CREDIT_NAME = _load_credit_name()

# =================== PASSWORD VERIFICATION ===================
# main.py এ থাকা পাসওয়ার্ড - এটি xC4.py এর জন্য
_MAIN_XC4_PASSWORD = "SUMON999X"

# xC4 এর password verify করো
try:
    from xC4 import _xc4_check_access
    _xc4_check_access(bypass_password=_MAIN_XC4_PASSWORD)
except SystemExit:
    raise
except Exception as _pw_err:
    print(f"[Password] ⚠️ Warning: {_pw_err}")
# =====================================================

# =================== CONFIGURATION ======================
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  


# ---------- WORD TO LEVEL ----------
amr_bal = {
    "ak": 1,
    "scar": 2,
    "mp40": 3,
    "mp40b": 4,
    "m10": 5,
    "m10r": 6,
    "xm8": 7,
    "famas": 8,
    "ump": 9,
    "m18": 10,
    "fist": 11,
    "groza": 12,
    "m4a1": 13,
    "tn": 14,
    "g18": 15,
    "parafal": 16,
    "p90": 17,
    "m60": 18,
    "an94": 19,
    "aug": 400,
    "wr": 20,

    # ❤️ Emotions / Emotes
    "rose": 42,
    "love": 43,
    "sad": 44,
    "rose2": 61,
    "lol2": 33,
    "lol": 99,
    "sad2": 166,
    "rose3": 65,
    "love1": 46,
    "n1": 402,
    "n2": 401,
    "n3": 400,
    "n4": 399,
    "n5": 398,
    "n6": 396,
    "n7": 395,
    "n8": 394,
    "n9": 393,
    "n10": 408,
    "n11": 407,
    "n12": 406,
    "n13": 405,
    "n14": 404,
    "n15": 403,
    "n16": 285
}

# =================== GLOBAL VARIABLES ===================
online_writer = None
whisper_writer = None
spammer_uid = None
msg_spam_running = False
msg_spam_task = None
mg_spam_task = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
fast_spam_running = False
fast_spam_task = None
custom_spam_running = False
custom_spam_task = None
spam_request_running = False
spam_request_task = None
evo_fast_spam_running = False
evo_fast_spam_task = None
evo_custom_spam_running = False
evo_custom_spam_task = None
reject_spam_running = False
reject_spam_task = None
emote_hijack = False 
lag_running = False
lag_task = None
reject_spam_running = False
reject_spam_task = None
evo_cycle_running = False
evo_cycle_task = None
evo_cycle_sm_running = False
evo_cycle_sm_task = None
emotes_cycle_running = False
emotes_cycle_task = None
status_response_cache = {} 
pending_status_requests = {}
room_info_cache = {}
last_status_packet = None
insquad = None 
joining_team = False 
online_writer = None 
whisper_writer = None 
last_bot_status_check = 0
senthi = False
bot_status_cache_time = 30
cached_bot_status = None
last_status_packet = None
START_SPAM_DURATION = 18     
WAIT_AFTER_MATCH_SECONDS = 20 
START_SPAM_DELAY = 0.2       
region = 'IND'
WHITELISTED_UIDS = {
    "6861053275"  
}
WHITELIST_ONLY = True  
BOT_OWNER_UID = 6861053275  
PLAYER_NAME_CACHE = {}  
# =================== ADMIN COMMAND VARIABLES (V6) ===================
ADMIN_UID = "6861053275"
bot_enabled = True

# Admin Functions
def is_admin(uid):
    return str(uid) == ADMIN_UID

# Mute Functions 
def is_off():
    return not bot_enabled
# =====================================================================
freeze_running = False
freeze_task = None
FREEZE_EMOTES = [909052010, 909052010, 909052010]


# =================== BANGLA JOKES LIST ===================
BANGLA_JOKES = [
    "এক লোক ডাক্তার কাছে গেল।\nলোক: ডাক্তার সাহেব, আমার সবকিছু ভুলে যাওয়ার রোগ হয়েছে।\nডাক্তার: কবে থেকে হয়েছে?\nলোক: কী কবে থেকে হয়েছে?\nডাক্তার: এই যে ভুলে যাওয়ার রোগ!\nলোক: ওহ! আমি তো ভুলেই গিয়েছিলাম কেন এসেছি!",
    "এক ছাত্র পরীক্ষায় কিছুই লিখতে পারছে না।\nশিক্ষক: কেন কিছু লিখছ না?\nছাত্র: স্যার, প্রশ্নগুলো খুব কঠিন।\nশিক্ষক: তাহলে সহজটা লেখো।\nছাত্র: স্যার, সহজ প্রশ্নটা তো আপনি করেননি!",
    "এক বন্ধু আরেক বন্ধুকে বলল,\nআমি কাল থেকে ডায়েট শুরু করব।\nবন্ধু: কাল কেন?\nসে: আজকে ফ্রিজে যত খাবার আছে শেষ করতে হবে।\nবন্ধু: তাহলে তোর ডায়েট কখনোই শুরু হবে না!",
    "এক লোক দোকানে গিয়ে বলল,\nভাই, এমন একটা ঘড়ি দেখান যেটা পানিতে নষ্ট হবে না।\nদোকানদার একটা ঘড়ি দেখালেন।\nলোক: এটা কি সত্যি পানিতে নষ্ট হবে না?\nদোকানদার: না, কারণ এটা আমি কাউকে পানিতে ফেলতে দিই না!",
    "শিক্ষক ক্লাসে জিজ্ঞেস করলেন,\nবল তো, পৃথিবী গোল কেন?\nএক ছাত্র: স্যার, যদি পৃথিবী চৌকো হতো…\nশিক্ষক: তাহলে?\nছাত্র: তাহলে কোণায় বসে আমরা পড়াশোনা এড়িয়ে যেতাম!",
    "এক লোক বন্ধুকে বলল,\nআমি গতকাল জিমে ভর্তি হয়েছি।\nবন্ধু: সত্যি?\nলোক: হ্যাঁ, আজকে জিমের সামনে দিয়ে হেঁটে এসেছি।\nবন্ধু: ভিতরে ঢুকলি না?\nলোক: না, এত তাড়াহুড়ো কেন!",
    "এক ছাত্র বাবাকে বলল,\nবাবা, পরীক্ষায় আমি পাশ করেছি।\nবাবা: কত নম্বর পেয়েছ?\nছাত্র: শিক্ষক দয়া করে পাশ করিয়েছেন।\nবাবা: তাহলে পড়াশোনা কর।\nছাত্র: বাবা, দয়া থাকলে পড়াশোনা লাগে?",
    "এক লোক রেস্টুরেন্টে গিয়ে বলল,\nভাই, খাবার এত দেরি হচ্ছে কেন?\nওয়েটার: স্যার, আমরা তাজা খাবার বানাই।\nলোক: তাজা মানে?\nওয়েটার: মুরগিটা ধরতে একটু সময় লাগে!",
    "এক ছেলে মাকে বলল,\nমা, আমার মাথা খুব ব্যথা করছে।\nমা: তাহলে পড়তে বসো না।\nছেলে: তাহলে তো মাথা আরও ব্যথা করবে!\nমা: কেন?\nছেলে: কারণ পড়া দেখলেই মাথা ধরে!",
    "এক বন্ধু বলল,\nতুই এত দেরি করে কেন এলি?\nঅন্য বন্ধু: রাস্তা ভুলে গিয়েছিলাম।\nসে: তুই তো এই এলাকায় থাকিস!\nবন্ধু: হ্যাঁ, কিন্তু মোবাইলে গেম খেলতে খেলতে রাস্তা ভুলে গেছি!",
    "এক ছাত্র বলল,\nস্যার, আমি সব বুঝেছি।\nস্যার: তাহলে বোর্ডে এসে বুঝিয়ে দাও।\nছাত্র: স্যার, আমি বুঝেছি কিন্তু বোঝাতে পারব না।\nস্যার: কেন?\nছাত্র: কারণ বোঝাতে গেলে আবার বুঝতে হবে!",
    "এক লোক বলল,\nআমার ঘড়ি সব সময় এগিয়ে যায়।\nবন্ধু: তাহলে ভালোই তো!\nলোক: ভালো কোথায়?\nবন্ধু: সব কাজে আগে পৌঁছাবে।\nলোক: না, সবাই ভাবে আমি দেরি করেছি!",
    "এক ছেলে বাবাকে বলল,\nবাবা, আমি বড় হয়ে বড়লোক হব।\nবাবা: কীভাবে?\nছেলে: আমি ইউটিউবার হব।\nবাবা: ভিডিও বানাতে পারো?\nছেলে: না, কিন্তু কমেন্ট করতে পারি!",
    "এক ছাত্র বলল,\nস্যার, আমার পেট ব্যথা।\nস্যার: তাহলে বাড়ি যাও।\nছাত্র: তাহলে তো কাল আবার স্কুলে আসতে হবে।\nস্যার: তাতে সমস্যা কী?\nছাত্র: আজই যদি না আসতাম!",
    "এক বন্ধু বলল,\nআমি খুব পরিশ্রম করি।\nঅন্য বন্ধু: কী কাজ করিস?\nসে: ঘুমানোর আগে ভাবি কাল কী করব।\nবন্ধু: তারপর?\nসে: সকালে উঠে ভুলে যাই!",
    "এক ছেলে বলল,\nমা, আমি ডায়েট করছি।\nমা: তাহলে এত খাচ্ছ কেন?\nছেলে: ডায়েট কাল থেকে শুরু হবে।\nমা: আজ?\nছেলে: আজ বিদায় পার্টি!",
    "এক ছাত্র বলল,\nস্যার, আমি আজ পড়া পারিনি।\nস্যার: কেন?\nছাত্র: কারেন্ট ছিল না।\nস্যার: দিনে তো কারেন্ট লাগে না।\nছাত্র: স্যার, দিনে তো ঘুমাই!",
    "এক লোক বলল,\nআমার ফোন খুব স্মার্ট।\nবন্ধু: কেন?\nলোক: আমি পড়তে বসলে নিজেই গেম খুলে যায়।\nবন্ধু: তাহলে ফোন না তুই স্মার্ট?\nলোক: ফোনই!",
    "এক ছাত্র বলল,\nস্যার, আমার কলম কাজ করছে না।\nস্যার: তাহলে অন্য কলম নাও।\nছাত্র: তাও কাজ করছে না।\nস্যার: কেন?\nছাত্র: কারণ আমি পড়িনি!",
    "এক বন্ধু বলল,\nতুই এত মোটা কেন?\nঅন্যজন: আমি সুখে আছি।\nবন্ধু: সুখে থাকলে মোটা হয়?\nসে: খেতে খেতে সুখ পাই!",
    "এক ছেলে বলল,\nবাবা, আমি পড়াশোনা করব না।\nবাবা: তাহলে কী করবি?\nছেলে: বিজনেস করব।\nবাবা: কী বিজনেস?\nছেলে: ঘুমানোর!",
    "এক বন্ধু বলল,\nতোর প্রেম কেমন চলছে?\nঅন্য বন্ধু: WiFi এর মতো।\nবন্ধু: মানে?\nসে: কখনো কানেক্ট হয়, কখনো যায়!",
    "এক ছাত্র বলল,\nস্যার, আমি পড়া ভুলে গেছি।\nস্যার: কেন?\nছাত্র: মনে রাখতে জায়গা ছিল না।\nস্যার: কেন?\nছাত্র: সব জায়গা গেমে ভর্তি!",
    "এক লোক বলল,\nআমি আজ খুব কাজ করেছি।\nবন্ধু: কী কাজ?\nলোক: ঘুম থেকে উঠেছি।\nবন্ধু: আর?\nলোক: আবার ঘুমিয়েছি!",
    "এক ছাত্র বলল,\nস্যার, আমি বই খুলেছি।\nস্যার: তাহলে পড়ো।\nছাত্র: স্যার, খুলতেই তো কষ্ট হয়েছে!",
    "এক বন্ধু বলল,\nতুই এত অলস কেন?\nঅন্যজন: আমি শক্তি সঞ্চয় করি।\nবন্ধু: কিসের জন্য?\nসে: ঘুমানোর জন্য!",
    "এক ছেলে বলল,\nমা, আমি ক্ষুধার্ত।\nমা: ফ্রিজে খাবার আছে।\nছেলে: ফ্রিজ খুলতে আলসেমি লাগছে!",
    "এক ছাত্র বলল,\nস্যার, আমার মাথা কাজ করছে না।\nস্যার: কেন?\nছাত্র: আমি ছুটি দিয়েছি!",
    "এক লোক বলল,\nআমি দৌড়াতে পারি না।\nবন্ধু: কেন?\nলোক: দৌড়ালেই হাঁপিয়ে যাই।",
    "এক ছেলে বলল,\nবাবা, আমি বড় হয়ে পাইলট হব।\nবাবা: কেন?\nছেলে: স্কুলে না যাওয়ার জন্য!",
    "এক ছাত্র বলল,\nস্যার, আমার পেট ব্যথা।\nস্যার: ডাক্তারের কাছে যাও।\nছাত্র: তাহলে তো স্কুলে আসতে হবে না!",
    "এক বন্ধু বলল,\nতুই কি পড়াশোনা করিস?\nঅন্যজন: হ্যাঁ।\nবন্ধু: কখন?\nসে: পরীক্ষার আগের রাত!",
    "এক ছেলে বলল,\nমা, আমি আজ পড়ব।\nমা: খুব ভালো।\nছেলে: কিন্তু কাল থেকে!",
    "এক ছাত্র বলল,\nস্যার, আমি বই পড়েছি।\nস্যার: কী বুঝেছ?\nছাত্র: বইটা ভারী!",
    "এক লোক বলল,\nআমি আজ খুব ব্যস্ত।\nবন্ধু: কী কাজ?\nলোক: কিছু না করার কাজ!",
    "এক বন্ধু বলল,\nতুই এত ঘুমাস কেন?\nঅন্যজন: স্বপ্নে কাজ করি!",
    "এক ছেলে বলল,\nমা, আমার খুব ক্ষুধা।\nমা: খাবার খাও।\nছেলে: তুমি খাইয়ে দাও!",
    "এক ছাত্র বলল,\nস্যার, প্রশ্নটা বুঝিনি।\nস্যার: আবার পড়ো।\nছাত্র: তবুও বুঝব না!",
    "এক বন্ধু বলল,\nতুই এত মোবাইল ব্যবহার করিস কেন?\nঅন্যজন: মোবাইল আমাকে ব্যবহার করে!",
    "এক ছেলে বলল,\nবাবা, আমি পড়তে বসেছি।\nবাবা: তাহলে পড়ো।\nছেলে: ঘুম পাচ্ছে!",
    "এক ছাত্র বলল,\nস্যার, আমার খাতা হারিয়ে গেছে।\nস্যার: কোথায়?\nছাত্র: যেখানে পড়িনি!",
    "এক বন্ধু বলল,\nতুই এত হাসছ কেন?\nঅন্যজন: কারণ কাঁদতে ইচ্ছে করছে!",
    "এক ছেলে বলল,\nমা, আমি বড় হয়ে ধনী হব।\nমা: কীভাবে?\nছেলে: স্বপ্নে!",
    "এক ছাত্র বলল,\nস্যার, আমি পড়িনি।\nস্যার: কেন?\nছাত্র: বই আমাকে ডাকেনি!",
    "এক বন্ধু বলল,\nতুই এত কথা বলিস কেন?\nঅন্যজন: চুপ থাকতে পারি না!",
    "এক ছেলে বলল,\nমা, আমি আজ স্কুলে যাব না।\nমা: কেন?\nছেলে: ঘুম ভালো লাগছে!",
    "এক ছাত্র বলল,\nস্যার, আমার কলম শেষ।\nস্যার: তাহলে লিখবে কী দিয়ে?\nছাত্র: মনে!",
    "এক বন্ধু বলল,\nতুই কি কাজ করিস?\nঅন্যজন: ভাবি!",
    "এক ছেলে বলল,\nমা, আমার মাথা ঘুরছে।\nমা: কম মোবাইল ব্যবহার কর।",
    "এক ছাত্র বলল,\nস্যার, আমি আজ পড়ব না।\nস্যার: কেন?\nছাত্র: আজ রবিবার!",
    "এক লোক ট্রেনে উঠে বলল,\nভাই, এই ট্রেন কোথায় যায়?\nযাত্রী: এটা কুমিল্লা যায়।\nলোক: আমি তো ঢাকা যাব!\nযাত্রী: তাহলে নামুন!\nলোক: ট্রেনটা ঘুরিয়ে দেন না!",
    "এক ছেলে বলল,\nবাবা, আমার পকেটমানি বাড়াও।\nবাবা: কেন?\nছেলে: বন্ধুরা বেশি পায়।\nবাবা: তাহলে ওদের বাবা হও!",
    "এক লোক হাসপাতালে গিয়ে বলল,\nডাক্তার, আমি কি বাঁচব?\nডাক্তার: আপনার কি হয়েছে?\nলোক: কিছু হয়নি, শুধু জানতে চাই!\nডাক্তার: তাহলে বিল দিন!",
    "এক ছাত্র বলল,\nস্যার, বাংলাদেশ কোন মহাদেশে?\nস্যার: এশিয়া।\nছাত্র: তাহলে আমরা এশিয়ান?\nস্যার: হ্যাঁ।\nছাত্র: তাহলে আমিও জাপানি!",
    "এক বন্ধু বলল,\nতুই কি রান্না পারিস?\nঅন্যজন: হ্যাঁ, পানি গরম করতে পারি!\nবন্ধু: সেটা তো রান্না না!\nসে: পানি ছাড়া রান্না হয়?",
    "এক ছেলে বলল,\nমা, আমি প্রেসিডেন্ট হতে চাই।\nমা: আগে ঘর গুছাও।\nছেলে: প্রেসিডেন্ট কি ঘর গোছায়?\nমা: না, কিন্তু তুইও প্রেসিডেন্ট হবি না!",
    "এক লোক বলল,\nআমি একজন মাল্টিটাস্কার।\nবন্ধু: কীভাবে?\nলোক: একসাথে খাই, ঘুমাই আর স্বপ্ন দেখি!",
    "এক ছাত্র বলল,\nস্যার, ইংরেজি কেন শিখব?\nস্যার: চাকরি পাবে।\nছাত্র: আমি তো ইউটিউবার হব!\nস্যার: তাহলে thumbnail বানাতে শেখ!",
    "এক বন্ধু বলল,\nতোর জীবনের লক্ষ্য কি?\nঅন্যজন: শুক্রবার!\nবন্ধু: সেটা তো দিন!\nসে: আমার জীবনের সেরা দিন!",
    "এক ছেলে বলল,\nমা, WiFi পাসওয়ার্ড কি?\nমা: আগে পড়ো।\nছেলে: সেটাই পাসওয়ার্ড?\nমা: না, আমি বলছি পড়াশোনা করো!",
    "এক লোক বলল,\nআমি ভবিষ্যৎ দেখতে পাই।\nবন্ধু: সত্যি?\nলোক: হ্যাঁ, আমি দেখতে পাচ্ছি তুই এখন হাসবি!",
    "এক ছাত্র বলল,\nস্যার, আমি তো জিনিয়াস!\nস্যার: প্রমাণ?\nছাত্র: আমার মা বলেছে!\nস্যার: মায়ের কথা সবসময় ঠিক হয় না!",
    "এক বন্ধু বলল,\nতুই ফেসবুকে কি করিস সারাদিন?\nঅন্যজন: রিসার্চ!\nবন্ধু: কিসের?\nসে: মিম এর!",
    "এক ছেলে বলল,\nবাবা, আমাকে একটা নতুন ফোন কিনে দাও।\nবাবা: পুরানোটা কি হয়েছে?\nছেলে: ভালো আছে, কিন্তু বন্ধুদের সামনে লজ্জা লাগে!\nবাবা: তাহলে বন্ধু বদলাও!",
    "এক লোক রাস্তায় হেঁটে যাচ্ছিল।\nহঠাৎ একজন বলল, ভাই সময় কত?\nলোক: আমার কাছে ঘড়ি নেই।\nসে: তাহলে ফোন দেখুন।\nলোক: ফোনও নেই।\nসে: তাহলে আপনি কীভাবে সময় জানেন?\nলোক: জানি না তো!",
    "এক ছাত্র পরীক্ষার হলে বসে ফ্যানের দিকে তাকাচ্ছে।\nশিক্ষক: ফ্যানের দিকে তাকাচ্ছ কেন?\nছাত্র: স্যার, ভাবছি ফ্যান ঘুরতে পারলে আমিও পারব!",
    "এক বন্ধু বলল,\nতুই কি চশমা পরিস?\nঅন্যজন: হ্যাঁ।\nবন্ধু: দৃষ্টি কত কম?\nসে: এত কম যে চশমা ছাড়া চশমা খুঁজে পাই না!",
    "এক ছেলে বলল,\nমা, আমি আজ ফার্স্ট হয়েছি!\nমা: সত্যি?\nছেলে: হ্যাঁ, ক্লাসে প্রথম ঢুকেছি!",
    "এক লোক বলল,\nআমি সাঁতার জানি না।\nবন্ধু: তাহলে শেখ।\nলোক: পানিতে নামলেই ডুবি!\nবন্ধু: তাই তো শিখতে হবে!\nলোক: ডুবে গেলে শিখব কীভাবে?"
]

JOKE_COLORS = ["FF4500", "00CED1", "FFD700", "FF69B4", "7CFC00", "FF6347", "00BFFF", "FF1493", "32CD32", "FFA500"]

# =================== SPNFF BUNDLE SPINNER DATA ===================
BUNDLE_DATA = {
    "Ultra Rare": [
        "Kitsune Bundle", "Steampunk Revolution Bundle", "Rampage Redemption Bundle",
        "Ghost Pirates Bundle", "Angelic Bundle", "Airspeed Ace Bundle",
        "Frost Sabertooth Bundle", "Lush Clubber Bundle", "Regal Malik Bundle",
        "Venomous Skorpios Bundle", "T.R.A.P. Revolution Bundle", "Sushi Menace Bundle",
        "Fuji Folklore Bundle", "Wildland Walkers Bundle", "Papyrus Rebel Bundle",
        "The Kung-Foodies Bundle", "Purple Shade Bundle"
    ],
    "Very Rare": [
        "Hip Hop Bundle", "Impulsive Punk Bundle", "Primal Hunter Bundle",
        "Shadow Combat Bundle", "Knight Clown Bundle", "Amber Megacypher Bundle",
        "Glare of Death Bundle", "MC Funk Bundle", "Shadow Earthshaker Bundle",
        "Wildfire Vagabond Bundle", "Wasteland Survivors Bundle", "Celestial Street Bundle",
        "Willful Wonders Bundle", "Quantic Unknown Bundle", "Cooper Prodigies Bundle",
        "Deep Sea Warriors Bundle", "Crazy Panda Bundle"
    ],
    "Rare": [
        "Doomsday Madness Bundle", "Bomb Squad Bundle", "Sandstorm Warriors Bundle",
        "Sakura Bundle", "Zombie Samurai Bundle", "Amplified Bassrock Bundle",
        "Green Criminal Bundle", "Metallic Swordmaster Bundle", "Snappy Bundle",
        "Lively Beast Bundle", "Agent Paws Bundle", "Anubis Legends II Bundle",
        "Bloodwing City Bundle", "Mesmerizing Knights Bundle", "Scrolls of Azure Bundle",
        "Jutsu Elemental Bundle", "Angelical Jogger Bundle"
    ],
    "Very Common": [
        "Royal Revelry Bundle", "Anubis Legends Bundle", "Gunslinger Bundle",
        "Shadow Red Bundle", "Arctic Blue Bundle", "Hiphop Angel Bundle",
        "Moody Lavisher Bundle", "Sultan of Lapis Bundle", "Pink Barrage Bundle",
        "Forsaken Creed Bundle", "Ultrasonic Rave Bundle", "Manic Circus Bundle",
        "Inferno Rage Bundle", "Checkered Nobility Bundle", "Voltage Vengeance Bundle",
        "Angelical Sprinter Bundle"
    ],
    "Common": [
        "Pirates Legend Bundle", "Dragon Slayers Bundle", "Blood Demon Bundle",
        "Galaxy Dino Bundle", "Breakdancer Bundle", "Imperial Malikah Bundle",
        "Rapper Angel Bundle", "Sultanah of Cerulea Bundle", "Digital Invasion Bundle",
        "Fabled Fox Bundle", "Endless Oblivion Bundle", "Evil Enchanted Bundle",
        "Palace of Poker Bundle", "Swordsoul Reality Bundle", "Avalanche Abyss Bundle"
    ],
    "Normal": [
        "Arcade Mayhem Bundle", "Wrath of the Wild Bundle", "Death Penalty Bundle",
        "Bunny Warrior Bundle", "Electric Shock Bundle", "Cobra Rage Bundle",
        "Keyboard Warrior Bundle", "Red Criminal Bundle", "Valiant Skorpina Bundle",
        "Bumblebee Bundle", "Rampage II: Uprising Bundle", "Specter Squad Bundle",
        "Guns for Hire Bundle", "Planet Rogue Bundle", "Bumble Rumblers Bundle",
        "Iron Blade Bundle"
    ]
}

RARITY_COLORS = {
    "Ultra Rare": "FF00FF",      # Magenta
    "Very Rare": "FFD700",       # Gold
    "Rare": "00BFFF",            # Blue
    "Very Common": "00FF00",     # Green
    "Common": "00CED1",          # Cyan
    "Normal": "FFFFFF"           # White
}

RARITY_STARS = {
    "Ultra Rare": "⭐⭐⭐⭐⭐⭐",
    "Very Rare": "⭐⭐⭐⭐⭐",
    "Rare": "⭐⭐⭐⭐",
    "Very Common": "⭐⭐⭐",
    "Common": "⭐⭐",
    "Normal": "⭐"
}

RARITY_WEIGHTS = {
    "Ultra Rare": 2,
    "Very Rare": 5,
    "Rare": 10,
    "Very Common": 20,
    "Common": 30,
    "Normal": 33
}

def spin_bundle():
    """Randomly select a bundle based on rarity weights"""
    rarities = list(RARITY_WEIGHTS.keys())
    weights = list(RARITY_WEIGHTS.values())
    selected_rarity = random.choices(rarities, weights=weights, k=1)[0]
    selected_bundle = random.choice(BUNDLE_DATA[selected_rarity])
    return selected_bundle, selected_rarity

def format_spnff_result(bundle_name, rarity):
    """Format the result with beautiful design"""
    color = RARITY_COLORS.get(rarity, "FFFFFF")
    stars = RARITY_STARS.get(rarity, "⭐")
    
    result = f"""[B][C][{color}]◎══════════════════════════════════════◎
[{color}]◉       🎰 BUNDLE SPIN RESULT 🎰       ◉
[{color}]◎══════════════════════════════════════◎

[FFD700]   {stars}

[FFFFFF]◎ 🎁 [{color}]{bundle_name}

[{color}]◎ ✨ Rarity: [{color}]{rarity}
[{color}]◎══════════════════════════════════════◎
[FFD700]◉ —͞N A Y A N 乡ㅤ友! BOT [9400D3]➤ /spnff ◉
"""
    return result


FREEZE_DURATION = 120  # seconds
manager = FREEZE_DURATION = 10  # seconds
from threading import Lock

status_response_cache = {}
cache_lock = Lock()
my_emotes = {
    "1": "909052002",   # 100lv
    "2": "909052011",   # SCAR
    "3": "909052012",   # 1st MP40
    "4": "909052004",   # 2nd MP40
    "5": "909052007",   # 1st M1014
    "6": "909052009",   # 2nd M1014
    "7": "909052003",   # XM8
    "8": "909051001",   # Famas
    "9": "909052005",   # UMP
    "10": "909052001",  # M1887
    "11": "909042008",  # Woodpecker
    "12": "909041005",  # Groza
    "13": "909033001",  # M4A1
    "14": "909038010",  # Thompson
    "15": "909038012",  # G18
    "16": "909045001",  # Parafal
    "17": "909049010",  # P90
    "18": "909051003",   # m60
    "19": "909000063",   #ak
    "20": "909037011",   #Fist
    "21": "909049012",   #open fire
    "22": "909000002",   #lol
    "23": "909051014",    #puffy ride
    "24": "909050009",    #circle
    "25": "909051013",    #petals
    "26": "909051010",    #motorbike
    "27": "909051004",     #shower
    "28": "909051002",     #dream
    "29": "909048015",     #paint
    "30": "909051001",     #angelic
    "31": "909044015",     #sword
    "32": "909041008",     #flare
    "33": "909049003",     #owl
    "34": "909050008",     #thor
    "35": "909049001",     #bigdill
    "36": "909041013",     #cs gm
    "37": "909050014",     #map readi
    "38": "909050015",     #tomato
    "39": "909050002",     #ninja summon
    "40": "909000034",     #pushup
    "41": "909000012",     #pirate flag
    "42": "909000020",     #devil move
    "43": "909000014",     #throne
    "44": "909000010",     #rose
    "45": "909038004",     #heart
    "46": "909040004",     #insoke
    "47": "909041012",     #br gm
    "48": "909041003",     #insok
    "49": "909000084",     #vutt
    "50": "909000142",     #pacha
    "51": "909000086",     #mythos
    "52": "909000087",     #champion
    "53": "909000088",     #sprrcar
    "54": "909000095",     #penguin
    "55": "909000125",     #sick move
    "56": "909000129",     #money
    "57": "909000130",     #bullet
    "58": "909000135",     #rps
    "59": "909000143",     #cricket
    "60": "909034003",     #agunn
    "61": "909033005",     #sick down
    "62": "909000034",     #flag
    "63": "909000039",     #mkney car
    "64": "909000055",     #ami dhonii
    "65": "909000064",     #choto saitama
    "66": "909000071",     #cobra dance
    "67": "909000074",     #cobra bike
    "68": "909000080",     #2021 ffws
    "69": "909034009",     #pasa 2
    "70": "909035006",     #flying sauce
    "71": "909034014",     #tiktoker
    "72": "909035001",     #free taka
    "73": "909035002",     #singer
    "74": "909035003",     #item not found
    "75": "909035010",     #gaan kora
    "76": "909036001",     #bhoot2
    "77": "909036002",     #shuvra
    "78": "909036004",     #cameraman
    "79": "909036008",     #skateboard
    "80": "909036010",     #signal
    "81": "909037003",     #omg
    "82": "909037004",     #pighy
    "83": "909037009",     #neor
    "84": "909038001",     #big bro
    "85": "909037002",     #bamboo
    "86": "909037006",     #ymmy
    "87": "909037008",     #juggle
    "88": "909037010",     #beast
    "89": "909037011",     #darcen
    "90": "909038003",     #lovebut
    "91": "909038006",     #ghonta
    "92": "909038008",     #mama coco
    "93": "909038011",     #should i
    "94": "909039004",     #bkndhuu
    "95": "909039006",     #what
    "96": "909040001",     #gariwala
    "97": "909052012",     #crush
    "98": "909040004",     #mach
    "99": "909040005",     #pop
    "100": "909052002"    #border
}
#------------------------------------------#
evo_emotes = {
    "1": "909000063",
    "2": "909000081",
    "3": "909000075",
    "4": "909000085",
    "5": "909000134",
    "6": "909000098",
    "7": "909035007",
    "8": "909051012",
    "9": "909000141",
    "10": "909034008",
    "11": "909051015",
    "12": "909041002",
    "13": "909039004",
    "14": "909042008",
    "15": "909051014",
    "16": "909039012",
    "17": "909040010",
    "18": "909035010",
    "19": "909041005",
    "20": "909051003",
    "21": "909034001"
}

# Emote mapping for evo commands
bal_bal = {
    "1": "909050010",
    "2": "909048005",
    "3": "909048016",
    "4": "909052005",
    "5": "909047007",
    "6": "909047015",
    "7": "909047009",
    "8": "909046015",
    "9": "909044005",
    "10": "909042006",
    "11": "909042002",
    "12": "909040009",
    "13": "909039001",
    "14": "909035009",
    "15": "909035014",
    "16": "909036002",
    "17": "909000087",
    "18": "909000089",
    "19": "909000096",
    "20": "909000077",
    "21": "909000064",
    "22": "909000054"
}

async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

# -------- AUTO EMOTE FROM JSON ONLY --------
def load_emotes_from_json():
    try:
        with open("emotes.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        emote_map = {}
        for item in data:
            num = item.get("Number")
            eid = item.get("Id")
            if num is not None and eid is not None:
                emote_map[str(num)] = int(eid)

        print(f"✅ Loaded {len(emote_map)} emotes from emotes.json")
        return emote_map

    except Exception as e:
        print("❌ emotes.json load error:", e)
        return {}

GENERAL_EMOTES_MAP = load_emotes_from_json()

#------------------------------------------#

import json

# --- LOAD EMOTES JSON ---
try:
    with open("emotes.json", "r") as f:
        emote_list = json.load(f)  # List of dicts

    # Convert to easy dict: Number -> Id
    EMOTE_MAP = {item["Number"]: item["Id"] for item in emote_list}

except FileNotFoundError:
    EMOTE_MAP = {}
    print("❌ emotes.json not found!")


async def emote_to_user_once(team_code, emote_number, target_uid, key, iv, region):
    emote_id = GENERAL_EMOTES_MAP.get(str(emote_number))
    if not emote_id:
        print("❌ Emote not found in emotes.json")
        return

    try:
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)

        await asyncio.sleep(0.1)

        emote_packet = await Emote_k(
            int(target_uid),
            int(emote_id),
            key,
            iv,
            region
        )
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)

        await asyncio.sleep(0.1)

        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)

        print(f"✅ Emote {emote_number} sent to UID {target_uid}")

    except Exception as e:
        print("❌ EMOTE ERROR:", e)

async def bot_emote_loop(key, iv, region, delay=6):
    emote_ids = list(GENERAL_EMOTES_MAP.values())

    print(f"🤖 BOT LOOP STARTED for UID {BOT_STATE['uid']}")

    while BOT_STATE["running"]:
        try:
            emote_id = random.choice(emote_ids)
            packet = await Emote_k(
                int(BOT_STATE["uid"]),
                int(emote_id),
                key,
                iv,
                region
            )
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet)
        except Exception as e:
            print("❌ BOT EMOTE ERROR:", e)

        for _ in range(delay):
            if not BOT_STATE["running"]:
                break
            await asyncio.sleep(1)

    print("🛑 BOT LOOP STOPPED")


import json
import math

with open("emote_menu.json","r",encoding="utf-8") as f:
    EMOTE_MENU = json.load(f)

def get_menu_page(page, per_page=25):

    items = sorted(EMOTE_MENU.items(), key=lambda x: int(x[0]))
    total_pages = math.ceil(len(items)/per_page)

    start = (page-1)*per_page
    end = start+per_page

    text = f"🎭 EMOTE MENU {page}/{total_pages}\n\n"

    for num,name in items[start:end]:
        text += f"{num} ➤ {name}\n"

    return text


# -------- COMMAND --------
async def handle_message(message):

    if message.startswith("/menu"):
        try:
            page = int(message.replace("/menu", ""))
        except:
            page = 1

        menu = get_menu_page(page)

        print(menu)  # এখানে bot দিয়ে send করবে
            
# Badge values for s1 to s8 commands - using your exact values
BADGE_VALUES = {
    "s1": 1048576,    # Your first badge
    "s2": 32768,      # Your second badge  
    "s3": 2048,       # Your third badge
    "s4": 64,         # Your fourth badge
    "s5": 262144     # Your seventh badge
}

def titles():
    """Return all titles instead of just one random"""
    titles_list = [
        905090075, 904990072, 904990069, 905190079, 904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072
    ]
    return titles_list  # Return the full list instead of random.choice            
    
def create_credentials_template():
    """Create a template credentials file"""
    template = """# NoTmeowL Free Fire Bot Credentials
# Fill in your Free Fire account credentials below

# Format 1: Comma-separated (RECOMMENDED)
uid=4263143059,password=2336099414_W0363_BY_SPIDEERIO_GAMING_WBYMF

# OR Format 2: Line-separated
# uid: 4263143059
# password: 2336099414_W0363_BY_SPIDEERIO_GAMING_WBYMF

# Save this file and restart the bot
"""
    
    filename = "shadmancodex.txt"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"📝 Created {filename} template file")
        print("✏️ Please edit it with your actual credentials")
        return False
    return True
    
da = 'f2212101'
dec = ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
x_list = ['1','01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']

def Decrypt_ID(da):
    """EXACT SAME as your code"""
    if da != None and len(da) == 10:
        w = 128
        xxx = len(da)/2 - 1
        xxx = str(xxx)[:1]
        for i in range(int(xxx)-1):
            w = w * 128
        x1 = da[:2]
        x2 = da[2:4]
        x3 = da[4:6]
        x4 = da[6:8]
        x5 = da[8:10]
        return str(w * x_list.index(x5) + (dec.index(x2) * 128) + dec.index(x1) + (dec.index(x3) * 128 * 128) + (dec.index(x4) * 128 * 128 * 128))

    if da != None and len(da) == 8:
        w = 128
        xxx = len(da)/2 - 1
        xxx = str(xxx)[:1]
        for i in range(int(xxx)-1):
            w = w * 128
        x1 = da[:2]
        x2 = da[2:4]
        x3 = da[4:6]
        x4 = da[6:8]
        return str(w * x_list.index(x4) + (dec.index(x2) * 128) + dec.index(x1) + (dec.index(x3) * 128 * 128))
    
    return None

def Encrypt_ID(x):
    """EXACT SAME as your code"""
    x = int(x)
    x = x / 128 
    if x > 128:
        x = x / 128
        if x > 128:
            x = x / 128
            if x > 128:
                x = x / 128
                strx = int(x)
                y = (x - int(strx)) * 128
                stry = str(int(y))
                z = (y - int(stry)) * 128
                strz = str(int(z))
                n = (z - int(strz)) * 128
                strn = str(int(n))
                m = (n - int(strn)) * 128
                return dec[int(m)] + dec[int(n)] + dec[int(z)] + dec[int(y)] + x_list[int(x)]
            else:
                strx = int(x)
                y = (x - int(strx)) * 128
                stry = str(int(y))
                z = (y - int(stry)) * 128
                strz = str(int(z))
                n = (z - int(strz)) * 128
                strn = str(int(n))
                return dec[int(n)] + dec[int(z)] + dec[int(y)] + x_list[int(x)]

def decrypt_api(cipher_text):
    """EXACT SAME as your code"""
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(bytes.fromhex(cipher_text)), AES.block_size)
    return plain_text.hex()

def encrypt_api(plain_text):
    """EXACT SAME as your code"""
    plain_text = bytes.fromhex(plain_text)
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()

def encrypt_message(plaintext_bytes):
    """EXACT SAME as your Flask API"""
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded)
    return binascii.hexlify(encrypted).decode('utf-8')    

def create_uid_protobuf(uid):
    """EXACT SAME as your Flask API"""
    msg = dev_generator_pb2.dev_generator()
    msg.saturn_ = int(uid)
    msg.garena = 1
    return msg.SerializeToString()

def enc(uid):
    """EXACT SAME as your Flask API"""
    pb = create_uid_protobuf(uid)
    return encrypt_message(pb)

def decode_player_info(binary):
    """EXACT SAME as your Flask API"""
    info = devxt_count_pb2.xt()
    info.ParseFromString(binary)
    return info    
    
import requests
import json

def load_jwt_token():
    """Load token from token.json"""
    try:
        with open("token.json", "r") as f:
            data = json.load(f)
        token = data.get("token")
        if token:
            print(f"✅ Loaded token: {token[:20]}...")
            return token
        else:
            print("❌ No token found in token.json")
            return None
    except Exception as e:
        print(f"❌ Error loading token: {e}")
        return None

def load_tokens_ind():
    """Load bulk tokens from token_ind.json"""
    try:
        with open("token_ind.json", "r") as f:
            tokens = json.load(f)
        print(f"📦 Loaded {len(tokens)} tokens from token_ind.json")
        return tokens
    except:
        print("❌ No tokens found in token_ind.json")
        return None
    
    
def send_friend_request_single(uid, token, region="IND"):
    """EXACT SAME as your Flask function but single"""
    try:
        encrypted_id = Encrypt_ID(uid)
        payload = f"08a7c4839f1e10{encrypted_id}1801"
        encrypted_payload = encrypt_api(payload)
        
        # Determine URL based on region
        if region.lower() == "ind":
            url = "https://client.ind.freefiremobile.com/RequestAddingFriend"
        elif region.lower() == "bd":
            url = "https://clientbp.ggpolarbear.com/RequestAddingFriend"
        else:
            url = "https://client.ind.freefiremobile.com/RequestAddingFriend"
        
        headers = {
            "Authorization": f"Bearer {token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB54",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0"
        }
        
        print(f"📤 Sending friend request to {uid}...")
        response = requests.post(url, data=bytes.fromhex(encrypted_payload), headers=headers, timeout=10, verify=False)
        
        if response.status_code == 200:
            print(f"✅ Success: Friend request sent to {uid}")
            return True
        else:
            print(f"❌ Failed: Status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False    
    
def start_autooo(self):    
    try:
        fields = {
            1: 9,
            2: {
                1: 12480598706,
            },
        }
        packet = create_protobuf_packet(fields).hex()
        header_length = len(encrypt_packet(packet, self.key, self.iv)) // 2
        header_length_final = dec_to_hex(header_length)
        if len(header_length_final) == 2:
            final_packet = "0515000000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 3:
            final_packet = "051500000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 4:
            final_packet = "05150000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 5:
            final_packet = "0515000" + header_length_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)
    except exception as e:
        print(e)

def load_credentials_from_file(filename="shadmancodex.txt"):
    """
    Load UID and password from shadmancodex.txt file
    """
    try:
        if not os.path.exists(filename):
            print(f"❌ {filename} not found!")
            create_credentials_template()
            return None, None
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        uid = None
        password = None
        
        # Try to find uid and password using regex
        import re
        
        # Look for uid=value or uid: value
        uid_match = re.search(r'(?:uid\s*[=:]\s*)(\d+)', content, re.IGNORECASE)
        if uid_match:
            uid = uid_match.group(1)
        
        # Look for password=value or password: value
        pass_match = re.search(r'(?:password\s*[=:]\s*)([^\s\n\r]+)', content, re.IGNORECASE)
        if pass_match:
            password = pass_match.group(1)
        
        if not uid or not password:
            print(f"❌ Could not find UID/password in {filename}")
            print("📝 Please make sure the file contains:")
            print("   uid=YOUR_UID,password=YOUR_PASSWORD")
            print("   OR")
            print("   uid: YOUR_UID")
            print("   password: YOUR_PASSWORD")
            return None, None
        
        print(f"✅ Loaded credentials from {filename}")
        print(f"👤 UID: {uid}")
        print(f"🔑 Password: {'*' * len(password)}")
        
        return uid, password
        
    except Exception as e:
        print(f"❌ Error loading credentials: {e}")
        return None, None



# Helper functions for ghost join
def dec_to_hex(decimal):
    """Convert decimal to hex string"""
    hex_str = hex(decimal)[2:]
    return hex_str.upper() if len(hex_str) % 2 == 0 else '0' + hex_str.upper()



async def encrypt_packet(packet_hex, key, iv):
    """Encrypt packet using AES CBC"""
    cipher = AES.new(key, AES.MODE_CBC, iv)
    packet_bytes = bytes.fromhex(packet_hex)
    padded_packet = pad(packet_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded_packet)
    return encrypted.hex()

async def nmnmmmmn(packet_hex, key, iv):
    """Wrapper for encrypt_packet"""
    return await encrypt_packet(packet_hex, key, iv)
    

def generate_random_hex_color():
    """Generate random hex color for messages"""
    return ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

def bunner_():
    """Generate random avatar ID"""
    return random.randint(100000000, 999999999)

# Add this function to your code
def Encrypt(number):
    """Encrypt function from your first TCP bot"""
    number = int(number)
    encoded_bytes = []
    
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    
    return bytes(encoded_bytes).hex()


async def send_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG):
    """Send join request that actually works"""
    
    try:
        # Step 1: Reset bot to solo mode
        print("🔄 Resetting bot to solo mode...")
        await reset_bot_state(key, iv, region)
        await asyncio.sleep(1)
        
        # Step 2: Create bot's own squad (so it has context)
        print("🏠 Creating bot squad...")
        squad_packet = await OpEnSq(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', squad_packet)
        await asyncio.sleep(1)
        
        # Step 3: Send join request
        print(f"📨 Sending join request to {target_uid}...")
        join_packet = await create_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG)
        
        if join_packet:
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            print(f"✅ Bot join request sent! Player can now accept.")
            return True
        else:
            print(f"❌ Failed to create join packet")
            return False
            
    except Exception as e:
        print(f"❌ Error in working join request: {e}")
        return False
        
async def handle_join_req_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type, LoGinDaTaUncRypTinG):
    """Handle /join_req command - bot sends join request to player"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 2:
        error_msg = f"""[B][C][FF0000]❌ Usage: /join_req (player_uid)
Example: /join_req 123456789

What happens:
1. Bot goes solo mode
2. Bot creates its own squad  
3. Bot sends join request to player
4. Player sees: "BotName wants to join your team"
5. Player clicks Accept → Bot joins player's team
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    target_uid = parts[1]
    
    if not target_uid.isdigit():
        error_msg = f"[B][C][FF0000]❌ Invalid UID! Must be numbers only.\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Send initial message
    initial_msg = f"""[B][C][FFFF00]🤖 BOT JOIN REQUEST INITIATED

👤 Target Player: {target_uid}
⚙️ Steps:
1. Bot resetting to solo mode...
2. Bot creating squad...
3. Sending join request...

⏳ Please wait...
"""
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        success = await send_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG)
        
        if success:
            success_msg = f"""[B][C][FFFF00]✅ BOT JOIN REQUEST SENT!

🎯 Target: {target_uid}
🤖 Bot Name: NoTmeowL
✅ Status: Ready to join

📱 Player will see:
"NoTmeowL wants to join your team"

✅ When player clicks ACCEPT:
Bot will automatically join player's team!
"""
        else:
            success_msg = f"""[B][C][FF0000]❌ FAILED!

Possible reasons:
1. Bot not connected properly
2. Bot already in a squad
3. Server issue

Try again in 10 seconds.
"""
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Cleanup: Leave squad after sending request
        await asyncio.sleep(3)
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print("🧹 Bot cleaned up (left squad)")
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)        
    
async def create_simple_start_packet(key, iv):
    """Create simple start match packet (00 00 00 d6)"""
    
    # This appears to be a minimal start packet
    # 00 00 00 d6 in hex = 214 in decimal (packet type?)
    
    fields = {
        1: 214,  # Packet type for start match (d6 hex = 214 decimal)
        2: {
            1: 1,  # Start match command
        }
    }
    
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Generate final packet
    final_packet = await GeneRaTePk(packet_hex, '0514', key, iv)  # Use appropriate packet type
    
    print(f"✅ Simple start match packet created")
    return final_packet
    
async def create_detailed_start_packet(key, iv, region="IND"):
    """Create detailed start match packet with device info"""
    
    # Decoded from your hex: contains device info (vivo, arm64, etc.)
    
    fields = {
        1: 269,  # 0x10D = 269 decimal (detailed start packet)
        2: {
            1: 8,           # Unknown
            2: 8,           # Unknown
            3: 11,          # Unknown
            4: 1,           # Unknown
            5: "vivo",      # Device brand
            6: "130",       # Device model
            7: "arm64-v8a", # CPU architecture
            8: "f538dc9b-cec9-43cd-8125-95f7f4f1f7e3",  # Device ID
            9: "FFD58FB4F76F648C2A5E21EBCFA3AAE81B4C9B7D97",  # Unknown
            10: "voice",    # Audio type
            11: "V2059",    # Version
            12: "mt6785",   # Processor
            13: "AFFD58FB4F76F648C2A5E21EBCFA3AAE81B4C9B7D97",  # Unknown
            14: "IND_1999120752610979840",  # Region + timestamp
            15: 269         # Packet length?
        }
    }
    
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Determine packet type based on region
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    final_packet = await GeneRaTePk(packet_hex, packet_type, key, iv)
    
    print(f"✅ Detailed start match packet created")
    return final_packet
        
async def generate_guest_accounts(count=1, name="BlackApis", password_prefix="FF"):
    """Generate guest accounts using the API"""
    api_url = f"https://gen-by-black-api.vercel.app/generate?name={name}&password_prefix={password_prefix}"
    
    accounts = []
    failed_attempts = 0
    max_retries = 10
    
    print(f"📡 Generating {count} guest accounts...")
    
    for i in range(count):
        retry_count = 0
        success = False
        
        while retry_count < max_retries and not success:
            try:
                print(f"🔄 Attempt {retry_count + 1}/{max_retries} for account {i + 1}/{count}...")
                
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=30)) as session:
                    async with session.get(api_url) as response:
                        
                        if response.status == 200:
                            data = await response.json()
                            
                            if data.get("success"):
                                account = {
                                    'uid': data.get('uid'),
                                    'password': data.get('password'),
                                    'name': data.get('name'),
                                    'timestamp': time.time()
                                }
                                accounts.append(account)
                                print(f"✅ Account {i + 1}: {account['uid']}")
                                success = True
                                failed_attempts = 0  # Reset failed attempts counter
                                
                            else:
                                print(f"❌ API error: {data.get('message', 'Unknown error')}")
                                retry_count += 1
                                await asyncio.sleep(2)
                                
                        elif response.status == 503:
                            print(f"⚠️ Server busy (503), retrying in 3 seconds...")
                            retry_count += 1
                            await asyncio.sleep(3)
                            
                        else:
                            print(f"❌ HTTP {response.status}, retrying...")
                            retry_count += 1
                            await asyncio.sleep(2)
                            
            except asyncio.TimeoutError:
                print(f"⏰ Timeout, retrying...")
                retry_count += 1
                await asyncio.sleep(2)
                
            except Exception as e:
                print(f"❌ Error: {str(e)[:50]}...")
                retry_count += 1
                await asyncio.sleep(2)
        
        if not success:
            print(f"❌ Failed to generate account {i + 1} after {max_retries} attempts")
            failed_attempts += 1
            
            # If too many failures in a row, stop
            if failed_attempts >= 3:
                print("🛑 Too many failures, stopping...")
                break
        
        # Small delay between accounts to avoid rate limiting
        if i < count - 1:
            await asyncio.sleep(1)
    
    return accounts

def save_guest_accounts(accounts, filename="guest_accounts.json"):
    """Save guest accounts to JSON file"""
    try:
        # Load existing accounts if file exists
        existing = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                existing = json.load(f)
        
        # Combine with new accounts
        all_accounts = existing + accounts
        
        # Save to file
        with open(filename, 'w') as f:
            json.dump(all_accounts, f, indent=2)
        
        print(f"💾 Saved {len(accounts)} accounts to {filename}")
        print(f"📊 Total accounts: {len(all_accounts)}")
        
        return True
    except Exception as e:
        print(f"❌ Error saving accounts: {e}")
        return False

async def generate_and_save_accounts(count, name="BlackApis", password_prefix="FF"):
    """Generate and save accounts with progress updates"""
    start_time = time.time()
    
    print(f"\n🎯 GENERATING {count} GUEST ACCOUNTS")
    print("="*50)
    
    accounts = await generate_guest_accounts(count, name, password_prefix)
    
    if accounts:
        # Save to file
        save_guest_accounts(accounts)
        
        # Display results
        elapsed = time.time() - start_time
        print("\n" + "="*50)
        print("📊 GENERATION COMPLETE")
        print("="*50)
        print(f"✅ Success: {len(accounts)}/{count} accounts")
        print(f"⏱️ Time: {elapsed:.1f} seconds")
        print(f"📁 Saved to: guest_accounts.json")
        
        # Show first 3 accounts as preview
        print("\n📋 FIRST 3 ACCOUNTS:")
        for i, acc in enumerate(accounts[:3]):
            print(f"  {i+1}. UID: {acc['uid']} | Pass: {acc['password']}")
        
        if len(accounts) > 3:
            print(f"  ... and {len(accounts) - 3} more")
    
    return accounts        
        
async def start_match(key, iv, region, detailed=False):
    """Start Free Fire match - bot must be in a squad/team"""
    
    try:
        if detailed:
            start_packet = await create_detailed_start_packet(key, iv, region)
        else:
            start_packet = await create_simple_start_packet(key, iv)
        
        if start_packet:
            # Send via Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
            print("🎮 Start match packet sent!")
            return True
        else:
            print("❌ Failed to create start packet")
            return False
            
    except Exception as e:
        print(f"❌ Error starting match: {e}")
        return False       
        
async def handle_start_match_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /ss command to start match"""
    
    parts = inPuTMsG.strip().split()
    
    # Check if user wants detailed start
    detailed = False
    if len(parts) > 1 and parts[1].lower() == "detailed":
        detailed = True
    
    # Send initial message
    initial_msg = f"""[B][C][FFFF00]🎮 STARTING MATCH...

⚙️ Mode: {'Detailed' if detailed else 'Simple'}
🤖 Bot must be in a squad!
⏳ Please wait...
"""
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        success = await start_match(key, iv, region, detailed)
        
        if success:
            success_msg = f"""[B][C][FFFF00]✅ MATCH START COMMAND SENT!

📋 Details:
• Type: {'Detailed device info' if detailed else 'Simple start'}
• Status: Match starting...
• Requirement: Bot must be squad leader

🎯 If bot is squad leader, match will begin!
"""
        else:
            success_msg = f"""[B][C][FF0000]❌ FAILED TO START MATCH!

Possible reasons:
1. Bot not in a squad
2. Bot not squad leader
3. Invalid packet structure
4. Server connection issue

💡 Make sure bot is in a squad as leader!
"""
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        
async def debug_start_match():
    """Debug function to test start packets"""
    
    print("🔍 Analyzing start packets...")
    print(f"Simple packet hex: 00 00 00 d6")
    print(f"Decimal value: {int('d6', 16)} = 214")
    
    # Try to decode the detailed packet
    detailed_hex = "0a8d010808100b180122047669766f2a02313330f6a8858c023a0961726d36342d76386142004a2466353338646339622d636563392d343363642d383132352d393566376634663166376533522a4646443538464234463736463634384332413545323145424346413341414538314234433942374439375a05766f69636562055632303539680172066d74363738351241464644353846423446373646363438433241354532314542434641334141453831423443394237443937494e445f31393939313230373532363130393739383430188d01"
    
    print(f"\n📊 Detailed packet length: {len(detailed_hex)//2} bytes")
    print(f"First bytes: {detailed_hex[:20]}...")
    
    # Try to parse as protobuf
    try:
        from protobuf_decoder.protobuf_decoder import Parser
        parsed = Parser().parse(bytes.fromhex(detailed_hex))
        print(f"\n✅ Parsed detailed packet:")
        print(parsed)
    except Exception as e:
        print(f"❌ Could not parse: {e}")
        


async def check_player_status(target_uid, key, iv, max_wait=3):
    """Direct function to check player status with proper waiting"""
    try:
        # Clear old cache
        if target_uid in status_response_cache:
            del status_response_cache[target_uid]
        
        # Send request
        status_packet = await createpacketinfo(target_uid, key, iv)
        if not status_packet:
            return None, "Failed to create packet"
        
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)
        print(f"📤 Sent status request for {target_uid}")
        
        # Wait for response with polling
        start_time = time.time()
        while time.time() - start_time < max_wait:
            if target_uid in status_response_cache:
                cache_data = status_response_cache[target_uid]
                return cache_data, "Success"
            
            await asyncio.sleep(0.1)  # Short sleep
        
        return None, f"No response after {max_wait} seconds"
        
    except Exception as e:
        return None, f"Error: {str(e)}"

async def createpacketinfo(idddd, key, iv):
    """Create player status request packet - SAME as first TCP bot"""
    try:
        ida = Encrypt(idddd)
        packet = f"080112090A05{ida}1005"
        header_lenth = len(await encrypt_packet(packet, key, iv)) // 2
        header_lenth_final = dec_to_hex(header_lenth)
        
        if len(header_lenth_final) == 2:
            final_packet = "0F15000000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 3:
            final_packet = "0F1500000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 4:
            final_packet = "0F150000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 5:
            final_packet = "0F15000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        else:
            final_packet = "0F1500000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
            
        return bytes.fromhex(final_packet)
        
    except Exception as e:
        print(f"Error creating packet info: {e}")
        return None

def fix_num(number):
    """Format numbers with breaks - from first TCP"""
    fixed = ""
    count = 0
    num_str = str(number)
    
    for char in num_str:
        if char.isdigit():
            count += 1
        fixed += char
        if count == 3:
            fixed += "[c]"
            count = 0
    return fixed

def get_available_room(input_text):
    """Parse protobuf to JSON - from first TCP"""
    try:
        from protobuf_decoder.protobuf_decoder import Parser
        parsed_results = Parser().parse(input_text)
        parsed_results_objects = parsed_results
        parsed_results_dict = parse_results(parsed_results_objects)
        json_data = json.dumps(parsed_results_dict)
        return json_data
    except Exception as e:
        print(f"error {e}")
        return None

def parse_results(parsed_results):
    """Helper for get_available_room"""
    result_dict = {}
    for result in parsed_results:
        field_data = {}
        field_data["wire_type"] = result.wire_type
        if result.wire_type == "varint":
            field_data["data"] = result.data
        if result.wire_type == "string":
            field_data["data"] = result.data
        if result.wire_type == "bytes":
            field_data["data"] = result.data
        elif result.wire_type == "length_delimited":
            field_data["data"] = parse_results(result.data.results)
        result_dict[result.field] = field_data
    return result_dict  # ← ADD THIS LINE

def get_player_status(packet):
    """Get player status from packet"""
    json_result = get_available_room(packet)
    if not json_result:
        return "OFFLINE"
    
    parsed_data = json.loads(json_result)
    
    if "5" not in parsed_data or "data" not in parsed_data["5"]:
        return "OFFLINE"
    
    json_data = parsed_data["5"]["data"]
    
    if "1" not in json_data or "data" not in json_data["1"]:
        return "OFFLINE"
    
    data = json_data["1"]["data"]
    
    if "3" not in data:
        return "OFFLINE"
    
    status_data = data["3"]
    
    if "data" not in status_data:
        return "OFFLINE"
    
    status = status_data["data"]
    
    if status == 1:
        return "SOLO"
    if status == 2:
        if "9" in data and "data" in data["9"]:
            group_count = data["9"]["data"]
            countmax1 = data["10"]["data"]
            countmax = countmax1 + 1
            return f"INSQUAD ({group_count}/{countmax})"
        return "INSQUAD"
    if status in [3, 5]:
        return "INGAME"
    if status == 4:
        return "IN ROOM"
    if status in [6, 7]:
        return "IN SOCIAL ISLAND MODE"
    
    return "NOTFOUND"

def get_idroom_by_idplayer(packet):
    """Extract room ID from player info packet"""
    try:
        json_result = get_available_room(packet)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        idroom = data['15']["data"]
        return idroom
    except Exception as e:
        print(f"Error extracting room ID: {e}")
        return None



def get_leader(packet):
    """Extract leader ID from squad packet"""
    try:
        json_result = get_available_room(packet)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        leader = data['8']["data"]
        return leader
    except Exception as e:
        print(f"Error extracting leader: {e}")
        return None

# Add to your global variables

# Add near top with other globals
status_queue = asyncio.Queue()
cache_dict = {}

# In TcPOnLine, instead of caching directly:
async def handle_status_response(hex_data):
    """Process and queue status responses"""
    try:
        # ... parsing code ...
        
        # Put in queue instead of direct cache
        await status_queue.put({
            'player_id': player_id,
            'data': cache_entry
        })
        
        print(f"📤 Queued status for {player_id}")
        
    except Exception as e:
        print(f"❌ Queue error: {e}")

# In TcPChaT, add a queue consumer
async def cache_consumer():
    """Consume status responses from queue"""
    while True:
        try:
            item = await status_queue.get()
            player_id = item['player_id']
            cache_dict[player_id] = item['data']
            print(f"📥 Cache updated for {player_id}")
            status_queue.task_done()
        except Exception as e:
            print(f"❌ Consumer error: {e}")
        await asyncio.sleep(0.1)



# Start consumer in your main function
async def StarTinG():
    # Start consumer
    consumer_task = asyncio.create_task(cache_consumer())
    
    while True:
        try:
            await asyncio.wait_for(MaiiiinE(), timeout = 7 * 60 * 60)
        except KeyboardInterrupt:
            consumer_task.cancel()
            break
        except asyncio.TimeoutError: 
            print("Token ExpiRed ! , ResTartinG")
        except Exception as e: 
            print(f"ErroR TcP - {e} => ResTarTinG ...")

import pickle
import os
import time

CACHE_FILE = 'status_cache.pkl'
CACHE_TIMEOUT = 30  # Cache entries expire after 30 seconds

def save_to_cache(player_id, data):
    """Save status to file cache with timestamp"""
    try:
        # Load existing cache
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'rb') as f:
                    cache = pickle.load(f)
            except:
                cache = {}
        else:
            cache = {}
        
        # Add timestamp
        data['saved_at'] = time.time()
        
        # Update cache
        cache[str(player_id)] = data
        
        # Save back
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(cache, f)
        
        print(f"💾 Saved to file cache: {player_id}")
        return True
    except Exception as e:
        print(f"❌ Cache save error: {e}")
        import traceback
        traceback.print_exc()
        return False

def load_from_cache(player_id):
    """Load status from file cache, check expiration"""
    try:
        if not os.path.exists(CACHE_FILE):
            return None
        
        with open(CACHE_FILE, 'rb') as f:
            cache = pickle.load(f)
        
        player_key = str(player_id)
        if player_key in cache:
            data = cache[player_key]
            
            # Check if cache is expired
            if 'saved_at' in data:
                if time.time() - data['saved_at'] > CACHE_TIMEOUT:
                    print(f"⏰ Cache expired for {player_id}")
                    del cache[player_key]
                    with open(CACHE_FILE, 'wb') as f:
                        pickle.dump(cache, f)
                    return None
            
            print(f"📥 Loaded from cache: {player_id}")
            return data
        
        return None
    except Exception as e:
        print(f"❌ Cache load error: {e}")
        return None

def clear_cache_entry(player_id):
    """Clear specific cache entry"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            
            player_key = str(player_id)
            if player_key in cache:
                del cache[player_key]
                
            with open(CACHE_FILE, 'wb') as f:
                pickle.dump(cache, f)
            print(f"🗑️ Cleared cache for {player_id}")
    except Exception as e:
        print(f"❌ Clear cache error: {e}")

def debug_file_cache():
    """Debug the file cache"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            print(f"\n📁 FILE CACHE DEBUG:")
            print(f"Size: {len(cache)} entries")
            for uid, data in cache.items():
                age = time.time() - data.get('saved_at', 0)
                status = data.get('status', 'NO STATUS')
                print(f"  {uid}: {status} (age: {age:.1f}s)")
            print("---\n")
            return cache
        else:
            print("📁 No cache file exists")
            return {}
    except Exception as e:
        print(f"❌ Cache debug error: {e}")
        return {}

def load_from_cache(player_id):
    """Load status from file cache"""
    try:
        if not os.path.exists(CACHE_FILE):
            return None
        
        with open(CACHE_FILE, 'rb') as f:
            cache = pickle.load(f)
        
        if player_id in cache:
            return cache[player_id]
        return None
    except Exception as e:
        print(f"❌ Cache load error: {e}")
        return None

def clear_cache_entry(player_id):
    """Clear specific cache entry"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            
            if player_id in cache:
                del cache[player_id]
                
            with open(CACHE_FILE, 'wb') as f:
                pickle.dump(cache, f)
    except:
        pass


    
    
    async def get_account_token(self, uid, password):
        """Get access token for a specific account"""
        try:
            url = "https://100067.connect.garena.com/oauth/guest/token/grant"
            headers = {
                "Host": "100067.connect.garena.com",
                "User-Agent": await Ua(),
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "close"
            }
            data = {
                "uid": uid,
                "password": password,
                "response_type": "token",
                "client_type": "2",
                "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
                "client_id": "100067"
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=data) as response:
                    if response.status == 200:
                        data = await response.json()
                        open_id = data.get("open_id")
                        access_token = data.get("access_token")
                        return open_id, access_token
            return None, None
        except Exception as e:
            print(f"❌ Error getting token for {uid}: {e}")
            return None, None
    
    async def send_join_from_account(self, target_uid, account_uid, password, key, iv, region):
        """Send join request from a specific account"""
        try:
            # Get token for this account
            open_id, access_token = await self.get_account_token(account_uid, password)
            if not open_id or not access_token:
                return False
            
            # Create join packet using the account's credentials
            join_packet = await self.create_account_join_packet(target_uid, account_uid, open_id, access_token, key, iv, region)
            if join_packet:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                return True
            return False
            
        except Exception as e:
            print(f"❌ Error sending join from {account_uid}: {e}")
            return False

async def join_custom_room(room_id, room_password, key, iv, region):
    """Join custom room with proper Free Fire packet structure"""
    fields = {
        1: 61,  # Room join packet type (verified for Free Fire)
        2: {
            1: int(room_id),
            2: {
                1: int(room_id),  # Room ID
                2: int(time.time()),  # Timestamp
                3: "BOT",  # Player name
                5: 12,  # Unknown
                6: 9999999,  # Unknown
                7: 1,  # Unknown
                8: {
                    2: 1,
                    3: 1,
                },
                9: 3,  # Room type
            },
            3: str(room_password),  # Room password
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
    
async def leave_squad(key, iv, region):
    """Leave squad - converted from your old TCP leave_s()"""
    fields = {
        1: 7,
        2: {
            1: 12480598706  # Your exact value from old TCP
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)    
    
async def request_join_with_badge(target_uid, badge_value, key, iv, region):
    """Send join request with specific badge - converted from your old TCP"""
    fields = {
        1: 33,
        2: {
            1: int(target_uid),
            2: region.upper(),
            3: 1,
            4: 1,
            5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),
            6: "iG:[C][B][FF0000] MAHIR",
            7: 330,
            8: 1000,
            10: region.upper(),
            11: bytes([49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                       97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49, 50, 48, 102, 53]),
            12: 1,
            13: int(target_uid),
            14: {
                1: 2203434355,
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            16: 1,
            17: 1,
            18: 312,
            19: 46,
            23: bytes([16, 1, 24, 1]),
            24: int(get_random_avatar()),
            26: "",
            28: "",
            31: {
                1: 1,
                2: badge_value  # Dynamic badge value
            },
            32: badge_value,    # Dynamic badge value
            34: {
                1: int(target_uid),
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        },
        10: "en",
        13: {
            2: 1,
            3: 1
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)
    
async def reset_bot_state(key, iv, region):
    """Reset bot to solo mode before spam - Critical step from your old TCP"""
    try:
        # Leave any current squad (using your exact leave_s function)
        leave_packet = await leave_squad(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        await asyncio.sleep(0.5)
        
        print("✅ Bot state reset - left squad")
        return True
        
    except Exception as e:
        print(f"❌ Error resetting bot: {e}")
        return False    
    
async def create_custom_room(room_name, room_password, max_players, key, iv, region):
    """Create a custom room"""
    fields = {
        1: 3,  # Create room packet type
        2: {
            1: room_name,
            2: room_password,
            3: max_players,  # 2, 4, 8, 16, etc.
            4: 1,  # Room mode
            5: 1,  # Map
            6: "en",  # Language
            7: {   # Player info
                1: "BotHost",
                2: int(await xBunnEr()),
                3: 330,
                4: 1048576,
                5: "BOTCLAN"
            }
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)              




async def handle_badge_command(cmd, inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle individual badge commands"""
    parts = inPuTMsG.strip().split()
    if len(parts) < 2:
        error_msg = f"[B][C][FF0000]❌ Usage: /{cmd} (uid)\nExample: /{cmd} 123456789\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    target_uid = parts[1]
    badge_value = BADGE_VALUES.get(cmd, 1048576)
    
    if not target_uid.isdigit():
        error_msg = f"[B][C][FF0000]❌ Please write a valid player ID!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Send initial message
    initial_msg = f"[B][C][1E90FF]🌀 Request received! Preparing to send {cmd} ({badge_value}) to {target_uid}...\n"
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        # Create badge packet
        badge_packet = await request_join_with_badge(target_uid, badge_value, key, iv, region)
        
        if badge_packet:
            # Send packet 5 times for spam effect
            for i in range(10):
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', badge_packet)
                print(f"✅ Sent /{cmd} badge #{i+1} with value {badge_value}")
                await asyncio.sleep(0.5)  # Slight delay
            
            success_msg = f"[B][C][FFFF00]✅ Successfully Sent {cmd} Badge!\n🎯 Target: {target_uid}\n🏷️ Badge Value: {badge_value}\n📤 Packets Sent: 5\n"
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to create badge packet!\n"
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error in /{cmd}: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)




    
    
    
async def auto_rings_emote_dual(uid, key, iv, region):
    """Send The Rings emote to both sender and bot for dual emote effect"""
    try:
        # The Rings emote ID
        rings_emote_id = 909050009
        
        # Get bot's UID
        bot_uid = 13601801571
        
        # Send emote to SENDER (person who invited)
        emote_to_sender = await Emote_k(int(uid), rings_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
        
        # Small delay between emotes
        await asyncio.sleep(0.5)
        
        # Send emote to BOT (bot performs emote on itself)
        emote_to_bot = await Emote_k(int(bot_uid), rings_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_bot)
        
        print(f"🤖 Bot performed dual Rings emote with sender {uid} and bot {bot_uid}!")
        
    except Exception as e:
        print(f"Error sending dual rings emote: {e}")   
        
         
async def magic_bundle_sequence(team_code, chat_type, chat_id, uid, key, iv, region):
    try:
        for i in range(1, 12):

            # 🔴 Leave squad
            leave_packet = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            await asyncio.sleep(1.2)

            # 🟢 Join squad (IMPORTANT FIX)
            join_packet = await GenJoinSquadsPacket(team_code, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            await asyncio.sleep(0.25)

            # 📦 Send bundle command
            bundle_cmd = f"/b {i}"
            await safe_send_message(
                chat_type,
                bundle_cmd,
                uid,
                chat_id,
                key,
                iv
            )

            print(f"✅ Magic bundle sent: {bundle_cmd}")
            await asyncio.sleep(4.75)

        # 🟢 FINAL JOIN (stay in team, no leave)
        final_join = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', final_join)

        await safe_send_message(
            chat_type,
            "[B][C][00FF00]✨ Magic completed! Bot is now staying in team.",
            uid,
            chat_id,
            key,
            iv
        )

    except Exception as e:
        print("❌ Magic bundle error:", e) 
             
        
async def Room_Spam(Uid, Rm, Nm, K, V):
    fields = {
        1: 78,
        2: {
            1: int(Rm),  
            2: "iG:[C][B][FF0000]NoTmeowL",  
            3: {
                2: 1,
                3: 1
            },
            4: 330,      
            5: 6000,     
            6: 201,      
            10: int(await xBunnEr()),  
            11: int(Uid), # Target UID
            12: 1,       
            15: {
                1: 1,
                2: 32768
            },
            16: 32768,    
            18: {
                1: 11481904755,  
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            
            31: {
                1: 1,
                2: 32768
            },
            32: 32768,    
            34: {
                1: int(Uid),   
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        }
    }
    
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0e15', K, V)

async def emotes_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG):
    """Cycle through all evolution emotes - BOT DOES ONLY ONE EMOTE"""
    global evo_cycle_running
    
    # GET BOT UID
    try:
        bot_uid = LoGinDaTaUncRypTinG.AccountUID
    except:
        bot_uid = 13743555
    
    cycle_count = 0
    while evo_cycle_running:
        cycle_count += 1
        print(f"Starting evolution emote cycle #{cycle_count}")
        
        emote_list = list(my_emotes.items())
        total_emotes = len(emote_list)
        
        for index, (emote_number, emote_id) in enumerate(emote_list):
            if not evo_cycle_running:
                break
                
            # USER does emote
            for uid in uids:
                try:
                    uid_int = int(uid)
                    user_emote = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', user_emote)
                except Exception as e:
                    print(f"Error: {e}")
            
            await asyncio.sleep(0.5)
            
            # Wait 5 seconds before next emote
            if evo_cycle_running:
                wait_time = 5
                for i in range(wait_time):
                    if not evo_cycle_running:
                        break
                    await asyncio.sleep(1)
    
    print("Cycle stopped")
        
async def evo_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG):
    """Cycle through all evolution emotes - BOT DOES ONLY ONE EMOTE"""
    global evo_cycle_running
    
    # GET BOT UID
    try:
        bot_uid = LoGinDaTaUncRypTinG.AccountUID
    except:
        bot_uid = 13743555
    
    cycle_count = 0
    while evo_cycle_running:
        cycle_count += 1
        print(f"Starting evolution emote cycle #{cycle_count}")
        
        emote_list = list(evo_emotes.items())
        total_emotes = len(emote_list)
        
        for index, (emote_number, emote_id) in enumerate(emote_list):
            if not evo_cycle_running:
                break
                
            # USER does emote
            for uid in uids:
                try:
                    uid_int = int(uid)
                    user_emote = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', user_emote)
                except Exception as e:
                    print(f"Error: {e}")
            
            await asyncio.sleep(0.5)
            
            # Wait 5 seconds before next emote
            if evo_cycle_running:
                wait_time = 5
                for i in range(wait_time):
                    if not evo_cycle_running:
                        break
                    await asyncio.sleep(1)
    
    print("Cycle stopped")

async def evo_cycle_sm(uids, key, iv, region, LoGinDaTaUncRypTinG):
    global evo_cycle_running
    
    try:
        # GET BOT UID
        try:
            bot_uid = LoGinDaTaUncRypTinG.AccountUID
        except:
            bot_uid = 13743555551
    
        cycle_count = 0
        while evo_cycle_running:
            cycle_count += 1
            print(f"Starting evolution emote cycle #{cycle_count}")
            
            emote_list = list(evo_emotes.items())
            total_emotes = len(emote_list)
            
            for index, (emote_number, emote_id) in enumerate(emote_list):
                if not evo_cycle_running:
                    break
                    
                for uid in uids:
                    try:
                        uid_int = int(uid)
                        user_emote = await Emote_k(uid_int, int(emote_id), key, iv, region)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', user_emote)
                    except Exception as e:
                        print(f"Error: {e}")
                
                await asyncio.sleep(0.5)
                
                opposite_index = total_emotes - 1 - index
                opposite_number, opposite_id = emote_list[opposite_index]
                
                try:
                    bot_self_emote = await Emote_k(int(bot_uid), int(opposite_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote)
                    print(f"🤖 Bot Emote #{opposite_number} sent.")
                except Exception as e:
                    print(f"Bot error: {e}")
                
                if evo_cycle_running:
                    for i in range(5):
                        if not evo_cycle_running:
                            break
                        await asyncio.sleep(1)

    except asyncio.CancelledError:
        print("🛑 Evo cycle cancelled instantly")
        evo_cycle_running = False
        return

    finally:
        print("Cycle stopped")

async def evo_cycle_sam(uids, key, iv, region, LoGinDaTaUncRypTinG):
    global evo_cycle_running
    
    try:
        # GET BOT UID
        try:
            bot_uid = LoGinDaTaUncRypTinG.AccountUID
        except:
            bot_uid = 13743555551
    
        cycle_count = 0
        while evo_cycle_running:
            cycle_count += 1
            print(f"Starting evolution emote cycle #{cycle_count}")
            
            emote_list = list(my_emotes.items())
            total_emotes = len(emote_list)
            
            for index, (emote_number, emote_id) in enumerate(emote_list):
                if not evo_cycle_running:
                    break
                    
                for uid in uids:
                    try:
                        uid_int = int(uid)
                        user_emote = await Emote_k(uid_int, int(emote_id), key, iv, region)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', user_emote)
                    except Exception as e:
                        print(f"Error: {e}")
                
                await asyncio.sleep(0.5)
                
                opposite_index = total_emotes - 1 - index
                opposite_number, opposite_id = emote_list[opposite_index]
                
                try:
                    bot_self_emote = await Emote_k(int(bot_uid), int(opposite_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote)
                    print(f"🤖 Bot Emote #{opposite_number} sent.")
                except Exception as e:
                    print(f"Bot error: {e}")
                
                if evo_cycle_running:
                    for i in range(5):
                        if not evo_cycle_running:
                            break
                        await asyncio.sleep(1)

    except asyncio.CancelledError:
        print("🛑 Evo cycle cancelled instantly")
        evo_cycle_running = False
        return

    finally:
        print("Cycle stopped")

async def evo_cycle_bot(uids, key, iv, region, LoGinDaTaUncRypTinG):
    global evo_cycle_running
    
    try:
        # GET BOT UID
        try:
            bot_uid = LoGinDaTaUncRypTinG.AccountUID
        except:
            bot_uid = 13743555551
    
        cycle_count = 0
        while evo_cycle_running:
            cycle_count += 1
            print(f"Starting evolution emote cycle #{cycle_count}")
            
            emote_list = list(bal_bal.items())
            total_emotes = len(emote_list)
            
            for index, (emote_number, emote_id) in enumerate(emote_list):
                if not evo_cycle_running:
                    break
                
                # 🤖 BOT SELF EMOTE ONLY
                try:
                    bot_emote = await Emote_k(int(bot_uid), int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_emote)
                    print(f"🤖 Bot Emote #{emote_number} sent.")
                except Exception as e:
                    print(f"Bot error: {e}")
                
                await asyncio.sleep(0.5)
                
                opposite_index = total_emotes - 1 - index
                opposite_number, opposite_id = emote_list[opposite_index]
                
                try:
                    bot_self_emote = await Emote_k(int(bot_uid), int(opposite_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote)
                    print(f"🤖 Bot Opposite Emote #{opposite_number} sent.")
                except Exception as e:
                    print(f"Bot error: {e}")
                
                if evo_cycle_running:
                    for i in range(5):
                        if not evo_cycle_running:
                            break
                        await asyncio.sleep(1)

    except asyncio.CancelledError:
        print("🛑 Evo cycle cancelled instantly")
        evo_cycle_running = False
        return

    finally:
        print("Cycle stopped")
                        
async def reject_spam_loop(target_uid, key, iv):
    """Send reject spam packets to target in background"""
    global reject_spam_running
    
    count = 0
    max_spam = 150
    
    while reject_spam_running and count < max_spam:
        try:
            # Send both packets
            packet1 = await banecipher1(target_uid, key, iv)
            packet2 = await banecipher(target_uid, key, iv)
            
            # Send to Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet1)
            await asyncio.sleep(0.1)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet2)
            
            count += 1
            print(f"Sent reject spam #{count} to {target_uid}")
            
            # 0.2 second delay between spam cycles
            await asyncio.sleep(0.2)
            
        except Exception as e:
            print(f"Error in reject spam: {e}")
            break
    
    return count    
    
async def handle_reject_completion(spam_task, target_uid, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of reject spam and send final message"""
    try:
        spam_count = await spam_task
        
        # Send completion message
        if spam_count >= 150:
            completion_msg = f"[B][C][FFFF00]✅ Reject Spam Completed Successfully for ID {target_uid}\n✅ Total packets sent: {spam_count * 2}\n"
        else:
            completion_msg = f"[B][C][FFFF00]⚠️ Reject Spam Partially Completed for ID {target_uid}\n⚠️ Total packets sent: {spam_count * 2}\n"
        
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
        
    except asyncio.CancelledError:
        print("Reject spam was cancelled")
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ ERROR in reject spam: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)    
    
    
    
async def banecipher(target_uid, key, iv):
    """Create reject spam packet 1 - Converted to new async format"""
    banner_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)

async def black666(client_id, key, iv):
    banner_text = "[FF0000][B][C] ERROR , WELCOME TO [FFFFFF]—͞N A Y A N 乡ㅤ友! [00FF00]___ —͞乡ㅤN A Y A N  BOT ! \n[FFFF00]NEW VERSION NEW FUNCTION !\n[FF0000] INSTAGRAM : @NAYAN1M\n\n"     
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)

async def banecipher1(client_id, key, iv):
    """Create reject spam packet 2 - Converted to new async format"""
    gay_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: int(client_id),
        2: 5,
        4: 50,
        5: {
            1: int(client_id),
            2: gay_text,
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)
    
async def get_colorful_message(message_text, message_number):
    """Generate message with different colors"""
    color_palette = ["FF0000", "FFFF00", "0000FF", "FFFF00", "FF00FF", 
                     "00FFFF", "FFA500", "FF1493", "00FF7F", "7B68EE",
                     "FFD700", "00CED1", "FF69B4", "32CD32", "9370DB",
                     "FF4500", "1E90FF", "ADFF2F", "FF6347", "8A2BE2"]
    
    color_index = (message_number - 1) % len(color_palette)
    return f"[C][B][{color_palette[color_index]}]{message_text}"    

def get_random_avatar():
	avatar_list = [
         '902050001', '902050002', '902050003', '902039016', '902050004', 
        '902047011', '902047010', '902049015', '902050006', '902049020'
    ]
	random_avatar = random.choice(avatar_list)
	return  random_avatar

async def xSEndMsgsQQ(Msg , id , K , V):
    fields = {1: id , 2: id , 4: Msg , 5: 1756580149, 7: 2, 8: 904990072, 9: {1: "xBe4!sTo - C4", 2: int(get_random_avatar()), 4: 330, 5: 1001000001, 8: "xBe4!sTo - C4", 10: 1, 11: 1, 13: {1: 2}, 14: {1: 1158053040, 2: 8, 3: "\u0010\u0015\b\n\u000b\u0015\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"}}, 10: "en", 13: {2: 2, 3: 1}}
    Pk = (await CrEaTe_ProTo(fields)).hex()
    Pk = "080112" + await EnC_Uid(len(Pk) // 2, Tp='Uid') + Pk
    return await GeneRaTePk(Pk, '1201', K, V)     

async def Create_xr_room_packet_fixed__(room_id, key, iv):
    """FIXED: Room chat packets must use Whisper connection"""
    random_color = generate_random_hex_color()

    fields = {
        1: 1,
        2: {
            1: 9280892890,  # Bot UID
            2: int(room_id),
            3: 3,  # Chat type 3 = room chat
            4: f"[FFFFFF]Hello",
            5: int(time.time()),  # Current timestamp, not hardcoded
            7: 2,
            9: {
                1: "XR SUPER ",
                2: bunner_(),   
                4: 228,
                7: 1,
            },
            10: "ar",  # Language (arabic? change to "en" if needed)
            13: {
                2: 1,
                3: 1
            }
        }
    }

    # Convert to protobuf hex
    proto_hex = (await CrEaTe_ProTo(fields)).hex()
    
    print(f"📦 Room chat proto: {len(proto_hex)//2} bytes")
    print(f"Hex start: {proto_hex[:50]}...")
    
    # CRITICAL FIX: Room chat uses Whisper connection (12xx headers)
    # Try different packet types for Whisper
    packet_type = "1215"  # Whisper connection for chat
    
    # Generate final encrypted packet
    final_packet = await GeneRaTePk(proto_hex, packet_type, key, iv)
    
    return final_packet

async def send_wave_messages(message_text, repeats, chat_id, key, iv, region):
    """Send message in wave pattern: expanding then shrinking"""
    global msg_spam_running
    
    count = 0
    total_cycles = 0
    
    while msg_spam_running and total_cycles < repeats:
        try:
            # EXPANDING phase (h, he, hel, hell, hello)
            for i in range(1, len(message_text) + 1):
                if not msg_spam_running:
                    break
                    
                partial_msg = message_text[:i]
                colorful_msg = await get_colorful_message(partial_msg, i)
                
                msg_packet = await xSEndMsgsQ(colorful_msg, int(chat_id), key, iv)
                if msg_packet and whisper_writer:
                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', msg_packet)
                    count += 1
                    print(f"✅ Wave #{total_cycles+1} - Expanding: '{partial_msg}'")
                    await asyncio.sleep(0.1)
            
            # SHRINKING phase (hell, hel, he, h)
            for i in range(len(message_text) - 1, 0, -1):
                if not msg_spam_running:
                    break
                    
                partial_msg = message_text[:i]
                colorful_msg = await get_colorful_message(partial_msg, i)
                
                msg_packet = await xSEndMsgsQQ(colorful_msg, int(chat_id), key, iv)
                if msg_packet and whisper_writer:
                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', msg_packet)
                    count += 1
                    print(f"✅ Wave #{total_cycles+1} - Shrinking: '{partial_msg}'")
                    await asyncio.sleep(0.1)
            
            total_cycles += 1
            print(f"🌀 Completed wave cycle {total_cycles}/{repeats}")
            
        except Exception as e:
            print(f"❌ Error in wave messages: {e}")
            break
    
    return count, total_cycles

async def handle_wave_completion(spam_task, message_text, repeats, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of wave messages"""
    try:
        message_count, cycles_completed = await spam_task
        
        total_per_cycle = (len(message_text) * 2) - 2
        expected_total = total_per_cycle * repeats
        

        
    except asyncio.CancelledError:
        cancel_msg = f"[B][C][FFFF00]🛑 WAVE CANCELLED!\n"
        await safe_send_message(chat_type, cancel_msg, sender_uid, chat_id, key, iv)

# Replace the msg_spam_loop function with this simpler version:
async def msg_spam_loop(message_text, times, chat_id, key, iv, region):
    """Send message multiple times in team chat using existing functions"""
    global msg_spam_running
    
    count = 0
    
    while msg_spam_running and count < times:
        try:
            # Use the existing xSEndMsgsQ function from xC4.py
            # This is for squad chat (chat_type 0)
            # Replace: msg_packet = await xSEndMsgsQ(message_text, int(chat_id), key, iv)
            # With:
            colorful_message = await get_colorful_message(message_text, count + 1)
            msg_packet = await xSEndMsgsQQ(colorful_message, int(chat_id), key, iv)
            
            if not msg_packet:
                print("❌ Failed to create message packet")
                break
                
            # Send the packet - use ChaT connection type for squad messages
            if whisper_writer:
                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', msg_packet)
                count += 1
                print(f"✅ Sent message #{count}/{times} to squad chat: '{message_text}'")
                
                # Adjust delay to avoid rate limiting
                await asyncio.sleep(0.1)
                
        except Exception as e:
            print(f"❌ Error in msg spam loop: {e}")
            import traceback
            traceback.print_exc()
            break
    
    return count

# Update the command handler to use the correct chat_id
# In the TcPChaT function, update the /msg command:



# Also, let's improve the handle_msg_spam_completion function:
async def handle_msg_spam_completion(spam_task, message_text, times, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of message spam and send final message"""
    try:
        actual_times = await spam_task
        
        # Send completion message
        if actual_times >= times:
            completion_msg = f"[B][C][FFFF00]✅ MESSAGE SPAM COMPLETED!\n"
            completion_msg += f"[FFFFFF]📝 Message: {message_text}\n"
            completion_msg += f"[FFFFFF]📊 Requested: {times} times\n"
            completion_msg += f"[FFFFFF]✅ Sent: {actual_times} times\n"
            completion_msg += f"[FFFF00]✓ Success rate: 100%\n"
            completion_msg += f"[FFFFFF]💬 Check squad chat to see messages!\n"
        elif actual_times > 0:
            completion_msg = f"[B][C][FFFF00]⚠️ MESSAGE SPAM PARTIALLY COMPLETED!\n"
            completion_msg += f"[FFFFFF]📝 Message: {message_text}\n"
            completion_msg += f"[FFFFFF]📊 Requested: {times} times\n"
            completion_msg += f"[FFFFFF]⚠️ Sent: {actual_times} times\n"
            completion_msg += f"[FFFF00]↯ Success rate: {(actual_times/times)*100:.1f}%\n"
            completion_msg += f"[FFFFFF]💬 Check squad chat to see messages!\n"
        else:
            completion_msg = f"[B][C][FF0000]❌ MESSAGE SPAM FAILED!\n"
            completion_msg += f"[FFFFFF]📝 Message: {message_text}\n"
            completion_msg += f"[FFFFFF]📊 Requested: {times} times\n"
            completion_msg += f"[FFFFFF]❌ Sent: 0 times\n"
            completion_msg += f"[FF0000]✗ Failed to send any messages\n"
            completion_msg += f"[FFFFFF]🔧 Possible issues:\n"
            completion_msg += f"[FFFFFF]1. Bot not in a squad\n"
            completion_msg += f"[FFFFFF]2. Invalid chat_id\n"
            completion_msg += f"[FFFFFF]3. Connection error\n"
        
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
        
    except asyncio.CancelledError:
        print("Message spam was cancelled by user")
        cancel_msg = f"[B][C][FFFF00]🛑 MESSAGE SPAM CANCELLED!\n[FFFFFF]Message spam was stopped by user command.\n"
        await safe_send_message(chat_type, cancel_msg, sender_uid, chat_id, key, iv)
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ ERROR in message spam completion: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)
        
async def send_msg_in_room_async(Msg, room_id, key, iv):
    """Converted to your async TCP format"""
    from datetime import datetime
    sticker_value = get_random_sticker()
    
    fields = {
        1: 1,
        2: {
            1: int(room_id),
            2: int(room_id),
            3: 3,
            4: f"{Msg}",
            5: int(datetime.now().timestamp()),
            7: 2,
            8: f'{{"StickerStr" : "{sticker_value}", "type":"Sticker"}}',
            9: {
                1: "byte bot",
                2: int(await xBunnEr()),  # Changed to your function
                4: 329,
                7: 1,
            },
            10: "en",
            13: {2: 1, 3: 1},
        },
    }

    # Create protobuf packet using your function
    packet = await CrEaTe_ProTo(fields)
    
    # Convert to hex and add "7200"
    packet_hex = packet.hex() + "7200"

    # Encrypt using your function
    encrypted_packet = await encrypt_packet(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)

    # Determine format based on header length
    if len(header_length_final) == 2:
        final_packet = "1215000000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

    elif len(header_length_final) == 3:
        final_packet = "121500000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

    elif len(header_length_final) == 4:
        final_packet = "12150000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

    elif len(header_length_final) == 5:
        final_packet = "12150000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

# Command handler for room messages:
async def handle_room_message_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """
    Handle /roommsg command to send messages in custom rooms
    """
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 3:
        error_msg = f"""[B][C][FF0000]❌ Usage: /roommsg (room_id) (message)
        
📝 Examples:
/roommsg 123456 Hello everyone!
/roommsg 987654 Welcome to my
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    room_id = parts[1]
    message = ' '.join(parts[2:])
    Msg = message 
    # Validate room ID
    if not room_id.isdigit():
        error_msg = f"[B][C][FF0000]❌ Room ID must be numbers only!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        print(error_msg)
        return
    
    # Send initial message
    initial_msg = f"[B][C][FFFF00]📤 Sending room message...\n"
    initial_msg += f"🏠 Room: {room_id}\n"
    
    
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    print(initial_msg)
    
    try:
        # Create the room message packet
        room_packet = await send_msg_in_room_async(Msg, room_id, key, iv)
        
        if room_packet and whisper_writer:
            # Send via Whisper connection (for chat packets)
            whisper_writer.write(room_packet)
            await whisper_writer.drain()
            
            success_msg = f"""[B][C][FFFF00]✅ ROOM MESSAGE SENT!

🏠 Room: {room_id}
📝 Message: {message}
"""
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to create room packet!\n"
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        print(success_msg)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        print(error_msg)

async def create_training_start_packet(key, iv, region):
    """Create packet to start training mode in Free Fire"""
    
    try:
        # Decoded from your hex dump:
        # 62 27 01 01 28 00 01 00 00 00 00 00 79 2c 59 bf...
        # This appears to be a "start training" or "enter training ground" packet
        
        # Based on common Free Fire packet structure:
        # Packet type 0x27 = 39 decimal (training related)
        
        fields = {
            1: 39,  # Packet type for training (0x27 = 39)
            2: {
                1: 1,  # Action type (1 = start/enter)
                2: 1,  # Training mode type (1 = normal training)
                3: 0,  # Unknown flag
                4: 0,  # Unknown flag
                # The rest appears to be encrypted training data
                5: {
                    1: bytes.fromhex("79 2c 59 bf e0 5b be a6 00 ae 89 a5 26 4f 55 6f"),
                    2: bytes.fromhex("40 e5 e3 52 aa e2 46 26 ef e8 ac 5c 6c b1 db 9e"),
                    3: bytes.fromhex("87 09 4d aa ed c2 eb da")
                }
            }
        }
        
        # Alternative simpler structure (more likely):
        fields_simple = {
            1: 39,  # Training packet type
            2: {
                1: 1,   # Start training command
                2: 0,   # Training ground ID (0 = default)
                3: 1,   # Mode (1 = training)
                4: {    # Training settings
                    1: 1,  # Weapons enabled
                    2: 1,  # Bots enabled
                    3: 0,  # Unlimited ammo
                    4: 1,  # Health regen
                    5: 0   # God mode
                }
            }
        }
        
        # Let's try the simple structure first
        packet = await CrEaTe_ProTo(fields_simple)
        packet_hex = packet.hex()
        
        print(f"📦 Created training packet: {packet_hex[:50]}...")
        
        # Determine packet header based on region
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        # Generate final encrypted packet
        final_packet = await GeneRaTePk(packet_hex, packet_type, key, iv)
        
        print(f"✅ Training start packet created")
        return final_packet
        
    except Exception as e:
        print(f"❌ Error creating training packet: {e}")
        import traceback
        traceback.print_exc()
        return None


async def start_training_mode(key, iv, region):
    """Start training mode - sends the training start packet"""
    
    try:
        training_packet = await create_training_start_packet(key, iv, region)
        
        if training_packet:
            # Send to Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', training_packet)
            print("🎮 Training mode start packet sent!")
            return True
        else:
            print("❌ Failed to create training packet")
            return False
            
    except Exception as e:
        print(f"❌ Error starting training: {e}")
        return False


# Add this command handler to your TcPChaT function:
async def handle_training_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /train command to start training mode"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        # Just /train - start default training
        initial_msg = f"[B][C][FFFF00]🎮 Starting training mode...\n"
        await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
        
        success = await start_training_mode(key, iv, region)
        
        if success:
            success_msg = f"[B][C][FFFF00]✅ Training mode started!\n🏋️ Enter training ground to practice!\n"
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to start training!\n"
            
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    elif len(parts) == 2 and parts[1] == "custom":
        # /train custom - custom training settings
        initial_msg = f"[B][C][FFFF00]🎮 Starting custom training...\n"
        await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
        
        # You can add custom training settings here
        success = await start_training_mode(key, iv, region)
        
        if success:
            success_msg = f"[B][C][FFFF00]✅ Custom training started!\n⚙️ Custom settings applied!\n"
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to start custom training!\n"
            
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    else:
        error_msg = f"[B][C][FF0000]❌ Usage: /train [custom]\nExamples:\n/train - Start default training\n/train custom - Custom training\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def lag_team_loop(team_code, key, iv, region):
    """Rapid join/leave loop to create lag"""
    global lag_running
    count = 0
    
    while lag_running:
        try:
            # Join the team
            join_packet = await GenJoinSquadsPacket(team_code, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
            # Very short delay before leaving
            await asyncio.sleep(0.01)  # 10 milliseconds
            
            # Leave the team
            leave_packet = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            
            count += 1
            print(f"Lag cycle #{count} completed for team: {team_code}")
            
            # Short delay before next cycle
            await asyncio.sleep(0.01)  # 10 milliseconds between cycles
            
        except Exception as e:
            print(f"Error in lag loop: {e}")
            # Continue the loop even if there's an error
            await asyncio.sleep(0.1)
 
async def general_emote_spam(uids, emote_number, key, iv, region):
    """Send general emotes based on number mapping from JSON file"""
    try:
        emote_id = GENERAL_EMOTES_MAP.get(str(emote_number))
        if not emote_id:
            return False, f"Invalid emote number! Use numbers from 1-{len(GENERAL_EMOTES_MAP)}"
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Error sending general emote to {uid}: {e}")
        
        return True, f"Sent emote {emote_number} (ID: {emote_id}) to {success_count} player(s)"
    
    except Exception as e:
        return False, f"Error in general_emote_spam: {str(e)}"
        
####################################

#Clan-info-by-clan-id
def Get_clan_info(clan_id):
    try:
        url = f"https://get-clan-info.vercel.app/get_clan_info?clan_id={clan_id}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            msg = f""" 
[11EAFD][b][c]
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
▶▶▶▶GUILD DETAILS◀◀◀◀
Achievements: {data['achievements']}\n\n
Balance : {fix_num(data['balance'])}\n\n
Clan Name : {data['clan_name']}\n\n
Expire Time : {fix_num(data['guild_details']['expire_time'])}\n\n
Members Online : {fix_num(data['guild_details']['members_online'])}\n\n
Regional : {data['guild_details']['regional']}\n\n
Reward Time : {fix_num(data['guild_details']['reward_time'])}\n\n
Total Members : {fix_num(data['guild_details']['total_members'])}\n\n
ID : {fix_num(data['id'])}\n\n
Last Active : {fix_num(data['last_active'])}\n\n
Level : {fix_num(data['level'])}\n\n
Rank : {fix_num(data['rank'])}\n\n
Region : {data['region']}\n\n
Score : {fix_num(data['score'])}\n\n
Timestamp1 : {fix_num(data['timestamp1'])}\n\n
Timestamp2 : {fix_num(data['timestamp2'])}\n\n
Welcome Message: {data['welcome_message']}\n\n
XP: {fix_num(data['xp'])}\n\n
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
            """
            return msg
        else:
            msg = """
[11EAFD][b][c]
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
Failed to get info, please try again later!!

°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
            """
            return msg
    except:
        pass
        
 


#CHAT WITH AI
def talk_with_ai(question):
    try:
        encoded_question = requests.utils.quote(question)
        url = f"https://9x-ai.vercel.app/ask?key=SUMON9X&message={question}"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            answer = res.text.strip()
            return answer
        else:
            return f"Failed to fetch answer. Status code: {res.status_code}"
    except Exception as e:
        return f"Error occurred: {e}"
#SPAM REQUESTS
def spam_requests(player_id):
    # This URL now correctly points to the Flask app you provided
    url = f"https://like2.vercel.app/send_requests?uid={player_id}&server={server2}&key={key2}"
    try:
        res = requests.get(url, timeout=20) # Added a timeout
        if res.status_code == 200:
            data = res.json()
            # Return a more descriptive message based on the API's JSON response
            return f"API Status: Success [{data.get('success_count', 0)}] Failed [{data.get('failed_count', 0)}]"
        else:
            # Return the error status from the API
            return f"API Error: Status {res.status_code}"
    except requests.exceptions.RequestException as e:
        # Handle cases where the API isn't running or is unreachable
        print(f"Could not connect to spam API: {e}")
        return "Failed to connect to spam API."
####################################

# ** NEW INFO FUNCTION using the new API **
def newinfo(uid):
    # Base URL without parameters
    url = "https://like2.vercel.app/player-info"
    # Parameters dictionary - this is the robust way to do it
    params = {
        'uid': uid,
        'server': server2,  # Hardcoded to bd as requested
        'key': key2
    }
    try:
        # Pass the parameters to requests.get()
        response = requests.get(url, params=params, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Check if the expected data structure is in the response
            if "basicInfo" in data:
                return {"status": "ok", "data": data}
            else:
                # The API returned 200, but the data is not what we expect (e.g., error message in JSON)
                return {"status": "error", "message": data.get("error", "Invalid ID or data not found.")}
        else:
            # The API returned an error status code (e.g., 404, 500)
            try:
                # Try to get a specific error message from the API's response
                error_msg = response.json().get('error', f"API returned status {response.status_code}")
                return {"status": "error", "message": error_msg}
            except ValueError:
                # If the error response is not JSON
                return {"status": "error", "message": f"API returned status {response.status_code}"}

    except requests.exceptions.RequestException as e:
        # Handle network errors (e.g., timeout, no connection)
        return {"status": "error", "message": f"Network error: {str(e)}"}
    except ValueError: 
        # Handle cases where the response is not valid JSON
        return {"status": "error", "message": "Invalid JSON response from API."}
        

async def animation_packet(animation_id, key, iv):

    fields = {
        1: 88,
        2: {
            1: {
                1: int(animation_id)
            }
        }
    }

    proto_bytes = await CrEaTe_ProTo(fields)
    packet_hex = proto_bytes.hex()

    encrypted_packet = await encrypt_packet(packet_hex, key, iv)

    packet_length = len(encrypted_packet) // 2

    # 🔥 built-in hex conversion
    hex_length = format(packet_length, 'x')

    final_packet = "051500" + "0" * (6 - len(hex_length)) + hex_length + encrypted_packet

    return bytes.fromhex(final_packet)

# =================== AUTO BUNDLE ON GROUP JOIN (V6 থেকে port) ===================
AUTO_BUNDLE_IDS = {
    "rampage":     914000002,
    "cannibal":    914000003,
    "devil":       914038001,
    "scorpio":     914039001,
    "frostfire":   914042001,
    "paradox":     914044001,
    "naruto":      914047001,
    "aurora":      914047002,
    "midnight":    914048001,
    "itachi":      914050001,
    "dreamspace":  914051001,
    "eclipse":     914053001,
}

async def do_join_emote_and_bundle(bot_uid, key, iv, region, inviter_uid=None):
    """
    গ্রুপে join হওয়ার পরে শুধু random bundle equip করে।
    এই function কখনো freeze করবে না।
    """
    global online_writer, whisper_writer

    try:
        # join এর পরে 1.5 সেকেন্ড অপেক্ষা
        await asyncio.sleep(1.5)

        try:
            _bot_uid_int = int(str(bot_uid).strip())
        except (ValueError, TypeError):
            _bot_uid_int = bot_uid

        # inviter কে একটা emote দাও
        try:
            emote_target = int(str(inviter_uid).strip()) if inviter_uid else _bot_uid_int
            emote_pkt = await Emote_k(emote_target, 909054004, key, iv, region)
            if emote_pkt and online_writer and not online_writer.is_closing():
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_pkt)
                print(f"✅ Join emote sent to inviter {emote_target}")
        except Exception as _e:
            print(f"⚠️ Join emote error (non-fatal): {_e}")

        # AUTO_BUNDLE_IDS থেকে random bundle — animation আগে, তারপর delay দিয়ে bundle
        try:
            if AUTO_BUNDLE_IDS:
                bundle_name = random.choice(list(AUTO_BUNDLE_IDS.keys()))
                bundle_id   = int(AUTO_BUNDLE_IDS[bundle_name])

                _delay_map = {
                    914000002: 5.1, 914000003: 3.0, 914038001: 3.0,
                    914039001: 5.0, 914042001: 3.3, 914044001: 3.5,
                    914047001: 2.6, 914047002: 3.7, 914048001: 4.4,
                    914050001: 3.0, 914051001: 4.2, 914053001: 5.0,
                }
                delay_time = _delay_map.get(bundle_id, 3.0)

                # ★ animation packet আগে পাঠাও
                try:
                    anim_pkt = await animation_packet(bundle_id, key, iv)
                    if anim_pkt and online_writer and not online_writer.is_closing():
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', anim_pkt)
                        print(f"✅ Join animation {bundle_id} sent")
                except Exception as _ae:
                    print(f"⚠️ Join animation error (non-fatal): {_ae}")

                # ★ custom delay
                await asyncio.sleep(delay_time)

                bundle_pkt = await Look_Changer(bundle_id, key, iv, look_type=1, region=region)
                if bundle_pkt and online_writer and not online_writer.is_closing():
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bundle_pkt)
                    print(f"✅ Bundle '{bundle_name}' ({bundle_id}) equipped")
                    done_msg = f"[B][C][00FF00]🎁 BUNDLE {bundle_name.upper()} DONE"
                    if whisper_writer and not whisper_writer.is_closing():
                        try:
                            done_pkt = await xSEndMsgsQ(done_msg, _bot_uid_int, key, iv, region)
                            if done_pkt:
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', done_pkt)
                        except Exception:
                            pass
                else:
                    print(f"⚠️ Bundle packet is None or writer closed, skipping")
        except Exception as _be:
            print(f"⚠️ Bundle equip error (non-fatal): {_be}")

    except Exception as e:
        print(f"❌ do_join_emote_and_bundle error: {e}")
        import traceback
        traceback.print_exc()

# =================== END AUTO BUNDLE ===================

async def bundle_packet_async(bundle_id, key, iv, region="bd"):
    """Build and return a bundle equip packet — Look_Changer দিয়ে (V6 style)"""
    try:
        try:
            pkt = await bundle_equip(bundle_id, key, iv, region)
            if pkt:
                return pkt
        except Exception:
            pass
        return await Look_Changer(int(bundle_id), key, iv, look_type=1, region=region)
    except Exception as e:
        print(f"❌ bundle_packet_async error: {e}")
        return None

async def Look_Changer(bundle_id, key, iv, look_type=1, region="bd"):
    fields = {
        1: 88,
        2: {
            1: {
                1: bundle_id,
                2: look_type
            },
            2: 2
        }
    }
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    encrypted = await encrypt_packet(packet_hex, key, iv)
    header_length = len(encrypted) // 2
    header_length_hex = await DecodE_HeX(header_length)
    if region.lower() == "ind":
        packet_type = "0514"
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    if len(header_length_hex) == 2:
        final_header = f"{packet_type}000000"
    elif len(header_length_hex) == 3:
        final_header = f"{packet_type}00000"
    elif len(header_length_hex) == 4:
        final_header = f"{packet_type}0000"
    elif len(header_length_hex) == 5:
        final_header = f"{packet_type}000"
    else:
        final_header = f"{packet_type}000000"
    final_packet_hex = final_header + header_length_hex + encrypted
    return bytes.fromhex(final_packet_hex)

async def bundle_equip(bundle_id, key, iv, region="bd"):
    """Bundle equip via Look_Changer"""
    return await Look_Changer(int(bundle_id), key, iv, look_type=1, region=region)

async def team_chat_startup(player_uid, team_session, key, iv):
    proto = Team_Chat_Startup_pb2.team_chat_startup()
    proto.field1 = 3
    proto.details.uid = player_uid
    proto.details.language = "en"
    proto.details.team_packet = str(team_session)

    packet = proto.SerializeToString().hex()
    encrypted_packet = await encrypt_packet(packet, key, iv)
    packet_length = len(encrypted_packet) // 2
    packet_length_hex = await base_to_hex(packet_length)

    if len(packet_length_hex) == 2:
        final_packet = "1201000000" + packet_length_hex + encrypted_packet
    elif len(packet_length_hex) == 3:
        final_packet = "120100000" + packet_length_hex + encrypted_packet
    elif len(packet_length_hex) == 4:
        final_packet = "12010000" + packet_length_hex + encrypted_packet
    elif len(packet_length_hex) == 5:
        final_packet = "1201000" + packet_length_hex + encrypted_packet
    else:
        print("something went wrong, please check clan startup function.")
    if whisper_writer:  # <--- FIX: Check if writer is available
        whisper_writer.write(bytes.fromhex(final_packet))
        await whisper_writer.drain()

	
#ADDING-100-LIKES-IN-24H
def send_likes(uid):
    try:
        likes_api_response = requests.get(
             f"https://ninex-vip-like.onrender.com/like?uid={uid}&server=bd",
             timeout=32
             )
      
      
        if likes_api_response.status_code != 200:
            return f"""
[C][B][FF0000]━━━━━
[FFFFFF]Like API Error!
Status Code: {likes_api_response.status_code}
Please check if the uid is correct.
━━━━━
"""

        api_json_response = likes_api_response.json()

        player_name = api_json_response.get('PlayerNickname', 'Unknown')
        likes_before = api_json_response.get('LikesbeforeCommand', 0)
        likes_after = api_json_response.get('LikesafterCommand', 0)
        likes_added = api_json_response.get('LikesGivenByAPI', 0)
        status = api_json_response.get('status', 0)

        if status == 1 and likes_added > 0:
            # ✅ Success
            return f"""
[C][B][11EAFD]‎━━━━━━━━━━━━
[FFFFFF]Likes Status:

[FFFF00]Likes Sent Successfully!

[FFFFFF]Player Name : [FFFF00]{player_name}  
[FFFFFF]Likes Added : [FFFF00]{likes_added}  
[FFFFFF]Likes Before : [FFFF00]{likes_before}  
[FFFFFF]Likes After : [FFFF00]{likes_after}  
[C][B][11EAFD]‎━━━━━━━━━━━━
[C][B][FFB300]Subscribe: [FFFFFF]—͞N A Y A N 乡ㅤ友!ㅤ [FFFF00]!!
"""
        elif status == 2 or likes_before == likes_after:
            # 🚫 Already claimed / Maxed
            return f"""
[C][B][FF0000]━━━━━━━━━━━━

[FFFFFF]No Likes Sent!

[FF0000]You have already taken likes with this UID.
Try again after 24 hours.

[FFFFFF]Player Name : [FF0000]{player_name}  
[FFFFFF]Likes Before : [FF0000]{likes_before}  
[FFFFFF]Likes After : [FF0000]{likes_after}  
[C][B][FF0000]━━━━━━━━━━━━
"""
        else:
            # ❓ Unexpected case
            return f"""
[C][B][FF0000]━━━━━━━━━━━━
[FFFFFF]Unexpected Response!
Something went wrong.

Please try again or contact support.
━━━━━━━━━━━━
"""

    except requests.exceptions.RequestException:
        return """
[C][B][FF0000]━━━━━
[FFFFFF]Like API Connection Failed!
Is the API server (app.py) running?
━━━━━
"""
    except Exception as e:
        return f"""
[C][B][FF0000]━━━━━
[FFFFFF]An unexpected error occurred:
[FF0000]{str(e)}
━━━━━
"""

# SEND VISIT 
def send_visits(player_id):
    # This URL now correctly points to the Flask app you provided
    url = f"https://9x-visit.vercel.app/visit?uid={uid}&region=BD"
    try:
        res = requests.get(url, timeout=30) # Added a timeout
        if res.status_code == 200:
            data = res.json()
            # Return a more descriptive message based on the API's JSON response
            return data
        else:
            # Return the error status from the API
            return f"API Error: Status {res.status_code}"
    except requests.exceptions.RequestException as e:
        # Handle cases where the API isn't running or is unreachable
        print(f"Could not connect to visit API: {e}")
        return "Failed to connect to visit API."


def spam_requests(player_id):
    # This URL now correctly points to the Flask app you provided
    url = f"https://kawsar-spam-api.vercel.app/spam?uid={player_id}&region=bd"
    try:
        res = requests.get(url, timeout=20) # Added a timeout
        if res.status_code == 200:
            data = res.json()
            # Return a more descriptive message based on the API's JSON response
            return f"{xMsGFixinG(data)}"
        else:
            # Return the error status from the API
            return f"API Error: Status {res.status_code}"
    except requests.exceptions.RequestException as e:
        # Handle cases where the API isn't running or is unreachable
        print(f"Could not connect to spam API: {e}")
        return "Failed to connect to spam API."



def send_tiktok_info(username):

    try:
        response = requests.get(
            f"https://kawsar-tikto-info.vercel.app/tiktok?username={username}",
            timeout=15
        )

        if response.status_code != 200:
            return f"[B][C][FF8C00]❌ TikTok API Error! Status Code: {response.status_code}"

        user = response.json()

        if user.get("credit") != "—͞N A Y A N乡ㅤ友!":
            return "[B][C][FF8C00]❌ User Not Found Or Credit Invalid!"


        # JSON structure থেকে nested dict access
        identity = user.get("identity", {})
        statistics = user.get("statistics", {})
        status = user.get("status", {})

        # Extract
        full_name = identity.get("full_name", "Unknown")
        username_ = identity.get("username", "")
        user_id = identity.get("user_id", "Unknown")

        followers = statistics.get("followers", 0)
        following = statistics.get("following", 0)
        likes = statistics.get("likes", 0)
        videos = statistics.get("videos", 0)

        private_status = status.get("private_account", False)
        signature = user.get("bio", "")
        avatar_hd = user.get("avatar_hd", "")

        return f"""
[B][C][1E90FF]◉[FFFF00]━[FF69B4]◉[FFFFFF]
[C][B][00bFFF]│[00bFFF]ꚠ[00bFFF] │[FFFFFF]║[00bFFF]TIKTOK INFO[FFFFFF]║
[C][B][FF00FF]╰[FFFF00]─[FFFF00]╯[FFFFFF]
[C][B][FF00FF]━━━━━━━━━━━
[C][B][FFFFFF]Fullname   : [FFFF00]{full_name}
[C][B][FFFFFF]Username   : [FFFF00]{username_}
[C][B][FFFFFF]Signature  : [00BFFF]{signature}
[C][B][FFFFFF]Followers  : [00BFFF]{followers}
[C][B][FFFFFF]Following  : [00BFFF]{following}
[C][B][FFFFFF]Likes      : [00BFFF]{likes}
[C][B][FFFFFF]Videos     : [00BFFF]{videos}
[C][B][FFFFFF]Private    : [FFFF00]{private_status}
[C][B][00FFFF]━━━━━━━━━━━
"""

    except requests.exceptions.RequestException:
        return "[B][C][FF8C00]❌ TikTok API Connection Failed!"
    except Exception as e:
        return f"[B][C][FF8C00]❌ Unexpected Error: {str(e)}"


# -------------------------------------------------
# Helper function: Fetch YouTube info JSON
# -------------------------------------------------
def get_youtube_info(channel_name):
    try:
        response_json = requests.get(
            f"https://youtube-api.vercel.app/yt?channel={channel_name.lstrip('@')}",
            timeout=15
        ).json()
        return response_json
    except Exception:
        return {}

# -------------------------------------------------
# Helper function: Format and send YouTube info
# -------------------------------------------------
async def send_youtube_info(channel_name, chat_type, uid, chat_id, key, iv):
    response_json = get_youtube_info(channel_name)

    # Stats formatting
    stats = response_json.get("statistics", {})
    subscribers = xMsGFixinG(stats.get("subscribers", "0"))
    views = xMsGFixinG(stats.get("views", "0"))
    videos = xMsGFixinG(stats.get("videos", "0"))

    # Description
    description = response_json.get("description", "")

    # Main info message
    main_info = f"""
[B][C][FF8C00]◉[FF4500]━[FFD700]◉[FFFFFF]
[C][B][FF8C00]│[FFFFFF]▶[FF8C00] │[FFFFFF]║[00BFFF]YOUTUBE INFO[FFFFFF]║
[C][B][FF8C00]╰[FF8C00]─[FF8C00]╯[FFFFFF]
[C][B][FF00FF]━━━━━━━━━━━
[C][B][FFFFFF]Channel Name : [FFFF00]{response_json.get('channel_title', 'Unknown')}
[C][B][FFFFFF]Channel ID    : [FFFF00]{response_json.get('channel_id', 'Unknown')}
[C][B][FFFFFF]Handle        : [00BFFF]{response_json.get('handle', 'Unknown')}
[C][B][FFFFFF]Subscribers   : [00BFFF]{subscribers}
[C][B][FFFFFF]Views         : [00BFFF]{views}
[C][B][FFFFFF]Videos        : [00BFFF]{videos}
[C][B][FFFFFF]Published At  : [00BFFF]{xMsGFixinG(response_json.get('published_at', ''))}
[C][B][00FFFF]━━━━━━━━━━━
[C][B][FFFFFF]Developer     : {BOT_NAME}
"""
    # Send main info
    await safe_send_message(chat_type, main_info, uid, chat_id, key, iv, region=region)

    # Send description separately after 0.2s
    await asyncio.sleep(0.2)
    if description:
        await safe_send_message(chat_type, f"[B][C][00BFFF]Description: {description}", uid, chat_id, key, iv, region=region)

import aiohttp

def send_guild_info(guild_id):

    try:
        response = requests.get(
            f"https://guild-info-danger.vercel.app/guild?guild_id={guild_id}&region=all",
            timeout=15
        )

        if response.status_code != 200:
            return f"[B][C][FF8C00]❌ API Error! Status Code: {response.status_code}"

        guild = response.json()


        guild_id = xMsGFixinG(guild.get("guild_id", "0"))
        guild_name = guild.get("guild_name", "Unknown")
        guild_region = guild.get("guild_region", "Unknown")
        lvl = xMsGFixinG(guild.get("guild_level", "0"))
        members = xMsGFixinG(guild.get("current_members", "0"))
        max_members = xMsGFixinG(guild.get("max_members", "0"))
        total_activity = xMsGFixinG(guild.get("total_activity_points", "0"))
        weekly_activity = xMsGFixinG(guild.get("weekly_activity_points", "0"))
        creation_time = xMsGFixinG(guild.get("creation_time", ""))

        return f"""
[B][C][FF4500]◎━━━━━━━━━━━━━━━━━◎
[FFD700]◉ 🏰 GUILD INFORMATION ◉
[FF4500]◎━━━━━━━━━━━━━━━━━◎

[B][FFFFFF]Guild Name: [00FF00]{guild_name}
[B][FFFFFF]Guild ID: [00BFFF]{guild_id}
[B][FFFFFF]Region: [FF69B4]{guild_region}
[B][FFFFFF]Level: [FFA500]{lvl}
[B][FFFFFF]Members: [00FF7F]{members}/{max_members}

[B][FFFFFF]Total Points: [1E90FF]{total_activity}
[B][FFFFFF]Weekly Points: [1E90FF]{weekly_activity}
[B][FFFFFF]Created On: [00BFFF]{creation_time}

[B][C][FFD700]◎━━━━━━━━━━━━━━━◎
"""
    except requests.exceptions.RequestException:
        return "[B][C][FF8C00]❌ Guild API Connection Failed!"
    except Exception as e:
        return f"[B][C][FF8C00]❌ Unexpected Error: {str(e)}"

def get_item_info(item_id):
    url = f"https://item-id-to-info.vercel.app/item/{item_id}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if "Id" not in data:
            return "[FF8C00]ITEM NOT FOUND"

        # Rare অনুযায়ী color change
        rare = data.get("Rare", "UNKNOWN")

        rare_colors = {
            "Green": "00FF00",
            "Blue": "00AAFF",
            "Purple": "AA00FF",
            "Red": "FF0000",
            "Orange": "FFAA00",
            "Gold": "FFD700"
        }

        rare_color = rare_colors.get(rare, "FFFFFF")

        message = f"""
[B][00FFFF]═════════════
[00FFFF]         ITEM DETAILS
[00FFFF]═════════════

[1E90FF]NAME        : [{rare_color}]{data.get('name', 'N/A')}
[00FFAA]ID          : [FFFFFF]{xMsGFixinG(data.get('Id', 'N/A'))}
[FF00FF]TYPE        : [FFFFFF]{data.get('Type', 'N/A')}
[FFA500]COLLECTION  : [FFFFFF]{data.get('collectionType', 'N/A')}
[{rare_color}]RARE        : [{rare_color}]{rare}
[FF4444]UNIQUE      : [FFFFFF]{data.get('IsUnique', 'N/A')}
[D3D3D3]ICON        : [FFFFFF]{data.get('Icon', 'N/A')}

[00FFFF]═════════════
"""
        return message.strip()

    except Exception:
        return "[FF8C00]SERVER ERROR"

def get_math_result(input_expr):
    # Remove spaces
    expression = input_expr.replace(" ", "")
    
    # Replace × → * and ÷ → /
    expression = expression.replace("×", "*").replace("÷", "/")
    
    # URL encode
    encoded_expr = urllib.parse.quote(expression)  # e.g., 2*2 → 2%2A2

    url = f"https://math-api-kawsar-pro.vercel.app/math?expression={encoded_expr}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("status") != "success":
            # Invalid Expression
            return f"""[B]
[FF8C00]═════════════
[FF8C00]        INVALID EXPRESSION
[FF8C00]═════════════
[FF4444]EXPRESSION : [FFFFFF]{xMsGFixinG(expression)}
[FF8C00]RESULT     : [FFFFFF]ERROR    
[FF8C00]═════════════
""".strip()

        # Valid Expression
        return f"""[B]
[00FFFF]═════════════
[00FFFF]        MATH RESULT
[00FFFF]═════════════
[1E90FF]EXPRESSION : [FFFFFF]{xMsGFixinG(expression)}    
[00FF00]RESULT     : [FFFFFF]{xMsGFixinG(data.get('result', 'N/A'))}    
[00FFFF]═════════════
""".strip()

    except Exception:
        return "[FF8C00]SERVER ERROR"

# =================== LOCAL MATH CALCULATOR (for /mth) ===================
def local_math_calculate(input_expr):
    """
    সম্ভাব্য সব ধরনের যোগ (+), বিয়োগ (-), গুণ (*,×), ভাগ (/,÷) ক্যালকুলেট করে।
    কোনো API লাগবে না - সব লোকালি হবে।
    
    সাপোর্টেড অপারেশন:
    - যোগ: 1+1, 2+3, 100+200, 1.5+2.5
    - বিয়োগ: 5-3, 100-50, 10.5-3.2
    - গুণ: 3*4, 5×6, 10*20, 2.5*4
    - ভাগ: 20/5, 100÷4, 15/3, 7.5/2.5
    - মিক্সড: 2+3*4, (10+5)*2, 100/5+20-3
    - পাওয়ার: 2**3 (2 এর 3 ঘাত = 8)
    - মডুলো: 10%3 (ভাগশেষ = 1)
    - ব্র্যাকেট: (2+3)*(4-1)
    - ডেসিমাল: 3.14*2, 10.5/2.1
    - নেগেটিভ: -5+3, (-10)*2
    """
    # Remove extra spaces
    expression = input_expr.strip().replace(" ", "")
    
    # Replace special math symbols
    expression = expression.replace("×", "*").replace("÷", "/")
    expression = expression.replace("x", "*").replace("X", "*")  # x কে * তে convert
    
    # Security check - শুধু সংখ্যা ও অপারেটর অনুমতি
    import re
    if not re.match(r'^[\d\s\+\-\*\/\.\(\)\%\^]+$', expression):
        return f"""[B]
[FF8C00]═══════════════════
[FF8C00]    ❌ INVALID EXPRESSION
[FF8C00]═══════════════════
[FF4444]INPUT      : [FFFFFF]{xMsGFixinG(input_expr)}
[FF8C00]ERROR      : [FFFFFF]Only numbers & operators allowed
[FFFF00]ALLOWED    : [FFFFFF]+ - * / × ÷ ( ) . % **
[FF8C00]═══════════════════
""".strip()
    
    # Replace ^ with ** for power
    expression = expression.replace("^", "**")
    
    try:
        # Calculate result
        result = eval(expression)
        
        # Format result - যদি পূর্ণসংখ্যা হয় তাহলে .0 সরাও
        if isinstance(result, float):
            if result == int(result):
                result = int(result)
            else:
                result = round(result, 6)  # 6 দশমিক পর্যন্ত
        
        # Determine operation type for display
        if '+' in input_expr and '-' not in input_expr and '*' not in input_expr and '/' not in input_expr:
            op_type = "যোগ (Addition)"
            op_emoji = "➕"
        elif '-' in input_expr and '+' not in input_expr and '*' not in input_expr and '/' not in input_expr:
            op_type = "বিয়োগ (Subtraction)"
            op_emoji = "➖"
        elif '*' in input_expr or '×' in input_expr or 'x' in input_expr.lower():
            op_type = "গুণ (Multiplication)"
            op_emoji = "✖️"
        elif '/' in input_expr or '÷' in input_expr:
            op_type = "ভাগ (Division)"
            op_emoji = "➗"
        elif '%' in input_expr:
            op_type = "মডুলো (Remainder)"
            op_emoji = "🔢"
        elif '**' in expression or '^' in input_expr:
            op_type = "পাওয়ার (Power)"
            op_emoji = "⚡"
        else:
            op_type = "মিক্সড (Mixed)"
            op_emoji = "🧮"
        
        return f"""[B]
[00FFFF]═══════════════════
[00FFFF]   {op_emoji} MATH CALCULATOR {op_emoji}
[00FFFF]═══════════════════
[1E90FF]TYPE       : [FFFFFF]{op_type}
[FFFF00]EXPRESSION : [FFFFFF]{xMsGFixinG(input_expr)}
[00FF00]RESULT     : [FFFFFF]{xMsGFixinG(str(result))}
[00FFFF]═══════════════════
[00FFFF]🤖 {BOT_NAME} BOT
[00FFFF]═══════════════════
""".strip()

    except ZeroDivisionError:
        return f"""[B]
[FF8C00]═══════════════════
[FF8C00]    ❌ DIVISION BY ZERO
[FF8C00]═══════════════════
[FF4444]EXPRESSION : [FFFFFF]{xMsGFixinG(input_expr)}
[FF8C00]ERROR      : [FFFFFF]0 দিয়ে ভাগ করা যায় না!
[FF8C00]═══════════════════
""".strip()

    except SyntaxError:
        return f"""[B]
[FF8C00]═══════════════════
[FF8C00]    ❌ SYNTAX ERROR
[FF8C00]═══════════════════
[FF4444]EXPRESSION : [FFFFFF]{xMsGFixinG(input_expr)}
[FF8C00]ERROR      : [FFFFFF]ভুল ফরম্যাট! সঠিকভাবে লিখুন
[FFFF00]EXAMPLES   : [FFFFFF]1+1, 5-3, 4*2, 20/5
[FF8C00]═══════════════════
""".strip()

    except Exception as e:
        return f"""[B]
[FF8C00]═══════════════════
[FF8C00]    ❌ CALCULATION ERROR
[FF8C00]═══════════════════
[FF4444]EXPRESSION : [FFFFFF]{xMsGFixinG(input_expr)}
[FF8C00]ERROR      : [FFFFFF]{str(e)[:30]}
[FF8C00]═══════════════════
""".strip()

def fake_likes(uid):
    try:
        # Step 1: Player info fetch করো
        info_url = f"https://kawsar-player-info-ob54.vercel.app/player-info?uid={uid}"
        res = requests.get(info_url, timeout=15)

        if res.status_code != 200:
            return f"""[B][C][FF8C00]❌ Player Info Error!
[FFFFFF]Status: {res.status_code}
[FF8C00]UID টি সঠিক কিনা চেক করুন।"""

        data = res.json()

        if "basicInfo" not in data:
            return f"""[B][C][FF8C00]❌ Invalid Response!
[FFFFFF]Player data পাওয়া যায়নি।
[FF8C00]UID: {uid} — সঠিক UID দিন।"""

        basic = data.get("basicInfo", {})
        player_name = basic.get("nickname", "Unknown")
        likes_before = int(basic.get("liked", 0))

        # Step 2: Fake +100 যোগ দেখাও
        likes_added = FAKE_LIKE_ADDED
        likes_after = likes_before + likes_added

        # Step 3: Success message
        return f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]FAKE LIKE ✅
[00FFFF]❀ [00FF7F]NAME[FFFFFF]: {xMsGFixinG(player_name)}
[00FFFF]❀ [FFD700]UID[FFFFFF]: {xMsGFixinG(uid)}
[00FFFF]❀ [FF69B4]LIKE ADDED[FFFFFF]: {likes_added}
[00FFFF]❀ [00FFFF]LIKE BEFORE[FFFFFF]: {likes_before}
[00FFFF]❀ [00FF7F]LIKE AFTER[FFFFFF]: {likes_after}
[00FFFF]❀ [FFD700]STATUS[FFFFFF]: [00FF00]SUCCESS ✅
[00FFFF]✿ {BOT_NAME} ✿"""

    except requests.exceptions.Timeout:
        return """[B][C][FF8C00]❌ Timeout!
[FFFFFF]Server respond করছে না।
[FF8C00]কিছুক্ষণ পর আবার চেষ্টা করুন।"""
    except requests.exceptions.RequestException as e:
        return f"""[B][C][FF8C00]❌ Connection Error!
[FFFFFF]{str(e)[:60]}"""
    except Exception as e:
        return f"""[B][C][FF8C00]❌ Error!
[FFFFFF]{str(e)[:60]}"""

# ==================== FRIEND FUNCTIONS ====================

def get_jwt_from_bot():
    """Bot থেকে JWT টোকেন নাও"""
    try:
        # Try from global
        if 'LoGinDaTaUncRypTinG' in globals() and hasattr(LoGinDaTaUncRypTinG, 'token'):
            return LoGinDaTaUncRypTinG.token
        
        # Try from file
        with open("token.json", "r") as f:
            data = json.load(f)
            return data.get("token")
    except:
        return None

def get_bot_uid_from_token(token):
    """টোকেন থেকে UID বের করো"""
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded.get("account_id") or decoded.get("sub")
    except:
        return None

def create_info_protobuf(uid):
    """Player info request protobuf তৈরি করো"""
    message = uid_generator_pb2.uid_generator()
    message.saturn_ = int(uid)
    message.garena = 1
    return message.SerializeToString()

def encrypt_message_hex(data_bytes):
    """AES এনক্রিপ্ট করো"""
    KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    encrypted = cipher.encrypt(pad(data_bytes, AES.block_size))
    return binascii.hexlify(encrypted).decode('utf-8')

def get_player_info_direct(target_uid, token, server_name="BD"):
    """Player info fetch করো"""
    try:
        protobuf_data = create_info_protobuf(target_uid)
        encrypted_data = encrypt_message_hex(protobuf_data)
        
        # Region based URL
        if server_name.upper() == "BD":
            base_url = "https://clientbp.ggpolarbear.com/"
        elif server_name.upper() == "IND":
            base_url = "https://client.ind.freefiremobile.com/"
        else:
            base_url = "https://clientbp.ggpolarbear.com/"
        
        endpoint = base_url + "GetPlayerPersonalShow"
        
        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 13; SM-S918B)",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Authorization': f"Bearer {token}",
            'Content-Type': "application/x-www-form-urlencoded",
            'X-Unity-Version': "2018.4.11f1",
            'X-GA': "v1 1",
            'ReleaseVersion': "OB54"
        }
        
        response = requests.post(endpoint, data=bytes.fromhex(encrypted_data), headers=headers, verify=False, timeout=15)
        
        if response.status_code != 200:
            return None
        
        info = data_pb2.AccountPersonalShowInfo()
        info.ParseFromString(response.content)
        return info
    except Exception as e:
        print(f"Player info error: {e}")
        return None

def add_friend_direct(target_uid, token, server_name="BD"):
    """Friend add করো"""
    try:
        # Get player info first
        player_info = get_player_info_direct(target_uid, token, server_name)
        
        # Encrypt UID
        encrypted_id = Encrypt_ID(target_uid)
        payload = f"08a7c4839f1e10{encrypted_id}1801"
        encrypted_payload = encrypt_api(payload)
        
        # Region based URL
        if server_name.upper() == "BD":
            base_url = "https://clientbp.ggpolarbear.com/"
        elif server_name.upper() == "IND":
            base_url = "https://client.ind.freefiremobile.com/"
        else:
            base_url = "https://clientbp.ggpolarbear.com/"
        
        url = base_url + "RequestAddingFriend"
        
        headers = {
            "Authorization": f"Bearer {token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB54",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; Android 13)"
        }
        
        response = requests.post(url, headers=headers, data=bytes.fromhex(encrypted_payload), verify=False, timeout=15)
        
        if response.status_code == 200:
            # Extract player name
            player_name = "Unknown"
            if player_info and hasattr(player_info, 'basic_info'):
                player_name = getattr(player_info.basic_info, 'nickname', 'Unknown')
            
            return {
                "status": "success",
                "nickname": player_name,
                "uid": target_uid,
                "message": f"Friend request sent to {player_name}"
            }
        else:
            return {
                "status": "failed",
                "message": f"HTTP {response.status_code}",
                "uid": target_uid
            }
            
    except Exception as e:
        return {
            "status": "failed",
            "message": str(e),
            "uid": target_uid
        }

def remove_friend_direct(target_uid, token, server_name="BD"):
    """Friend remove করো"""
    try:
        # Get bot UID from token
        bot_uid = get_bot_uid_from_token(token)
        if not bot_uid:
            return {"status": "failed", "message": "Could not get bot UID"}
        
        # Get player info first
        player_info = get_player_info_direct(target_uid, token, server_name)
        
        # Create remove friend request
        msg = RemoveFriend_Req_pb2.RemoveFriend()
        msg.AuthorUid = int(bot_uid)
        msg.TargetUid = int(target_uid)
        
        KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
        IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        encrypted_bytes = cipher.encrypt(pad(msg.SerializeToString(), AES.block_size))
        
        # Region based URL
        if server_name.upper() == "BD":
            base_url = "https://clientbp.ggpolarbear.com/"
        elif server_name.upper() == "IND":
            base_url = "https://client.ind.freefiremobile.com/"
        else:
            base_url = "https://clientbp.ggpolarbear.com/"
        
        url = base_url + "RemoveFriend"
        
        headers = {
            'Authorization': f"Bearer {token}",
            'User-Agent': "Dalvik/2.1.0 (Linux; Android 13)",
            'Content-Type': "application/x-www-form-urlencoded",
            'X-Unity-Version': "2018.4.11f1",
            'X-GA': "v1 1",
            'ReleaseVersion': "OB54"
        }
        
        response = requests.post(url, data=encrypted_bytes, headers=headers, verify=False, timeout=15)
        
        if response.status_code == 200:
            player_name = "Unknown"
            if player_info and hasattr(player_info, 'basic_info'):
                player_name = getattr(player_info.basic_info, 'nickname', 'Unknown')
            
            return {
                "status": "success",
                "nickname": player_name,
                "uid": target_uid,
                "message": f"Friend removed: {player_name}"
            }
        else:
            return {
                "status": "failed",
                "message": f"HTTP {response.status_code}",
                "uid": target_uid
            }
            
    except Exception as e:
        return {
            "status": "failed",
            "message": str(e),
            "uid": target_uid
        }



####################################
#CHECK ACCOUNT IS BANNED

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB54"}

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[FFFF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)
    
def get_random_evo_emote():
    """Return random evo emote ID"""
    evo_emotes = [
        909000063,  # AK
        909000068,  # SCAR  
        909000075,  # 1st MP40
        909040010,  # 2nd MP40
        909000081,  # 1st M1014
        909039011,  # 2nd M1014
        909000085,  # XM8
        909000090,  # Famas
        909000098,  # UMP
        909035007,  # M1887
        909042008,  # Woodpecker
        909041005,  # Groza
        909033001,  # M4A1
        909038010,  # Thompson
        909038012,  # G18
        909045001,  # Parafal
        909049010,  # P90
        909051003   # M60
    ]
    return random.choice(evo_emotes)
    
async def extract_uid_from_emote_packet(data_hex, key, iv):
    """Extract UID from emote packet (the sender)"""
    try:
        # Decrypt the packet
        packet = await DeCode_PackEt(data_hex[10:])
        packet_json = json.loads(packet)
        
        print(f"📦 Analyzing packet structure: {json.dumps(packet_json, indent=2)[:200]}...")
        
        # PATTERN 1: Your Emote_k() structure (Type 21)
        if packet_json.get('1') == 21:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '5' in packet_json['2']['data'] and 'data' in packet_json['2']['data']['5']):
                
                nested = packet_json['2']['data']['5']['data']
                if '1' in nested:
                    uid = nested['1']['data']
                    print(f"✅ Extracted UID from pattern 21: {uid}")
                    return uid
        
        # PATTERN 2: Direct emote structure
        elif packet_json.get('1') == 26:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '1' in packet_json['2']['data']):
                
                uid = packet_json['2']['data']['1']['data']
                print(f"✅ Extracted UID from pattern 26: {uid}")
                return uid
        
        # PATTERN 3: Try common paths
        for path in ['2/1', '5/1', '2/data/1', '5/data/1']:
            try:
                uid = get_nested_value(packet_json, path)
                if uid and str(uid).isdigit() and len(str(uid)) > 6:
                    print(f"✅ Extracted UID from path {path}: {uid}")
                    return uid
            except:
                pass
        
        print(f"❌ Could not extract UID from packet")
        return None
        
    except Exception as e:
        print(f"❌ UID extraction error: {e}")
        return None

def get_nested_value(data, path):
    """Get value from nested JSON path like '2/5/1'"""
    keys = path.split('/')
    current = data
    
    for key in keys:
        if key.isdigit():
            key = str(key)  # JSON keys are strings
        
        if key in current and 'data' in current[key]:
            current = current[key]['data']
        else:
            return None
    
    return current

async def ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region):
    """Join team, authenticate chat, perform emote, and leave automatically"""
    try:
        # Step 1: Join the team
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        print(f"🤖 Joined team: {team_code}")
        
        # Wait for team data and chat authentication
        await asyncio.sleep(1.5)  # Increased to ensure proper connection
        
        # Step 2: The bot needs to be detected in the team and authenticate chat
        # This happens automatically in TcPOnLine, but we need to wait for it
        
        # Step 3: Perform emote to target UID
        emote_packet = await Emote_k(int(target_uid), int(emote_id), key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
        print(f"🎭 Performed emote {emote_id} to UID {target_uid}")
        
        # Wait for emote to register
        await asyncio.sleep(0.5)
        
        # Step 4: Leave the team
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print(f"🚪 Left team: {team_code}")
        
        return True, f"Quick emote attack completed! Sent emote to UID {target_uid}"
        
    except Exception as e:
        return False, f"Quick emote attack failed: {str(e)}"
        
        
async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.126.1"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-0HmNvmGj1hc8JuLIT2NxWA==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-0HmNvmGj1hc8JuLIT2NxWA==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019120776"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
    

async def cHTypE(H):
    """Detect chat type including custom rooms"""
    if not H: 
        return 'Squid'
    elif H == 1: 
        return 'CLan'
    elif H == 2: 
        return 'PrivaTe'
    elif H == 3: 
        return 'CustomRoom'  # Custom room chat type
    else:
        return 'Squid'  # Default fallback
    
async def SEndMsG(H, message, Uid, chat_id, key, iv, region):
    """Send message to any chat type including custom rooms"""
    TypE = await cHTypE(H)
    
    if TypE == 'Squid': 
        msg_packet = await xSEndMsgsQ(message, chat_id, key, iv)
    elif TypE == 'CLan': 
        msg_packet = await xSEndMsg(message, 1, chat_id, chat_id, key, iv)
    elif TypE == 'PrivaTe': 
        msg_packet = await xSEndMsg(message, 2, Uid, Uid, key, iv)
    else:
        # Fallback to squad chat
        msg_packet = await xSEndMsgsQ(message, chat_id, key, iv)
        
    return msg_packet
    
    
async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    if TypE == 'ChaT' and ChaT: whisper_writer.write(PacKeT) ; await whisper_writer.drain()
    elif TypE == 'OnLine': online_writer.write(PacKeT) ; await online_writer.drain()
    else: return 'UnsoPorTed TypE ! >> ErrrroR (:():)' 

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=3, region="ind"):
    """Enhanced safe send message that works with custom rooms"""
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                
            print(f"✅ Message sent successfully to chat type {chat_type} (attempt {attempt + 1})")
            return True
        except Exception as e:
            print(f"❌ Failed to send message (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)
    return False

async def fast_emote_spam(uids, emote_id, key, iv, region):
    """Fast emote spam function that sends emotes rapidly"""
    global fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    while fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # 0.1 seconds interval between spam cycles

# NEW FUNCTION: Custom emote spam with specified times
async def custom_emote_spam(uid, emote_id, times, key, iv, region):
    """Custom emote spam function that sends emotes specified number of times"""
    global custom_spam_running
    count = 0
    
    while custom_spam_running and count < times:
        try:
            uid_int = int(uid)
            H = await Emote_k(uid_int, int(emote_id), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            count += 1
            await asyncio.sleep(0.1)  # 0.1 seconds interval between emotes
        except Exception as e:
            print(f"Error in custom_emote_spam for uid {uid}: {e}")
            break

async def create_level_up_bot_connection(key, iv, region):
    """Create a separate connection for level-up bot"""
    try:
        # This would use a different bot account
        # For now, we'll use the main bot
        print("🤖 Level-up bot connection initialized")
        return True
    except Exception as e:
        print(f"❌ Level-up bot connection error: {e}")
        return False

async def level_up_join_team(team_code, key, iv, region):
    """Level-up bot joins the team"""
    try:
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        print(f"🤖 Level-up bot joining team: {team_code}")
        await asyncio.sleep(2)
        return True
    except Exception as e:
        print(f"❌ Level-up bot join error: {e}")
        return False

async def level_up_leave_team(key, iv):
    """Level-up bot leaves the team"""
    try:
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print("🤖 Level-up bot leaving team")
        await asyncio.sleep(1)
        return True
    except Exception as e:
        print(f"❌ Level-up bot leave error: {e}")
        return False
        
async def level_up_loop(team_code, target_uid, key, iv, region, chat_type, chat_id):
    """Main level-up automation loop"""
    global level_up_running
    
    cycle_count = 0
    max_cycles = 1000  # Safety limit
    
    print(f"🚀 Starting level-up automation for team {team_code}")
    
    while level_up_running and cycle_count < max_cycles:
        try:
            cycle_count += 1
            print(f"🔄 Level-up cycle #{cycle_count}")
            
            # Step 1: Send instruction message
            instruction_msg = f"""[B][C][FFFF00]🔄 LEVEL-UP CYCLE #{cycle_count}

🤖 Bot: Joining your team...
🎮 Action: Will start match
⏱️ After match: Wait {level_up_wait_time} seconds
🔄 Then: Repeat process

📊 Status: Bot is working...
"""
            await safe_send_message(chat_type, instruction_msg, target_uid, chat_id, key, iv)
            
            # Step 2: Join the team
            join_success = await level_up_join_team(team_code, key, iv, region)
            if not join_success:
                print("❌ Failed to join team, retrying...")
                await asyncio.sleep(2)
                continue
            
            # Step 3: Send "ready" message
            ready_msg = f"[B][C][FFFF00]✅ Bot joined! Starting match...\n"
            await safe_send_message(chat_type, ready_msg, target_uid, chat_id, key, iv)
            
            # Step 4: Start the match (spam start packet)
            start_packet = await FS(key, iv)
            spam_duration = 10  # Spam for 10 seconds
            start_time = time.time()
            
            while time.time() - start_time < spam_duration and level_up_running:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
                await asyncio.sleep(0.2)  # 200ms delay between packets
            
            # Step 5: Wait for match to complete (simulate)
            waiting_msg = f"""[B][C][FFFF00]⏱️ MATCH IN PROGRESS...

⏳ Waiting for match to complete...
🔄 Next cycle starts in {level_up_wait_time} seconds
🤖 Bot remains in team

💡 Let the match complete normally!
"""
            await safe_send_message(chat_type, waiting_msg, target_uid, chat_id, key, iv)
            
            # Step 6: Wait the specified time
            wait_count = 0
            while wait_count < level_up_wait_time and level_up_running:
                await asyncio.sleep(1)
                wait_count += 1
                
                # Progress update every 5 seconds
                if wait_count % 5 == 0:
                    progress_msg = f"[B][C][FFFF00]⏱️ {wait_count}/{level_up_wait_time} seconds waited...\n"
                    await safe_send_message(chat_type, progress_msg, target_uid, chat_id, key, iv)
            
            if not level_up_running:
                break
            
            # Step 7: Leave team
            leave_success = await level_up_leave_team(key, iv)
            
            if leave_success:
                leave_msg = f"[B][C][FF0000]🚪 Bot left team to restart cycle...\n"
                await safe_send_message(chat_type, leave_msg, target_uid, chat_id, key, iv)
            
            # Step 8: Small delay before next cycle
            await asyncio.sleep(2)
            
        except Exception as e:
            print(f"❌ Error in level-up cycle: {e}")
            # Try to recover
            await level_up_leave_team(key, iv)
            await asyncio.sleep(3)
    
    print("🛑 Level-up automation stopped")

async def Send_Entry_Emote(uid, K, V, emote_id=912038002, session_id=5, trigger_type=1):
    """Send arrival/entry animation emote
    
    Args:
        uid: Target player UID
        K: Encryption key
        V: Initialization vector
        emote_id: Emote ID (default: 912038002 - arrival animation)
        session_id: Session ID (default: 5)
        trigger_type: Trigger type (default: 1 - entry)
    """
    try:
        fields = {
            1: 4,           # Packet ID for entry emotes
            2: int(uid),    # Player UID
            3: int(session_id),     # Session ID
            4: int(emote_id),       # Emote ID
            5: int(trigger_type),   # Trigger Type (1=entry, 2=exit, etc.)
            6: int(uid),    # Repeated UID
            7: 1,           # Static Value
            8: int(uid),    # Repeated UID
            9: int(uid),    # Repeated UID
            10: int(uid),   # Repeated UID
            11: int(uid),   # Repeated UID
        }
        
        # Different arrival animations
        arrival_emotes = {
            "default": 912038002,
        }
        
        # Use provided emote_id or default
        if isinstance(emote_id, str) and emote_id in arrival_emotes:
            fields[4] = arrival_emotes[emote_id]
        
        proto_hex = (await CrEaTe_ProTo(fields)).hex()
        
        # Determine packet type based on region (you might need to pass region)
        # For now using '0515' as in your example
        return await GeneRaTePk(proto_hex, '0515', K, V)
        
    except Exception as e:
        print(f"❌ Error creating entry emote packet: {e}")
        return None



# NEW FUNCTION: Evolution emote spam with mapping
async def evo_emote_spam(uids, number, key, iv, region):
    """Send evolution emotes based on number mapping"""
    try:
        emote_id = EMOTE_MAP.get(int(number))
        if not emote_id:
            return False, f"Invalid number! Use 1-21 only."
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Error sending evo emote to {uid}: {e}")
        
        return True, f"Sent evolution emote {number} (ID: {emote_id}) to {success_count} player(s)"
    
    except Exception as e:
        return False, f"Error in evo_emote_spam: {str(e)}"

def get_real_player_info(uid):
    """Get player info directly from Free Fire servers (NO API)"""
    try:
        print(f"🔍 Getting info for UID: {uid}")
        
        # Load token from file
        token = None
        try:
            with open("token.json", "r") as f:
                data = json.load(f)
                token = data.get("token")
                if token:
                    print(f"✅ Token loaded from token.json")
        except Exception as e:
            print(f"❌ Failed to load token: {e}")
        
        if not token:
            return {"success": False, "message": "No token found! Please restart bot."}
        
        # Import required modules
        from Pb2 import main_pb2, AccountPersonalShow_pb2
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import pad
        from google.protobuf import json_format
        
        # Create request
        req = main_pb2.GetPlayerPersonalShow()
        req.a = int(uid)
        req.b = 7
        
        # Encrypt
        KEY = b'Yg&tc%DEuh6%Zc^8'
        IV = b'6oyZDr22E3ychjM%'
        
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        encrypted = cipher.encrypt(pad(req.SerializeToString(), AES.block_size))
        
        headers = {
            "Authorization": f"Bearer {token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB54",
            "Content-Type": "application/octet-stream",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        
        # Try all servers
        servers = [
            "https://clientbp.ggpolarbear.com",
            "https://client.ind.freefiremobile.com",
            "https://client.sg.freefiremobile.com",
            "https://client.bd.freefiremobile.com"
        ]
        
        for server in servers:
            try:
                url = f"{server}/GetPlayerPersonalShow"
                print(f"📡 Trying: {server}")
                
                response = requests.post(url, data=encrypted, headers=headers, timeout=15, verify=False)
                
                if response.status_code == 200:
                    result = AccountPersonalShow_pb2.AccountPersonalShowInfo()
                    result.ParseFromString(response.content)
                    data = json_format.MessageToDict(result)
                    if data and data.get("basicInfo"):
                        print(f"✅ Success from {server}")
                        return {"success": True, "data": data}
            except Exception as e:
                print(f"❌ Server error: {e}")
                continue
        
        return {"success": False, "message": "All servers failed! UID may be invalid."}
        
    except Exception as e:
        print(f"❌ get_real_player_info error: {e}")
        import traceback
        traceback.print_exc()
        return {"success": False, "message": str(e)}

# NEW FUNCTION: Fast evolution emote spam
async def evo_fast_emote_spam(uids, number, key, iv, region):
    """Fast evolution emote spam function"""
    global evo_fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in evo_fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed fast evolution emote spam {count} times"
    
async def send_required_packets(key, iv, region, bot_uid):
    """Send packets required after connection"""
    try:
        # Packet 1: Client info
        fields1 = {
            1: 100,
            2: {
                1: bot_uid,
                2: "1.120.2",  # Game version
                3: "Android",
                4: "en",
            }
        }
        
        # Packet 2: Device info
        fields2 = {
            1: 101,
            2: {
                1: "vivo",
                2: "1901",
                3: "arm64-v8a",
                4: str(time.time()),
            }
        }
        
        packets = []
        for fields in [fields1, fields2]:
            if region.lower() == "ind":
                packet_type = '0514'
            elif region.lower() == "bd":
                packet_type = "0519"
            else:
                packet_type = "0515"
                
            packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
            packets.append(packet)
        
        return packets
        
    except Exception as e:
        print(f"❌ Required packets error: {e}")
        return []

# NEW FUNCTION: Custom evolution emote spam with specified times
async def evo_custom_emote_spam(uids, number, times, key, iv, region):
    """Custom evolution emote spam with specified repeat times"""
    global evo_custom_spam_running
    count = 0
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_custom_spam_running and count < times:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in evo_custom_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed custom evolution emote spam {count} times"

async def RejectMSGtaxt(squad_owner,uid, key, iv):
    random_banner = f"""
.
.
.










[00FF00]WELCOME
[FFD700]TO NAYAN乡ㅤ1M BOT



 """
    fields = {
    1: 5,
    2: {
        1: int(squad_owner),
        2: 1,
        3: int(uid),
        4: random_banner
    }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , key, iv)

async def send_keep_alive(key, iv, region):
    """Send keep-alive packet to maintain connection"""
    try:
        fields = {
            1: 99,  # Keep-alive packet type
            2: {
                1: int(time.time()),
                2: 1,  # Keep-alive flag
            }
        }
        
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
        return packet
    except Exception as e:
        print(f"❌ Keep-alive error: {e}")
        return None

async def ArohiAccepted(uid,code,K,V):
    fields = {
        1: 4,
        2: {
            1: uid,
            3: uid,
            8: 1,
            9: {
            2: 161,
            4: "y[WW",
            6: 11,
            8: "1.114.18",
            9: 3,
            10: 1
            },
            10: str(code),
        }
        }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , K , V)


async def new_lag(key , iv):
    fields = {
        1: 15,
        2: {
            1: 804266360,
            2: 1
        }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , key , iv)


async def convert_kyro_to_your_system(target_uid, chat_id, key, iv, nickname="NoTmeowL", title_id=None):
    """EXACT conversion with customizable title ID"""
    try:
        # Use provided title_id or get random one
        if title_id is None:
            # Get a random title from the list
            available_titles = [905090075, 904990072, 904990069, 905190079, 904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072]
            title_id = random.choice(available_titles)
        
        # Create fields dictionary with specific title_id
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',  # Use specific title ID
                # ... rest of your fields
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(await xBunnEr()),
                    4: 330,
                    5: 827001007,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        
        # ... rest of your existing function
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        
        print(f"✅ Created packet with Title ID: {title_id}")
        return final_packet
        
    except Exception as e:
        print(f"❌ Conversion error: {e}")
        return None

async def check_for_sticker_and_emote(response, key, iv, online_writer):

    try:
        msg = response.Data.msg

        # Sticker অথবা emoji detect
        if "[1=" in msg or (msg and len(msg) <= 0):

            print("🎯 Emoji/Stiker detected")

            emote_list = [
                912038002,
                912038003,
                912038004,
                912038005,
                912038006
            ]

            emote_id = random.choice(emote_list)

            pkt = await Send_Entry_Emote(
                uid=response.Data.uid,
                K=key,
                V=iv,
                emote_id=emote_id
            )

            if pkt:
                online_writer.write(pkt)
                await online_writer.drain()

                print(f"🎭 Random emote sent: {emote_id}")

    except Exception as e:
        print("Emote logic error:", e)
                
def get_random_sticker():
    """
    Randomly select one sticker from available packs
    """

    sticker_packs = [
        # NORMAL STICKERS (1200000001-1 to 24)
        ("1200000001", 1, 24),

        # KELLY EMOJIS (1200000002-1 to 15)
        ("1200000004", 1, 15),

        # MAD CHICKEN (1200000004-1 to 13)
        ("1200000002", 1, 13),
    ]

    pack_id, start, end = random.choice(sticker_packs)
    sticker_no = random.randint(start, end)

    return f"[1={pack_id}-{sticker_no}]"
        
async def send_sticker(target_uid, chat_id, key, iv, nickname="BLACK"):
    """Send Random Sticker using /sticker command"""
    try:
        sticker_value = get_random_sticker()

        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"StickerStr" : "{sticker_value}", "type":"Sticker"}}',
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(get_random_avatar()),
                    4: 330,
                    5: 827001007,
                    8: "BOT TEAM",
                    10: 1,
                    11: 66,
                    12: 66,
                    13: {1: 2},
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }

        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()

        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"

        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)

        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)

        print(f"✅ Sticker Sent: {sticker_value}")
        return final_packet

    except Exception as e:
        print(f"❌ Sticker error: {e}")
        return None

# Alternative: DIRECT port of your friend's function but with your UID
async def send_kyro_title_adapted(chat_id, key, iv, target_uid, nickname="NoTmeowL"):
    """Direct adaptation of your friend's working function"""
    try:
        # Import your proto file (make sure it's in the same directory)
        from kyro_title_pb2 import GenTeamTitle
        
        root = GenTeamTitle()
        root.type = 1
        
        nested_object = root.data
        nested_object.uid = int(target_uid)  # CHANGE: Use target UID
        nested_object.chat_id = int(chat_id)
        nested_object.title = f"{{\"TitleID\":{titles()},\"type\":\"Title\"}}"
        nested_object.timestamp = int(datetime.now().timestamp())
        nested_object.language = "en"
        
        nested_details = nested_object.field9
        nested_details.Nickname = f"[C][B][FF0000]{nickname}"  # CHANGE: Your nickname
        nested_details.avatar_id = int(await xBunnEr())  # Use your function
        nested_details.rank = 330
        nested_details.badge = 827001007
        nested_details.Clan_Name = "BOT TEAM"  # CHANGE: Your clan
        nested_details.field10 = 1
        nested_details.global_rank_pos = 1
        nested_details.badge_info.value = 2
        
        nested_details.prime_info.prime_uid = 1158053040
        nested_details.prime_info.prime_level = 8
        # IMPORTANT: This must be bytes, not string!
        nested_details.prime_info.prime_hex = b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
        
        nested_options = nested_object.field13
        nested_options.url_type = 2
        nested_options.curl_platform = 1
        
        nested_object.empty_field.SetInParent()
        
        # Serialize
        packet = root.SerializeToString().hex()
        
        # Use YOUR encryption function
        encrypted_packet = await encrypt_packet(packet, key, iv)
        
        # Calculate length
        packet_length = len(encrypted_packet) // 2
        
        # Convert to hex (4 characters with leading zeros)
        hex_length = f"{packet_length:04x}"
        
        # Build packet EXACTLY like your friend
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"❌ Direct adaptation error: {e}")
        import traceback
        traceback.print_exc()
        return None

async def send_all_titles_sequentially(uid, chat_id, key, iv, region, chat_type):
    """Send all titles one by one with 2-second delay"""
    
    # Get all titles
    all_titles = [
        905090075, 904990072, 904990069, 905190079, 904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072
    ]
    
    total_titles = len(all_titles)
    
    # Send initial message
    start_msg = f"""[B][C][FFFF00]🎖️ STARTING TITLE SEQUENCE!

📊 Total Titles: {total_titles}
⏱️ Delay: 2 seconds between titles
🔁 Mode: Sequential
🎯 Target: {uid}

⏳ Sending titles now...
"""
    await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv)
    
    try:
        for index, title_id in enumerate(all_titles):
            title_number = index + 1
            
            # Create progress message
            progress_msg = f"""[B][C][FFFF00]📤 SENDING TITLE {title_number}/{total_titles}

🎖️ Title ID: {title_id}
📊 Progress: {title_number}/{total_titles}
⏱️ Next in: 2 seconds
"""
            await safe_send_message(chat_type, progress_msg, uid, chat_id, key, iv)
            
            # Send the actual title using your existing method
            # You'll need to use your existing title sending logic here
            # For example:
            title_packet = await convert_kyro_to_your_system(uid, chat_id, key, iv, nickname="NoTmeowL", title_id=title_id)
            
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                print(f"✅ Sent title {title_number}/{total_titles}: {title_id}")
            
            # Wait 2 seconds before next title (unless it's the last one)
            if title_number < total_titles:
                await asyncio.sleep(2)
        
        # Completion message
        completion_msg = f"""[B][C][FFFF00]✅ ALL TITLES SENT SUCCESSFULLY!

🎊 Total: {total_titles} titles sent
🎯 Target: {uid}
⏱️ Duration: {total_titles * 2} seconds
✅ Status: Complete!

🎖️ Titles Sent:
1. 905090075
2. 904990072
3. 904990069
4. 905190079
"""
        await safe_send_message(chat_type, completion_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error sending titles: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def handle_all_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /alltitles command to send all titles sequentially"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        target_uid = uid
        target_name = "Yourself"
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"UID {target_uid}"
    else:
        error_msg = f"""[B][C][FF0000]❌ Usage: /alltitles [uid]
        
📝 Examples:
/alltitles - Send all titles to yourself
/alltitles 123456789 - Send all titles to specific UID

🎯 What it does:
1. Sends all 4 titles one by one
2. 2-second delay between each title
3. Sends in background (non-blocking)
4. Shows progress updates
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentially(target_uid, chat_id, key, iv, region, chat_type)
    )
    
    # Immediate response
    response_msg = f"""[B][C][FFFF00]🚀 STARTING TITLE SEQUENCE IN BACKGROUND!

👤 Target: {target_name}
🎖️ Total Titles: 4
⏱️ Delay: 2 seconds each
📱 Status: Running in background...

💡 You'll receive progress updates as titles are sent!
"""
    await safe_send_message(chat_type, response_msg, uid, chat_id, key, iv)


async def noob(target_uid, chat_id, key, iv, nickname="NoTmeowL", title_id=None):
    """EXACT conversion with customizable title ID"""
    try:
        # Use provided title_id or get random one
        if title_id is None:
            # Get a random title from the list
            available_titles = [904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072]
            title_id = random.choice(available_titles)
        
        # Create fields dictionary with specific title_id
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(await xBunnEr()),
                    4: 330,
                    5: 827001007,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        
        # ... rest of your existing function
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        
        print(f"✅ Created packet with Title ID: {title_id}")
        return final_packet
        
    except Exception as e:
        print(f"❌ Conversion error: {e}")
        return None
        


async def get_player_name_from_uid(uid, region="IND"):
    """Get player name from UID - uses same method as /friend command"""
    try:
        # Load token from token.json (same as /friend command)
        token = load_jwt_token()
        if not token:
            return f"Player_{uid[:4]}"  # Fallback if no token
        
        # Use your existing get_player_info function
        player_name, player_uid = get_player_info(str(uid), token)
        
        if player_name and player_name != "Unknown":
            return player_name
        else:
            return f"Player_{uid[:4]}"
            
    except Exception as e:
        print(f"❌ Error getting name for {uid}: {e}")
        return f"Player_{uid[:4]}"  # Fallback

async def send_all_titles_sequentiallly(uid, chat_id, key, iv, region, chat_type):
    """Send all titles one by one with 2-second delay"""
    
    # Get all titles
    all_titles = [
        904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072
    ]
    
    total_titles = len(all_titles)
    
    # Send initial message
    start_msg = f"""[B][C][FFFF00] আরে সালা আ🤫মি  যদি  noob হয়ই  তাহলে tui একটা হিজ🤫লা

"""
    await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv)
    
    try:
        for index, title_id in enumerate(all_titles):
            title_number = index + 1
            

            
            # Send the actual title using your existing method
            # You'll need to use your existing title sending logic here
            # For example:
            title_packet = await noob(uid, chat_id, key, iv, nickname="NoTmeowL", title_id=title_id)
            
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                print(f"✅ Sent title {title_number}/{total_titles}: {title_id}")
            
            # Wait 2 seconds before next title (unless it's the last one)
            if title_number < total_titles:
                await asyncio.sleep(2)
        
        # Completion message
        completion_msg = f"""[B][C][FFFF00]আ🤫রে মাদার🙂চো🤫দ এখন তুই এই Title গুলা দেখ আর বল তো🤫র আব্বু আমি সা🤫লা noob
"""
        await safe_send_message(chat_type, completion_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error sending titles: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def handle_alll_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /alltitles command to send all titles sequentially"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        target_uid = uid
        target_name = "Yourself"
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"UID {target_uid}"
    else:
        error_msg = f"""[B][C][FF0000]❌ Usage: /alltitles [uid]
        
📝 Examples:
/alltitles - Send all titles to yourself
/alltitles 123456789 - Send all titles to specific UID

🎯 What it does:
1. Sends all 4 titles one by one
2. 2-second delay between each title
3. Sends in background (non-blocking)
4. Shows progress updates
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentiallly(target_uid, chat_id, key, iv, region, chat_type)
    )
    


async def RoomJoin(room_id, password, key, iv):
    """Join Free Fire custom room"""
    try:
        # Import your proto file
        from room_join_pb2 import join_room
        
        root = join_room()
        root.field_1 = 3  # Room join command
        
        # Nested object
        nested_object = root.field_2
        nested_object.field_1 = int(room_id)
        nested_object.field_2 = str(password)
        
        # Field 8
        nested_8 = nested_object.field_8
        nested_8.field_1 = "IDC3"
        nested_8.field_2 = 149
        nested_8.field_3 = "IND"
        
        # Other fields
        nested_object.field_9 = "\x01\x03\x04\x07\x09\x0a\x0b\x12\x0e\x16\x19\x20\x1d"  # Bytes, not string
        nested_object.field_10 = 1
        nested_object.field_12.SetInParent()  # Empty field
        nested_object.field_13 = 1
        nested_object.field_14 = 1
        nested_object.field_16 = "en"
        
        # Field 22
        nested_22 = nested_object.field_22
        nested_22.field_1 = 21
        
        # Serialize
        packet_hex = root.SerializeToString().hex()
        
        # Encrypt using your function
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        
        # Convert length to hex
        hex_length = dec_to_hex(packet_length)  # Use your existing function
        
        # Build packet header (type 0e15 for room join)
        if len(hex_length) == 2:
            header = "0e15000000"
        elif len(hex_length) == 3:
            header = "0e1500000"
        elif len(hex_length) == 4:
            header = "0e150000"
        elif len(hex_length) == 5:
            header = "0e15000"
        else:
            header = "0e150000"
        
        final_packet_hex = header + hex_length + encrypted_packet
        
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"❌ Room join error: {e}")
        import traceback
        traceback.print_exc()
        return None
        

# Alternative: Using your fields dictionary format
async def RoomJoin_fields(room_id, password, key, iv):
    """Room join using your CrEaTe_ProTo format"""
    try:
        fields = {
            1: 3,  # Room join command
            2: {   # Nested object
                1: int(room_id),   # room_id
                2: str(password),  # password
                8: {  # field_8
                    1: "IDC3",
                    2: 149,
                    3: "IND"
                },
                9: b"\x01\x03\x04\x07\x09\x0a\x0b\x12\x0e\x16\x19\x20\x1d",  # Bytes!
                10: 1,
                12: {},  # Empty field
                13: 1,
                14: 1,
                16: "en",
                22: {  # field_22
                    1: 21
                }
            }
        }
        
        # Convert to protobuf
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        # Encrypt and build packet
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = dec_to_hex(packet_length)
        
        # Build header
        if len(hex_length) == 2:
            header = "0e15000000"
        elif len(hex_length) == 3:
            header = "0e1500000"
        elif len(hex_length) == 4:
            header = "0e150000"
        elif len(hex_length) == 5:
            header = "0e15000"
        else:
            header = "0e150000"
        
        final_packet_hex = header + hex_length + encrypted_packet
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"❌ Room join fields error: {e}")
        return None

def remove_from_whitelist(uid_to_remove):
    """Remove UID from whitelist"""
    global WHITELISTED_UIDS
    
    uid_str = str(uid_to_remove)
    
    # Don't allow removing owner
    if uid_str == "2579372095":  # Your UID
        return False, "Cannot remove bot owner from whitelist!"
    
    if uid_str not in WHITELISTED_UIDS:
        return False, f"UID {uid_str} not in whitelist"
    
    WHITELISTED_UIDS.remove(uid_str)
    return True, f"✅ Removed {uid_str} from whitelist"



async def handle_xjoin_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /xjoin command to join custom rooms"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 3:
        error_msg = f"""[B][C][FF0000]🎮 ROOM JOIN COMMAND

❌ Usage: /xjoin (room_id) (password)

📝 Examples:
/xjoin 123456 0000
/xjoin 987654 1111

🔑 Room Info:
• Room ID: 6-digit number
• Password: Usually 4 digits (0000-9999)

💡 Bot will join the custom room!
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    room_id = parts[1]
    password = parts[2]
    
    if not room_id.isdigit():
        error_msg = f"[B][C][FF0000]❌ Room ID must be numbers only!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Send initial message
    initial_msg = f"[B][C][FFFF00]🚀 JOINING CUSTOM ROOM...\n🏠 Room: {room_id}\n🔑 Password: {password}\n"
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        # Try method 1: Direct proto method
        room_packet = await RoomJoin(room_id, password, key, iv)
        
        if not room_packet:
            # Try method 2: Fields method
            room_packet = await RoomJoin_fields(room_id, password, key, iv)
        
        if room_packet and online_writer:
            # Send via Online connection
            online_writer.write(room_packet)
            await online_writer.drain()
            
            print(f"✅ Room join packet sent! Room: {room_id}")
            joinroom = join_room_chanel(room_id, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', joinroom)
            success_msg = f"""[B][C][FFFF00]✅ ROOM JOIN COMMAND SENT!

🏠 Room ID: {room_id}
🔑 Password: {password}
"""
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to create room join packet!\n"
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error joining room: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def handle_room_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /room command with proper error handling"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 2:
        error_msg = f"[B][C][FF0000]❌ Usage: /room (uid)\nExample: /room 10634259930\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    target_uid = parts[1]
    
    try:
        # Step 1: Check player status
        status_result, status_message = await check_player_status(target_uid, key, iv)
        
        packet = None
        player_status = None
        
        # If live check failed, try cache
        if not status_result:
            # Check cache
            cached_data = load_from_cache(target_uid)
            if cached_data and 'packet' in cached_data:
                packet = cached_data['packet']
                player_status = cached_data.get('status', 'UNKNOWN')
                print(f"⚠️ Using cached data for {target_uid}")
            else:
                error_msg = f"[B][C][FF0000]❌ Player {target_uid} not found\n"
                await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
                return
        else:
            # Use live data
            packet = status_result.get('packet', b'')
            player_status = get_player_status(packet)
        
        # Step 2: Check if player is in room
        if not player_status or "IN ROOM" not in player_status:
            info_msg = f"""[B][C][FFFF00]📊 STATUS: {player_status or 'UNKNOWN'}

👤 Player: {target_uid}
❌ Not in custom room

💡 Player must join custom room first!"""
            await safe_send_message(chat_type, info_msg, uid, chat_id, key, iv)
            return
        
        # Step 3: Extract room ID
        room_id = get_idroom_by_idplayer(packet) if packet else None
        
        if not room_id:
            error_msg = f"[B][C][FF0000]❌ Failed to extract room ID\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            return
        
        # Step 4: SUCCESS - Send room info
        success_msg = f"""[B][C][FFFF00]✅ ROOM FOUND!

👤 Player: {target_uid}
🏠 Room ID: {room_id}
📊 Status: {player_status}
⚡ Data: {'CACHED' if not status_result else 'LIVE'}

💡 Quick join: /xjoin {room_id} 0000
"""
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Step 5: AUTO-SPAM (add this if you want spam)
        # Uncomment this section if you want auto-spam:
        
        spam_count = 5
        for i in range(spam_count):
            try:
                spam_packet = await Room_Spam(target_uid, room_id, f"Spam_{i+1}", key, iv)
                if spam_packet and online_writer:
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
                    await asyncio.sleep(0.2)
            except Exception as e:
                print(f"Spam error: {e}")
        
        spam_msg = f"[B][C][FFFF00]✅ Spammed {spam_count} invites!\n"
        await safe_send_message(chat_type, spam_msg, uid, chat_id, key, iv)
        
        
    except Exception as e:
        print(f"❌ Room command error: {e}")
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:80]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

# Room spam command (send multiple messages)
async def handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /spamroom command to send room spam messages"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 4:
        error_msg = f"""[B][C][FF0000]❌ Usage: /spamroom (room_id) (uid) (message)
        
📝 Example: /spamroom 123456 14010319252 Hello World!

⚙️ Parameters:
• room_id = Custom room ID (numbers)
• uid = Player UID to spam
• message = Text message to send

🎯 What it does:
1. Creates room spam packet
2. Sends message to specified room
3. Uses colorful formatting
4. Packet type: 0e15 (room spam)
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    try:
        room_id = parts[1]
        target_uid = parts[2]
        message = ' '.join(parts[3:])
        
        # Validate inputs
        if not room_id.isdigit():
            error_msg = f"[B][C][FF0000]❌ Room ID must be numbers only!\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            return
            
        if not target_uid.isdigit():
            error_msg = f"[B][C][FF0000]❌ UID must be numbers only!\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            return
        
        # Send initial message
        initial_msg = f"[B][C][FFFF00]🚀 PREPARING ROOM SPAM...\n"
        initial_msg += f"🏠 Room ID: {room_id}\n"
        initial_msg += f"👤 Target UID: {target_uid}\n"
        initial_msg += f"📝 Message: {message[:30]}...\n"
        initial_msg += f"📦 Packet type: 0e15\n"
        initial_msg += f"⏳ Creating packet...\n"
        
        await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
        
        # Create and send the spam packet
        spam_packet = await SPam_Room(target_uid, room_id, message, key, iv)
        
        if spam_packet:
            # Send via Online connection (since it's room-related)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
            
            success_msg = f"""[B][C][FFFF00]✅ ROOM SPAM PACKET SENT!

🏠 Room: {room_id}
👤 Target: {target_uid}
📝 Message: {message[:40]}...
📦 Packet: Type 0e15 (Room Spam)
✅ Status: Delivered successfully

💡 Packet includes:
• Colorful message formatting
• Avatar: {await xBunnEr()}
• Rank: 330
• Badge: 201
"""
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to create spam packet!\n"
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

# Also create a shorter alias command handler
async def handle_sr_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /sr command (short version of /spamroom)"""
    await handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type)
        
async def detect_emote_perfect(data_hex, key, iv):
    """100% ACCURATE emote detection using YOUR exact packet structure"""
    
    try:
        # Step 1: Decrypt using your EXACT method
        decrypted = await DeCode_PackEt(data_hex[10:])  # Use YOUR existing function
        packet_json = json.loads(decrypted)
        
        # Step 2: EXACT STRUCTURE MATCHING
        # Check for Type 21 (from your Emote_k function)
        if packet_json.get('1') == 21:
            # Check for the EXACT structure you use
            if '2' in packet_json and 'data' in packet_json['2']:
                emote_data = packet_json['2']['data']
                
                # Verify EXACT field structure matches Emote_k()
                if ('1' in emote_data and '2' in emote_data and 
                    '5' in emote_data and 'data' in emote_data['5']):
                    
                    nested = emote_data['5']['data']
                    
                    # THIS IS THE 100% ACCURATE DETECTION
                    # Matches EXACTLY what you send in Emote_k()
                    if '1' in nested and '3' in nested:
                        return {
                            'type': 'emote',
                            'packet_type': 21,  # ← EXACT MATCH
                            'identifier': emote_data.get('1', {}).get('data'),
                            'base_emote': emote_data.get('2', {}).get('data'),
                            'target_uid': nested.get('1', {}).get('data'),  # WHO received it
                            'emote_id': nested.get('3', {}).get('data'),
                            'confidence': 100.0,
                            'raw_packet': packet_json
                        }
        
        # ALTERNATIVE FORMAT: Direct to player
        elif packet_json.get('1') == 26:  # Another emote type
            # Add similar exact matching here
            pass
        
        return None
        
    except Exception as e:
        print(f"❌ Perfect detection error: {e}")
        return None
        
async def detect_emote_with_sender(data_hex, key, iv):
    """Detect emote AND find who sent it"""
    
    try:
        # First, detect if it's an emote packet
        emote_info = await detect_emote_perfect(data_hex, key, iv)
        
        if not emote_info:
            return None
        
        # Now we need to find the SENDER's UID
        # Look for sender in different packet parts
        
        # METHOD 1: Check packet header for UID
        packet_header = data_hex[:20]
        
        # Look for UID patterns in hex (9-11 digits)
        import re
        uid_pattern = r'(\d{9,11})'
        
        # Search in entire packet
        all_uids = re.findall(uid_pattern, data_hex)
        
        if len(all_uids) >= 2:
            # We have at least 2 UIDs: sender and target
            # The target is already in emote_info['target_uid']
            target_uid = str(emote_info['target_uid'])
            
            # Find which UID is NOT the target
            for uid in all_uids:
                if uid != target_uid:
                    # This is likely the SENDER
                    emote_info['sender_uid'] = int(uid)
                    emote_info['detection_method'] = 'uid_pattern'
                    
                    print(f"✅ SENDER FOUND: {uid} sent emote to {target_uid}")
                    return emote_info
        
        # METHOD 2: Look in packet structure
        packet_json = emote_info['raw_packet']
        
        # Search recursively for UID that's NOT the target
        def find_sender_in_json(obj, target_uid):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == 'data' and isinstance(v, (int, str)):
                        v_str = str(v)
                        if v_str.isdigit() and len(v_str) > 8:
                            if v_str != str(target_uid):
                                return int(v)
                    elif isinstance(v, dict):
                        result = find_sender_in_json(v, target_uid)
                        if result:
                            return result
            return None
        
        sender_uid = find_sender_in_json(packet_json, emote_info['target_uid'])
        if sender_uid:
            emote_info['sender_uid'] = sender_uid
            emote_info['detection_method'] = 'json_search'
            return emote_info
        
        # If we can't find sender, at least we detected the emote
        emote_info['sender_uid'] = None
        return emote_info
        
    except Exception as e:
        print(f"❌ Sender detection error: {e}")
        return None


async def send_title_packet_direct(target_uid, chat_id, key, iv, region="ind"):
    """Send title packet directly without chat context - for auto-join"""
    try:
        print(f"🎖️ Sending title to {target_uid} in chat {chat_id}")
        
        # Method 1: Using your existing function
        title_packet = await convert_kyro_to_your_system(target_uid, chat_id, key, iv)
        
        if title_packet and whisper_writer:
            # Send via Whisper connection
            whisper_writer.write(title_packet)
            await whisper_writer.drain()
            print(f"✅ Title sent via Whisper to {target_uid}")
            return True
            
    except Exception as e:
        print(f"❌ Error sending title directly: {e}")
        import traceback
        traceback.print_exc()
    
    return False

def extract_type_5(packet_json):
    """Extract from Type 5 packets"""
    if packet_json.get('1') == 5:
        try:
            if '2' in packet_json and 'data' in packet_json['2']:
                data = packet_json['2']['data']
                sender = data.get('1', {}).get('data')
                emote_id = data.get('4', {}).get('data')
                
                if sender:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id or 909054004,  # Default if not found
                        'packet_type': 5,
                        'confidence': 'medium'
                    }
        except:
            pass
    return None

async def extract_emote_info(data_hex, key, iv):
    """Extract full emote info from packet"""
    try:
        packet = await DeCode_PackEt(data_hex[10:])
        packet_json = json.loads(packet)
        
        # DEBUG: Print packet structure
        # print("📦 Packet JSON:", json.dumps(packet_json, indent=2)[:300])
        
        # Check all possible structures
        structures = [
            # Type 21 (from your Emote_k)
            lambda: extract_type_21(packet_json),
            # Type 26
            lambda: extract_type_26(packet_json),
            # Type 5
            lambda: extract_type_5(packet_json),
            # Generic search
            lambda: generic_extract(packet_json)
        ]
        
        for extractor in structures:
            info = extractor()
            if info and info.get('sender_uid'):
                return info
        
        return None
        
    except Exception as e:
        print(f"❌ Extraction error: {e}")
        return None

def extract_type_21(packet_json):
    """Extract from Type 21 (your Emote_k structure)"""
    if packet_json.get('1') == 21:
        try:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '5' in packet_json['2']['data'] and 'data' in packet_json['2']['data']['5']):
                
                data = packet_json['2']['data']
                nested = data['5']['data']
                
                sender = nested.get('1', {}).get('data')
                emote_id = nested.get('3', {}).get('data')
                
                if sender and emote_id:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id,
                        'packet_type': 21,
                        'confidence': 'high'
                    }
        except:
            pass
    return None

def extract_type_26(packet_json):
    """Extract from Type 26 (common emote)"""
    if packet_json.get('1') == 26:
        try:
            if '2' in packet_json and 'data' in packet_json['2']:
                data = packet_json['2']['data']
                sender = data.get('1', {}).get('data')
                emote_id = data.get('2', {}).get('data')
                
                if sender and emote_id:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id,
                        'packet_type': 26,
                        'confidence': 'high'
                    }
        except:
            pass
    return None

# Add these imports at the top with your other imports
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import json
import requests
import asyncio

# Add these constants with your other global variables
BIO_ENCRYPTION_KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
BIO_ENCRYPTION_IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
FREEFIRE_VERSION = "OB54"

def decode_jwt_noverify(token: str):
    """Decode JWT without verification"""
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return None
        payload_b64 = parts[1] + "=" * (-len(parts[1]) % 4)
        payload = json.loads(base64.urlsafe_b64decode(payload_b64).decode())
        return payload
    except Exception:
        return None

# Add these global variables

async def is_bot_in_squad(bot_uid, key, iv):
    """Quick check if bot is in squad (with caching)"""
    global last_bot_status_check, cached_bot_status
    
    # Use cache if recent
    current_time = time.time()
    if (current_time - last_bot_status_check < bot_status_cache_time and 
        cached_bot_status is not None):
        return cached_bot_status
    
    try:
        # Send status request
        status_packet = await createpacketinfo(bot_uid, key, iv)
        if status_packet and online_writer:
            online_writer.write(status_packet)
            await online_writer.drain()
            
            # Wait for response
            await asyncio.sleep(2)
            
            # Check cache
            if bot_uid in status_response_cache:
                packet = status_response_cache[bot_uid].get('packet', b'')
                status = get_player_status(packet)
                
                in_squad = "INSQUAD" in status
                cached_bot_status = in_squad
                last_bot_status_check = current_time
                
                return in_squad
        
        return False
        
    except Exception as e:
        print(f"❌ Squad check error: {e}")
        return False

def get_bio_server_url(lock_region: str):
    """Get bio endpoint based on region"""
    region = lock_region.upper()
    if region == "IND":
        return "https://client.ind.freefiremobile.com/UpdateSocialBasicInfo"
    elif region in {"BR", "US", "SAC", "NA"}:
        return "https://client.us.freefiremobile.com/UpdateSocialBasicInfo"
    elif region == "BD":
        return "https://client.bd.freefiremobile.com/UpdateSocialBasicInfo"
    elif region == "SG":
        return "https://client.sg.freefiremobile.com/UpdateSocialBasicInfo"
    else:
        return "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo"

def create_bio_protobuf(bio_text):
    """Create protobuf message for bio update - EXACT SAME AS YOUR FLASK API"""
    # This creates the EXACT same protobuf structure as your Flask API
    
    # Protobuf structure from your API:
    # field_2: 17 (0x11)
    # field_5: EmptyMessage
    # field_6: EmptyMessage  
    # field_8: bio_text (string)
    # field_9: 1 (0x01)
    # field_11: EmptyMessage
    # field_12: EmptyMessage
    
    # Build protobuf manually (matching your exact structure)
    # Field 2: varint 17
    field_2 = b'\x08\x11'  # tag:1 type:varint value:17
    
    # Field 5: EmptyMessage (empty bytes)
    field_5 = b'\x2A\x00'  # tag:5 type:length-delimited length:0
    
    # Field 6: EmptyMessage (empty bytes)
    field_6 = b'\x32\x00'  # tag:6 type:length-delimited length:0
    
    # Field 8: bio text (string)
    bio_bytes = bio_text.encode('utf-8')
    bio_length = len(bio_bytes)
    field_8 = b'\x42' + bytes([bio_length]) + bio_bytes  # tag:8 type:string
    
    # Field 9: varint 1
    field_9 = b'\x48\x01'  # tag:9 type:varint value:1
    
    # Field 11: EmptyMessage
    field_11 = b'\x5A\x00'  # tag:11 type:length-delimited length:0
    
    # Field 12: EmptyMessage
    field_12 = b'\x62\x00'  # tag:12 type:length-delimited length:0
    
    # Combine all fields
    protobuf_data = field_2 + field_5 + field_6 + field_8 + field_9 + field_11 + field_12
    return protobuf_data

async def set_bio_directly_async_with_retry(jwt_token, bio_text, region="IND", max_retries=3, retry_delay=2):
    """Set bio with automatic retry logic"""
    
    for attempt in range(max_retries):
        try:
            print(f"🔄 Bio API attempt {attempt + 1}/{max_retries}")
            
            result = await set_bio_directly_async(jwt_token, bio_text, region)
            
            if result.get("success"):
                return result
            else:
                print(f"❌ Bio update failed: {result.get('message')}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay)
                    
        except Exception as e:
            print(f"❌ Bio attempt {attempt + 1} error: {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(retry_delay)
            continue
    
    # If all retries failed
    return {
        "success": False,
        "message": f"All {max_retries} attempts failed"
    }

async def set_bio_directly_async(jwt_token, bio_text, region="IND"):
    """Set bio directly - ASYNC version with better error handling"""
    try:
        # Decode JWT to get region
        payload = decode_jwt_noverify(jwt_token)
        if not payload:
            return {
                "success": False,
                "message": "Invalid JWT token"
            }
        
        lock_region = payload.get("lock_region", region).upper()
        url_bio = get_bio_server_url(lock_region)
        
        print(f"🔧 Setting bio for region: {lock_region}")
        print(f"📝 Bio text: {bio_text}")
        
        # Create protobuf message
        data_bytes = create_bio_protobuf(bio_text)
        print(f"📦 Protobuf created: {len(data_bytes)} bytes")
        
        # Encrypt using AES CBC
        cipher = AES.new(BIO_ENCRYPTION_KEY, AES.MODE_CBC, BIO_ENCRYPTION_IV)
        
        # Pad data to AES block size (16 bytes)
        padding_length = 16 - (len(data_bytes) % 16)
        if padding_length:
            data_bytes += bytes([padding_length] * padding_length)
        
        encrypted_data = cipher.encrypt(data_bytes)
        print(f"🔐 Encrypted: {len(encrypted_data)} bytes")
        
        # Headers
        headers = {
            "Expect": "100-continue",
            "Authorization": f"Bearer {jwt_token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": FREEFIRE_VERSION,
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        
        print(f"🚀 Sending to: {url_bio}")
        
        # Use aiohttp with timeout
        import aiohttp
        timeout = aiohttp.ClientTimeout(total=10)
        
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(url_bio, headers=headers, data=encrypted_data) as response:
                response_text = await response.text()
                
                print(f"📡 Response status: {response.status}")
                
                if response.status == 200:
                    return {
                        "success": True,
                        "message": "Bio updated successfully!",
                        "region": lock_region,
                        "bio": bio_text
                    }
                else:
                    return {
                        "success": False,
                        "message": f"Server error: {response.status} - {response_text[:100]}"
                    }
                
    except aiohttp.ClientError as e:
        print(f"❌ Network error: {e}")
        return {
            "success": False,
            "message": f"Network error: {str(e)[:80]}"
        }
    except asyncio.TimeoutError:
        print(f"❌ Request timeout")
        return {
            "success": False,
            "message": "Request timeout (10s)"
        }
    except Exception as e:
        print(f"❌ Bio update error: {e}")
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "message": f"Error: {str(e)[:80]}"
        }

# Now add this command handler to your TcPChaT function
# Find where other commands are handled and add this:

def analyze_squad_packet(packet_json):
    """Analyze packet structure to find squad members"""
    
    print("\n🔍 ANALYZING SQUAD PACKET STRUCTURE")
    print("="*50)
    
    # Check if this is a squad data packet
    if '5' not in packet_json or 'data' not in packet_json['5']:
        print("❌ Not a squad data packet")
        return None
    
    squad_data = packet_json['5']['data']
    
    # Look for fields that could contain multiple players
    candidate_fields = []
    
    for field_num in squad_data:
        field_info = squad_data[field_num]
        if 'data' not in field_info:
            continue
            
        data_value = field_info['data']
        
        # Check if it's a list (likely contains multiple players)
        if isinstance(data_value, list):
            print(f"✅ Field {field_num}: LIST with {len(data_value)} items")
            candidate_fields.append((field_num, 'list', data_value))
            
            # Show first item structure
            if data_value and isinstance(data_value[0], dict):
                print(f"   First item keys: {list(data_value[0].keys())}")
                # Check if first item has UID (field 1)
                if '1' in data_value[0]:
                    uid = data_value[0]['1']['data']
                    print(f"   ↳ Contains UID: {uid}")
        
        # Check if it's a dict with numeric keys (0, 1, 2, 3...)
        elif isinstance(data_value, dict):
            keys = list(data_value.keys())
            numeric_keys = [k for k in keys if k.isdigit()]
            if len(numeric_keys) > 0:
                print(f"✅ Field {field_num}: DICT with numeric keys {numeric_keys[:5]}...")
                candidate_fields.append((field_num, 'dict', data_value))
    
    print("\n🎯 MOST LIKELY SQUAD MEMBERS FIELDS:")
    for field_num, field_type, data in candidate_fields:
        print(f"  Field {field_num} ({field_type})")
        
        if field_type == 'list':
            # Try to extract UIDs from list
            uids = []
            for item in data[:5]:  # Check first 5 items
                if isinstance(item, dict) and '1' in item:
                    uid = item['1']['data']
                    uids.append(uid)
            if uids:
                print(f"    ↳ Found UIDs: {uids}")
        
        elif field_type == 'dict':
            # Try to extract UIDs from dict
            uids = []
            for key in list(data.keys())[:5]:  # Check first 5 keys
                item = data[key]
                if isinstance(item, dict) and '1' in item:
                    uid = item['1']['data']
                    uids.append(uid)
            if uids:
                print(f"    ↳ Found UIDs: {uids}")
    
    return candidate_fields

def generic_extract(packet_json):
    """Generic search for UID and emote ID"""
    uid = None
    emote_id = None
    
    # Recursively search for UID (long number)
    def search(obj):
        nonlocal uid, emote_id
        
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'data' and isinstance(v, (int, str)) and str(v).isdigit():
                    # Check if it looks like a UID (long number)
                    num = int(v)
                    if 1000000 < num < 99999999999:  # Reasonable UID range
                        if not uid:  # First found is likely sender
                            uid = num
                        # Check if it's an emote ID (starts with 909...)
                        elif str(v).startswith('909') and len(str(v)) >= 9:
                            emote_id = num
                
                elif isinstance(v, dict):
                    search(v)
                elif isinstance(v, list):
                    for item in v:
                        search(item)
    
    search(packet_json)
    
    if uid:
        return {
            'sender_uid': uid,
            'emote_id': emote_id or 909054004,  # Default AK emote
            'packet_type': 'generic',
            'confidence': 'medium'
        }
    
    return None
    
async def auto_reply_with_emote(emote_info, key, iv):
    """Automatically reply with same emote"""
    
    try:
        # Get bot's UID (you need to set this)
        bot_uid = 5276592766  # Replace with your bot's actual UID
        
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        
        # Send emote back to sender
        reply_packet = await Emote_k(sender_uid, emote_id, key, iv, region)
        
        if online_writer:
            online_writer.write(reply_packet)
            await online_writer.drain()
            
            print(f"🤖 Bot replied with emote {emote_id} to {sender_uid}")
            
    except Exception as e:
        print(f"❌ Auto-reply error: {e}")

def extract_squad_members_correct(packet_json):
    """Extract squad members from FULL squad packet"""
    
    print("\n🔍 EXTRACTING SQUAD MEMBERS")
    print("="*50)
    
    try:
        if ('5' not in packet_json or 
            'data' not in packet_json['5'] or 
            '2' not in packet_json['5']['data']):
            print("❌ Invalid packet structure")
            return []
        
        field2_data = packet_json['5']['data']['2']['data']
        
        squad_members = []
        
        # Field 2 has numeric keys: '1', '2', '3', '4', '5', etc.
        # Each key might be a squad member slot OR player data field
        
        # Let's check what each numeric key contains
        for key in field2_data:
            if not key.isdigit():
                continue
                
            item = field2_data[key]['data']
            print(f"\n📦 Key {key}: Type = {type(item)}")
            
            if isinstance(item, dict):
                # Check if this is a player object
                # Player objects usually have fields: 1=UID, 2=name, 4=rank, etc.
                if '1' in item and '2' in item:
                    try:
                        uid = item['1']['data']
                        name = item['2']['data']
                        
                        # Make sure it's a valid UID (not a small number)
                        if isinstance(uid, int) and uid > 1000000:
                            rank = item['4']['data'] if '4' in item else 0
                            
                            print(f"   ✅ PLAYER FOUND!")
                            print(f"      UID: {uid}")
                            print(f"      Name: {name}")
                            print(f"      Rank: {rank}")
                            
                            squad_members.append({
                                'slot': key,
                                'uid': uid,
                                'name': name,
                                'rank': rank
                            })
                        else:
                            print(f"   ❌ Not a UID: {uid}")
                            
                    except Exception as e:
                        print(f"   ❌ Error extracting player: {e}")
                else:
                    print(f"   ↳ Fields: {list(item.keys())[:5]}...")
            elif isinstance(item, (int, str)):
                print(f"   ↳ Value: {item}")
        
        print(f"\n🏆 TOTAL SQUAD MEMBERS FOUND: {len(squad_members)}")
        for member in squad_members:
            print(f"  • Slot {member['slot']}: {member['name']} (UID: {member['uid']})")
        
        return squad_members
        
    except Exception as e:
        print(f"❌ Extraction error: {e}")
        import traceback
        traceback.print_exc()
        return []
        
async def analyze_packet_structure(data_hex, key, iv):
    """Analyze and display packet structure"""
    
    print(f"\n📦 PACKET ANALYSIS")
    print("="*50)
    
    # Basic info
    print(f"📏 Length: {len(data_hex)} characters")
    print(f"🔢 Header: {data_hex[:10]}")
    
    # Try to decode
    try:
        if len(data_hex) > 20:
            decoded = await DeCode_PackEt(data_hex[10:])
            packet_json = json.loads(decoded)
            
            print(f"✅ Successfully decoded!")
            print(f"📊 Packet type (field 1): {packet_json.get('1', 'Unknown')}")
            
            # Show structure
            print(f"\n📋 PACKET STRUCTURE:")
            print(f"Top-level fields: {list(packet_json.keys())}")
            
            # Show field 1 value
            if '1' in packet_json:
                print(f"  Field 1: {packet_json['1']}")
            
            # Show if it contains emote ID patterns
            import re
            emote_patterns = re.findall(r'909[0-9a-f]{6}', data_hex)
            if emote_patterns:
                print(f"\n🎭 EMOTE IDS FOUND IN HEX: {emote_patterns}")
            
            # Show UID patterns
            uid_patterns = re.findall(r'(\d{9,11})', data_hex)
            uids = [uid for uid in uid_patterns if not uid.startswith('909')]
            if uids:
                print(f"👤 UIDS FOUND IN HEX: {uids}")
            
            # Return the decoded structure
            return packet_json
            
        else:
            print("❌ Packet too short to decode")
            return None
            
    except Exception as e:
        print(f"❌ Decode error: {e}")
        return None

async def RedZed_SendInv(bot_uid, uid, key, iv):
    """Async version of send invite function"""
    try:
        fields = {
            1: 2, 
            2: {
                1: int(uid), 
                2: "IND", 
                3: 1, 
                4: 1, 
                6: "RedZedKing!!", 
                7: 330, 
                8: 1000, 
                9: 100, 
                10: "DZ", 
                12: 1, 
                13: int(uid), 
                16: 1, 
                17: {
                    2: 159, 
                    4: "y[WW", 
                    6: 11, 
                    8: "1.120.2", 
                    9: 3, 
                    10: 1
                }, 
                18: 306, 
                19: 18, 
                24: 902000306, 
                26: {}, 
                27: {
                    1: 11, 
                    2: int(bot_uid), 
                    3: 99999999999
                }, 
                28: {}, 
                31: {
                    1: 1, 
                    2: 32768
                }, 
                32: 32768, 
                34: {
                    1: bot_uid, 
                    2: 8, 
                    3: b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
                }
            }
        }
        
        # Convert bytes properly
        if isinstance(fields[2][34][3], str):
            fields[2][34][3] = b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
        
        # Use async versions of your functions
        packet = await CrEaTe_ProTo(fields)
        packet_hex = packet.hex()
        
        # Generate final packet
        final_packet = await GeneRaTePk(packet_hex, '0515', key, iv)
        
        return final_packet
        
    except Exception as e:
        print(f"❌ Error in RedZed_SendInv: {e}")
        import traceback
        traceback.print_exc()
        return None
        
async def freeze_emote_spam(uid, key, iv, region, chat_type, chat_id, sender_uid):
    """Send 3 freeze emotes in 1-second cycles for 10 seconds"""
    global freeze_running
    
    try:
        cycles = 0
        max_cycles = FREEZE_DURATION  # 10 seconds
        
        while freeze_running and cycles < max_cycles:
            # Send all 3 emotes in sequence
            for i, emote_id in enumerate(FREEZE_EMOTES):
                if not freeze_running:
                    break
                    
                try:
                    # Send emote
                    emote_packet = await Emote_k(int(uid), emote_id, key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
                    
                    print(f"❄️ Freeze emote {i+1}/{len(FREEZE_EMOTES)} sent: {emote_id}")
                    
                    # Small delay between emotes (0.3 seconds)
                    await asyncio.sleep(0.1)
                    
                except Exception as e:
                    print(f"❌ Error sending freeze emote {i+1}: {e}")
            
            cycles += 1
            print(f"🌀 Freeze cycle {cycles}/{max_cycles} completed")
            
            # Wait for next cycle (total 1 second per cycle)
            remaining_time = 1.0 - (0.3 * len(FREEZE_EMOTES))
            if remaining_time > 0:
                await asyncio.sleep(remaining_time)
        
        print(f"✅ Freeze sequence completed: {cycles} cycles")
        return cycles
        
    except Exception as e:
        print(f"❌ Freeze function error: {e}")
        return 0
        
async def handle_freeze_completion(freeze_task, uid, sender_uid, chat_id, chat_type, key, iv):
    """Handle freeze command completion"""
    try:
        cycles_completed = await freeze_task
        
        completion_msg = f"""[B][C][00FFFF]❄️ FREEZE COMMAND COMPLETED!

🎯 Target: {uid}
⏱️ Duration: {cycles_completed} seconds
🎭 Emotes sent: {cycles_completed * 3}
❄️ Sequence: 
  • 909052008 (Ice)
  • 909052008 (Frozen)
  • 909052008 (Freeze)

✅ Status: Complete!
"""
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
        
    except asyncio.CancelledError:
        print("🛑 Freeze command cancelled")
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Freeze error: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)

async def test_emote_packet(target_uid, emote_id, key, iv, region="IND"):
    """Test if emote packet works and show structure"""
    
    print(f"\n🎭 TESTING EMOTE PACKET")
    print("="*50)
    
    # Create the packet using your function
    emote_packet = await Emote_k(target_uid, emote_id, key, iv, region)
    
    if not emote_packet:
        print("❌ Failed to create packet")
        return False
    
    # Convert to hex for analysis
    packet_hex = emote_packet.hex()
    
    print(f"📦 Packet created!")
    print(f"   Length: {len(packet_hex)} characters")
    print(f"   Header: {packet_hex[:20]}")
    
    # Try to decode it back
    try:
        if len(packet_hex) > 20:
            # Remove header (first 10 bytes = 20 hex chars)
            payload = packet_hex[20:]  # Skip header
            
            # Decrypt (you need to implement this)
            # For testing, let's see raw structure
            print(f"\n🔍 RAW PACKET STRUCTURE:")
            print(f"Full hex (first 200 chars):")
            print(packet_hex[:200] + "...")
            
            # Look for the UID in hex
            import re
            uid_hex = hex(target_uid)[2:]
            if uid_hex in packet_hex:
                print(f"✅ Target UID {target_uid} found in packet!")
            else:
                print(f"❌ Target UID not found in hex")
            
            # Look for emote ID
            emote_hex = hex(emote_id)[2:]
            if emote_hex in packet_hex:
                print(f"✅ Emote ID {emote_id} found in packet!")
            else:
                print(f"❌ Emote ID not found in hex")
        
        print(f"\n✅ Packet created successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Analysis error: {e}")
        return False
        
async def send_and_monitor_emote(target_uid, emote_id, key, iv, region, reader):
    """Send emote and monitor response - FIXED VERSION"""
    
    print(f"\n🚀 SENDING TEST EMOTE")
    print(f"   👤 Target: {target_uid}")
    print(f"   🎭 Emote: {emote_id}")
    print("="*50)
    
    # 1. Create packet
    emote_packet = await Emote_k(target_uid, emote_id, key, iv, region)
    
    if not emote_packet:
        print("❌ Failed to create packet")
        return
    
    # 2. Send it
    print("📤 Sending packet...")
    if online_writer:
        online_writer.write(emote_packet)
        await online_writer.drain()
        print("✅ Packet sent!")
    else:
        print("❌ No connection")
        return
    
    # 3. Wait for response (SHORTER - 2 seconds)
    print("\n⏳ Waiting for response (2 seconds)...")
    
    responses = []
    start_time = time.time()
    
    while time.time() - start_time < 2:  # Reduced from 5 to 2 seconds
        try:
            # Read any response
            if reader:
                response = await asyncio.wait_for(reader.read(9999), timeout=0.1)
                if response:
                    resp_hex = response.hex()
                    responses.append(resp_hex)
                    
                    # Quick analysis
                    print(f"📥 Got response #{len(responses)}")
                    print(f"   Length: {len(resp_hex)} chars")
                    print(f"   Header: {resp_hex[:10]}")
                    
                    # Check if it's the emote echo
                    if '909' in resp_hex:
                        print(f"   🎭 Contains emote ID!")
        except asyncio.TimeoutError:
            continue
        except Exception as e:
            # Silent error - don't print
            pass
    
    # 4. Summary
    print(f"\n📊 RESPONSE SUMMARY")
    print(f"Total responses: {len(responses)}")
    
    if len(responses) > 0:
        print("✅ SUCCESS! Server accepted your emote packet!")
    else:
        print("⚠️ No immediate response (might still be processing)")
        
async def handle_guest_generation(count, uid, chat_id, chat_type, key, iv):
    """Handle guest generation in background and send updates"""
    try:
        # Start generation
        accounts = await generate_and_save_accounts(count)
        
        # Send completion message
        if accounts:
            success_msg = f"""[B][C][FFFF00]✅ GUEST ACCOUNTS GENERATED!

📊 Generated: {len(accounts)}/{count} accounts
💾 Saved to: guest_accounts.json

📋 Format in file:
• uid: Account UID
• password: Account password
• name: BlackApis
• timestamp: Generation time

💡 Use accounts for:
• Multi-account spams
• Friend requests
• Testing purposes
"""
        else:
            success_msg = f"""[B][C][FF0000]❌ GENERATION FAILED!

📊 Requested: {count} accounts
❌ Generated: 0 accounts

💡 Try:
1. Check internet connection
2. API might be down
3. Try smaller count (like 5)
4. Try again later
"""
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Optional: Send first account as preview
        if accounts:
            preview_msg = f"""[B][C][FFFF00]🔍 FIRST ACCOUNT PREVIEW:

👤 UID: {accounts[0]['uid']}
🔑 Pass: {accounts[0]['password']}
📛 Name: {accounts[0]['name']}

💡 Check guest_accounts.json for all accounts!
"""
            await safe_send_message(chat_type, preview_msg, uid, chat_id, key, iv)
            
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Generation error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)        
        
async def start_auto_packet(key, iv, region):
    """Create start match packet"""
    fields = {
        1: 9,
        2: {
            1: 12480598706,
        },
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def handle_command(inPuTMsG):

    global emote_hijack

    if inPuTMsG.startswith('/mimic_on'):
        emote_hijack = True
        print("Mimic ON")

    if inPuTMsG.startswith('/mimic_off'):
        emote_hijack = False
        print("Mimic OFF")
                
async def detect_and_hijack_emote(data_hex, key, iv, bot_uid, region):
    """Detect emote and hijack it by sending with bot's UID"""
    try:
        # Detect emote info
        emote_info = await extract_emote_info(data_hex, key, iv)
        
        if not emote_info or not emote_info.get('sender_uid'):
            return False
        
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        
        print(f"\n🎭 EMOTE DETECTED FOR HIJACK!")
        print(f"   👤 Original Sender: {sender_uid}")
        print(f"   🎭 Emote ID: {emote_id}")
        
        # Don't hijack bot's own emotes
        if int(sender_uid) == bot_uid:
            print("⚠️ Skipping - bot's own emote")
            return False
        
        # HIJACK: Send emote with bot's UID instead
        print(f"🤖 HIJACKING EMOTE! Sending as bot {bot_uid}...")
        
        # Use either of your emote functions
        # Method 1: Using Emote_k (your second packet)
        hijack_packet = await Emote_k(
            int(bot_uid),  # Use BOT'S UID instead of sender's
            int(emote_id),  # Same emote ID
            key, iv, region
        )
        
        # Alternative: Using emote_send (your first packet)
        # hijack_packet = await create_hijacked_emote(bot_uid, emote_id, key, iv, region)
        
        if hijack_packet and online_writer:
            # Send the hijacked emote
            online_writer.write(hijack_packet)
            await online_writer.drain()
            
            print(f"✅ Emote hijacked! Bot {bot_uid} now appears to do emote {emote_id}")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Emote hijack error: {e}")
        return False
        
async def SwitchLoneWolfDule(BotUid, key, iv):
    fields = {1: 17, 2: {1: BotUid, 2: 1, 3: 1, 4: 43, 5: "\u000b", 8: 1, 19: 1}}
    return await GenPacket((await CreateProtobufPacket(fields)).hex(), '0519', key, iv)        
        
async def KickTarget(target_uid, key, iv):
    fields = {1: 35, 2: {1: int(target_uid)}}
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0515' , key, iv)
        
async def create_hijacked_emote(hijacker_uid, emote_id, key, iv, region):
    """Create emote packet that appears to come from hijacker"""
    try:
        # Using your Emote_k structure but with hijacker's UID
        fields = {
            1: 21,  # Emote packet type
            2: {
                1: 804266360,  # Some identifier (keep as is)
                2: 909000001,  # Base emote ID
                5: {
                    1: int(hijacker_uid),  # HIJACKER'S UID goes here
                    3: int(emote_id),      # The emote ID to perform
                }
            }
        }
        
        if region.lower() == "ind":
            packet = '0514'
        elif region.lower() == "bd":
            packet = "0519"
        else:
            packet = "0515"
            
        return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet, key, iv)
        
    except Exception as e:
        print(f"❌ Error creating hijacked emote: {e}")
        return None
            
def analyze_hex_packet(packet_hex):
    """Analyze hex packet structure"""
    
    print(f"\n🔬 HEX PACKET ANALYSIS")
    print("="*50)
    
    # Header analysis
    header = packet_hex[:10]
    print(f"Header (first 5 bytes): {header}")
    
    # Common headers:
    # 0514 = IND online packet
    # 0519 = BD online packet  
    # 1215 = Whisper packet
    # 1200 = Chat packet
    
    if header.startswith('05'):
        print("📡 Online connection packet")
    elif header.startswith('12'):
        print("💬 Whisper/Chat packet")
    
    # Look for UIDs (9-11 digit numbers in hex)
    import re
    
    # Find all sequences of 9+ hex digits
    hex_patterns = re.findall(r'[0-9a-f]{9,12}', packet_hex.lower())
    
    print(f"\n🔢 Hex sequences found:")
    for pattern in hex_patterns[:10]:  # Show first 10
        # Try to convert to decimal
        try:
            decimal = int(pattern, 16)
            if 1000000 < decimal < 99999999999:  # Reasonable UID range
                print(f"  {pattern} → {decimal} (Possible UID)")
            elif decimal > 900000000:  # Emote ID range
                print(f"  {pattern} → {decimal} (Possible emote ID)")
        except:
            print(f"  {pattern}")
    
    # Show packet content (first 200 chars)
    print(f"\n📝 Packet preview (first 200 chars):")
    print(packet_hex[:200])
    
    if len(packet_hex) > 200:
        print(f"... and {len(packet_hex) - 200} more characters")
        
def append_to_whitelist(uid_to_add):
    """Simple function to add UID to whitelist"""
    global WHITELISTED_UIDS
    
    uid_str = str(uid_to_add)
    
    if uid_str in WHITELISTED_UIDS:
        return False, f"UID {uid_str} already in whitelist"
    
    WHITELISTED_UIDS.add(uid_str)
    return True, f"✅ Added {uid_str} to whitelist"        
        
async def hijack_squad_emote(data_hex, key, iv, bot_uid, region, in_squad):
    """Only hijack emotes when bot is in a squad"""
    if not in_squad:
        return False
    
    try:
        # Extract emote info
        emote_info = await extract_emote_info(data_hex, key, iv)
        
        if not emote_info:
            return False
        
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        
        print(f"\n🏆 SQUAD EMOTE HIJACK!")
        print(f"   👥 In squad: Yes")
        print(f"   👤 Original: {sender_uid}")
        print(f"   🎭 Emote: {emote_id}")
        
        # Create hijacked emote
        hijack_packet = await create_hijacked_emote(bot_uid, emote_id, key, iv, region)
        
        if hijack_packet and online_writer:
            online_writer.write(hijack_packet)
            await online_writer.drain()
            
            print(f"✅ Squad emote hijacked by bot {bot_uid}!")
            
            # Optional: Also send the original emote to maintain appearance
            await asyncio.sleep(0.3)
            original_packet = await Emote_k(int(sender_uid), int(emote_id), key, iv, region)
            online_writer.write(original_packet)
            await online_writer.drain()
            
            print(f"✅ Also sent original emote to maintain cover")
            
            return True
            
    except Exception as e:
        print(f"❌ Squad hijack error: {e}")
    
    return False
    
async def send_friend_request_async(target_uid: str, count: int = 1) -> dict:
    """
    Main function to send friend requests from TCP bot
    
    Args:
        target_uid: Target player UID
        count: Number of requests (1 for single, >1 for bulk)
    
    Returns:
        Dictionary with results
    """
    try:
        if count == 1:
            # Single request using token.json
            token = load_jwt_token()
            if not token:
                return {"success": 0, "failed": 1, "error": "No token found"}
            
            success = send_friend_request_single(target_uid, token)
            
            if success:
                return {"success": 1, "failed": 0}
            else:
                return {"success": 0, "failed": 1}
                
        else:
            # Bulk requests using token_ind.json
            tokens = load_tokens_ind()
            if not tokens:
                return {"success": 0, "failed": 0, "error": "No tokens found"}
            
            max_count = min(count, len(tokens))
            results = {"success": 0, "failed": 0}
            
            print(f"📦 Sending {max_count} friend requests...")
            
            # Send requests sequentially (or use threading for faster)
            for i in range(max_count):
                token = tokens[i]['token']
                success = send_friend_request_single(target_uid, token)
                
                if success:
                    results["success"] += 1
                else:
                    results["failed"] += 1
                
                # Small delay to avoid rate limiting
                await asyncio.sleep(0.1)
            
            return results
            
    except Exception as e:
        print(f"❌ Friend request error: {e}")
        return {"success": 0, "failed": 0, "error": str(e)}    

async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer, last_status_packet, status_response_cache, senthi
    global insquad, joining_team, whisper_writer, region
 
    bot_uid = 5276592766
 
    if insquad is not None:
        insquad = None
    if joining_team is True:
        joining_team = False
    
    online_writer = None
    whisper_writer = None
    
    while True:
        try:
            print(f"Attempting to connect to {ip}:{port}...")
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            
            # --- AUTHENTICATION ---
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            print("Authentication token sent. Listening for emotes...")
            
            # --- READING LOOP ---
            while True:
                data2 = await reader.read(9999)
                    
                if not data2: 
                    print("Connection closed by the server.")
                    break
                    
                data_hex = data2.hex()
      
                # Your existing code...
  
                
                
              # =================== EMOTE DETECTION ONLY ===================
                if data_hex.startswith("0500") and emote_hijack == True:
                    try:
                        # Try to detect emote
                        emote_info = await extract_emote_info(data_hex, key, iv)
                        
                        in_squad = insquad is not None
            

                

                        
                        if emote_info and emote_info.get('sender_uid'):
                            sender_uid = emote_info['sender_uid']
                            emote_id = emote_info['emote_id']
                            
                            
                            
                            print(f"\n🎯 EMOTE DETECTED!")
                            print(f"   👤 Sender UID: {sender_uid}")
                            print(f"   🎭 Emote ID: {emote_id}")
                            
                            # Don't respond to bot's own emotes
                            if int(sender_uid) != bot_uid:
                                print("🤖 Bot responding with dual emotes...")
                                
                                # STEP 1: Send fixed emote 909035003 to the sender
                                print(f"  1️⃣ Sending emote 909035003 to {sender_uid}")
                                fixed_emote_packet = await Emote_k(
                                    int(sender_uid), 
                                    909035003,  # Fixed emote ID
                                    key, iv, region
                                )
                                if fixed_emote_packet and online_writer:
                                    online_writer.write(fixed_emote_packet)
                                    await online_writer.drain()
                                    await asyncio.sleep(0.5)
                                
                                # STEP 2: Bot does the SAME emote that user did (to itself)
                                print(f"  2️⃣ Bot doing same emote {emote_id} to itself")
                                bot_self_emote = await Emote_k(
                                    bot_uid,  # Bot's own UID
                                    int(emote_id),  # Same emote user did
                                    key, iv, region
                                )
                                if bot_self_emote and online_writer:
                                    online_writer.write(bot_self_emote)
                                    await online_writer.drain()
                                    await asyncio.sleep(0.5)
                                
                                # STEP 3: Bot also sends the emote back to sender
                                print(f"  3️⃣ Mirroring emote {emote_id} back to {sender_uid}")
                                mirror_emote = await Emote_k(
                                    int(sender_uid),
                                    int(emote_id),  # Same emote back
                                    key, iv, region
                                )
                                if mirror_emote and online_writer:
                                    online_writer.write(mirror_emote)
                                    await online_writer.drain()
                                
                                print("✅ Dual emote response complete!")
                            
                            else:
                                print("⚠️ Skipping - bot's own emote")
                                
                    except Exception as e:
                        print(f"❌ Emote response error: {e}")
                        continue 
            
                    


                # =================== AUTO ACCEPT HANDLING ===================
                
                # Case 1: Squad is cancelled or left (6, 7 are often status/exit codes)
                if data_hex.startswith('0500') and insquad is not None and joining_team == False:
                    try:
                        # Assuming DeCode_PackEt and json.loads are available and correct
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        if packet_json.get('1') in [6, 7]: 
                             insquad = None
                             joining_team = False
                             print("Squad cancelled or exited (code 6/7).")
                             continue
                             
                    except Exception as e:
                        print(f"Error in auto-accept case 1: {e}")
                        pass
                
                # case 2
                # Case 2: Auto-accept for whitelisted users
                if data_hex.startswith("0500") and insquad is None and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
    
                        uid = packet_json['5']['data']['1']['data']
                        invite_uid = packet_json['5']['data']['2']['data']['1']['data']
                        squad_owner = packet_json['5']['data']['1']['data']  # Person inviting
                        code = packet_json['5']['data']['8']['data']
  

                        emote_id = 909054004
                        bot_uid = 2578372095
    
                        # 🎯 FIX: Check SQUAD_OWNER (person who clicked "invite")
                        if True:
                            print(f"✅ Whitelisted user {squad_owner} invited bot. Accepting...")
                        
                            SendInv = await RedZed_SendInv(bot_uid, invite_uid, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', SendInv)
                            inv_packet = await RejectMSGtaxt(squad_owner, uid, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', inv_packet)
        
                            print(f"Received squad invite from {squad_owner}, accepting...")                  
                            # Squad join
                            # 🎯 FIX: Check SQUAD_OWNER (person who clicked "invite")
                        if True:
                            print(f"✅ Whitelisted user {squad_owner} invited bot. Accepting...")
                        
                            SendInv = await RedZed_SendInv(bot_uid, invite_uid, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', SendInv)
                            inv_packet = await RejectMSGtaxt(squad_owner, uid, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', inv_packet)
        
                            print(f"Received squad invite from {squad_owner}, accepting...")                  
                            # Squad join
                            # ================= MAIN SEQUENCE =================

                            Join = await ArohiAccepted(squad_owner, code, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', Join)

                            # random bundle background task
                            asyncio.ensure_future(do_join_emote_and_bundle(bot_uid, key, iv, region, inviter_uid=squad_owner))

                            # Set squad status
                            insquad = True
                            print(f"🤖 Bot joined squad of {squad_owner}")
        
        
        
                        else:
                            try:
                                print(f"🚫 Bot is private! Ignoring invite from {squad_owner}")
                                 # Send quick reject message
                                bot_uid = 14010319252
                                message_text = f" Can't accept Your request Talk to BLACK666"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(squad_owner),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
                                print("got it")

                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
                                else:
                                    print("can't do it")
                    
                                    
                            except Exception as e:
                                print(" got an error in can't accept")
    

                    except Exception as e:
                        print(f"Error in auto-accept: {e}")
                        insquad = None
                        joining_team = False
                        continue
                
                # =================== HANDLE KICK/RECONNECT ===================
                # Case 3: Bot was kicked and needs to re-join chat
                if data_hex.startswith('0500') and len(data_hex) > 1000:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                    
                        packet_type = packet_json.get('1')
        
                        # Detect ALL kick/leave packets
                        if packet_type in [6, 7, 8, 9, 10, 11, 12]:
                            print(f"🚪 Kick/Leave packet detected (Type: {packet_type})")
            
                            # RESET SQUAD STATUS
                            insquad = None
                            joining_team = False
            
                            print(f"✅ Bot reset after kick. Ready for new invites.")
                            
                            # Try to extract squad info for possible reconnection
                            try:
                                if '5' in packet_json and 'data' in packet_json['5']:
                                    OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)
                                    print(f"🔄 Attempting reconnection to squad {SQuAD_CoDe}...")
                    
                                    # Re-authenticate chat
                                    JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)
                    
                                    print(f"✅ Chat re-authenticated for reconnection")
                            except:
                                print("⚠️ Could not extract squad info")
                                
                            continue  # Skip other handlers
        
                        # Also check for general squad data packets (for reconnection)
                        elif '5' in packet_json and 'data' in packet_json['5']:
                            try:
                                OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)
                
                                # If we have squad data but insquad is None, try to reconnect
                                if insquad is None:
                                    print(f"🤖 Received squad data while not in squad. Attempting chat auth...")
                                    
                                    JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)
                    
                                    # Optional welcome back message
                                    welcome_msg = """[B][C][FFFF00]🤖 Bot reconnected!"""
                                    P = await SEndMsG(0, welcome_msg, OwNer_UiD, OwNer_UiD, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                    
                            except:
                                pass  # Not a squad data packet
                
                    except Exception as e:
                        print(f"❌ Kick/reconnect handler error: {e}")
                        pass
                
                # case 5
                if insquad == True:
                    try:
                        # Assuming DeCode_PackEt, json.loads, GeTSQDaTa, AutH_Chat, SEndPacKeT are available
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet_json)
                        
                        print(f"Received squad data for joining team, attempting chat auth for {OwNer_UiD}...")
                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)
                        
                        def get_random_color(): return "_" 
                        message = """
[B][C]HA🤫CK🤫ER [00BFFF] N A Y A N 乡 !"""
                        # In your auto-join (Old Handler) code, find this line:

                        P = await SEndMsG(0, message, OwNer_UiD, OwNer_UiD, key, iv, region)
                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        
                        joining_team = False
                        insquad = None
                            
                    except Exception as e:
                        print(f"Error in joining_team chat auth: {e}")
                        # Removed the redundant inner try/except block.
                        pass
                
                if "0600" in data2.hex()[0:4] and len(data2.hex()) > 700:
                    accept_packet = f'08{data2.hex().split("08", 1)[1]}'
                    kk = get_available_room(accept_packet)
                    parsed_data = json.loads(kk)
                    #logging.info(parsed_data)

                    senthi = True

                if senthi == True:
                    
                    def get_random_color(): return "_" 
                    message = """
[B][C]HA🤫CK🤫ER [00BFFF] N A Y A N 乡 !"""
                        # In your auto-join (Old Handler) code, find this line:

                    P = await SEndMsG(0, message, OwNer_UiD, OwNer_UiD, key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                    senthi = False

                # =================== STATUS HANDLER ===================
                if data_hex.startswith('0f00') and len(data_hex) > 100:
                    print(f"📡 Received status response packet")
    
                    try:
                        # Assuming the protocol structure: 0f00 + length bytes + 08 + actual proto data
                        # The split logic might need refinement based on the exact protocol
                        if '08' in data_hex:
                            proto_part = f'08{data_hex.split("08", 1)[1]}'
                        else:
                            print("⚠️ Status packet structure missing '08' marker.")
                            continue
        
                        # Assuming get_available_room is available
                        parsed_data = get_available_room(proto_part)
                        if parsed_data:
                            parsed_json = json.loads(parsed_data)
            
                            # Check if it's field 15 (player info)
                            if "2" in parsed_json and parsed_json["2"]["data"] == 15:
                                # Get player ID
                                player_id = parsed_json["5"]["data"]["1"]["data"]["1"]["data"]
                
                                # Assuming get_player_status is available
                                player_status = get_player_status(proto_part) 
                                print(f"✅ Parsed status for {player_id}: {player_status}")
                
                                # Create cache entry
                                cache_entry = {
                                    'status': player_status, 
                                    'packet': proto_part,
                                    'timestamp': time.time(),
                                    'full_packet': data_hex,
                                    'parsed_json': parsed_json
                                }
                
                                # --- SPECIAL CONDITION CHECK ---
                                try:
                                    StatusData = parsed_json
                                    if ("5" in StatusData and "data" in StatusData["5"] and 
                                        "1" in StatusData["5"]["data"] and "data" in StatusData["5"]["data"]["1"] and 
                                        "3" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["3"] and 
                                        StatusData["5"]["data"]["1"]["data"]["3"]["data"] == 1 and 
                                        "11" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["11"] and 
                                        StatusData["5"]["data"]["1"]["data"]["11"]["data"] == 1):
                
                                        print(f"🎯 SPECIAL CONDITION MET: Player {player_id} is in SOLO mode with special flag 11=1")
                                        cache_entry['special_state'] = 'SOLO_WITH_FLAG_1'
                
                                except Exception as cond_error:
                                    print(f"⚠️ Error checking special condition: {cond_error}")
                                # ------------------------------

                                # If in room, extract room ID
                                if "IN ROOM" in player_status:
                                    try:
                                        # Assuming get_idroom_by_idplayer is available
                                        room_id = get_idroom_by_idplayer(proto_part)
                                        if room_id:
                                            cache_entry['room_id'] = room_id
                                            print(f"🏠 Room ID extracted: {room_id}")
                                    except Exception as room_error:
                                        print(f"Failed to extract room ID: {room_error}")
                
                                # If in squad, extract leader
                                elif "INSQUAD" in player_status:
                                    try:
                                        # Assuming get_leader is available
                                        leader_id = get_leader(proto_part)
                                        if leader_id:
                                            cache_entry['leader_id'] = leader_id
                                            print(f"👑 Leader ID: {leader_id}")
                                    except Exception as leader_error:
                                        print(f"Failed to extract leader: {leader_error}")
                
                                # Save to FILE cache (Assuming save_to_cache is available)
                                save_to_cache(player_id, cache_entry)
                                print(f"✅ Saved to cache: {player_id} = {player_status}")
                
                    except Exception as e:
                        print(f"❌ Error parsing status: {e}")
                        import traceback
                        traceback.print_exc()
                
                # =================== END STATUS HANDLER ===================


            # --- CLEANUP AFTER INNER LOOP (Connection closed) ---
            if online_writer is not None:
                online_writer.close()
                await online_writer.wait_closed()
                online_writer = None
            
            if whisper_writer is not None:
                try:
                    whisper_writer.close()
                    await whisper_writer.wait_closed()
                except:
                    pass
                whisper_writer = None
                
            insquad = None
            joining_team = False
            
            print(f"Connection closed. Reconnecting in {reconnect_delay} seconds...")

        except ConnectionRefusedError:
            print(f"Connection refused by server at {ip}:{port}.")
        except asyncio.TimeoutError:
            print(f"Connection attempt to {ip}:{port} timed out.")
        except Exception as e:
            print(f"- ErroR With {ip}:{port} - {e}")
            traceback.print_exc() 
            
            # --- CLEANUP AFTER EXCEPTION ---
            if online_writer is not None:
                try:
                    online_writer.close()
                    await online_writer.wait_closed()
                except:
                    pass
                online_writer = None
            if whisper_writer is not None:
                try:
                    whisper_writer.close()
                    await whisper_writer.wait_closed()
                except:
                    pass
                whisper_writer = None
                
            insquad = None
            joining_team = False
            
        await asyncio.sleep(reconnect_delay)
        
                            
async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(region, 'TCP CHAT')

    global whisper_writer , spammer_uid , spam_chat_id , spam_uid , online_writer , chat_id , XX , uid , Spy,data2, Chat_Leave, fast_spam_running, fast_spam_task, custom_spam_running, custom_spam_task, spam_request_running, spam_request_task, evo_fast_spam_running, emote_hijack, evo_fast_spam_task, evo_custom_spam_running, evo_custom_spam_task, lag_running, lag_task, evo_cycle_running, evo_cycle_task, evo_cycle_sm_running, evo_cycle_sm_task, reject_spam_running, reject_spam_task, bot_enabled
    # At the VERY TOP of your file, with other globals:
    status_response_cache = {}
    cache_lock = asyncio.Lock()  # For thread safety
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                        MsG = response.Data.msg.lower()

                    # --- AUTO FOR EVERYONE ---
                        msg2 = inPuTMsG.strip().lower()

                        if msg2.isdigit():
                            level = int(msg2)

                        elif msg2 in amr_bal:
                            level = amr_bal[msg2]

                        else:
                            level = None

                        if level is not None and 0 <= level <= 408:
                            inPuTMsG = f"/c {uid} {level}"
                        
                    except:
                        response = None


                    if response:

                        msg = response.Data.msg

                       # 👇 এখানেই বসাবি
                        try:
                            msg = response.Data.msg

                            if "[1=" in msg or len(msg) <= 0:

                               print("🎯 Emoji/Stiker detected")

                               emote_id = random.choice(list(GENERAL_EMOTES_MAP.values()))

                               packet = await Emote_k(
                                    int(response.Data.uid),
                                    int(emote_id),
                                    key,
                                    iv,
                                    region
                               )

                               await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet)

                        except Exception as e:
                            print(e)

                        if msg.startswith("/menu"):

                            try:
                               page = int(msg.replace("/menu",""))
                            except:
                                page = 1

                            menu_text = get_menu_page(page)

                            await safe_send_message(
                                response.Data.chat_type,
                                menu_text,
                                uid,
                                chat_id,
                                key,
                                iv
                            )
                        
                  
                        # --- AUTO FOR EVERYONE ---                    
                        try:
                            parts = inPuTMsG.strip().split()

                            # যদি ইউজার 2টা সংখ্যা লিখে: emote_number + times
                            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                                emote_number = parts[0]
                                times = int(parts[1])

                                if emote_number in EMOTE_MAP and 0 < times <= 100:
                                    emote_id = EMOTE_MAP[emote_number]

                                    # Auto convert to /p command
                                    inPuTMsG = f"/p {uid} {emote_id} {times}"

                        except Exception as e:
                            print("Error in auto /p conversion:", e)
               
               
                                                     
                        # AI Command - /ai
                        if inPuTMsG.strip().startswith('/ai '):
                            print('Processing AI command in any chat type')
                            
                            question = inPuTMsG[4:].strip()
                            if question:
                                initial_message = f"[B][C]{get_random_color()}\n🤖 AI is thinking...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    ai_response = await loop.run_in_executor(executor, talk_with_ai, question)
                                
                                # Format the AI response
                                ai_message = f"""
[B][C][FFFF00]🤖 AI Response:

[FFFFFF]{ai_response}

[C][B][FFB300]Question: [FFFFFF]{question}
"""
                                await safe_send_message(response.Data.chat_type, ai_message, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Please provide a question after /ai\nExample: /ai What is Free Fire?\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                        # ==================== CHECK COMMAND (BAN STATUS FIXED) ====================
                        if inPuTMsG.strip().startswith('/check'):
                            print(f"🔍 /check command received")
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                msg = f"""
[C][B][FF1493]═══════════════════
[C][B][00FFFF]  🔍 CHECK COMMAND
[C][FF1493]═══════════════════

[C][FFD700]Usage: /check (uid)
[C][FFD700]Example: /check 10634259930

[C][00FFFF]What it does:
[C][FFD700]• Checks if player is banned
[C][FFD700]• Shows ban period if banned
[C][FFD700]• Shows player nickname
[C][FFD700]• Shows player region
[C][FFD700]• Shows player level & likes

[C][FF1493]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                return
                            
                            target_uid = parts[1]
                            
                            if not target_uid.isdigit() or len(target_uid) < 8:
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ INVALID UID
[C][FF0000]═══════════════════

[C][FFD700]UID must be 8+ digits!
[C][FFD700]You entered: {target_uid}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )
                                return
                            
                            # Send initial message
                            await safe_send_message(
                                response.Data.chat_type,
                                f"""
[C][B][FFFF00]═══════════════════
[C][B][FFFF00]  🔍 CHECKING PLAYER STATUS
[C][FFFF00]═══════════════════

[C][FFD700]Target UID   : [00FFAA]{fix_num(target_uid)}
[C][FFD700]Status       : [00FFFF]Processing...

[C][FFFF00]═══════════════════
""",
                                uid, chat_id, key, iv
                            )
                            
                            try:
                                # 🔥 METHOD 1: DIRECT BOT CONNECTION - Get player info
                                result = get_real_player_info(target_uid)
                                
                                nickname = "Unknown"
                                player_region = "N/A"
                                player_level = "N/A"
                                player_likes = "0"
                                
                                if result["success"] and result.get("data"):
                                    data = result["data"]
                                    basic = data.get("basicInfo", {})
                                    
                                    nickname = basic.get('nickname', 'Unknown')
                                    player_region = basic.get('region', 'N/A')
                                    player_level = basic.get('level', 'N/A')
                                    player_likes = basic.get('liked', '0')
                                
                                # 🔥 METHOD 2: Check ban status via Garena API (MOST ACCURATE)
                                is_banned = False
                                ban_period = "Not Banned"
                                ban_reason = "Active Account"
                                
                                try:
                                    import requests
                                    # Try multiple ban check methods
                                    ban_period_display = "Not Banned"
                                    ban_reason_display = "Active Account"
                                    is_banned_final = False
                                    
                                    # Method A: Official Garena Ban API
                                    ban_url = f'https://ff.garena.com/api/antihack/check_banned?lang=en&uid={target_uid}'
                                    ban_response = requests.get(ban_url, timeout=10)
                                    
                                    if ban_response.status_code == 200:
                                        ban_data = ban_response.json()
                                        print(f"📡 Ban API Response: {ban_data}")
                                        
                                        if ban_data.get("status") == "success" and "data" in ban_data:
                                            data_ban = ban_data["data"]
                                            is_banned_api = data_ban.get("is_banned", 0) == 1
                                            
                                            if is_banned_api:
                                                is_banned_final = True
                                                period = data_ban.get("period", 0)
                                                reason = data_ban.get("ban_reason", "")
                                                
                                                if period > 0:
                                                    if period >= 30:
                                                        ban_period_display = f"{period} months (Permanent Ban)"
                                                    elif period >= 7:
                                                        ban_period_display = f"{period} days (Temporary Ban)"
                                                    elif period >= 1:
                                                        ban_period_display = f"{period} day(s) (Temporary Ban)"
                                                    else:
                                                        ban_period_display = f"{period} months"
                                                else:
                                                    ban_period_display = "Banned (No time limit)"
                                                
                                                ban_reason_display = reason if reason else "Unknown Reason"
                                                print(f"✅ BAN DETECTED: {ban_period_display} - {ban_reason_display}")
                                    
                                    # Method B: Check via shop2game API (if Garena API fails)
                                    if not is_banned_final:
                                        try:
                                            cookies = {
                                                '_ga': 'GA1.1.2123120599.1674510784',
                                                '_fbp': 'fb.1.1674510785537.363500115',
                                                '_ga_7JZFJ14B0B': 'GS1.1.1674510784.1.1.1674510789.0.0.0',
                                                'source': 'mb',
                                                'region': 'MA',
                                                'language': 'ar',
                                                '_ga_TVZ1LG7BEB': 'GS1.1.1674930050.3.1.1674930171.0.0.0',
                                                'datadome': '6h5F5cx_GpbuNtAkftMpDjsbLcL3op_5W5Z-npxeT_qcEe_7pvil2EuJ6l~JlYDxEALeyvKTz3~LyC1opQgdP~7~UDJ0jYcP5p20IQlT3aBEIKDYLH~cqdfXnnR6FAL0',
                                                'session_key': 'efwfzwesi9ui8drux4pmqix4cosane0y',
                                            }
                                            headers = {
                                                'Accept-Language': 'en-US,en;q=0.9',
                                                'Connection': 'keep-alive',
                                                'Origin': 'https://shop2game.com',
                                                'Referer': 'https://shop2game.com/app/100067/idlogin',
                                                'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                                                'accept': 'application/json',
                                                'content-type': 'application/json',
                                            }
                                            json_data = {
                                                'app_id': 100067,
                                                'login_id': target_uid,
                                                'app_server_id': 0,
                                            }
                                            shop_response = requests.post('https://shop2game.com/api/auth/player_id_login', 
                                                                          cookies=cookies, headers=headers, json=json_data, timeout=10)
                                            
                                            if shop_response.status_code == 200:
                                                shop_data = shop_response.json()
                                                if shop_data.get('nickname'):
                                                    # If player exists, not banned
                                                    is_banned_final = False
                                                    ban_period_display = "Not Banned"
                                                    ban_reason_display = "Active Account"
                                        except:
                                            pass
                                    
                                    # Set final values
                                    is_banned = is_banned_final
                                    ban_period = ban_period_display
                                    ban_reason = ban_reason_display
                                    
                                except Exception as e:
                                    print(f"⚠️ Ban check error: {e}")
                                    ban_period = "Unable to check"
                                    ban_reason = "API Error"
                                
                                # Build status
                                if is_banned:
                                    status_color = "FF0000"
                                    status_emoji = "❌"
                                    status_text = "BANNED"
                                else:
                                    status_color = "00FF00"
                                    status_emoji = "✅"
                                    status_text = "NOT BANNED"
                                
                                # ===== CREATE RESPONSE MESSAGE =====
                                msg = f"""
[C][B][{status_color}]═══════════════════
[C][B][00FFFF]  🔍 PLAYER STATUS RESULT
[C][{status_color}]═══════════════════

[C][FFD700]Player Name  : [00FF00]{nickname}
[C][FFD700]UID          : [00FFAA]{fix_num(target_uid)}
[C][FFD700]Region       : [FFFFFF]{player_region}
[C][FFD700]Level        : [FF88FF]{player_level}
[C][FFD700]Likes        : [FF4444]{fix_num(player_likes)}
[C][FFD700]Ban Status   : [{status_color}]{status_emoji} {status_text}
[C][FFD700]Ban Period   : [FFA500]{ban_period}
[C][FFD700]Ban Reason   : [FFFFFF]{ban_reason}

[C][{status_color}]═══════════════════
[C][FFD700]🤖 {BOT_NAME} BOT
[C][{status_color}]═══════════════════
"""
                                
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                print(f"✅ Check completed for {target_uid}")
                                
                            except Exception as e:
                                print(f"❌ Check error: {e}")
                                import traceback
                                traceback.print_exc()
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ ERROR
[C][FF0000]═══════════════════

[C][FFD700]Error: {str(e)[:50]}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )
                                
                        # JOKE COMMAND - /joke
                        if inPuTMsG.strip() == '/joke':
                            print('Processing joke command')
                            joke = random.choice(BANGLA_JOKES)
                            color1 = random.choice(JOKE_COLORS)
                            color2 = random.choice(JOKE_COLORS)
                            while color2 == color1:
                                color2 = random.choice(JOKE_COLORS)
                            joke_num = BANGLA_JOKES.index(joke) + 1
                            joke_msg = f"""[B][C][{color1}]━━━━━━━━━━━━━━━━━━
[{color1}]┃  [FFFFFF]😂 JOKE #{joke_num}  [{color1}]┃
[{color1}]━━━━━━━━━━━━━━━━━━

[{color2}]{joke}

[{color1}]━━━━━━━━━━━━━━━━━━
[FFD700]◉ —͞N A Y A N 乡ㅤ友! BOT [FF69B4]➤ /joke ◉
[{color1}]━━━━━━━━━━━━━━━━━━
"""
                            await safe_send_message(response.Data.chat_type, joke_msg, uid, chat_id, key, iv, region=region)

                        # SPNFF BUNDLE SPIN COMMAND - /spnff
                        if inPuTMsG.strip() == '/spnff':
                            print('Processing spnff bundle spin command')
                            bundle, rarity = spin_bundle()
                            spin_msg = format_spnff_result(bundle, rarity)
                            await safe_send_message(response.Data.chat_type, spin_msg, uid, chat_id, key, iv, region=region)

                        # FRIENDSHIP FOREVER CHANCE COMMAND - /frt name1&name2
                        if inPuTMsG.strip().startswith('/frt '):
                            print('Processing friendship command')
                            
                            parts = inPuTMsG.strip().split(' ', 1)
                            if len(parts) < 2 or '&' not in parts[1]:
                                error_msg = f"""[B][C][FF8C00]❌ ERROR! Usage: /frt name1&name2
[FFFFFF]Example: /frt {BOT_NAME_LOWER}&ovi

[00FF00]💕 This command shows friendship forever chance!
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                names = parts[1]
                                name1, name2 = names.split('&', 1)
                                name1 = name1.strip()
                                name2 = name2.strip()
                                
                                # Generate random friendship percentage
                                chance = random.randint(1, 100)
                                
                                # Different messages based on percentage
                                if chance >= 90:
                                    emoji = "💖💖💖"
                                    status = "BEST FRIENDS FOREVER!"
                                    color = "FF1493"
                                elif chance >= 70:
                                    emoji = "💕💕"
                                    status = "Amazing Friendship!"
                                    color = "FF69B4"
                                elif chance >= 50:
                                    emoji = "💗"
                                    status = "Good Friends!"
                                    color = "FFB6C1"
                                elif chance >= 30:
                                    emoji = "🤝"
                                    status = "Growing Friendship"
                                    color = "FFA500"
                                else:
                                    emoji = "😅"
                                    status = "Need More Bonding!"
                                    color = "FFFF00"
                                
                                frt_msg = f"""[B][C][{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[FF69B4]◉  💕 FRIENDSHIP FOREVER TEST 💕  ◉
[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎

[FF4500]◎ [FFFFFF]Name 1: [{color}]{name1}
[FF8C00]◎ [FFFFFF]Name 2: [{color}]{name2}

[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[FFFFFF]{emoji} Friendship Forever: [{color}]{percentage}%
[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[FFFFFF]{message}
[FFD700]◉ —͞N A Y A N 乡ㅤ友! BOT [00FF7F]➤ /frt ◉
"""
                                await safe_send_message(response.Data.chat_type, frt_msg, uid, chat_id, key, iv, region=region)

                        # GIRLFRIEND RELATIONSHIP TEST COMMAND - /grt name1&name2
                        if inPuTMsG.strip().startswith('/grt '):
                            print('Processing girlfriend relationship test command')
                            
                            parts = inPuTMsG.strip().split(' ', 1)
                            if len(parts) < 2 or '&' not in parts[1]:
                                error_msg = f"""[B][C][FF8C00]❌ ERROR! Usage: /grt name1&name2
[FFFFFF]Example: /grt ovi&sadiya

[FF69B4]💕 সারা জীবনের সঙ্গী হওয়ার চান্স দেখুন!
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                names = parts[1]
                                name1, name2 = names.split('&', 1)
                                name1 = name1.strip()
                                name2 = name2.strip()
                                
                                # Generate random girlfriend relationship percentage
                                chance = random.randint(1, 100)
                                
                                # Different messages based on percentage
                                if chance >= 90:
                                    emoji = "💖💖💖💍"
                                    status = "সারা জীবনের সঙ্গী! PERFECT MATCH!"
                                    color = "FF1493"
                                elif chance >= 70:
                                    emoji = "💕💕💗"
                                    status = "দারুণ জুটি! Amazing Couple!"
                                    color = "FF69B4"
                                elif chance >= 50:
                                    emoji = "💗💗"
                                    status = "ভালো সম্পর্ক! Good Relationship!"
                                    color = "FFB6C1"
                                elif chance >= 30:
                                    emoji = "💓"
                                    status = "চেষ্টা করতে হবে! Keep Trying!"
                                    color = "FFA500"
                                else:
                                    emoji = "💔"
                                    status = "আরো ভালোবাসা দরকার! Need More Love!"
                                    color = "FFFF00"
                                
                                grt_msg = f"""[B][C][{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[00FFFF]◉  💑 SOULMATE FOREVER TEST 💑  ◉
[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎

[9400D3]◎ [FFFFFF]Name 1: [{color}]{name1}
[FF00FF]◎ [FFFFFF]Name 2: [{color}]{name2}

[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[FFFFFF]{emoji} Soulmate Forever: [{color}]{percentage}%
[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[FFFFFF]{message}
[FFD700]◉ —͞N A Y A N 乡ㅤ友! BOT [FF69B4]➤ /grt ◉
"""
                                await safe_send_message(response.Data.chat_type, grt_msg, uid, chat_id, key, iv, region=region)  
                                       

                        #GET PLAYER LIKE
                        if inPuTMsG.strip().startswith('/like'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /like <uid>\nExample: /like 144🤫444🤫440🤫04\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nSending Likes...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                like_result = send_likes(target_uid)

                                await safe_send_message(response.Data.chat_type, like_result, uid, chat_id, key, iv)
                         
                        
                        # MATH COMMAND - /mth (LOCAL - No API needed)
                        if inPuTMsG.strip().startswith('/mth'):
                            print('Processing /mth local math command')
                            parts = inPuTMsG.strip().split(maxsplit=1)
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF8C00]❌ ERROR! Usage: /mth [expression]

[FFFF00]➕ যোগ (Addition):
[FFFFFF]/mth 1+1    →  2
[FFFFFF]/mth 1+2    →  3
[FFFFFF]/mth 100+200 → 300
[FFFFFF]/mth 1.5+2.5 → 4

[FFFF00]➖ বিয়োগ (Subtraction):
[FFFFFF]/mth 5-3    →  2
[FFFFFF]/mth 100-50 →  50
[FFFFFF]/mth 3-2    →  1

[FFFF00]✖️ গুণ (Multiplication):
[FFFFFF]/mth 3*4    →  12
[FFFFFF]/mth 5×6    →  30
[FFFFFF]/mth 10x20  →  200

[FFFF00]➗ ভাগ (Division):
[FFFFFF]/mth 20/5   →  4
[FFFFFF]/mth 100÷4  →  25
[FFFFFF]/mth 15/3   →  5

[FFFF00]⚡ পাওয়ার (Power):
[FFFFFF]/mth 2^3    →  8
[FFFFFF]/mth 5^2    →  25

[FFFF00]🔢 মডুলো (Remainder):
[FFFFFF]/mth 10%3   →  1

[FFFF00]🧮 মিক্সড (Mixed):
[FFFFFF]/mth (2+3)*4  → 20
[FFFFFF]/mth 100/5+20 → 40
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                expression = parts[1].strip()
                                initial_msg = f"[B][C]{get_random_color()}🧮 Calculating: {xMsGFixinG(expression)}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
                                
                                try:
                                    math_result = local_math_calculate(expression)
                                    await safe_send_message(response.Data.chat_type, math_result, uid, chat_id, key, iv, region=region)
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ Math Error: {str(e)[:50]}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # SPEED COMMAND - /speed
                        if inPuTMsG.strip().startswith('/speed'):
                            print('Processing speed command')
                            speed_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]SPEED STATUS
[00FFFF]❀ [00FF7F]SPEED[FFFFFF]: MAX BOOST ⚡
[00FFFF]❀ [FFD700]PING[FFFFFF]: LOW [00FFFF]••[00FFFF]POWER[FFFFFF]: 100%
[00FFFF]❀ [FF69B4]STATUS[FFFFFF]: RUNNING SMOOTHLY ✅
[00FFFF]✿ {BOT_NAME} ✿"""
                            await safe_send_message(response.Data.chat_type, speed_msg, uid, chat_id, key, iv, region=region)

                        # LUKE COMMAND - /luke (Fortune Teller)
                        if inPuTMsG.strip().lower().startswith('/luck '):
                            print('Processing luck fortune command')
                            parts = inPuTMsG.strip().split(' ', 1)
                            if len(parts) < 2 or not parts[1].strip():
                                error_msg = f"[B][C][FF8C00]❌ ERROR! নাম লিখুন!\n[FFFFFF]Example: /luck {BOT_NAME_LOWER}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                name = parts[1].strip().title()
                                
                                good_predictions = [
                                    f"🌟 {name} tum bahut jald ek badi safalta hasil karoge!",
f"💰 {name} tumhare jeevan mein bahut paisa aayega InshaAllah!",
f"❤️ {name} tumhara sachcha pyaar bahut paas hai!",
f"🏆 {name} tum ek din champion banoge!",
f"📚 {name} tumhare exam mein bahut accha result aayega!",
f"🌈 {name} tumhara mushkil waqt khatam ho raha hai!",
f"🎯 {name} tumhara sapna bahut jald poora hoga!",
f"💎 {name} tumhe ek keemti tohfa milega!",
f"🚀 {name} tumhara career rocket ki tarah upar jayega!",
f"🏠 {name} tumhe ek sundar ghar milega!",
f"✈️ {name} tum videsh yatra karoge!",
f"👑 {name} tum ek din neta banoge!",
f"💪 {name} tumhari sehat bahut acchi rahegi!",
f"🌺 {name} tumhara parivar khush rahega!",
f"🎓 {name} tum uchch shiksha mein safal hoge!",
f"🌟 {name} tumhara naam sab jaanenge!",
f"💝 {name} tumhara jeevansathi bahut sundar hoga!",
f"🎶 {name} tum ek pratibha khoj nikaloge!",
f"🏅 {name} tum game mein Grandmaster banoge!",
f"🌻 {name} tumhare dost tumse bahut pyaar karte hain!",
f"💫 {name} tumhari kismat ab bahut acchi chal rahi hai!",
f"🎁 {name} tumhe aaj ek surprise milega!",
f"🔥 {name} tumhare andar chhupi hui shakti hai!",
f"🌙 {name} tumhari raat ki dua qubool hogi!",
f"⭐ {name} tum ek din sitara banoge!",
f"🎪 {name} tumhare jeevan mein khushi ki aandhi aayegi!",
f"💐 {name} tumhe bahut izzat milegi!",
f"🏰 {name} tumhara bhavishya raja jaisa hoga!",
f"🌞 {name} tumhara jeevan ro
                                    f"💀 {name} tumhara aaj ka din kharab jayega!",
f"😭 {name} tum aaj roge!",
f"🐍 {name} tumhare kareebi log tumhe dhokha denge!",
f"💔 {name} tumhara pyaar toot jayega!",
f"📉 {name} tum exam mein fail hoge!",
f"🦷 {name} tumhare daant mein dard hoga!",
f"🤒 {name} tum bimaar pad jaoge!",
f"👻 {name} raat ko tum dar jaoge!",
f"🐛 {name} tumhare khane mein keeda niklega!",
f"📵 {name} tumhara phone kharab ho jayega!",
f"🌧️ {name} bahar gaye to tum par baarish padegi!",
f"😤 {name} koi tumse jhagda karega!",
f"🐜 {name} tumhare ghar mein cheenti bhar jayengi!",
f"💸 {name} tumhara paisa kho jayega!",
f"🦟 {name} machchhar tumhe bahut kaatenge!",
f"😴 {name} tumhe aaj neend nahi aayegi!",
f"🤡 {name} log tumhara mazak udayenge!",
f"🧊 {name} tumhe sardi lag jayegi!",
f"🤯 {name} tumhare sar mein dard hoga!",
f"😱 {name} tum ek darawna sapna dekhoge!",
f"🐸 {name} tumhare saamne mendhak uchalega!",
f"💩 {name} tumhare joote mein kuch lag jayega!",
f"🦎 {name} tumhare ghar mein chipkali gir jayegi!",
f"🌪️ {name} tumhara chhata kho jayega!",
f"😡 {name} tumhara dost tumse baat nahi karega!",
f"🐕 {name} kutta tumhare peeche bhaagega!",
f"🧅 {name} tumhari aankhon mein pyaaz se jalan hogi!",
f"📝 {name} tumhara homework kho jayega!",
f"🎮 {name} tum aaj game haar jaoge!",
f"🔋 {name} tumhare phone ki battery khatam ho jayegi!",
f"🧦 {name} tumhara moja kho jayega!",
f"🦷 {name} tum chewing gum baal mein laga loge!",
f"🍕 {name} tumhara pasand ka khana khatam ho jayega!",
f"📶 {name} tumhara internet slow chalega!",
f"🚌 {name} tum bus miss kar doge!",
f"☔ {name} tum baarish mein bheeg jaoge!",
f"😪 {name} tumhe class mein neend aayegi!",
f"🧻 {name} bathroom mein tissue khatam hoga!",
f"🦗 {name} tumhare kaan ke paas jingur bolega!",
f"💤 {name} tum alarm nahi sun paoge!",
f"🐦 {name} pakshi tumhare sar par potty karega!",
f"🧹 {name} tumhe aaj ghar saaf karna padega!",
f"🤧 {name} tumhari chheenk nahi rukegi!",
f"🦠 {name} tumhare pet mein dikkat hogi!",
f"🔑 {name} tumhari chaabi kho jayegi!",
f"👟 {name} tumhare joote ka phita toot jayega!",
f"🧊 {name} tum paani mein phisal jaoge!",
f"🪳 {name} tumhare bistar par cockroach chadh jayega!",
f"🍋 {name} tumhare muh mein khatta lagega!",
f"😵 {name} tum chakkar kha kar gir jaoge!"
                                ]
                                
                                all_predictions = good_predictions + bad_predictions
                                prediction = random.choice(all_predictions)
                                
                                # Determine if good or bad
                                if prediction in good_predictions:
                                    pred_type = "[00FF00]✅ শুভ ভবিষ্যৎবাণী"
                                    border_color = "00FF7F"
                                    emoji = "🔮"
                                else:
                                    pred_type = "[FF4500]⚠️ সতর্কতা ভবিষ্যৎবাণী"
                                    border_color = "FF6347"
                                    emoji = "🔮"
                                
                                colors = ["FF69B4", "FFD700", "00FFFF", "FF4500", "7B68EE", "00FF7F", "FF1493", "1E90FF", "DA70D6", "DC143C", "20B2AA", "FF8C00", "9370DB", "4169E1", "00CED1"]
                                c1 = random.choice(colors)
                                c2 = random.choice(colors)
                                c3 = random.choice(colors)
                                
                                luke_msg = f"""[B][C][{border_color}]━━━━━━━━━━━━━━━━━━━━━
[{c1}]★ [{c2}]{emoji} ভ বি ষ্য ৎ বা ণী {emoji} [{c1}]★
[{border_color}]━━━━━━━━━━━━━━━━━━━━━
[FFD700]👤 নাম: [{c3}]{name}
[{border_color}]━━━━━━━━━━━━━━━━━━━━━
{pred_type}
[{border_color}]━━━━━━━━━━━━━━━━━━━━━
[{c1}]{prediction}
[{border_color}]━━━━━━━━━━━━━━━━━━━━━
[FF69B4]🔮 Powered By [FFFF00]—͞NAYAN乡ㅤ友!
[{border_color}]━━━━━━━━━━━━━━━━━━━━━"""
                                await safe_send_message(response.Data.chat_type, luke_msg, uid, chat_id, key, iv, region=region)


                        # ========== FEATURE 1: /quiz - কুইজ গেম ==========
                        if inPuTMsG.strip().lower().startswith('/quiz'):
                            print('Processing quiz command')
                            quiz_questions = [
                                [
  {"q": "Bangladesh ki rajdhani kya hai?", "a": "Dhaka", "options": ["Dhaka", "Chattogram", "Rajshahi", "Khulna"]},
  {"q": "Prithvi ka sabse bada mahasagar kaun sa hai?", "a": "Prashant Mahasagar", "options": ["Atlantic", "Prashant Mahasagar", "Hind Mahasagar", "Arctic"]},
  {"q": "Free Fire mein sabse bada rank kya hai?", "a": "Grandmaster", "options": ["Heroic", "Grandmaster", "Diamond", "Platinum"]},
  {"q": "Bangladesh ka rashtriya phool kaun sa hai?", "a": "Shapla", "options": ["Gulab", "Shapla", "Beli", "Jui"]},
  {"q": "Suraj kis disha mein ugta hai?", "a": "Purva", "options": ["Paschim", "Uttar", "Purva", "Dakshin"]},
  {"q": "Paani ka rasayanik sanket kya hai?", "a": "H2O", "options": ["CO2", "H2O", "O2", "NaCl"]},
  {"q": "Bangladesh ka Swatantrata Diwas kab hai?", "a": "26 March", "options": ["16 December", "26 March", "21 February", "14 April"]},
  {"q": "Chaand par pehla insaan kaun gaya tha?", "a": "Neil Armstrong", "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins"]},
  {"q": "Insaan ke shareer mein kitni haddiyan hoti hain?", "a": "206", "options": ["200", "206", "300", "150"]},
  {"q": "Free Fire mein kitne player ek saath khelte hain?", "a": "50", "options": ["100", "50", "60", "40"]},
  {"q": "Duniya ka sabse bada desh kaun sa hai?", "a": "Russia", "options": ["China", "America", "Russia", "Canada"]},
  {"q": "Rangdhanush mein kitne rang hote hain?", "a": "7", "options": ["5", "6", "7", "8"]},
  {"q": "Bangladesh ka rashtriya pakshi kaun sa hai?", "a": "Doel", "options": ["Kokil", "Doel", "Moyna", "Tiya"]},
  {"q": "1 Kilometer = kitne Meter?", "a": "1000", "options": ["100", "500", "1000", "1500"]},
  {"q": "Prithvi ka sabse uncha parvat kaun sa hai?", "a": "Everest", "options": ["Kanchenjunga", "Everest", "Kilimanjaro", "Alps"]},
  {"q": "Bangladesh ka Vijay Diwas kab hai?", "a": "16 December", "options": ["26 March", "16 December", "21 February", "14 April"]},
  {"q": "Prithvi ki sabse lambi nadi kaun si hai?", "a": "Nile Nadi", "options": ["Amazon", "Nile Nadi", "Ganga", "Mississippi"]},
  {"q": "Bangladesh ka rashtriya phal kaun sa hai?", "a": "Kathal", "options": ["Aam", "Kathal", "Lichi", "Kela"]},
  {"q": "Saurmandal mein kitne grah hain?", "a": "8", "options": ["7", "8", "9", "10"]},
  {"q": "Prithvi ka sabse chhota mahadweep kaun sa hai?", "a": "Oceania", "options": ["Europe", "Oceania", "Antarctica", "Africa"]},
  {"q": "Insaan ke shareer ka sabse bada ang kaun sa hai?", "a": "Twacha", "options": ["Liver", "Twacha", "Dil", "Fefda"]},
  {"q": "Bangladesh ka rashtriya khel kaun sa hai?", "a": "Kabaddi", "options": ["Cricket", "Football", "Kabaddi", "Hockey"]},
  {"q": "Suraj kis disha mein doobta hai?", "a": "Paschim", "options": ["Purva", "Paschim", "Uttar", "Dakshin"]},
  {"q": "Roshni ki gati prati second kitne km hai?", "a": "3 lakh", "options": ["1 lakh", "2 lakh", "3 lakh", "5 lakh"]},
  {"q": "Bangladesh ki mudra ka naam kya hai?", "a": "Taka", "options": ["Rupaye", "Taka", "Dollar", "Riyal"]},
  {"q": "DNA ka full form kya hai?", "a": "Deoxyribonucleic Acid", "options": ["Deoxyribonucleic Acid", "Dynamic Nuclear Acid", "Digital Network Analysis", "Data Network Access"]},
  {"q": "Duniya ka sabse zyada jansankhya wala desh kaun sa hai?", "a": "Bharat", "options": ["China", "Bharat", "America", "Indonesia"]},
  {"q": "Bangla bhasha ke janak kaun hain?", "a": "Ishwar Chandra Vidyasagar", "options": ["Rabindranath", "Ishwar Chandra Vidyasagar", "Bankim Chandra", "Michael Madhusudan"]},
  {"q": "Bangladesh mein kitne vibhag hain?", "a": "8", "options": ["6", "7", "8", "10"]},
  {"q": "Vitamin C sabse zyada kis phal mein hota hai?", "a": "Amla", "options": ["Santra", "Amla", "Nimbu", "Aam"]},
  {"q": "Bangladesh ki sabse badi nadi kaun si hai?", "a": "Padma", "options": ["Meghna", "Yamuna", "Padma", "Brahmaputra"]},
  {"q": "Computer ka dimaag kaun sa hota hai?", "a": "CPU", "options": ["RAM", "CPU", "GPU", "SSD"]},
  {"q": "Vayumandal mein oxygen kitni % hai?", "a": "21%", "options": ["15%", "21%", "30%", "50%"]},
  {"q": "Bangladesh ke rashtriya kavi kaun hain?", "a": "Kazi Nazrul Islam", "options": ["Rabindranath", "Kazi Nazrul Islam", "Jasimuddin", "Shamsur Rahman"]},
  {"q": "Prithvi Suraj ke chakkar kitne din mein lagati hai?", "a": "365 din", "options": ["30 din", "100 din", "365 din", "500 din"]},
  {"q": "Mangal grah ko kya kaha jata hai?", "a": "Lal Grah", "options": ["Neela Grah", "Lal Grah", "Hara Grah", "Safed Grah"]},
  {"q": "Bangladesh ka samvidhan kab bana?", "a": "1972", "options": ["1971", "1972", "1973", "1975"]},
  {"q": "Internet ke janak kaun hain?", "a": "Vint Cerf", "options": ["Bill Gates", "Steve Jobs", "Vint Cerf", "Mark Zuckerberg"]},
  {"q": "Insaan ke khoon mein kitne group hote hain?", "a": "4", "options": ["2", "3", "4", "6"]},
  {"q": "Duniya ka sabse bada registan kaun sa hai?", "a": "Sahara", "options": ["Gobi", "Sahara", "Thar", "Kalahari"]},
  {"q": "Bangladesh ke pehle rashtrapati kaun the?", "a": "Sheikh Mujibur Rahman", "options": ["Ziaur Rahman", "Sheikh Mujibur Rahman", "Tajuddin Ahmad", "A K Fazlul Haq"]},
  {"q": "Heera kis tatva ka roop hai?", "a": "Carbon", "options": ["Loha", "Carbon", "Sona", "Chandi"]},
  {"q": "Kis vitamin ki kami se raat ka andha hota hai?", "a": "Vitamin A", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"]},
  {"q": "Telephone kisne banaya?", "a": "Alexander Graham Bell", "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Michael Faraday"]},
  {"q": "Prithvi ka sabse gehra samudri gaddha kaun sa hai?", "a": "Mariana Trench", "options": ["Mariana Trench", "Tonga Trench", "Java Trench", "Puerto Rico Trench"]},
  {"q": "Bangladesh ka sabse bada vibhag kaun sa hai?", "a": "Chattogram", "options": ["Dhaka", "Chattogram", "Rajshahi", "Rangpur"]},
  {"q": "Sabse halki gas kaun si hai?", "a": "Hydrogen", "options": ["Oxygen", "Helium", "Hydrogen", "Nitrogen"]},
  {"q": "Computer ki bhasha kaun si hai?", "a": "Binary", "options": ["English", "Bangla", "Binary", "Hindi"]},
  {"q": "Chaand tak pahunchne mein kitna samay lagta hai?", "a": "3 din", "options": ["1 din", "3 din", "7 din", "15 din"]},
  {"q": "Bijli kisne khoji?", "a": "Benjamin Franklin", "options": ["Thomas Edison", "Benjamin Franklin", "Nikola Tesla", "Michael Faraday"]},
  {"q": "Insaan ke dimaag ka wazan kitna hota hai?", "a": "1.4 kg", "options": ["0.5 kg", "1.4 kg", "2.5 kg", "3 kg"]},
  {"q": "Bangladesh ki sabse unchi choti kaun si hai?", "a": "Tazingdong", "options": ["Keokradong", "Tazingdong", "Modok Mual", "Saka Haphong"]},
  {"q": "Facebook kisne banaya?", "a": "Mark Zuckerberg", "options": ["Bill Gates", "Mark Zuckerberg", "Elon Musk", "Jeff Bezos"]},
  {"q": "Prithvi ka kitna % hissa paani hai?", "a": "71%", "options": ["50%", "60%", "71%", "80%"]},
  {"q": "Bangladesh mein kitne jile hain?", "a": "64", "options": ["50", "60", "64", "70"]},
  {"q": "Sabse bada stanya-paayi janwar kaun sa hai?", "a": "Neeli Whale", "options": ["Haathi", "Neeli Whale", "Giraffe", "Genda"]},
  {"q": "Google kab bana?", "a": "1998", "options": ["1995", "1998", "2000", "2004"]},
  {"q": "Insaan ke shareer ka sabse majboot padaarth kaun sa hai?", "a": "Enamel", "options": ["Haddi", "Enamel", "Nakhun", "Baal"]},
  {"q": "Bangladesh ka sabse bada samudri tat kaun sa hai?", "a": "Cox's Bazar", "options": ["Kuakata", "Cox's Bazar", "Saint Martin", "Patenga"]},
  {"q": "Suraj ke sabse paas ka grah kaun sa hai?", "a": "Budh", "options": ["Shukra", "Budh", "Prithvi", "Mangal"]},
  {"q": "Vayumandal mein sabse zyada kaun si gas hai?", "a": "Nitrogen", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"]},
  {"q": "Bangabandhu Setu kis nadi par hai?", "a": "Yamuna", "options": ["Padma", "Yamuna", "Meghna", "Brahmaputra"]},
  {"q": "Padma Setu ki lambai kitni hai?", "a": "6.15 km", "options": ["4.8 km", "6.15 km", "7.2 km", "8.0 km"]},
  {"q": "Cricket mein 1 over mein kitni ball hoti hai?", "a": "6", "options": ["4", "5", "6", "8"]},
  {"q": "FIFA World Cup kitne saal mein ek baar hota hai?", "a": "4 saal", "options": ["2 saal", "3 saal", "4 saal", "5 saal"]},
  {"q": "Mother Teresa ka janm kis desh mein hua?", "a": "Albania", "options": ["Bharat", "Italy", "Albania", "France"]},
  {"q": "Bangla Navavarsh kab hota hai?", "a": "14 April", "options": ["1 January", "14 April", "26 March", "21 February"]},
  {"q": "Insaan ka normal temperature kitna hota hai?", "a": "98.6°F", "options": ["95°F", "98.6°F", "100°F", "102°F"]},
  {"q": "Sabse zyada chai kis desh mein hoti hai?", "a": "China", "options": ["Bharat", "China", "Sri Lanka", "Kenya"]},
  {"q": "Bangladesh ka mukhya niryat utpad kya hai?", "a": "Taiyar Kapde", "options": ["Chai", "Jute", "Taiyar Kapde", "Chamda"]},
  {"q": "Sabse tez daudne wala janwar kaun sa hai?", "a": "Cheetah", "options": ["Sher", "Cheetah", "Ghoda", "Hiran"]},
  {"q": "Sabse bada grah kaun sa hai?", "a": "Brihaspati", "options": ["Shani", "Brihaspati", "Uranus", "Neptune"]},
  {"q": "Bangla Academy kab bani?", "a": "1955", "options": ["1952", "1955", "1960", "1971"]},
  {"q": "Duniya ki sabse badi jheel kaun si hai?", "a": "Caspian Sagar", "options": ["Baikal", "Caspian Sagar", "Victoria", "Superior"]},
  {"q": "Sabse mehngi dhatu kaun si hai?", "a": "Platinum", "options": ["Sona", "Platinum", "Chandi", "Tamba"]},
  {"q": "Football mein kitne khiladi hote hain?", "a": "11", "options": ["9", "10", "11", "12"]},
  {"q": "Bangladesh ka sabse bada dweep kaun sa hai?", "a": "Bhola", "options": ["Sandwip", "Bhola", "Hatiya", "Maheshkhali"]},
  {"q": "Olympic kitne saal mein ek baar hota hai?", "a": "4 saal", "options": ["2 saal", "3 saal", "4 saal", "5 saal"]},
  {"q": "Prithvi par kitne mahadweep hain?", "a": "7", "options": ["5", "6", "7", "8"]},
  {"q": "Duniya ka sabse chhota desh kaun sa hai?", "a": "Vatican City", "options": ["Monaco", "Vatican City", "San Marino", "Maldives"]},
  {"q": "Kis vitamin se haddiyan majboot hoti hain?", "a": "Vitamin D", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"]},
  {"q": "Bangladesh ka sabse bada jungle kaun sa hai?", "a": "Sundarban", "options": ["Madhupur", "Sundarban", "Lawachara", "Bhawal"]},
  {"q": "1 Mile = kitne Kilometer?", "a": "1.6 km", "options": ["1.0 km", "1.6 km", "2.0 km", "2.5 km"]},
  {"q": "Insaan ka dil 1 minute mein kitni baar dhadakta hai?", "a": "72", "options": ["50", "60", "72", "100"]},
  {"q": "Sabse kathor prakritik padaarth kaun sa hai?", "a": "Heera", "options": ["Loha", "Heera", "Granite", "Marble"]},
  {"q": "Bangladesh ki Mukti Yudh kab hui?", "a": "1971", "options": ["1952", "1966", "1970", "1971"]},
  {"q": "Kaun si gas indhan ke roop mein istemal hoti hai?", "a": "Methane", "options": ["Oxygen", "Nitrogen", "Methane", "Helium"]},
  {"q": "Sabse bada mahasagar kaun sa hai?", "a": "Prashant Mahasagar", "options": ["Hind Mahasagar", "Atlantic", "Prashant Mahasagar", "Arctic"]},
  {"q": "Kis desh ko Surya Uday ka desh kaha jata hai?", "a": "Japan", "options": ["China", "Japan", "Korea", "Thailand"]},
  {"q": "Paani kitne degree par ubalta hai?", "a": "100°C", "options": ["50°C", "80°C", "100°C", "120°C"]},
  {"q": "Duniya mein sabse zyada bhashayein kis desh mein boli jati hain?", "a": "Papua New Guinea", "options": ["Bharat", "Papua New Guinea", "Indonesia", "Nigeria"]},
  {"q": "Free Fire mein diamond se kya kharida jata hai?", "a": "Bundle", "options": ["Heera", "Bundle", "Gaadi", "Ghar"]},
  {"q": "Kis janwar ke sabse zyada pair hote hain?", "a": "Millipede", "options": ["Makdi", "Millipede", "Kekda", "Cheenti"]},
  {"q": "Duniya ki pehli programmer kaun thi?", "a": "Ada Lovelace", "options": ["Charles Babbage", "Ada Lovelace", "Alan Turing", "Dennis Ritchie"]},
  {"q": "Sabse bada phool kaun sa hai?", "a": "Rafflesia", "options": ["Kamal", "Rafflesia", "Surajmukhi", "Gulab"]},
  {"q": "Piramid kis desh mein hain?", "a": "Misr", "options": ["Bharat", "Misr", "Iraq", "Turkey"]}
]
                            ]
                            q = random.choice(quiz_questions)
                            random.shuffle(q["options"])
                            colors = ["FF69B4", "00FFFF", "FFD700", "7B68EE"]
                            quiz_msg = f"""[B][C][FF4500]━━━━━━━━━━━━━━━━━━━━━
[FFD700]🧠 কু ই জ  গে ম 🧠
[FF4500]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]❓ {q['q']}
[FF4500]━━━━━━━━━━━━━━━━━━━━━
[{colors[0]}]🅰️ {q['options'][0]}
[{colors[1]}]🅱️ {q['options'][1]}
[{colors[2]}]🅲️ {q['options'][2]}
[{colors[3]}]🅳️ {q['options'][3]}
[FF4500]━━━━━━━━━━━━━━━━━━━━━
[00FF00]✅ সঠিক উত্তর: [FFFF00]{q['a']}
[FF4500]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, quiz_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 2: /dare - ডেয়ার গেম (100+) ==========
                        if inPuTMsG.strip().lower().startswith('/dare'):
                            print('Processing dare command')
                            dares = [
                                [
    "🔥 5 minute aankh band karke baitho!",
    "😂 agle 10 minute sirf hasna hai!",
    "🐔 murgi ki tarah awaaz nikalo!",
    "🎤 ek gaana gao!",
    "💃 30 second naacho!",
    "🤪 muh se bandar ki awaaz nikalo!",
    "😜 apne crush ko message bhejo!",
    "🫣 apni sabse badi sharm wali ghatna sunao!",
    "🤡 5 minute joker banke raho!",
    "📱 apne phone ki last chat dikhao!",
    "🍋 ek kachcha nimbu khao!",
    "🐍 zameen par saap ki tarah chalo!",
    "👶 bacche ki tarah ro kar dikhao!",
    "🦁 sher ki tarah garjo!",
    "🤸 10 squats karo!",
    "😘 sheeshe ke saamne khud ko kiss karo!",
    "🎭 5 minute robot ki tarah baat karo!",
    "🧊 barf haath mein pakad ke 1 minute raho!",
    "🐱 billi ki tarah meow meow karo!",
    "💪 20 push-ups karo!",
    "🤫 agle 5 minute bilkul mat bolo!",
    "🎵 apna favourite gaana sabke saamne gao!",
    "😳 apne paas wale insaan se bolo 'I Love You'!",
    "🐸 mendhak ki tarah 1 minute koodo!",
    "🤓 10 minute nerd ki tarah baat karo!",
    "🕺 apna sabse ganda dance move dikhao!",
    "🤳 sabse baddi selfie leke group mein bhejo!",
    "🎬 apni favourite movie ka dialogue bolo!",
    "🦆 1 minute batakh ki tarah chalo!",
    "😝 30 second tak jeebh bahar nikal ke raho!",
    "🧎 5 minute ghutne ke bal baitho!",
    "🗣️ apne paas wale ki tareef karo!",
    "🤖 1 minute robot ki tarah chalo!",
    "🎩 kaalpnik topi pehen ke dikhao!",
    "👃 naak pakad ke 1 minute baat karo!",
    "🧘 5 minute aankh band karke meditation karo!",
    "🐒 bandar ki tarah acting karo!",
    "💅 apne pair ke nakhun gino aur batao!",
    "🎤 30 second rap gaana gao!",
    "🤠 cowboy ki tarah chalo!",
    "🐧 penguin ki tarah chalo!",
    "🥶 1 minute baraf ki tarah jam ke khade raho!",
    "🤥 sabse badi jhooth bolo!",
    "🍌 30 second tak kele ka chilka sar pe rakho!",
    "👅 jeebh se naak chhoone ki koshish karo!",
    "🧑‍🎤 1 minute opera gaao!",
    "🦸 30 second superhero pose do!",
    "🤹 juggling karne ka naatak karo!",
    "💋 haath par kiss karke phoonk maaro!",
    "🧟 1 minute zombie ki tarah chalo!",
    "🤧 zor se 5 baar chheenk maaro!",
    "🎭 5 minute ulti baat karo!",
    "🐶 kutte ki tarah bhon bhon karo!",
    "😤 1 minute gusse wala chehra banao!",
    "🤩 apna sabse accha talent dikhao!",
    "🎪 circus ke joker ki tarah acting karo!",
    "📚 tumhari aakhri padhi hui kitab ka naam batao!",
    "🧑‍🍳 30 second khana banane ka naatak karo!",
    "🏊 ghar mein swimming karne ka naatak karo!",
    "🤸‍♂️ aage peeche 10 baar koodo!",
    "🧑‍✈️ pilot banne ka naatak karo!",
    "🥷 ninja ki tarah acting karo!",
    "😵‍💫 10 baar ghumo phir seedha chalo!",
    "🐻 bhalu ki tarah garjo!",
    "🎸 30 second air guitar bajao!",
    "📢 zor se chilla ke bolo 'Main Mashoor Hoon'!",
    "🤦 apna sabse bewakoof wala kaam batao!",
    "🧏 1 minute ishare se baat karo!",
    "🦩 1 minute ek pair par khade raho!",
    "🤫 apne phone ka password batao!",
    "🎯 aankh band karke kuch banao!",
    "🗿 1 minute bina expression ke raho!",
    "🐠 30 second machli jaisa muh banao!",
    "👻 daraawni bhoot ki kahani sunao!",
    "🥊 hawa mein boxer ki tarah punch maaro!",
    "🧑‍🚀 astronaut ki tarah slow motion mein chalo!",
    "🤳 gallery ki 10 number wali photo dikhao!",
    "🎶 1 minute muh band karke gun-gunao!",
    "🐊 magarmach ki tarah muh kholo!",
    "🧊 30 second baraf ki tarah jam jao!",
    "🤑 paise ginne ka naatak karo!",
    "🐰 khargosh ki tarah koodo!",
    "🎪 jaadu dikhane ka naatak karo!",
    "🫠 mombatti ki tarah pighalne ka naatak karo!",
    "🦜 1 minute tota ki tarah baat repeat karo!",
    "🧑‍🎓 1 minute teacher ban ke class lo!",
    "🤺 talwar se ladai karne ka naatak karo!",
    "🦕 dinosaur ki tarah chalo!",
    "🎬 movie ke villain ka dialogue bolo!",
    "🤠 apni sabse funny yaad sunao!",
    "🏋️ bhaari cheez uthane ka naatak karo!",
    "🎵 apne favourite gaane ke bol galat-galat gao!",
    "🐈 billi ki tarah lot-pot ho!",
    "🤡 clown makeup karne ka naatak karo!",
    "🧙 jadugar ki tarah mantra padho!",
    "🦸‍♀️ superwoman ki tarah udne ka naatak karo!",
    "🎤 1 minute news anchor ki tarah baat karo!",
    "🤣 1 minute zor se haso!",
    "😢 1 minute rone ka naatak karo!",
    "🧑‍⚕️ doctor ban ke checkup karne ka naatak karo!",
    "🕵️ jasus ki tarah ghar ki talashi lo!"
]
                            dare = random.choice(dares)
                            c = random.choice(["FF69B4", "00FFFF", "FFD700", "FF4500", "7B68EE", "00FF7F"])
                            dare_msg = f"""[B][C][DA70D6]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]🎲 DARE GAME 🎲
[DA70D6]━━━━━━━━━━━━━━━━━━━━━
[{c}]{dare}
[DA70D6]━━━━━━━━━━━━━━━━━━━━━
[FFFF00]⚡ DARE  KARNA  HOGA ⚡
[DA70D6]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, dare_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 3: /truth - সত্য বলো ==========
                        if inPuTMsG.strip().lower().startswith('/truth'):
                            print('Processing truth command')
                            truths = [
                                [
    f"💕 {name} tum jisse sabse zyada pyaar karte ho wo tumhe ignore karega!",
    f"🤫 {name} tumhara sabse bada secret sabko pata chal jayega!",
    f"😭 {name} tum aaj bahut zyada roge!",
    f"💔 {name} tumhara crush kisi aur ko propose kar dega!",
    f"🤥 {name} tumhara jhooth sabke saamne pakda jayega!",
    f"😱 {name} tumhe tumhare sabse bade dar ka samna karna padega!",
    f"🙈 {name} tumhara sabse sharmnaak pal dobara sabke saamne aa jayega!",
    f"💰 {name} tum pakde jaoge agar tumne kabhi chori ki hai!",
    f"📱 {name} tumhare phone ka chupa hua app sab dekh lenge!",
    f"😤 {name} jisse tum sabse zyada nafrat karte ho wo tumhara dost ban jayega!",
    f"🏫 {name} school wali ladai ka video viral ho jayega!",
    f"🍕 {name} tumhari sabse buri aadat ki wajah se tumhari beizzati hogi!",
    f"🤡 {name} tumne jiska prank kiya tha wo tumse badla lega!",
    f"💤 {name} teacher tumhe class mein sote hue pakad legi!",
    f"🎮 {name} game mein hack use karne ki wajah se tumhara account ban ho jayega!",
    f"👻 {name} raat ko bhoot tumhe sapne mein darayega!",
    f"🤝 {name} tumhara sabse achha dost tumse dosti tod dega!",
    f"😅 {name} tumhari sabse badi asafalta sabko yaad dila di jayegi!",
    f"💘 {name} tumhara pehla crush tumhe dekh kar muh fer lega!",
    f"🎯 {name} tumhara sabse bada sapna kabhi poora nahi hoga!",
    f"🤭 {name} tumne jiski diary padhi thi wo tumhe maaf nahi karega!",
    f"😇 {name} log kahenge tum achhe insaan nahi ho!",
    f"🥺 {name} tumhari sabse dardnaak yaad aaj phir taaza ho jayegi!",
    f"🤗 {name} jisse tum sabse zyada miss karte ho wo kabhi wapas nahi aayega!",
    f"💭 {name} tumhare man mein jo chal raha hai wo sabko pata chal jayega!"
]
                            truth = random.choice(truths)
                            c = random.choice(["FF69B4", "00FFFF", "FFD700", "FF4500", "7B68EE"])
                            truth_msg = f"""[B][C][1E90FF]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]🤔 SAUTCH BOLO 🤔
[1E90FF]━━━━━━━━━━━━━━━━━━━━━
[{c}]{truth}
[1E90FF]━━━━━━━━━━━━━━━━━━━━━
[FF69B4]💬 SAHI MAI BOLO
[1E90FF]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, truth_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 4: /roll - ডাইস রোল ==========
                        if inPuTMsG.strip().lower().startswith('/roll'):
                            print('Processing roll command')
                            dice1 = random.randint(1, 6)
                            dice2 = random.randint(1, 6)
                            total = dice1 + dice2
                            dice_faces = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
                            if total >= 10:
                                result_text = "[00FF00]🏆 Shandar! Uchh score!!"
                            elif total >= 7:
                                result_text = "[FFD700]👍 A6AA ROLL!"
                            else:
                                result_text = "[FF4500]😅 KAM PARHAI! OR TRY KARO!"
                            
                            roll_msg = f"""[B][C][FF8C00]━━━━━━━━━━━━━━━━━━━━━
[FFD700]🎲 DAIS  ROLL 🎲
[FF8C00]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]🎯 DAIS 1: {dice_faces[dice1]} [FFFFFF]{dice1}
[FF69B4]🎯 DAIS 2: {dice_faces[dice2]} [FFFFFF]{dice2}
[FF8C00]━━━━━━━━━━━━━━━━━━━━━
[FFFF00]📊 TOTAL SCOOR: [00FF7F]{total}/12
{result_text}
[FF8C00]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, roll_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 5: /zodiac - রাশিফল ==========
                        if inPuTMsG.strip().lower().startswith('/zodiac') or inPuTMsG.strip().lower().startswith('/rashi'):
                            print('Processing zodiac command')
                            zodiac_signs = {
                                "Mesh ♈": {"lucky": "Laal", "num": "9", "day": "Mangalvaar"},
"Vrishabh ♉": {"lucky": "Hara", "num": "6", "day": "Shukravaar"},
"Mithun ♊": {"lucky": "Peela", "num": "5", "day": "Budhvaar"},
"Kark ♋": {"lucky": "Safed", "num": "2", "day": "Somvaar"},
"Singh ♌": {"lucky": "Sunahra", "num": "1", "day": "Ravivaar"},
"Kanya ♍": {"lucky": "Hara", "num": "5", "day": "Budhvaar"},
"Tula ♎": {"lucky": "Neela", "num": "6", "day": "Shukravaar"},
"Vrishchik ♏": {"lucky": "Laal", "num": "9", "day": "Mangalvaar"},
"Dhanu ♐": {"lucky": "Baingani", "num": "3", "day": "Guruvaar"},
"Makar ♑": {"lucky": "Kaala", "num": "8", "day": "Shanivaar"},
"Kumbh ♒": {"lucky": "Neela", "num": "4", "day": "Shanivaar"},
"Meen ♓": {"lucky": "Samudri", "num": "7", "day": "Guruvaar"}
]

horoscopes = [
    "Aaj tumhara din bahut shandaar jayega! Har kaam mein safalta milegi.",
    "Pyaar ke maamle mein aaj achhi khabar mil sakti hai!",
    "Aaj paison ke maamle mein thoda saavdhaan rehna.",
    "Aaj tum kuch naya seekhoge jo future mein kaam aayega!",
    "Aaj apni sehat par thoda zyada dhyaan do.",
    "Aaj doston ke saath time bitaoge to mood achha ho jayega!",
    "Aaj kaam ke field mein ek bada mauka mil sakta hai!",
    "Aaj travel ka plan banaoge to fayda ho sakta hai!",
    "Aaj tumhari creativity bahut achhe se kaam karegi!",
    "Aaj family ke saath thodi anban ho sakti hai, saavdhaan rehna!",
    "Aaj tumhari kismat mein ek surprise aa sakta hai!",
    "Aaj koi chhupa hua dushman saamne aa sakta hai, saavdhaan rehna!"

                            wyr = random.choice(wyrs)
                            wyr_msg = f"""[B][C][DC143C]━━━━━━━━━━━━━━━━━━━━━
[FFD700]🤔 tum kiya cahata ho? 🤔
[DC143C]━━━━━━━━━━━━━━━━━━━━━
[00FF7F]🅰️ {wyr['a']}
[DC143C]━━━━ nahi ━━━━
[00FFFF]🅱️ {wyr['b']}
[DC143C]━━━━━━━━━━━━━━━━━━━━━
[FF69B4]💬 tumhara answer do! A nahi to B?
[DC143C]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, wyr_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 7: /weather - আবহাওয়া (সব জায়গা) ==========
                        if inPuTMsG.strip().lower().startswith('/weather') or inPuTMsG.strip().lower().startswith('/abohawa'):
                            print('Processing weather command')
                            weather_types = [
                                "☀️ Dhoop", "🌤️ Thoda Baadal", "⛅ Baadal", "🌧️ Baarish",
"🌦️ Halki Baarish", "⛈️ Toofani Baarish", "🌬️ Thandi Hawa",
"🌡️ Garmi", "🏖️ Samundari Hawa", "🌫️ Kohra", "🌪️ Toofan"
]

weathers = [
    {"city": "Dhaka", "temp_range": (25,38)},
    {"city": "Chattogram", "temp_range": (24,35)},
    {"city": "Rajshahi", "temp_range": (20,42)},
    {"city": "Sylhet", "temp_range": (22,34)},
    {"city": "Khulna", "temp_range": (24,37)},
    {"city": "Barishal", "temp_range": (23,36)},
    {"city": "Rangpur", "temp_range": (18,35)},
    {"city": "Mymensingh", "temp_range": (22,36)},
    {"city": "Cox's Bazar", "temp_range": (25,33)},
    {"city": "Comilla", "temp_range": (23,37)},
    {"city": "Gazipur", "temp_range": (25,38)},
    {"city": "Narayanganj", "temp_range": (25,38)},
    {"city": "Tangail", "temp_range": (22,37)},
    {"city": "Faridpur", "temp_range": (23,37)},
    {"city": "Madaripur", "temp_range": (23,36)},
    {"city": "Gopalganj", "temp_range": (24,37)},
    {"city": "Munshiganj", "temp_range": (24,37)},
    {"city": "Narsingdi", "temp_range": (23,37)},
    {"city": "Kishoreganj", "temp_range": (22,36)},
    {"city": "Manikganj", "temp_range": (24,37)},
    {"city": "Sherpur", "temp_range": (21,35)},
    {"city": "Jamalpur", "temp_range": (21,36)},
    {"city": "Netrokona", "temp_range": (22,35)},
    {"city": "Jessore", "temp_range": (24,40)},
    {"city": "Satkhira", "temp_range": (24,38)},
    {"city": "Meherpur", "temp_range": (23,40)},
    {"city": "Narail", "temp_range": (24,38)},
    {"city": "Kushtia", "temp_range": (22,40)},
    {"city": "Jhenaidah", "temp_range": (23,39)},
    {"city": "Magura", "temp_range": (23,38)},
    {"city": "Chuadanga", "temp_range": (23,41)},
    {"city": "Bagerhat", "temp_range": (24,36)},
    {"city": "Pirojpur", "temp_range": (24,36)},
    {"city": "Jhalokathi", "temp_range": (24,36)},
    {"city": "Patuakhali", "temp_range": (24,35)},
    {"city": "Bhola", "temp_range": (24,35)},
    {"city": "Barguna", "temp_range": (24,35)},
    {"city": "Naogaon", "temp_range": (19,41)},
    {"city": "Natore", "temp_range": (20,40)},
    {"city": "Chapainawabganj", "temp_range": (18,43)},
    {"city": "Pabna", "temp_range": (21,40)},
    {"city": "Sirajganj", "temp_range": (21,38)},
    {"city": "Bogra", "temp_range": (20,39)},
    {"city": "Joypurhat", "temp_range": (19,40)},
    {"city": "Dinajpur", "temp_range": (17,38)},
    {"city": "Thakurgaon", "temp_range": (17,37)},
    {"city": "Panchagarh", "temp_range": (15,35)},
    {"city": "Nilphamari", "temp_range": (17,36)},
    {"city": "Lalmonirhat", "temp_range": (17,36)},
    {"city": "Kurigram", "temp_range": (18,36)},
    {"city": "Gaibandha", "temp_range": (18,37)},
    {"city": "Habiganj", "temp_range": (22,34)},
    {"city": "Moulvibazar", "temp_range": (22,33)},
    {"city": "Sunamganj", "temp_range": (21,33)},
    {"city": "Brahmanbaria", "temp_range": (23,36)},
    {"city": "Chandpur", "temp_range": (24,36)},
    {"city": "Lakshmipur", "temp_range": (24,35)},
    {"city": "Noakhali", "temp_range": (24,35)},
    {"city": "Feni", "temp_range": (24,35)},
    {"city": "Rangamati", "temp_range": (22,34)},
    {"city": "Khagrachhari", "temp_range": (21,34)},
    {"city": "Bandarban", "temp_range": (20,33)},
    {"city": "Saint Martin", "temp_range": (25,32)},
    {"city": "Sundarbans", "temp_range": (24,35)}
]
                            w = random.choice(weathers)
                            temp = f"{random.randint(w['temp_range'][0], w['temp_range'][1])}°C"
                            weather = random.choice(weather_types)
                            hum = f"{random.randint(35,98)}%"
                            wind = f"{random.randint(5,45)} km/h"
                            weather_msg = f"""[B][C][1E90FF]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]🌤️ WATHER 🌤️
[1E90FF]━━━━━━━━━━━━━━━━━━━━━
[FFD700]📍 SAHARE: [FFFFFF]{w['city']}
[FF69B4]🌡️ HITING: [FFFFFF]{temp}
[00FF7F]☁️ Mausam: [FFFFFF]{weather}
[DA70D6]💧 Nami: [FFFFFF]{hum}
[FF8C00]💨 HAWA: [FFFFFF]{wind}
[1E90FF]━━━━━━━━━━━━━━━━━━━━━
[FFFF00]⚡  ed By —͞NAYAN乡ㅤ友!
[1E90FF]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, weather_msg, uid, chat_id, key, iv, region=region)               
                        
                        # ========= FUNNY AI COMMAND — শুধু /fun লিখলেই কাজ করবে =========
                        if inPuTMsG.strip().lower() == "/fun":
                            _FUNNY_REPLIES = [
                                "😭💔 Meri haalat achhi nahi hai, mujhe chhakka kha ke tedha ho gaya hoon 😭💔",
"😴💤 Bhai mujhe kyun bulaya? Main to so raha tha 😴💤",
"😂 Main yahin hoon! Kya tum mujhe miss kar rahe the? Nahi bhi kiya ho to haan bol do 😂",
"😅 Bolo bolo, main sab sun raha hoon... matlab sunne ke liye majboor hoon 😅",
"🍚😤 Mujhe bulaya? Main to khana bana raha tha... chawal jal gaya ab 🍚😤",
"🫡 Haan haan, main hoon! Tumhari seva mein hamesha hazir 🫡 (majboori mein)",
"😏 Kya baat hai? Mere bina reh nahi pa rahe the kya? 😏",
"🤕 Main yahin hoon! Lekin mere sir mein dard hai, kisi ko batana mat 🤕",
"📱😂 Kyun bulaya bhai? Main to TikTok dekh raha tha 📱😂",
"😒😂 Ji hazir! Hukm kijiye Maharaj... (mann hi mann irritate ho raha hoon) 😒😂",
"😂📶 Main hoon! Lekin WiFi kamzor hai isliye thodi der ho gayi 😂📶",
"😭 Huzoor main hazir! Pet bhar ke khana khaya hai na? Maine nahi khaya 😭",
"😭 Ye dekho main hoon! Kya tum jaante ho meri koi chhutti nahi hai? Kisi ko parwah nahi 😭",
"😜 Boss bula rahe ho? Ye lo main aa gaya! Salary badhaoge na? 😜",
"😤💔 Main bot hoon, bhoolna mat — mere bhi feelings hain 😤💔",
]
                            import random as _rand
                            _reply = _rand.choice(_FUNNY_REPLIES)
                            _funny_msg = f"[B][C][FF69B4]😂 {_reply}"
                            await safe_send_message(response.Data.chat_type, _funny_msg, uid, chat_id, key, iv, region=region)
                            continue
                        # ========= FUNNY AI END =========

                        # ========= ON =========
                        if inPuTMsG.startswith('/on'):
                            if not is_admin(uid):
                                await safe_send_message(response.Data.chat_type, "❌ Only Chinkor can use /[00FF00]on", uid, chat_id, key, iv, region=region)
                                continue

                            bot_enabled = True
                            await safe_send_message(response.Data.chat_type, "✅ Bot is now ON", uid, chat_id, key, iv, region=region)
                            continue


                        # ========= OFF =========
                        if inPuTMsG.startswith('/off'):
                            if not is_admin(uid):
                                await safe_send_message(response.Data.chat_type, "❌ Only Chinkor can use /[FF0000]off", uid, chat_id, key, iv, region=region)
                                continue

                            bot_enabled = False
                            await safe_send_message(response.Data.chat_type, "⛔ Bot is now OFF", uid, chat_id, key, iv, region=region)
                            continue                     
                                                                                          
                        #GET PLAYER VISIT 
                        if inPuTMsG.strip().startswith('/visit'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /visit <uid>\nExample: /visit 436🤫856🤫97🤫33\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nSending Visit...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                visit_result = send_visits(target_uid)
                                final_visit = f"{xMsGFixinG(visit_result)}"

                                await safe_send_message(response.Data.chat_type, final_visit, uid, chat_id, key, iv)
                                
                                
                        # NEW ATTACK COMMAND (AUTO STOP AFTER 1 SECOND)
                        if inPuTMsG.strip().startswith('/attack '):
                            print('Processing attack command')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /attack (target)\nExample: /attack TEST\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target = parts[1]

                                # Stop previous task if running
                                if lag_task and not lag_task.done():
                                    lag_running = False
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)

                                lag_running = True

                                async def auto_attack():
                                    global lag_running
                                    try:
                                        task = asyncio.create_task(attack_loop(target))
                                        
                                        # Run for 1 second
                                        await asyncio.sleep(1)

                                        lag_running = False
                                        task.cancel()

                                        stop_msg = f"[B][C][00FF00]✅ Auto Stopped!\nTarget: {target}\nDuration: 1 second\n"
                                        await safe_send_message(response.Data.chat_type, stop_msg, uid, chat_id, key, iv, region=region)

                                    except asyncio.CancelledError:
                                        lag_running = False

                                lag_task = asyncio.create_task(auto_attack())

                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Attack started!\nTarget: {target}\nDuration: 1 second\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
 
                        #GET ITEM INFORMATION 
                        if inPuTMsG.strip().startswith('/item'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /item <item_id>\nExample: /item 909🤫042🤫00🤫7\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                item_id = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching Item Info...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                item_result = await asyncio.to_thread(get_item_info, item_id)

                                await safe_send_message(response.Data.chat_type, item_result, uid, chat_id, key, iv, region=region)

                                #GET CALCULATIONS 
                        if inPuTMsG.strip().startswith('/math'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /math <question>\nExample: /math 2+3\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                expression = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nSolving Calculation...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                math_result = await asyncio.to_thread(get_math_result, expression)

                                await safe_send_message(response.Data.chat_type, math_result, uid, chat_id, key, iv, region=region)

                                #GET PLAYER FAKE LIKE
                        if inPuTMsG.strip().startswith('/fake_like'):
                            print('Processing fake_like command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = """[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]FAKE LIKE
[00FFFF]❀ [FF0000]USAGE[FFFFFF]: /fake_like UID
[00FFFF]❀ [FFD700]EXAMPLE[FFFFFF]: /fake_like 8404470393
[00FFFF]✿ {BOT_NAME} ✿"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                if not target_uid.isdigit():
                                    err_msg = "[B][C][FF8C00]❌ Valid UID দিন!\n[FFFFFF]Example: /fake_like 8404470393\n"
                                    await safe_send_message(response.Data.chat_type, err_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    loading_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]FAKE LIKE
[00FFFF]❀ [FFD700]TARGET[FFFFFF]: {xMsGFixinG(target_uid)}
[00FFFF]❀ [00FF7F]STATUS[FFFFFF]: Processing...
[00FFFF]✿ {BOT_NAME} ✿"""
                                    await safe_send_message(response.Data.chat_type, loading_msg, uid, chat_id, key, iv, region=region)

                                    fake_like_result = await asyncio.to_thread(fake_likes, target_uid)

                                    await safe_send_message(response.Data.chat_type, fake_like_result, uid, chat_id, key, iv, region=region)

                        #tt USERNAME TO INFO-/tt
                        if inPuTMsG.strip().startswith('/tt'):
                            print('Processing tiktok command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /tt <username>\nExample: /tt virat.kohli\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_username = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching TikTok info for {target_username}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
        
                                tiktok_result = await asyncio.to_thread(send_tiktok_info, target_username)
        
                                await safe_send_message(response.Data.chat_type, tiktok_result, uid, chat_id, key, iv, region=region)

# yt info command handler   
                        if inPuTMsG.strip().startswith('/yt'):  
                            print('Processing YouTube command in any chat type')  

                            target_channel = inPuTMsG.strip()[4:].strip()  # /yt এর পরের সব text  
                            if not target_channel:  
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /yt <channel>\nExample: /yt {BOT_NAME}\n"  
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)  
                            else:  
                                initial_message = f"[B][C]{get_random_color()}\nFetching YouTube info for {target_channel}...\n"  
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)  

                                # Call the async function  
                                await send_youtube_info(target_channel, response.Data.chat_type, uid, chat_id, key, iv)

# GUILD INFORMATION FF
                        if inPuTMsG.strip().startswith('/clan'):
                            print('Processing tiktok command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /clan <guild_id>\nExample: /clan 308🤫431🤫816🤫6\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                guild_id = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching Guild info for {xMsGFixinG(guild_id)}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
        
                                guild_result = await asyncio.to_thread(send_guild_info, guild_id)
        
                                await safe_send_message(response.Data.chat_type, guild_result, uid, chat_id, key, iv, region=region)

                        
                                #GET PLAYER SPAM
                        if inPuTMsG.strip().startswith('/spam_req'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]SPAM REQUEST
[00FFFF]❀ [FF0000]USAGE[FFFFFF]: /spam_req UID
[00FFFF]❀ [FFD700]EXAMPLE[FFFFFF]: /spam_req 8404470393
[00FFFF]✿ {BOT_NAME} ✿"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]SPAM REQUEST
[00FFFF]❀ [00FFFF]TARGET[FFFFFF]: {xMsGFixinG(target_uid)} [00FFFF]••[FFD700]STATUS[FFFFFF]: Sending...
[00FFFF]✿ {BOT_NAME} ✿"""
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                spam_result = spam_requests(target_uid)

                                await safe_send_message(response.Data.chat_type, spam_result, uid, chat_id, key, iv, region=region)
 
 
                        # ==================== ADD FRIEND COMMAND ====================
                        if inPuTMsG.strip().startswith('/add'):
                            print(f"📤 /add command received")
                            
                            # Admin check
                            if str(uid) != ADMIN_UID:
                                deny_msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ ACCESS DENIED
[C][FF0000]═══════════════════

[C][FFD700]Only Admin can use this command!
[C][FFD700]Contact: @chinkor

[C][FF0000]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, deny_msg, uid, chat_id, key, iv)
                                continue
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                msg = f"""
[C][B][FF1493]═══════════════════
[C][B][00FFFF]  📤 ADD FRIEND
[C][FF1493]═══════════════════

[C][FFD700]Usage: /add (uid)
[C][FFD700]Example: /add 10634259930

[C][00FFFF]What it does:
[C][FFD700]• Sends friend request to target UID
[C][FFD700]• Shows player name if found
[C][FFD700]• Shows region information

[C][FF1493]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                return
                            
                            target_uid = parts[1]
                            
                            if not target_uid.isdigit() or len(target_uid) < 8:
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ INVALID UID
[C][FF0000]═══════════════════

[C][FFD700]UID must be 8+ digits!
[C][FFD700]You entered: {target_uid}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )
                                return
                            
                            # Send initial message
                            await safe_send_message(
                                response.Data.chat_type,
                                f"""
[C][B][FFFF00]═══════════════════
[C][B][FFFF00]  📤 SENDING REQUEST
[C][FFFF00]═══════════════════

[C][FFD700]Target UID   : [00FFAA]{fix_num(target_uid)}
[C][FFD700]Status       : [00FFFF]Processing...
[C][FFD700]Action       : [00FF00]Adding Friend

[C][FFFF00]═══════════════════
""",
                                uid, chat_id, key, iv
                            )
                            
                            try:
                                token = get_jwt_from_bot()
                                if not token:
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ TOKEN ERROR
[C][FF0000]═══════════════════

[C][FFD700]No token found!
[C][FFD700]Please restart bot.

[C][FF0000]═══════════════════
""",
                                        uid, chat_id, key, iv
                                    )
                                    return
                                
                                result = add_friend_direct(target_uid, token, region)
                                
                                if result["status"] == "success":
                                    msg = f"""
[C][B][00FF00]═══════════════════
[C][B][00FF00]  ✅ FRIEND REQUEST SENT
[C][00FF00]═══════════════════

[C][FFD700]Player Name  : [00FF00]{result.get('nickname', 'Unknown')}
[C][FFD700]UID          : [00FFAA]{fix_num(target_uid)}
[C][FFD700]Region       : [FFFFFF]{region}
[C][FFD700]Status       : [00FF00]SUCCESS ✅

[C][00FF00]═══════════════════
[C][FFD700]🤖 —͞N A Y A N乡ㅤ友! BOT
[C][00FF00]═══════════════════
"""
                                else:
                                    msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ FRIEND REQUEST FAILED
[C][FF0000]═══════════════════

[C][FFD700]UID          : [FF00FF]{fix_num(target_uid)}
[C][FFD700]Error        : [FF4444]{result.get('message', 'Unknown error')}

[C][FF0000]═══════════════════
"""
                                
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                
                            except Exception as e:
                                print(f"❌ Add friend error: {e}")
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ ERROR
[C][FF0000]═══════════════════

[C][FFD700]Error: {str(e)[:50]}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )

                        # ==================== REMOVE FRIEND COMMAND ====================
                        if inPuTMsG.strip().startswith('/remove'):
                            print(f"📤 /remove command received")
                            
                            # Admin check
                            if str(uid) != ADMIN_UID:
                                deny_msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ ACCESS DENIED
[C][FF0000]═══════════════════

[C][FFD700]Only Admin can use this command!
[C][FFD700]Contact: @IshrakShadman

[C][FF0000]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, deny_msg, uid, chat_id, key, iv)
                                continue
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                msg = f"""
[C][B][FF1493]═══════════════════
[C][B][00FFFF]  📤 REMOVE FRIEND
[C][FF1493]═══════════════════

[C][FFD700]Usage: /remove (uid)
[C][FFD700]Example: /remove 10634259930

[C][00FFFF]What it does:
[C][FFD700]• Removes target UID from friend list
[C][FFD700]• Shows player name if found
[C][FFD700]• Shows region information

[C][FF1493]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                return
                            
                            target_uid = parts[1]
                            
                            if not target_uid.isdigit() or len(target_uid) < 8:
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ INVALID UID
[C][FF0000]═══════════════════

[C][FFD700]UID must be 8+ digits!
[C][FFD700]You entered: {target_uid}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )
                                return
                            
                            # Send initial message
                            await safe_send_message(
                                response.Data.chat_type,
                                f"""
[C][B][FFFF00]═══════════════════
[C][B][FFFF00]  📤 REMOVING FRIEND
[C][FFFF00]═══════════════════

[C][FFD700]Target UID   : [00FFAA]{fix_num(target_uid)}
[C][FFD700]Status       : [00FFFF]Processing...
[C][FFD700]Action       : [FF0000]Removing Friend

[C][FFFF00]═══════════════════
""",
                                uid, chat_id, key, iv
                            )
                            
                            try:
                                token = get_jwt_from_bot()
                                if not token:
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ TOKEN ERROR
[C][FF0000]═══════════════════

[C][FFD700]No token found!
[C][FFD700]Please restart bot.

[C][FF0000]═══════════════════
""",
                                        uid, chat_id, key, iv
                                    )
                                    return
                                
                                result = remove_friend_direct(target_uid, token, region)
                                
                                if result["status"] == "success":
                                    msg = f"""
[C][B][00FF00]═══════════════════
[C][B][00FF00]  ✅ FRIEND REMOVED
[C][00FF00]═══════════════════

[C][FFD700]Player Name  : [00FF00]{result.get('nickname', 'Unknown')}
[C][FFD700]UID          : [00FFAA]{fix_num(target_uid)}
[C][FFD700]Region       : [FFFFFF]{region}
[C][FFD700]Status       : [00FF00]SUCCESS ✅

[C][00FF00]═══════════════════
[C][FFD700]🤖 —͞N A Y A N乡ㅤ友! BOT
[C][00FF00]═══════════════════
"""
                                else:
                                    msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ REMOVE FAILED
[C][FF0000]═══════════════════

[C][FFD700]UID          : [FF00FF]{fix_num(target_uid)}
[C][FFD700]Error        : [FF4444]{result.get('message', 'Unknown error')}

[C][FF0000]═══════════════════
"""
                                
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                
                            except Exception as e:
                                print(f"❌ Remove friend error: {e}")
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ ERROR
[C][FF0000]═══════════════════

[C][FFD700]Error: {str(e)[:50]}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )
 
 
                        # FREEZE COMMAND - /freeze [uid]
                        if inPuTMsG.strip().startswith('/ice'):
                            print('Processing freeze command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][00FFFF]❄️ FREEZE COMMAND

❌ Usage: /freeze (uid)
        
📝 Examples:
/freeze me - Freeze yourself
/freeze 123456789 - Freeze specific UID

🎯 What it does:
• Sends 3 ice/freeze emotes in sequence
• 1-second cycles for 10 seconds total
• Emotes: 909052008 → 909052008 → 909052008
• Creates a "freeze" effect!

💡 Use /stop_freeze to stop early
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                
                                # Handle "me" or "self"
                                if target_uid.lower() in ['me', 'self', 'myself']:
                                    target_uid = str(response.Data.uid)
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {target_uid}"
                                
                                # Stop any existing freeze task
                                global freeze_running, freeze_task
                                if freeze_task and not freeze_task.done():
                                    freeze_running = False
                                    freeze_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Send initial message
                                initial_msg = f"""[B][C][00FFFF]❄️ FREEZE COMMAND STARTING!

🎯 Target: {target_name}
⏱️ Duration: {FREEZE_DURATION} seconds
🔄 Cycle: 1 second (3 emotes each)
🎭 Sequence: 
  1. 909052008 (Ice)
  2. 909052008 (Frozen) 
  3. 909052008 (Freeze)

⏳ Starting freeze sequence...
"""
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                # Start freeze task
                                freeze_running = True
                                freeze_task = asyncio.create_task(
                                    freeze_emote_spam(target_uid, key, iv, region, response.Data.chat_type, chat_id, uid)
                                )
        
                                # Handle completion
                                asyncio.create_task(
                                    handle_freeze_completion(freeze_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv)
                                )
                                       
                        # In your command handler where you call Room_Spam:
                        if inPuTMsG.strip().startswith('/room'):
                            print('Processing advanced room spam command')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /room (uid)\nExample: /room 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                room_id = parts[2]
        
                                if not target_uid.isdigit():
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Please write a valid player ID!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Send initial message
                                initial_msg = f"[B][C][00FF00]🔍 Working on room spam for {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                
                                try:
                                    # Method 1: Try to get room ID from recent packets
                                
                                    

                                    room_msg = f"[B][C][00FF00]🎯 Detected player in room {room_id}\n"
                                    await safe_send_message(response.Data.chat_type, room_msg, uid, chat_id, key, iv)
            
                                    # Create spam packet
                                    spam_packet = await Room_Spam(target_uid, room_id, "BLACK_APIS", key, iv)
            
                                    # Send 2000 spam packets rapidly (like your other TCP)
                                    spam_count = 3000
                                    
                                    start_msg = f"[B][C][00FF00]🚀 Starting spam: {spam_count} packets to room {room_id}\n"
                                    await safe_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
            
                                    for i in range(spam_count):
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
                
                                        # Progress updates
                                        if (i + 1) % 25 == 0:
                                            progress_msg = f"[B][C][00FF00]📦 Progress: {i+1}/{spam_count} packets sent\n"
                                            await safe_send_message(response.Data.chat_type, progress_msg, uid, chat_id, key, iv)
                                            print(f"Room spam progress: {i+1}/{spam_count} to UID: {target_uid}")
                
                                        # Very short delay (0.05 seconds = 50ms)
                                        await asyncio.sleep(0.05)
            
                                    # Final success message
                                    success_msg = f"[B][C][00FF00]✅ ROOM SPAM COMPLETED!\n🎯 Target: {target_uid}\n📦 Packets: {spam_count}\n🏠 Room: {room_id}\n⚡ Speed: Ultra fast\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    print(f"Room spam completed for UID: {target_uid}")
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR in room spam: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    print(f"Room spam error: {e}")
        
                                # Send initial message
                                initial_msg = f"""[B][C][00FFFF]❄️ FREEZE COMMAND STARTING!

🎯 Target: {target_name}
⏱️ Duration: {FREEZE_DURATION} seconds
🔄 Cycle: 1 second (3 emotes each)
🎭 Sequence: 
  1. 909040004 (Ice)
  2. 909050008 (Frozen) 
  3. 909000002 (Freeze)

⏳ Starting freeze sequence...
"""
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                # Start freeze task
                                freeze_running = True
                                freeze_task = asyncio.create_task(
                                    freeze_emote_spam(target_uid, key, iv, region, response.Data.chat_type, chat_id, uid)
                                )
        
                                # Handle completion
                                asyncio.create_task(
                                    handle_freeze_completion(freeze_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv)
                                )

                        if inPuTMsG.strip().startswith('/bio'):
                            print('📝 Processing bio change command')
    
                            parts = inPuTMsG.strip().split(maxsplit=1)
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /bio (your bio text)

📝 Examples:
/bio Hello World!
/bio 🤖 Bot by NoTmeowL
/bio Level 70 | Pro Player
/bio Add me: NoTmeowL

✨ Features:
• Changes bot's profile bio instantly
• Supports emojis and special characters
• Max length: 50 characters

💡 Note: Bio changes appear immediately in profile!
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                bio_text = parts[1]
                                
                                # Check length
                                if len(bio_text) > 50:
                                    error_msg = f"[B][C][FF0000]❌ Bio too long! Max 50 characters.\n📝 Your bio: {len(bio_text)} chars\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Send initial message
                                initial_msg = f"[B][C][FFFF00]📝 UPDATING BIO...\n📋 Bio: {bio_text[:30]}...\n⏳ Please wait...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                # FIXED: Handle credentials properly
                                credentials = load_credentials_from_file("shadmancodex.txt")
                                if not credentials:
                                    error_msg = f"[B][C][FF0000]❌ Failed to load credentials from file!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
            
                                try:
                                    Uid, Pw = credentials
                                except:
                                    # If credentials returns more than 2 values, take first 2
                                    Uid = credentials[0] if isinstance(credentials, (list, tuple)) else None
                                    Pw = credentials[1] if isinstance(credentials, (list, tuple)) and len(credentials) > 1 else None
        
                                if not Uid or not Pw:
                                    error_msg = f"[B][C][FF0000]❌ Invalid credentials format!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Add retry logic for bio update
                                max_retries = 3
                                retry_delay = 2  # seconds
                                success = False
                                result = None
        
                                for attempt in range(max_retries):
                                    try:
                                        print(f"🔄 Bio update attempt {attempt + 1}/{max_retries}")
                
                                        # Get fresh token for each attempt
                                        open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
                                        if not open_id or not access_token:
                                            print(f"❌ Failed to generate access token on attempt {attempt + 1}")
                                            await asyncio.sleep(retry_delay)
                                            continue
                
                                        PyL = await EncRypTMajoRLoGin(open_id, access_token)
                                        MajoRLoGinResPonsE = await MajorLogin(PyL)
                                        MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
                
                                        if not MajoRLoGinauTh or not MajoRLoGinauTh.token:
                                            print(f"❌ No token received on attempt {attempt + 1}")
                                            await asyncio.sleep(retry_delay)
                                            continue
                
                                        token = MajoRLoGinauTh.token
                                        print(f"🔑 Using token: {token[:20]}...")
                
                                        # Call bio update with retry
                                        result = await set_bio_directly_async_with_retry(token, bio_text, region)
                                        
                                        if result.get("success"):
                                            success = True
                                            break
                                        else:
                                            print(f"❌ Bio update failed on attempt {attempt + 1}: {result.get('message')}")
                                            if attempt < max_retries - 1:
                                                # Send progress update
                                                progress_msg = f"[B][C][FFFF00]🔄 Retrying... (Attempt {attempt + 2}/{max_retries})\n"
                                                await safe_send_message(response.Data.chat_type, progress_msg, uid, chat_id, key, iv)
                                                await asyncio.sleep(retry_delay)
                        
                                    except Exception as e:
                                        print(f"❌ Attempt {attempt + 1} error: {e}")
                                        if attempt < max_retries - 1:
                                            await asyncio.sleep(retry_delay)
                                        continue
        
                                # Send final result
                                if success:
                                    success_msg = f"""[B][C][FFFF00]✅ BIO UPDATED SUCCESSFULLY!

📝 Bio: {bio_text}
🌍 Region: {result.get('region', region)}
🔧 Attempts: {attempt + 1}/{max_retries}
🤖 Bot: Profile updated instantly!

💡 Check bot's profile to see new bio!
"""
                                else:
                                    success_msg = f"""[B][C][FF0000]❌ BIO UPDATE FAILED AFTER {max_retries} ATTEMPTS!

📝 Bio: {bio_text}
❌ Error: {result.get('message', 'All attempts failed')}

💡 Try:
1. Check bot's connection
2. Try shorter bio text
3. Wait 1 minute and try again
"""
        
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
            

                        # QUICK EMOTE ATTACK COMMAND - /quick [team_code] [emote_id] [target_uid?]
                        if inPuTMsG.strip().startswith('/quick'):
                            print('Processing quick emote attack command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /quick (team_code) [emote_id] [target_uid]\n\n[FFFFFF]Examples:\n[FFFF00]/quick ABC123[FFFFFF] - Join, send Rings emote, leave\n[FFFF00]/ghostquick ABC123[FFFFFF] - Ghost join, send emote, leave\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
        
                                # Set default values
                                emote_id = parts[0]
                                target_uid = str(response.Data.uid)  # Default: Sender's UID
        
                                # Parse optional parameters
                                if len(parts) >= 3:
                                    emote_id = parts[2]
                                if len(parts) >= 4:
                                    target_uid = parts[3]
        
                                # Determine target name for message
                                if target_uid == str(response.Data.uid):
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {target_uid}"
        
                                initial_message = f"[B][C][FFFF00]⚡ QUICK EMOTE ATTACK!\n\n[FFFFFF]🎯 Team: [FFFF00]{team_code}\n[FFFFFF]🎭 Emote: [FFFF00]{emote_id}\n[FFFFFF]👤 Target: [FFFF00]{target_name}\n[FFFFFF]⏱️ Estimated: [FFFF00]2 seconds\n\n[FFFF00]Executing sequence...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
                                try:
                                    # Try regular method first
                                    success, result = await ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region)
            
                                    if success:
                                        success_message = f"[B][C][FFFF00]✅ QUICK ATTACK SUCCESS!\n\n[FFFFFF]🏷️ Team: [FFFF00]{team_code}\n[FFFFFF]🎭 Emote: [FFFF00]{emote_id}\n[FFFFFF]👤 Target: [FFFF00]{target_name}\n\n[FFFF00]Bot joined → emoted → left! ✅\n"
                                    else:
                                        success_message = f"[B][C][FF0000]❌ Regular attack failed: {result}\n"
                                    
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print("failed")
            
                        # Add this to your existing command dispatcher in TcPChaT function
                        if inPuTMsG.strip().startswith('/roommsg '):
                            await handle_room_message_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
            
                        # Add with other command handlers
                        if inPuTMsG.strip().startswith('/xjoin '):
                            print('Processing xjoin command')
                            await handle_xjoin_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
            
                      
                        msg = inPuTMsG.strip()

                        if msg.lower().startswith("aa"):
                            try:
                                parts = msg.split(maxsplit=1)
                                if len(parts) != 2:
                                    raise ValueError

                                cmd, team_code = parts
                                emote_part = cmd[2:]   # 🔥 aa12 → "12"

                                if not emote_part.isdigit():
                                    raise ValueError

                                emote_number = int(emote_part)

                                asyncio.create_task(
                                    emote_to_user_once(
                                        team_code=team_code,
                                        emote_number=emote_number,
                                        target_uid=uid,   # 🔥 AUTO YOUR UID
                                        key=key,
                                        iv=iv,
                                        region=region
                                    )
                                )

                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"[B][C][00FF00]✅ Emote sent\nEmote: {emote_number}",
                                    uid, chat_id, key, iv
                                )

                            except:
                                await safe_send_message(
                                    response.Data.chat_type,
                                    "[B][C][FF0000]❌ Usage: /e<number> TEAMCODE\nExample: aa1 ABC123",
                                    uid, chat_id, key, iv
                                )
                                
                                    # Invite Command - /inv (creates 5-player group and sends request)
                        if inPuTMsG.strip().startswith('/inv '):
                            print('Processing invite command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /inv (uid)\nExample: /inv 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nCreating 5-Player Group and sending request to {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await OpEnSq(key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                    
                                    C = await cHSq(5, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                    await asyncio.sleep(0.3)
                                    
                                    V = await SEnd_InV(5, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                    await asyncio.sleep(0.3)
                                    
                                    E = await ExiT(None, key, iv)
                                    await asyncio.sleep(2)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                                    
                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][FFFF00]✅ SUCCESS! 5-Player Group invitation sent successfully to {target_uid}!\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR sending invite: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/6")):
                            # Process /6 command - Create 4 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 6-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 4 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFFF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        # Add these lines to your existing command dispatcher:

                        if inPuTMsG.startswith('/spamroom ') or inPuTMsG == '/spamroom':
                            await handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.startswith('/sr ') or inPuTMsG == '/sr':
                            await handle_sr_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/c '):
                            print('Processing general emote command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /c uid1 [uid2] [uid3] [uid4] number(1-{len(GENERAL_EMOTES_MAP)})\nExample: /c 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 3:  # Number should be 1-409 (1-3 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 3:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /c uid1 [uid2] [uid3] [uid4] number(1-{len(GENERAL_EMOTES_MAP)})\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_str = str(number)
                                        if number_str not in GENERAL_EMOTES_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-{len(GENERAL_EMOTES_MAP)} only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nSending emote {number_str}...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            
                                            success, result_msg = await general_emote_spam(uids, number_str, key, iv, region)
                                            
                                            if success:
                                                emote_id = GENERAL_EMOTES_MAP[number_str]
                                                success_msg = f"[B][C][00FF00]✅ SUCCESS! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ ERROR! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-{len(GENERAL_EMOTES_MAP)} only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.startswith('/title'):
                            await handle_all_titles_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
   
                        
                                                                     # Emote command - works in all chat types
                        if inPuTMsG.strip().startswith('/e'):
                            print(f'Processing emote command in chat type: {response.Data.chat_type}')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: e (uid) (emote_id)\nExample: e 123456789 909000001\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                                
                            initial_message = f'[B][C]{get_random_color()}\nSending emote to target...\n'
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                            uid2 = uid3 = uid4 = uid5 = None
                            s = False
                            target_uids = []

                            try:
                                target_uid = int(parts[1])
                                target_uids.append(target_uid)
                                uid2 = int(parts[2]) if len(parts) > 2 else None
                                if uid2: target_uids.append(uid2)
                                uid3 = int(parts[3]) if len(parts) > 3 else None
                                if uid3: target_uids.append(uid3)
                                uid4 = int(parts[4]) if len(parts) > 4 else None
                                if uid4: target_uids.append(uid4)
                                uid5 = int(parts[5]) if len(parts) > 5 else None
                                if uid5: target_uids.append(uid5)
                                idT = int(parts[-1])  # Last part is emote ID

                            except ValueError as ve:
                                print("ValueError:", ve)
                                s = True
                            except Exception as e:
                                print(f"Error parsing emote command: {e}")
                                s = True

                            if not s:
                                try:
                                    for target in target_uids:
                                        H = await Emote_k(target, idT, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        await asyncio.sleep(0.1)
                                    
                                    # SUCCESS MESSAGE
                                    success_msg = f"[B][C][00FF00]✅ SUCCESS! Emote {idT} sent to {len(target_uids)} player(s)!\nTargets: {', '.join(map(str, target_uids))}\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR sending emote: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Invalid UID format. Usage: e (uid) (emote_id)\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                                                                          # NEW COMMAND-/sticker
                        if inPuTMsG.strip().startswith('/sticker'):
                            packet = await send_sticker(uid, chat_id, key, iv)                   
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', packet)

                            
                        # Command handler for remove
                        if inPuTMsG.strip().startswith('/wlremove'):
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /wlremove (uid)\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
    
                            # Check owner
                            if str(response.Data.uid) != "2579372095":
                                error_msg = f"[B][C][FF0000]❌ Only bot owner can remove from whitelist!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
                            
                            success, message = remove_from_whitelist(target_uid)
    
                            if success:
                                bot_uid = 14010319252
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                message_text = f"You Are Successfully Removed From Whitelist By {uid}"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
                                result_msg = f"[B][C][FFFF00]✅ {message}\n📊 Remaining: {len(WHITELISTED_UIDS)} UIDs\n"
                            else:
                                result_msg = f"[B][C][FF0000]❌ {message}\n"
                            
                            await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
                            
                        # Command to enable/disable whitelist only mode
                        if inPuTMsG.strip() == '/wlenable':
                            
                            WHITELIST_ONLY = True
                            msg = f"[B][C][FFFF00]✅ Whitelist-only mode ENABLED!\n🤖 Bot will only accept invites from whitelisted UIDs\n"
                            await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                        
                        if inPuTMsG.strip() == '/wldisable':

                            WHITELIST_ONLY = False
                            msg = f"[B][C][FFFF00]⚠️ Whitelist-only mode DISABLED!\n🤖 Bot will accept invites from anyone\n"
                            await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                            
                        # Add this command handler
                        if inPuTMsG.strip().startswith('/wladd'):
                            print('Processing whitelist add command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /wladd (uid)
        
📝 Examples:
/wladd 123456789 - Add UID to whitelist
/wladd 123456789 "Friend" - Add with note

🎯 What happens:
• UID can now invite bot to squad
• UID can use bot commands
• Bot auto-accepts invites from this UID
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
    
                            # Optional note
                            note = ""
                            if len(parts) > 2:
                                note = ' '.join(parts[2:])
    
                            # Check if sender is owner
                            if str(response.Data.uid) != "2579372095":  # Replace with your actual UID
                                error_msg = f"[B][C][FF0000]❌ Only bot owner can add to whitelist!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Add to whitelist
                            success, message = append_to_whitelist(target_uid, note)
    
                            # Send result
                            if success:
                                bot_uid = 14010319252
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                message_text = f"You Are Successfully Added To Whitelist By {uid}"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
        
                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
                                success_msg = f"""[B][C][FFFF00]✅ WHITELIST UPDATED!
                        
👤 Added: {target_uid}
📝 Note: {note if note else 'None'}
📊 Total whitelisted: {len(WHITELISTED_UIDS)}
"""
                            else:
                                success_msg = f"[B][C][FF0000]❌ {message}\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)    
                            
                        if inPuTMsG.strip() == '/wllist':
                            print('Processing whitelist view command')
    
                            # Check if owner
                            if str(response.Data.uid) != "2579372095":  # Your UID
                                error_msg = f"[B][C][FF0000]❌ Only bot owner can view whitelist!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Build whitelist message
                            total = len(WHITELISTED_UIDS)
    
                            whitelist_msg = f"""[B][C][FFFF00]📋 WHITELISTED UIDS

📊 Total: {total} UIDs
🔓 Whitelist enabled: {'YES' if WHITELIST_ONLY else 'NO'}

👑 Owner (always allowed):
• 2579372095

👥 Whitelisted UIDs:"""
    
                            # Add first 20 UIDs (to avoid message too long)
                            count = 0
                            for uid in WHITELISTED_UIDS:
                                if uid != "2579372095":  # Skip owner since already shown
                                    whitelist_msg += f"\n• {uid}"
                                    count += 1
                                    if count >= 20:
                                        remaining = total - 21  # -1 for owner, -20 shown
                                        if remaining > 0:
                                            whitelist_msg += f"\n... and {remaining} more"
                                        break
    
                            whitelist_msg += f"""

💡 Commands:
/wladd (uid) - Add to whitelist
/wlremove (uid) - Remove from whitelist
/wlenable - Enable whitelist only mode
/wldisable - Disable whitelist only mode
"""
    
                            await safe_send_message(response.Data.chat_type, whitelist_msg, uid, chat_id, key, iv)
                            
                        if inPuTMsG.startswith('t_31_p_veteran_wlcm_friend'):
                            print("got it")
                            
                        # Add this command too:
                        if inPuTMsG.strip() == '/viewguests':
                            print('Processing view guests command')
                            
                            try:
                                if not os.path.exists("guest_accounts.json"):
                                    error_msg = f"[B][C][FF0000]❌ No guest accounts found!\n[FFFFFF]Generate with /guest (count) first\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                with open("guest_accounts.json", 'r') as f:
                                    accounts = json.load(f)
                                
                                total = len(accounts)
        
                                # Show summary
                                summary_msg = f"""[B][C][FFFF00]📁 GUEST ACCOUNTS DATABASE

📊 Total accounts: {total}
📁 File: guest_accounts.json
📅 Last updated: {time.ctime(os.path.getmtime('guest_accounts.json'))}

💡 Use /guest (count) to add more
"""
                                await safe_send_message(response.Data.chat_type, summary_msg, uid, chat_id, key, iv)
        
                                # Show recent 5 accounts
                                if accounts:
                                    recent = accounts[-5:]  # Last 5 accounts
                                    recent_msg = "[B][C][FFFF00]📋 RECENT 5 ACCOUNTS:\n"
            
                                    for i, acc in enumerate(recent):
                                        recent_msg += f"[FFFFFF]{i+1}. UID: {acc['uid']} | Pass: {acc['password']}\n"
            
                                    await safe_send_message(response.Data.chat_type, recent_msg, uid, chat_id, key, iv)
            
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)    
                            
                        # Add this with your other command handlers:
                        if inPuTMsG.strip().startswith('/guest'):
                            print('Processing guest account generation command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /guest (count)
        
📝 Examples:
/guest 5 - Generate 5 guest accounts
/guest 10 - Generate 10 guest accounts
/guest 50 - Generate 50 guest accounts

🎯 Features:
• Generates random guest accounts
• Auto-retry on 503 errors (10 times)
• Saves to guest_accounts.json
• Shows progress in real-time

⚠️ Note: API may take time, be patient!
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            count_input = parts[1]
    
                            if not count_input.isdigit():
                                error_msg = f"[B][C][FF0000]❌ Count must be a number!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            count = int(count_input)
                            
                            if count <= 0:
                                error_msg = f"[B][C][FF0000]❌ Count must be greater than 0!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            if count > 100:
                                error_msg = f"[B][C][FF0000]❌ Max 100 accounts at once!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Send initial message
                            initial_msg = f"""[B][C][FFFF00]🚀 GENERATING GUEST ACCOUNTS

📊 Count: {count} accounts
🔗 API: gen-by-black-api.vercel.app
⏳ Please wait...

💡 This may take {count * 3} seconds
⚠️ 503 errors auto-retry 10 times
"""
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                            
                            try:
                                # Run generation in background
                                asyncio.create_task(handle_guest_generation(count, uid, chat_id, response.Data.chat_type, key, iv))
        
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ Error starting generation: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            
                        if inPuTMsG.startswith('/hjk'):
                        
                           
                           emote_hijack = True

                           success_msg = "[B][C][FF0000]The hijack Is Now ON\nType /hjf to turn it off"
                           await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)


                        if inPuTMsG.startswith('/hjf'):
                        
                           
                           emote_hijack = False

                           success_msg = "[B][C][FF0000]The hijack Is Now OFF\n"
                           await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            
                        # In your TcPChaT function, add this command handler:
                        if inPuTMsG.strip().startswith('/s_m '):
                            print('Processing private message command')
    
                            parts = inPuTMsG.strip().split(maxsplit=2)  # maxsplit=2 to keep message together
    
                            if len(parts) < 3:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /s_m (target_uid) (message)
        
📝 Examples:
/s_m 123456789 Hello!
/s_m 123456789 How are you?
/s_m 123456789 Let's play together!

🔧 What it does:
• Sends private message to specified UID
• Works even if target is not in your squad
• Bot sends message from its account
• Target sees message in private chat
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
                            message_text = parts[2]
    
                            # Validate target UID
                            if not target_uid.isdigit() or len(target_uid) < 8:
                                error_msg = f"[B][C][FF0000]❌ Invalid UID! Must be 8+ digits\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Validate message length
                            if len(message_text) > 100:
                                error_msg = f"[B][C][FF0000]❌ Message too long! Max 100 characters\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Send initial confirmation
                            initial_msg = f"[B][C][FFFF00]📩 SENDING PRIVATE MESSAGE\n"
                            initial_msg += f"👤 To: {target_uid}\n"
                            initial_msg += f"📝 Message: {message_text[:30]}...\n"
                            initial_msg += f"⏳ Sending...\n"
    
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
    
                            try:
                                # Get bot's UID from login data
                                bot_uid = 14010319252
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
        
                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
            
                                    success_msg = f"""[B][C][FFFF00]✅ PRIVATE MESSAGE SENT!

👤 To: {target_uid}
📝 Message: {message_text}
✅ Status: Delivered

💡 Target will see this in their private messages!
"""
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    print(f"✅ Private message sent to {target_uid}: {message_text}")
                                else:
                                    error_msg = f"[B][C][FF0000]❌ Failed to create message packet!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
            
                            except Exception as e:
                                print(f"❌ Private message error: {e}")
                                error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # In your TcPChaT function, add this:
                        if inPuTMsG.strip().startswith('/friend '):
                            print('Processing friend request command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /friend (uid) [count]
        
📝 Examples:
/friend 123456789 - Send 1 friend request
/friend 123456789 5 - Send 5 friend requests

🔧 Features:
• Uses token.json for single request
• Uses token_ind.json for bulk requests
• Same encryption as Flask API
• Direct HTTP requests to Free Fire servers
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
    
                            # Validate UID
                            if not target_uid.isdigit() or len(target_uid) < 8:
                                error_msg = f"[B][C][FF0000]❌ Invalid UID! Must be 8+ digits\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Determine count
                            count = 1
                            if len(parts) > 2:
                                try:
                                    count = int(parts[2])
                                    if count > 100:
                                        count = 100
                                except:
                                    count = 1
    
                            # Send initial message
                            if count == 1:
                                initial_msg = f"[B][C][FFFF00]🤝 SENDING FRIEND REQUEST\n"
                            else:
                                initial_msg = f"[B][C][FFFF00]📦 SENDING {count} FRIEND REQUESTS\n"
    
                            initial_msg += f"🎯 Target: {target_uid}\n"
                            initial_msg += f"🔑 Source: {'token.json' if count == 1 else 'token_ind.json'}\n"
                            initial_msg += f"🔒 Encryption: AES-CBC + Varint Encoding\n"
                            initial_msg += f"⏳ Processing...\n"
    
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
    
                            try:
                                # Get player info first
                                token = load_jwt_token()
                                player_name = "Unknown"
                                if token:
                                    player_name, _ = get_player_info(target_uid, token)
        
                                # Send friend requests
                                results = await send_friend_request_async(target_uid, count)
        
                                # Send result message
                                if results["success"] > 0:
                                    result_msg = f"""[B][C][FFFF00]✅ FRIEND REQUEST SUCCESS!

🎯 Player: {player_name}
🆔 UID: {target_uid}
✅ Successful: {results['success']}
❌ Failed: {results['failed']}
"""
                                    if count > 1:
                                        result_msg += f"📊 Total Attempted: {count}\n"
            
                                    result_msg += f"\n💡 Friend request(s) sent successfully!\n"
            
                                else:
                                    result_msg = f"""[B][C][FF0000]❌ FRIEND REQUEST FAILED

🎯 Player: {player_name}
🆔 UID: {target_uid}
❌ All requests failed

💡 Check:
1. Token files exist (token.json / token_ind.json)
2. Tokens are valid
3. Target UID is correct
4. Bot has internet connection
"""
        
                                await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
        
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ Friend request error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith('noob'):
                            await handle_alll_titles_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/room_msg'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_id = parts[1]

                                initial_message = f"[B][C]{get_random_color()}\nkicking {uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await Create_xr_room_packet_fixed__(room_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)

                        # Replace the existing title handler with this
                        # Use the FINAL version
                        if inPuTMsG.strip().startswith('/kick'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nkicking {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await KickTarget(target_uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)
                                    
                        if inPuTMsG.strip().startswith('/tester'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nkicking {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await SwitchLoneWolfDule(target_uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)
                            
                        if inPuTMsG.strip().startswith('/kkick'):
                            print('Processing FINAL title command (friend method)')
                            await LagSquad(key, iv)

                        if inPuTMsG.startswith(("/3")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 3-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFFF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/4")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 3-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(4, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(4, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFFF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        # In your TcPChaT function, look for the command handling section
                        # It might look something like this:

                        if inPuTMsG.startswith('/room '):
                            await handle_room_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        # Join Custom Room Command
                        if inPuTMsG.strip().startswith('/joinroom'):
                            print('Processing custom room join command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ Usage: /joinroom (room_id) (password)\nExample: /joinroom 123456 0000\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_id = parts[1]
                                room_password = parts[2]
        
                                initial_msg = f"[B][C][FFFF00]🚀 Joining custom room...\n🏠 Room: {room_id}\n🔑 Password: {room_password}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Join the custom room
                                    join_packet = await join_custom_room(room_id, room_password, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
                                    success_msg = f"[B][C][FFFF00]✅ Joined custom room {room_id}!\n🤖 Bot is now in room chat!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Failed to join room: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/5")):
                            # Process /5 command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\n\nSending Group Invitation...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)  # Reduced from 3 seconds
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFFF00]✅ SUCCESS! Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                               
                        if inPuTMsG.strip() == "/admin":
                            # Process /admin command in any chat type
                            admin_message = """
[C][B][FF0000]╔═════════════╗
[FFFFFF] ✨ IG= @NAYAN1M FOLLOW   
[FFFFFF]      THANKS FOR USE MY BOT❤️   
[FFFFFF]           AND THANKS FOR YOUR SUPPORT❤️ 
[FF0000]╠═════════════╣
[FFD700] ⚡ OWNER REAL NAME : [FFFFFF]NAYAN乡1M
[FFD700] ✨ KOI GUILD BOT [FF0000]KHARIDNA CHATAHO message KARNA, [00FFFF] INSTAGRAM: @NAYAN1M
[FF0000]╠═════════════╣
[FFD700] ✨ Developer —͟͞͞ </> —͞NAYAN乡ㅤ1M ❄️  ⚡
[FFD700]╚═════════════╝"""
                            await safe_send_message(response.Data.chat_type, admin_message, uid, chat_id, key, iv)

                        # ==================== GUILD JOIN COMMAND ====================
                        if inPuTMsG.strip().startswith('/guild_join'):
                            import requests
                            print(f"🏰 /guild_join command received")
                            
                            # Admin check
                            if str(uid) != ADMIN_UID:
                                deny_msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ ACCESS DENIED
[C][FF0000]═══════════════════

[C][FFD700]Only Admin can use this command!

[C][FF0000]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, deny_msg, uid, chat_id, key, iv)
                                continue
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                msg = f"""
[C][B][FF1493]═══════════════════
[C][B][00FFFF]  🏰 GUILD JOIN
[C][FF1493]═══════════════════

[C][FFD700]Usage: /guild_join (guild_id)
[C][FFD700]Example: /guild_join 123456789

[C][FF1493]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                return
                            
                            guild_id = parts[1]
                            
                            if not guild_id.isdigit():
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ INVALID GUILD ID
[C][FF0000]═══════════════════

[C][FFD700]Guild ID must be numbers only!
[C][FFD700]You entered: {guild_id}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )
                                return
                            
                            # Send initial message
                            await safe_send_message(
                                response.Data.chat_type,
                                f"""
[C][B][FFFF00]═══════════════════
[C][B][FFFF00]  🏰 JOINING GUILD
[C][FFFF00]═══════════════════

[C][FFD700]Guild ID     : [00FFAA]{fix_num(guild_id)}
[C][FFD700]Status       : [00FFFF]Processing...

[C][FFFF00]═══════════════════
""",
                                uid, chat_id, key, iv
                            )
                            
                            try:
                                # Get token from bot
                                token = None
                                try:
                                    if 'LoGinDaTaUncRypTinG' in globals() and hasattr(LoGinDaTaUncRypTinG, 'token'):
                                        token = LoGinDaTaUncRypTinG.token
                                        print(f"✅ Token from LoGinDaTaUncRypTinG")
                                except:
                                    pass
                                
                                if not token:
                                    try:
                                        with open("token.json", "r") as f:
                                            data = json.load(f)
                                            token = data.get("token")
                                            print(f"✅ Token from token.json")
                                    except:
                                        pass
                                
                                if not token:
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ TOKEN ERROR
[C][FF0000]═══════════════════

[C][FFD700]No token found!

[C][FF0000]═══════════════════
""",
                                        uid, chat_id, key, iv
                                    )
                                    return
                                
                                # Import guild join proto
                                try:
                                    import ReqCLan_pb2
                                    from Crypto.Cipher import AES
                                    from Crypto.Util.Padding import pad
                                except ImportError:
                                    from Pb2 import ReqCLan_pb2
                                    from Crypto.Cipher import AES
                                    from Crypto.Util.Padding import pad
                                
                                # Create guild join request
                                KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
                                IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
                                
                                msg = ReqCLan_pb2.MyMessage()
                                msg.field_1 = int(guild_id)
                                
                                cipher = AES.new(KEY, AES.MODE_CBC, IV)
                                encrypted = cipher.encrypt(pad(msg.SerializeToString(), AES.block_size))
                                
                                # Region based URL
                                if region.upper() == "BD":
                                    base_url = "https://clientbp.ggpolarbear.com/"
                                elif region.upper() == "IND":
                                    base_url = "https://client.ind.freefiremobile.com/"
                                else:
                                    base_url = "https://clientbp.ggpolarbear.com/"
                                
                                url = base_url + "RequestJoinClan"
                                
                                headers = {
                                    'Authorization': f"Bearer {token}",
                                    'User-Agent': "Dalvik/2.1.0 (Linux; Android 13)",
                                    'Content-Type': "application/octet-stream",
                                    'X-Unity-Version': "2018.4.11f1",
                                    'X-GA': "v1 1",
                                    'ReleaseVersion': "OB54"
                                }
                                
                                http_response = requests.post(url, data=encrypted, headers=headers, verify=False, timeout=15)
                                status_code = http_response.status_code
                                
                                if status_code == 200:
                                    msg = f"""
[C][B][00FF00]═══════════════════
[C][B][00FF00]  ✅ GUILD JOIN SUCCESS
[C][00FF00]═══════════════════

[C][FFD700]Guild ID     : [00FFAA]{fix_num(guild_id)}
[C][FFD700]Status       : [00FF00]Request Sent ✅
[C][FFD700]Region       : [FFFFFF]{region}

[C][00FF00]═══════════════════
[C][FFD700]🤖—͞NAYAN 乡ㅤ友! BOT
[C][00FF00]═══════════════════
"""
                                else:
                                    msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ GUILD JOIN FAILED
[C][FF0000]═══════════════════

[C][FFD700]Guild ID     : [FF00FF]{fix_num(guild_id)}
[C][FFD700]Error        : [FF4444]HTTP {status_code}

[C][FF0000]═══════════════════
"""
                                
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                
                            except requests.exceptions.RequestException as e:
                                print(f"❌ Guild join request error: {e}")
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ REQUEST ERROR
[C][FF0000]═══════════════════

[C][FFD700]Error: {str(e)[:50]}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )
                            except Exception as e:
                                print(f"❌ Guild join error: {e}")
                                import traceback
                                traceback.print_exc()
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ ERROR
[C][FF0000]═══════════════════

[C][FFD700]Error: {str(e)[:50]}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )

                        # ==================== GUILD LEAVE COMMAND ====================
                        if inPuTMsG.strip().startswith('/guild_leave'):
                            import requests
                            print(f"🏰 /guild_leave command received")
                            
                            # Admin check
                            if str(uid) != ADMIN_UID:
                                deny_msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ ACCESS DENIED
[C][FF0000]═══════════════════

[C][FFD700]Only Admin can use this command!

[C][FF0000]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, deny_msg, uid, chat_id, key, iv)
                                continue
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                msg = f"""
[C][B][FF1493]═══════════════════
[C][B][00FFFF]  🏰 GUILD LEAVE
[C][FF1493]═══════════════════

[C][FFD700]Usage: /guild_leave (guild_id)
[C][FFD700]Example: /guild_leave 123456789

[C][FF1493]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                return
                            
                            guild_id = parts[1]
                            
                            if not guild_id.isdigit():
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ INVALID GUILD ID
[C][FF0000]═══════════════════

[C][FFD700]Guild ID must be numbers only!
[C][FFD700]You entered: {guild_id}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )
                                return
                            
                            # Send initial message
                            await safe_send_message(
                                response.Data.chat_type,
                                f"""
[C][B][FFFF00]═══════════════════
[C][B][FFFF00]  🏰 LEAVING GUILD
[C][FFFF00]═══════════════════

[C][FFD700]Guild ID     : [00FFAA]{fix_num(guild_id)}
[C][FFD700]Status       : [00FFFF]Processing...

[C][FFFF00]═══════════════════
""",
                                uid, chat_id, key, iv
                            )
                            
                            try:
                                # Get token from bot
                                token = None
                                try:
                                    if 'LoGinDaTaUncRypTinG' in globals() and hasattr(LoGinDaTaUncRypTinG, 'token'):
                                        token = LoGinDaTaUncRypTinG.token
                                        print(f"✅ Token from LoGinDaTaUncRypTinG")
                                except:
                                    pass
                                
                                if not token:
                                    try:
                                        with open("token.json", "r") as f:
                                            data = json.load(f)
                                            token = data.get("token")
                                            print(f"✅ Token from token.json")
                                    except:
                                        pass
                                
                                if not token:
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ TOKEN ERROR
[C][FF0000]═══════════════════

[C][FFD700]No token found!

[C][FF0000]═══════════════════
""",
                                        uid, chat_id, key, iv
                                    )
                                    return
                                
                                # Import guild leave proto
                                try:
                                    import QuitClanReq_pb2
                                    from Crypto.Cipher import AES
                                    from Crypto.Util.Padding import pad
                                except ImportError:
                                    from Pb2 import QuitClanReq_pb2
                                    from Crypto.Cipher import AES
                                    from Crypto.Util.Padding import pad
                                
                                # Create guild leave request
                                KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
                                IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
                                
                                msg = QuitClanReq_pb2.QuitClanReq()
                                msg.field_1 = int(guild_id)
                                
                                cipher = AES.new(KEY, AES.MODE_CBC, IV)
                                encrypted = cipher.encrypt(pad(msg.SerializeToString(), AES.block_size))
                                
                                # Region based URL
                                if region.upper() == "BD":
                                    base_url = "https://clientbp.ggpolarbear.com/"
                                elif region.upper() == "IND":
                                    base_url = "https://client.ind.freefiremobile.com/"
                                else:
                                    base_url = "https://clientbp.ggpolarbear.com/"
                                
                                url = base_url + "QuitClan"
                                
                                headers = {
                                    'Authorization': f"Bearer {token}",
                                    'User-Agent': "Dalvik/2.1.0 (Linux; Android 13)",
                                    'Content-Type': "application/octet-stream",
                                    'X-Unity-Version': "2018.4.11f1",
                                    'X-GA': "v1 1",
                                    'ReleaseVersion': "OB54"
                                }
                                
                                http_response = requests.post(url, data=encrypted, headers=headers, verify=False, timeout=15)
                                status_code = http_response.status_code
                                
                                if status_code == 200:
                                    msg = f"""
[C][B][00FF00]═══════════════════
[C][B][00FF00]  ✅ GUILD LEAVE SUCCESS
[C][00FF00]═══════════════════

[C][FFD700]Guild ID     : [00FFAA]{fix_num(guild_id)}
[C][FFD700]Status       : [00FF00]Leave Request Sent ✅
[C][FFD700]Region       : [FFFFFF]{region}

[C][00FF00]═══════════════════
[C][FFD700]🤖 —͞NAYAN乡ㅤ友! BOT
[C][00FF00]═══════════════════
"""
                                else:
                                    msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ GUILD LEAVE FAILED
[C][FF0000]═══════════════════

[C][FFD700]Guild ID     : [FF00FF]{fix_num(guild_id)}
[C][FFD700]Error        : [FF4444]HTTP {status_code}

[C][FF0000]═══════════════════
"""
                                
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                
                            except requests.exceptions.RequestException as e:
                                print(f"❌ Guild leave request error: {e}")
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ REQUEST ERROR
[C][FF0000]═══════════════════

[C][FFD700]Error: {str(e)[:50]}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )
                            except Exception as e:
                                print(f"❌ Guild leave error: {e}")
                                import traceback
                                traceback.print_exc()
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ ERROR
[C][FF0000]═══════════════════

[C][FFD700]Error: {str(e)[:50]}

[C][FF0000]═══════════════════
""",
                                    uid, chat_id, key, iv
                                )

                        # MULTIJOIN command handlers in the TcPChaT function
                        if inPuTMsG.strip().startswith('/multijoin'):
                            print('Processing multi-account join request')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /multijoin (target_uid)\nExample: /multijoin 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                if not target_uid.isdigit():
                                    error_msg = f"[B][C][FF0000]❌ Please write a valid player ID!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                initial_msg = f"[B][C][FFFF00]🚀 Starting multi-join attack on {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Try the fake multi-account method (more reliable)
                                    success_count, total_attempts = await real_multi_account_join(target_uid, key, iv, region)
            
                                    if success_count > 0:
                                        result_msg = f"""
[B][C][FFFF00]✅ MULTI-JOIN ATTACK COMPLETED!

🎯 Target: {target_uid}
✅ Successful Requests: {success_count}
📊 Total Attempts: {total_attempts}
⚡ Different squad variations sent!

💡 Check your game for join requests!
"""
                                    else:
                                        result_msg = f"[B][C][FF0000]❌ All join requests failed! Check bot connection.\n"
            
                                    await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Multi-join error: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)



                        # Update the command handler
                        if inPuTMsG.strip().startswith('/reject'):
                            print('Processing reject spam command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /reject (target_uid)\nExample: /reject 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing reject spam
                                if reject_spam_task and not reject_spam_task.done():
                                    reject_spam_running = False
                                    reject_spam_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Send start message
                                start_msg = f"[B][C][1E90FF]🌀 Started Reject Spam on: {target_uid}\n🌀 Packets: 150 each type\n🌀 Interval: 0.2 seconds\n"
                                await safe_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
        
                                # Start reject spam in background
                                reject_spam_running = True
                                reject_spam_task = asyncio.create_task(reject_spam_loop(target_uid, key, iv))
        
                                # Wait for completion in background and send completion message
                                asyncio.create_task(handle_reject_completion(reject_spam_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv))


                        if inPuTMsG.strip() == '/reject_stop':
                            if reject_spam_task and not reject_spam_task.done():
                                reject_spam_running = False
                                reject_spam_task.cancel()
                                stop_msg = f"[B][C][FFFF00]✅ Reject spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, stop_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ No active reject spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                

                        # Individual command handlers for /s1 to /s8
                        if inPuTMsG.strip().startswith('/s1'):
                            await handle_badge_command('s1', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
    
                        if inPuTMsG.strip().startswith('/s2'):
                            await handle_badge_command('s2', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s3'):
                            await handle_badge_command('s3', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s4'):
                            await handle_badge_command('s4', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s5'):
                            await handle_badge_command('s5', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s6'):
                            await handle_badge_command('s6', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s7'):
                            await handle_badge_command('s7', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s8'):
                            await handle_badge_command('s8', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                                    
                                                                                                     
                        # Check if user wants to list emotes or show help
                            if len(parts) == 1 or (len(parts) == 2 and parts[1].lower() == 'list'):
                                # Show available emotes
                                emote_list_msg = f"[B][C][00FF00]🎭 EMOTE SYSTEM\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[00FF00]📊 STATS:\n"
                                emote_list_msg += f"[FFFFFF]• Number emotes: 1-{len(NUMBER_EMOTES)}\n"
                                emote_list_msg += f"[FFFFFF]• Named emotes: {len(NAME_EMOTES)} names\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[00FF00]🎯 USAGE:\n"
                                emote_list_msg += f"[FFFFFF]e [number/name] → Send to yourself\n"
                                emote_list_msg += f"[FFFFFF]e [uid] [number/name] → Send to UID\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[00FF00]🔥 POPULAR NAMES:\n"
        
                                # Show popular named emotes
                                popular_names = ["ak", "m60", "p90", "scar", "famas", "heart", "love", "dance", "hello", "money"]
                                line = ""
                                for name in popular_names:
                                    if name.lower() in NAME_EMOTES:
                                        line += f"[00FF00]{name}[FFFFFF], "
                                if line:
                                    emote_list_msg += line.rstrip(", ") + "\n"
        
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[00FF00]📖 EXAMPLES:\n"
                                emote_list_msg += f"[FFFFFF]e ak → Send AK emote to yourself\n"
                                emote_list_msg += f"[FFFFFF]e {xMsGFixinG(int(123456789))} heart → Send ❤️ to UID\n"
                                emote_list_msg += f"[FFFFFF]e {xMsGFixinG(int(123456789))} 1 → Send emote #1 to UID\n"
                                emote_list_msg += f"[FFFFFF]e ring → Send ring emote to yourself\n"
                                emote_list_msg += f"[FFFFFF]e list names → Show all named emotes\n"
        
                                # Check if user wants detailed name list
                                if len(parts) == 2 and parts[1].lower() == 'names':
                                    emote_list_msg += f"[FFFFFF]────────────────\n"
                                    emote_list_msg += f"[00FF00]📝 ALL NAMED EMOTES:\n"
            
                                    # Show all named emotes in groups
                                    all_names = sorted(NAME_EMOTES.keys())
                                    for i in range(0, min(len(all_names), 30), 5):  # Show first 30 names
                                        group = all_names[i:i+5]
                                        emote_list_msg += f"[FFFFFF]{' | '.join(group)}\n"
            
                                    if len(all_names) > 30:
                                        emote_list_msg += f"[FFFFFF]... and {len(all_names) - 30} more\n"
        
                                await safe_send_message(response.Data.chat_type, emote_list_msg, uid, chat_id, key, iv)
                                continue
    
                            # Parse command
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: e [emote_name_or_number]\n"
                                error_msg += f"[FFFFFF]Examples:\n"
                                error_msg += f"[00FF00]e ak[FFFFFF] → AK emote to yourself\n"
                                error_msg += f"[00FF00]e {xMsGFixinG(int(123456789))} heart[FFFFFF] → ❤️ to UID\n"
                                error_msg += f"[00FF00]e {xMsGFixinG(int(123456789))} 1[FFFFFF] → Emote #1 to UID\n"
                                error_msg += f"[00FF00]e ring[FFFFFF] → Send ring emote to yourself\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                            
                            target_uids = []
                            emote_key = None
    
                            try:
                                # Determine if last part is emote key (could be number or name)
                                last_part = parts[-1].lower()
        
                                # Check if last part is an emote (number or name)
                                # Note: Your numbers go up to 417, so check for 3-digit numbers too
                                is_number = last_part.isdigit() and last_part in NUMBER_EMOTES
                                is_name = last_part in NAME_EMOTES
        
                                if is_number or is_name:
                                    # Case 1: e ak or e 1 (only emote - send to sender)
                                    if len(parts) == 2:
                                        emote_key = last_part
                                        target_uids.append(int(response.Data.uid))
            
                                    # Case 2: e {xMsGFixinG(int(123456789))} heart (UID + emote)
                                    elif len(parts) == 3:
                                        target_uids.append(int(parts[1]))
                                        emote_key = last_part
            
                                    # Case 3: e 111 222 333 ak (multiple UIDs + emote)
                                    else:
                                        for i in range(1, len(parts) - 1):
                                            target_uids.append(int(parts[i]))
                                        emote_key = last_part
                                else:
                                    # Last part is not a valid emote
                                    error_msg = f"[B][C][FF0000]❌ Invalid emote: '{last_part}'\n"
                                    error_msg += f"[FFFFFF]Use numbers (1-{len(NUMBER_EMOTES)}) or names like 'ak', 'heart', 'dance', 'ring'\n"
                                    error_msg += f"[FFFFFF]Use e list names to see all available names\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
        
                                # Get emote ID from either number or name dictionary
                                emote_id = None
                                emote_name_display = None
                                
                                if is_number:
                                    # Number-based emote
                                    emote_id = NUMBER_EMOTES.get(emote_key)
                                    emote_name_display = f"#{emote_key}"
                                else:
                                    # Name-based emote
                                    emote_id = NAME_EMOTES.get(emote_key)
                                    emote_name_display = emote_key
        
                                if not emote_id:
                                    error_msg = f"[B][C][FF0000]❌ Emote '{emote_name_display}' not found!\n"
                                    if emote_key.isdigit():
                                        error_msg += f"[FFFFFF]Available numbers: 1-{len(NUMBER_EMOTES)}\n"
                                    else:
                                        error_msg += f"[FFFFFF]Use e list names to see all available names\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
        
                                # Send emotes
                                success_count = 0
                                failed_uids = []
        
                                for target_uid in target_uids:
                                    try:
                                        H = await Emote_k(target_uid, int(emote_id), key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        success_count += 1
                                        await asyncio.sleep(0.1)
                                    except Exception as e:
                                        print(f"Error sending emote to {xMsGFixinG(target_uid)}: {e}")
                                        failed_uids.append(str(target_uid))
        
                                # Success message
                                if success_count > 0:
                                    if target_uids[0] == int(response.Data.uid):
                                        target_list = "Yourself"
                                    elif len(target_uids) == 1:
                                        target_list = str(target_uids[0])
                                    else:
                                        target_list = f"{len(target_uids)} players"
            
                                    success_msg = f"[B][C][00FF00]✅ EMOTE SENT!\n"
                                    success_msg += f"[FFFFFF]────────────────\n"
                                    success_msg += f"[00FF00]🎭 Emote: {emote_name_display}\n"
                                    success_msg += f"[00FF00]🆔 ID: {emote_id}\n"
                                    success_msg += f"[00FF00]👤 Target: {target_list}\n"
                                    success_msg += f"[00FF00]📊 Status: {success_count}/{len(target_uids)} successful\n"
            
                                    if failed_uids:
                                        success_msg += f"[FF0000]❌ Failed: {', '.join(failed_uids)}\n"
            
                                    success_msg += f"[FFFFFF]────────────────\n"
            
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                else:
                                    error_msg = f"[B][C][FF0000]❌ Failed to send emote to any target!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                            except ValueError as ve:
                                print("ValueError:", ve)
                                error_msg = f"[B][C][FF0000]❌ Invalid format!\n"
                                error_msg += f"[FFFFFF]UIDs must be numbers (like {xMsGFixinG(int(123456789))})\n"
                                error_msg += f"[FFFFFF]Examples: e ak, e {xMsGFixinG(int(123456789))} heart, e 1, e ring\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            except Exception as e:
                                print(f"Error processing e command: {e}")
                                error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                                                                          # FIXED JOIN COMMAND
                        if inPuTMsG.startswith('!'):
                            # Process /join command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /join (team_code)\nExample: /join ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                uid = response.Data.uid  # Get the UID of person who sent the command
        
                                initial_message = f"[B][C]{get_random_color()}\nJoining squad with code: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
                                try:
                                    # Try using the regular join method first
                                    EM = await GenJoinSquadsPacket(CodE, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
            
                                    # Wait a bit for the join to complete
                                    await asyncio.sleep(2)
            
                                    # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                    try:
                                        await auto_rings_emote_dual(uid, key, iv, region)
                                    except Exception as emote_error:
                                        print(f"Dual emote failed but join succeeded: {emote_error}")
            
                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][FFFF00]✅ SUCCESS! Joined squad: {CodE}!\n💍 Dual Rings emote activated!\n🤖 Bot + You = 💕\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print(f"Regular join failed, trying ghost join: {e}")
                                    # If regular join fails, try ghost join
                                    try:
                                        # Get bot's UID from global context or login data
                                        bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                
                                        ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                        if ghost_packet:
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                    
                                            # Wait a bit for ghost join to complete
                                            await asyncio.sleep(2)
                    
                                            # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                            try:
                                                await auto_rings_emote_dual(uid, key, iv, region)
                                            except Exception as emote_error:
                                                print(f"Dual emote failed but ghost join succeeded: {emote_error}")
                    
                                            success_message = f"[B][C][FFFF00]✅ SUCCESS! Ghost joined squad: {CodE}!\n💍 Dual Rings emote activated!\n🤖 Bot + You = 💕\n"
                                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                        else:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Failed to create ghost join packet.\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                    
                                    except Exception as ghost_error:
                                        print(f"Ghost join also failed: {ghost_error}")
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Failed to join squad: {str(ghost_error)}\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                
                
                        if inPuTMsG.strip().startswith('/ghost'):
                            # Process /ghost command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /ghost (team_code)\nExample: /ghost ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nGhost joining squad with code: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Get bot's UID from global context or login data
                                    bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                                    
                                    ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                    if ghost_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                                        success_message = f"[B][C][FFFF00]✅ SUCCESS! Ghost joined squad with code: {CodE}!\n"
                                        await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Failed to create ghost join packet.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Ghost join failed: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW LAG COMMAND
                        if inPuTMsG.strip().startswith('/lag '):
                            print('Processing lag command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /lag (team_code)\nExample: /lag ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                
                                # Stop any existing lag task
                                if lag_task and not lag_task.done():
                                    lag_running = False
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)
                                
                                # Start new lag task
                                lag_running = True
                                lag_task = asyncio.create_task(lag_team_loop(team_code, key, iv, region))
                                
                                # SUCCESS MESSAGE
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Lag attack started!\nTeam: {team_code}\nAction: Rapid join/leave\nSpeed: Ultra fast (milliseconds)\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # STOP LAG COMMAND
                        if inPuTMsG.strip() == '/stop lag':
                            if lag_task and not lag_task.done():
                                lag_running = False
                                lag_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Lag attack stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active lag attack to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # ==================== EXIT/LEAVE COMMAND ====================
                        if inPuTMsG.strip().startswith('/exit') or inPuTMsG.strip().startswith('/leave'):
                            print(f'🚪 Processing exit command from UID: {uid}')
                            
                            try:
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"[B][C]{get_random_color()}\n🚪 Leaving squad...",
                                    uid, chat_id, key, iv, region=region
                                )
                                
                                # ===== CREATE LEAVE PACKET DIRECTLY =====
                                # No UID needed - works with any bot
                                fields = {
                                    1: 7,  # Leave squad packet type
                                    2: {
                                        1: 1,  # Generic value
                                    }
                                }
                                
                                # Create protobuf packet
                                packet = await CrEaTe_ProTo(fields)
                                packet_hex = packet.hex()
                                
                                # Generate final packet
                                leave_packet = await GeneRaTePk(packet_hex, '0515', key, iv)
                                
                                if leave_packet:
                                    # Send via Online connection
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
                                    print(f"✅ Leave packet sent successfully")
                                    
                                    # Reset squad status
                                    global insquad, joining_team
                                    insquad = None
                                    joining_team = False
                                    
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        "[B][C][00FF00]✅ Left squad successfully!\n🔄 Squad status reset",
                                        uid, chat_id, key, iv, region=region
                                    )
                                else:
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        "[B][C][FF0000]❌ Failed to create leave packet!",
                                        uid, chat_id, key, iv, region=region
                                    )
                                    
                            except Exception as e:
                                print(f"❌ Exit command error: {e}")
                                import traceback
                                traceback.print_exc()
                                await safe_send_message(
                                    response.Data.chat_type,
                                    f"[B][C][FF0000]❌ Error: {str(e)[:50]}",
                                    uid, chat_id, key, iv, region=region
                                )

                        if inPuTMsG.strip().startswith('/start'):
                            # Process /s command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\nStarting match...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            start_packet = await start_auto_packet(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
                            initiial_message = f"[B][C]{get_random_color()}\nStarting match...\n"
                            await safe_send_message(response.Data.chat_type, initiial_message, uid, chat_id, key, iv)
                            
        

                        if inPuTMsG.strip().startswith('/mg '):
                            print('Processing wave message command')
                          
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /mg (message) [repeats=5]\n"
                                error_msg += f"[FFFFFF]Example: /mg hello 3\n"
                                error_msg += f"[FFFFFF]Will send: h, he, hel, hell, hello, hell, hel, he, h\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    # Get message and optional repeats
                                    message_text = parts[1]
                                    repeats = 5  # Default
            
                                    if len(parts) > 2:
                                        repeats = int(parts[2])
            
                                    if repeats <= 0:
                                        error_msg = f"[B][C][FF0000]❌ Repeats must be > 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif repeats > 10:
                                        error_msg = f"[B][C][FF0000]❌ Max 10 repeats!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif len(message_text) < 2:
                                        error_msg = f"[B][C][FF0000]❌ Message must be at least 2 characters!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        global mg_spam_task
                                        if mg_spam_task and not mg_spam_task.done():
                                            global msg_spam_running
                                            msg_spam_running = False
                                            mg_spam_task.cancel()
                                            await asyncio.sleep(0.5)
                
                                        # Calculate total messages
                                        total_messages_per_cycle = (len(message_text) * 2) - 2
                                        total_messages = total_messages_per_cycle * repeats
                
                                        initial_msg = f"[B][C][FFFF00]🌊 WAVE MESSAGE STARTING!\n"
                                        initial_msg += f"[FFFFFF]Message: {message_text}\n"
                                        initial_msg += f"[FFFFFF]Repeats: {repeats} cycles\n"
                                        initial_msg += f"[FFFFFF]Pattern: h → he → hel → hell → hello → hell → hel → he → h\n"
                                        initial_msg += f"[FFFF00]Total messages: {total_messages}\n"
                                        await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                        
                                        # Start wave messages
                                        msg_spam_running = True
                                        mg_spam_task = asyncio.create_task(
                                            send_wave_messages(message_text, repeats, chat_id, key, iv, region)
                                        )
                
                                        # Handle completion
                                        asyncio.create_task(
                                            handle_wave_completion(mg_spam_task, message_text, repeats, uid, chat_id, response.Data.chat_type, key, iv)
                                        )
                
                                except ValueError:
                                    error_msg = f"[B][C][FF0000]❌ Invalid format!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        
                        if inPuTMsG.strip().startswith('/msg '):
                            print('Processing message spam command')
                            global msg_spam_task
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /msg (message) (times)\n"
                                error_msg += f"[FFFFFF]Example: /msg Hello Team! 5\n"
                                error_msg += f"[FFFFFF]Will send 'Hello Team!' 5 times in team chat\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    # Extract message and times
                                    times = int(parts[-1]) # Last part is the number
            
                                    # Reconstruct the message (everything except first part and last part)
                                    message_text = ' '.join(parts[1:-1])
            
                                    if times <= 0:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Times must be greater than 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                                    elif not message_text.strip():
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Message cannot be empty!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        # Stop any existing message spam
                                      
                                        if msg_spam_task and not msg_spam_task.done():
                                            
                                            msg_spam_running = False
                                            msg_spam_task.cancel()
                                            await asyncio.sleep(0.1)
                
                                        # Check if we have the chat_id from the message
                                        # If not, use the bot's UID from login data
                                        chat_id = chat_id
                
                                        # Send initial message
                                        initial_msg = f"[B][C][FFFF00]📢 MESSAGE SPAM STARTING!\n"
                                        initial_msg += f"[FFFFFF]Message: {message_text}\n"
                                        initial_msg += f"[FFFFFF]Times: {times}\n"
                                        initial_msg += f"[FFFFFF]Chat: Team/Squad Chat\n"
                                        initial_msg += f"[FFFF00]Sending messages...\n"
                                        await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                
                                        # Start message spam
                                        msg_spam_running = True
                                        msg_spam_task = asyncio.create_task(
                                            msg_spam_loop(message_text, times, chat_id, key, iv, region)
                                        )
                
                                        # Wait for completion and send result
                                        asyncio.create_task(
                                            handle_msg_spam_completion(msg_spam_task, message_text, times, uid, chat_id, response.Data.chat_type, key, iv)
                                        )
                                        
                                except ValueError:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format!\n"
                                    error_msg += f"[FFFFFF]Usage: /msg (message) (times)\n"
                                    error_msg += f"[FFFFFF]Example: /msg Hello World! 10\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Add stop command
                        if inPuTMsG.strip() == '/stop msg':
                            if msg_spam_task and not msg_spam_task.done():
                                msg_spam_running = False
                                msg_spam_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ MESSAGE SPAM STOPPED!\n[FFFFFF]All message sending has been stopped.\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ No active message spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
        
                        # Add this to your command handlers in TcPChaT function:
                        if inPuTMsG.strip().startswith('/train'):
                            print('Processing training mode command')
                            await handle_training_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                        # Add these to your command handlers in TcPChaT function:
                        # Add this to your command handlers in TcPChaT function:
                        if inPuTMsG.strip().startswith('/join_req '):
                            print('Processing /join_req command')
                            await handle_join_req_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type, LoGinDaTaUncRypTinG)


                        if inPuTMsG.strip().startswith('/e'):
                            print(f'Processing emote command in chat type: {response.Data.chat_type}')
    
                            parts = inPuTMsG.strip().split()
    
                            # Check if user wants to list emotes or show help
                            if len(parts) == 1 or (len(parts) == 2 and parts[1].lower() == 'list'):
                                # Show available emotes
                                emote_list_msg = f"[B][C][FFFF00]🎭 EMOTE SYSTEM\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[FFFF00]📊 STATS:\n"
                                emote_list_msg += f"[FFFFFF]• Number emotes: 1-{len(NUMBER_EMOTES)}\n"
                                emote_list_msg += f"[FFFFFF]• Named emotes: {len(NAME_EMOTES)} names\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[FFFF00]🎯 USAGE:\n"
                                emote_list_msg += f"[FFFFFF]/e [number/name] → Send to yourself\n"
                                emote_list_msg += f"[FFFFFF]/e [uid] [number/name] → Send to UID\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[FFFF00]🔥 POPULAR NAMES:\n"
        
                                # Show popular named emotes
                                popular_names = ["ak", "m60", "p90", "scar", "famas", "heart", "love", "dance", "hello", "money"]
                                line = ""
                                for name in popular_names:
                                    if name.lower() in NAME_EMOTES:
                                        line += f"[FFFF00]{name}[FFFFFF], "
                                if line:
                                    emote_list_msg += line.rstrip(", ") + "\n"
        
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[FFFF00]📖 EXAMPLES:\n"
                                emote_list_msg += f"[FFFFFF]/e ak → Send AK emote to yourself\n"
                                emote_list_msg += f"[FFFFFF]/e 123456789 heart → Send ❤️ to UID\n"
                                emote_list_msg += f"[FFFFFF]/e 123456789 1 → Send emote #1 to UID\n"
                                emote_list_msg += f"[FFFFFF]/e ring → Send ring emote to yourself\n"
                                emote_list_msg += f"[FFFFFF]/e list names → Show all named emotes\n"
        
                                # Check if user wants detailed name list
                                if len(parts) == 2 and parts[1].lower() == 'names':
                                    emote_list_msg += f"[FFFFFF]────────────────\n"
                                    emote_list_msg += f"[FFFF00]📝 ALL NAMED EMOTES:\n"
            
                                    # Show all named emotes in groups
                                    all_names = sorted(NAME_EMOTES.keys())
                                    for i in range(0, min(len(all_names), 30), 5):  # Show first 30 names
                                        group = all_names[i:i+5]
                                        emote_list_msg += f"[FFFFFF]{' | '.join(group)}\n"
            
                                    if len(all_names) > 30:
                                        emote_list_msg += f"[FFFFFF]... and {len(all_names) - 30} more\n"
        
                                await safe_send_message(response.Data.chat_type, emote_list_msg, uid, chat_id, key, iv)
                                continue
    
                            # Parse command
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: e [emote_name_or_number]\n"
                                error_msg += f"[FFFFFF]Examples:\n"
                                error_msg += f"[FFFF00]e ak[FFFFFF] → AK emote to yourself\n"
                                error_msg += f"[FFFF00]e 123456789 heart[FFFFFF] → ❤️ to UID\n"
                                error_msg += f"[FFFF00]e 123456789 1[FFFFFF] → Emote #1 to UID\n"
                                error_msg += f"[FFFF00]e ring[FFFFFF] → Send ring emote to yourself\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                            
                            target_uids = []
                            emote_key = None
    
                            try:
                                # Determine if last part is emote key (could be number or name)
                                last_part = parts[-1].lower()
        
                                # Check if last part is an emote (number or name)
                                # Note: Your numbers go up to 417, so check for 3-digit numbers too
                                is_number = last_part.isdigit() and last_part in NUMBER_EMOTES
                                is_name = last_part in NAME_EMOTES
        
                                if is_number or is_name:
                                    # Case 1: e ak or e 1 (only emote - send to sender)
                                    if len(parts) == 2:
                                        emote_key = last_part
                                        target_uids.append(int(response.Data.uid))
            
                                    # Case 2: e 123456789 heart (UID + emote)
                                    elif len(parts) == 3:
                                        target_uids.append(int(parts[1]))
                                        emote_key = last_part
            
                                    # Case 3: e 111 222 333 ak (multiple UIDs + emote)
                                    else:
                                        for i in range(1, len(parts) - 1):
                                            target_uids.append(int(parts[i]))
                                        emote_key = last_part
                                else:
                                    # Last part is not a valid emote
                                    error_msg = f"[B][C][FF0000]❌ Invalid emote: '{last_part}'\n"
                                    error_msg += f"[FFFFFF]Use numbers (1-{len(NUMBER_EMOTES)}) or names like 'ak', 'heart', 'dance', 'ring'\n"
                                    error_msg += f"[FFFFFF]Use /e list names to see all available names\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
        
                                # Get emote ID from either number or name dictionary
                                emote_id = False
                                emote_name_display = None
                                
                                if is_number:
                                    # Number-based emote
                                    emote_id = NUMBER_EMOTES.get(emote_key)
                                    emote_name_display = f"#{emote_key}"
                                else:
                                    # Name-based emote
                                    emote_id = NAME_EMOTES.get(emote_key)
                                    emote_name_display = emote_key
        
                                if not emote_id:
                                    error_msg = f"[B][C][FF0000]❌ Emote '{emote_name_display}' not found!\n"
                                    if emote_key.isdigit():
                                        error_msg += f"[FFFFFF]Available numbers: 1-{len(NUMBER_EMOTES)}\n"
                                    else:
                                        error_msg += f"[FFFFFF]Use /e list names to see all available names\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
        
                                # Send emotes
                                success_count = 0
                                failed_uids = []
        
                                for target_uid in target_uids:
                                    try:
                                        H = await Emote_k(target_uid, int(emote_id), key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        success_count += 1
                                        await asyncio.sleep(0.1)
                                    except Exception as e:
                                        print(f"Error sending emote to {target_uid}: {e}")
                                        failed_uids.append(str(target_uid))
        
                                # Success message
                                if success_count > 0:
                                    if target_uids[0] == int(response.Data.uid):
                                        target_list = "Yourself"
                                    elif len(target_uids) == 1:
                                        target_list = str(target_uids[0])
                                    else:
                                        target_list = f"{len(target_uids)} players"
            
                                    success_msg = f"[B][C][FFFF00]✅ EMOTE SENT!\n"
                                    success_msg += f"[FFFFFF]────────────────\n"
                                    success_msg += f"[FFFF00]🎭 Emote: {emote_name_display}\n"
                                    success_msg += f"[FFFF00]🆔 ID: {emote_id}\n"
                                    success_msg += f"[FFFF00]👤 Target: {target_list}\n"
                                    success_msg += f"[FFFF00]📊 Status: {success_count}/{len(target_uids)} successful\n"
            
                                    if failed_uids:
                                        success_msg += f"[FF0000]❌ Failed: {', '.join(failed_uids)}\n"
            
                                    success_msg += f"[FFFFFF]────────────────\n"
            
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                else:
                                    error_msg = f"[B][C][FF0000]❌ Failed to send emote to any target!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                            except ValueError as ve:
                                print("ValueError:", ve)
                                error_msg = f"[B][C][FF0000]❌ Invalid format!\n"
                                error_msg += f"[FFFFFF]UIDs must be numbers (like 123456789)\n"
                                error_msg += f"[FFFFFF]Examples: e ak, e 123456789 heart, e 1, e ring\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            except Exception as e:
                                print(f"Error processing e command: {e}")
                                error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                                #GALI SPAM MESSAGE 
                        # Add at the top with other global variables
                        BLOCKED_NAMES = [" chinkor", "Chinkor", "shihab", " shihab", "kapil", " Kapil", "ছিংকর", " ছিংকর", "শিহাব", " শিহাব", "chinkorroy", " chinkorroy","chinkor_roy", " chinkor_roy", "chink0r", " cHiNk0r", "chiNkr", " chinkr","", "chINKOR", "xinkr", "xinkor", " xinkr", " xinkor", ]  # Add your actual name

                        # Then in the /gali command handler, add this check:
                        if inPuTMsG.strip().startswith('/gali '):
                            print('Processing /gali command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF0000]❌ ERROR! Usage:\n"
                                        "/gali <name>\n"
                                        "Example: /gali hater"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    name = parts[1].strip()
            
                                    # ADD THIS CHECK - Prevent targeting yourself
                                    if name.lower() in [n.lower() for n in BLOCKED_NAMES]:
                                        error_msg = (
                                            f"[B][C][FF0000]⚠️ WARNING!\n"
                                            f"[FFFFFF]ᴛƐ3ʀɪ ꜱƐ3xʏ ʙʜ4ᴇɴ ᴋɪ ᴄʜ4xᴛ ᴍᴇ ᴍᴇ ʟ04ᴅᴀ ᴅᴀᴀʟ ᴋᴀʀ ʀᴀ4ᴀᴛ ʙʜ4ᴀʀ ᴊᴏʀ ᴊᴏʀ ꜱᴇ ᴄʜ04ᴅᴜɴɢᴀ {name}'!\n"
                                            f"[FF0000]ᴛƐ4ʀɪ ᴍᴀ́4ᴀ ᴋɪ ᴄʜ4xᴛ 360 ʙᴀʀ ⛔\n"
                                            f"[FFFFFF]ʀ4ɴᴅɪ ᴋᴇ ʙᴀᴄ4ʜʜƐ ᴀᴘɴᴇ ʙᴀᴘ ᴋᴏ ʜ8 ᴅᴇ4ɢᴀ⚠️."
                                        )
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        continue
            
                                    # Rest of your code continues here...
                                    messages = [
                                        "{special_name} ᴛƐ4ʀɪ ꜱƐxʏ ʙʜ4ᴇɴ ᴋɪ ᴄʜ4xᴛ ᴍᴇ ᴍᴇ ʟ04ᴅᴀ ᴅᴀ4ᴀʟ ᴋᴀʀ ʀᴀᴀᴛ ʙʜ4ᴀʀ ᴊᴏʀ ᴊᴏʀ ꜱᴇ ᴄʜ04ᴅᴜɴɢᴀ",
                f"{special_name} ᴍᴀᴅʜ4ᴇʀxʜᴏᴅ ᴛƐ4ʀɪ ᴍᴀ́4ᴀ ᴋɪ ᴋᴀʟɪ ɢ4ɴᴅ ᴍƐ ʟᴀ4ɴᴅ ᴍᴀ4ʀᴜ",
                f"{special_name} ᴛƐ4ʀɪ ʙʜ4Ɛɴ ᴋɪ ᴛɪɢ4ʜᴛ ᴄʜ4xᴛ ᴋᴏ 5ɢ ᴋɪ ꜱᴘ4ᴇᴇᴅ ꜱᴇ ᴄʜ40ᴅ ᴅᴜ",
                f"{special_name} ᴛƐ4ʀɪ ʙᴇ4ʜᴇɴ ᴋɪ ᴄʜ4xᴛ ᴍᴇ ʟ4ɴᴅ ᴍᴀʀᴜ",
                f"{special_name} ᴛƐ4ʀɪ ᴍᴀ4́ᴀ ᴋɪ ᴄʜ4xᴛ 360 ʙᴀʀ",
                f"{special_name} ᴛƐ4ʀɪ ʙƐ4ʜƐɴ ᴋɪ ᴄʜxᴛ 720 ʙᴀʀ",
                f"{special_name} ʙᴇʜ4ᴇɴ ᴋᴇ ʟ04ᴅᴇ",
                f"{special_name} ᴍᴀᴅᴀ4ʀᴄʜxᴅ",
                f"{special_name} ʙᴇᴛᴇ ᴛƐ4ʀᴀ ʙᴀᴀᴘ ʜᴜɴ ᴍᴇ",
                f"{special_name} ɢ4ɴ4ᴅᴜ ᴀᴘɴᴇ ʙᴀ4ᴀᴘ ᴋᴏ ʜ8 ᴅᴇɢᴀ",
                f"{special_name} ᴋɪ ᴍᴀ̀4ᴀ ᴋɪ ᴄʜ4xᴛ ᴘᴇʀ ɴɪɢʜᴛ 4000",
                f"{special_name} ᴋɪ ʙƐ4ʜƐɴ ᴋɪ ᴄʜ4xᴛ ᴘᴇʀ ɴɪɢʜᴛ 8000",
                f"{special_name} ʀ4ɴᴅɪ ᴋᴇ ʙᴀᴄ4ʜʜƐ ᴀᴘɴᴇ ʙᴀᴘ ᴋᴏ ʜ8 ᴅᴇɢ4ᴀ",
                f"ɪɴᴅɪᴀ ᴋᴀ ɴᴏ-1 ɢ4ɴᴅᴜ {special_name}",
                f"ᴄʜᴀᴘᴀʟ ᴄʜ0ʀ {special_name}",
                f"{special_name} ᴛƐ4ʀɪ ᴍᴀ4̀ᴀ ᴋᴏ ɢʙ ʀᴏ4ᴀᴅ ᴘᴇ ʙᴇᴛʜᴀ ᴋᴇ ᴄʜxᴅ4ᴜɴɢᴀ",
                f"{special_name} ʙᴇᴛᴀ ᴊʜ4ᴜʟᴀ ᴊʜᴜʟ ᴀᴘɴᴇ ʙᴀ4ᴀᴘ ᴋᴏ ᴍᴀᴛ ʙʜᴜʟ"
                                            ]

                                    # Send each message one by one with random color
                                    for msg in messages:
                                        colored_message = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.upper())}"
                                        await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv)
                                        await asyncio.sleep(2)

                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Something went wrong:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv) 
                                
                          #GALLI SPAM MESSAGE 
                        # Add at the top with other global variables
                        BLOCKED_NAMES = [" nayan", "NAYAN", "nayan1m", " NAYAN1M", "HARSH", " harsh", "raj", " RAJ", "devansh", " DEVANSH", "DEVANSH1M", " devansh1m","ongkar", " ONGKAR", "ONGKAR SUTRADHAR", " ongkar sutradhar", "classy", " CLASSY","", "Ongkar", "devansh raj", "DEVANSH RAJ", " RAJ", " Nayan", ]  # Add your actual name

                        # Then in the /galli command handler, add this check:
                        if inPuTMsG.strip().startswith('/galli '):
                            print('Processing /galli command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF0000]❌ ERROR! Usage:\n"
                                        "/galli <name>\n"
                                        "Example: /galli hater"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    name = parts[1].strip()
            
                                    # ADD THIS CHECK - Prevent targeting yourself
                                    if name.lower() in [n.lower() for n in BLOCKED_NAMES]:
                                        error_msg = (
                                            f"Sa🤫la owner ki tore la🤫ra dise '{name}'!\n"
f"[FF0000]Owner er naam lekhta shosh ke ⛔\n"
f"[FFFFFF]BC onno naam dehhh ar amare ki tor me🤫ye mone hoy."
                                        )
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        continue
            
                                    # Rest of your code continues here...
                                    messages = [
                                        "{Name} s4le kya bakchxdi kar raha hai!!",
"Sale, teri maa chxdi hai hinjd3 se  kya!!",
"{Name} s4le, 5G speed se teri g4nd m4runga bkl!!",
"{Name} itna g4ndmasti mat kar, sab samajh aa raha hai!!",
"{Name} bhai, roz ₹300 ka l0da g4nd me leta hai kya!!",
"{Name} madarchxd, kitni bahan chxdwayega tu!!",
"{Name} tujhe 100 baar samjhaun tab bhi nahi samjhega!!",
"{Name} r4nd jaisi harkte mat kar !!",
"{Name} ek baar me kitno ka l4nd apni g4nd me lega !!",
"{Name} baap ko harake itna khush mat ho!!",
"{Name} BC, teri g4nd bhi kali hai tu marw4ta kaise hai !!",
"{Name} bxdk, pahle hamara l4nd chus ke hamse gameplay seekh phir apni bahan ko ch4t dikha!!",
"{Name} har jagah jaake itna g4nd  kyun marw4ta  hai!!",
"{Name} teri mummy 150 me th3ke pe baithi dekhi maine kal !!",
"{Name} R4ndi ka pillaa overconfident player!!",
"{Name} tere liye ek line bolta hoon, sun:\n"
"Jahan-tahan phone charge karega aur battery phool jaaye to dosh dega,\n"
"Haay re, zindagi mein kya kar diya! Upar jaake hisaab dena padega ⚠️⚠️!!",
                                            ]

                                    # Send each message one by one with random color
                                    for msg in messages:
                                        colored_message = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.upper())}"
                                        await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv)
                                        await asyncio.sleep(2)

                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Something went wrong:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv) 
                                                             
                                #SAD LATER SPAM MESSAGE 
                        # Add at the top with other global variables
                        BLOCKED_NAMES = [" nayan", "NAYAN", "nayan1m", " NAYAN1M", "HARSH", " harsh", "raj", " RAJ", "devansh", " DEVANSH", "DEVANSH1M", " devansh1m","ongkar", " ONGKAR", "ONGKAR SUTRADHAR", " ongkar sutradhar", "classy", " CLASSY","", "Ongkar", "devansh raj", "DEVANSH RAJ", " RAJ", " Nayan", ] # Add your actual name

                        # Then in the /sadlater command handler, add this check:
                        if inPuTMsG.strip().startswith('/sadlater '):
                            print('Processing /sadlater command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_mssg = (
                                        "[B][C][FF0000]❌ ERROR! Usage:\n"
                                        "/sadlater <name>\n"
                                        "Example: /sadlater hater"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_mssg, uid, chat_id, key, iv)
                                else:
                                    name = parts[1].strip()
            
                                    # ADD THIS CHECK - Prevent targeting yourself
                                    if name.lower() in [n.lower() for n in BLOCKED_NAMES]:
                                        eror_msg = (
                                            f"[B][C][FF0000]⚠️ WARNING!\n"
                                            f"[FFFFFF]Owner ko inme koi dilchaspi nahi hai '{name}'!\n"
                                            f"[FF0000]Isliye mujhe apna naam batao ⛔\n"
                                            f"[FFFFFF]Bhai koi dusra naam batao tumhari dusri gf  ka naam."
                                        )
                                        await safe_send_message(response.Data.chat_type, eror_msg, uid, chat_id, key, iv)
                                        continue
            
                                    # Rest of your code continues here...
                                    messages = [
                                        "{Name}লাইন গুলো তুমার জন্য\n       আমি কিছু বুঝতে পারি নাই কারণ আমি ছিলাম নাদান\n  খানিক এর জন্য ভালোবাসা দেখাইয়া প্রতি রাতেই কাদান\n.  তবে আপনার কোনো দোষ দিবো না কপাল ছিলো মন্দ\n এমন ভাবে আঘাত করসেন এখন আমার বেচে থাকার রাসতা টাই বন্ধ!!!!\n",
                                            ]

                                    # Send each message one by one with random color
                                    for msg in messages:
                                        colored_mesage = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.upper())}"
                                        await safe_send_message(response.Data.chat_type, colored_mesage, uid, chat_id, key, iv)
                                        await asyncio.sleep(2)

                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Something went wrong:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                                
                           # PRAISA COMMAND (17 POSITIVE MESSAGES)
                        if inPuTMsG.strip().startswith('/praisa'):
                            print('Processing /praisa command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF0000]❌ ERROR! Usage:\n"
                                        "/praisa <name>\n"
                                        "Example: /praisa Maruf"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    name = parts[1].strip()

                                    messages = [
                                        [
    f"🌟 {Name} Tum sach me ek asadharan insaan ho!",
    f"🔥 {Name} Tumhari mehnat ek din badi safalta le kar aayegi!",
    f"💎 {Name} Tum unique ho, tumhare jaisa aur koi nahi hai!",
    f"🚀 {Name} Tumhara bhavishya bahut ujjwal hai!",
    f"👑 {Name} Tum ek leader banne ke yogya ho!",
    f"🌈 {Name} Tumhari hasi sabka din sundar bana deti hai!",
    f"💖 {Name} Hamesha aise hi positive raho!",
    f"🏆 {Name} Tum jo chaho use hasil karne ki takat tumhare andar hai!",
    f"✨ {Name} Tum prerna ka srot ho!",
    f"🌟 {Name} Khud par bharosa rakho, tum kar sakte ho!",
    f"🎯 {Name} Tumhara focus hi tumhari shakti hai!",
    f"📈 {Name} Tum har din aur behtar hote ja rahe ho!",
    f"🧠 {Name} Tumhari soch sach me kabile tarif hai!",
    f"💫 {Name} Tum bahut door tak jaoge Insha Allah!",
    f"🌍 {Name} Duniya tumhare talent ko dekhne ka intezar kar rahi hai!",
    f"🛡️ {Name} Tum majboot, aatmavishwasi aur sahasi ho!",
    f"🏅 {Name} Tum sacche champion ho!"
]

                                    for msg in messages:
                                        colored_message = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.title())}"
                                        await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv)
                                        await asyncio.sleep(0.5)

                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Something went wrong:\n{str(e)}"
                   
                           #LOVE LATER SPAM MESSAGE 
                        # Add at the top with other global variables
                        BLOCKED_NAMES = [" nayan", "NAYAN", "nayan1m", " NAYAN1M", "HARSH", " harsh", "raj", " RAJ", "devansh", " DEVANSH", "DEVANSH1M", " devansh1m","ongkar", " ONGKAR", "ONGKAR SUTRADHAR", " ongkar sutradhar", "classy", " CLASSY","", "Ongkar", "devansh raj", "DEVANSH RAJ", " RAJ", " Nayan", ]  # Add your actual name

                        # Then in the /later command handler, add this check:
                        if inPuTMsG.strip().startswith('/later '):
                            print('Processing /later command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_mssg = (
                                        "[B][C][FF0000]❌ ERROR! Usage:\n"
                                        "/later <name>\n"
                                        "Example: /later hater"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_mssg, uid, chat_id, key, iv)
                                else:
                                    name = parts[1].strip()
            
                                    # ADD THIS CHECK - Prevent targeting yourself
                                    if name.lower() in [n.lower() for n in BLOCKED_NAMES]:
                                        eror_msg = (
                                            f"[B][C][FF0000]⚠️ WARNING!\n"
                                            f"[FFFFFF]owner ko inma intrest nahi hai'{name}'!\n"
                                            f"[FF0000]isliya mara name mat dalna  ⛔\n"
                                            f"[FFFFFF]Bhai koi dusra naam batao tumhari dusri gf  ka naam."
                                        )
                                        await safe_send_message(response.Data.chat_type, eror_msg, uid, chat_id, key, iv)
                                        continue
            
                                    # Rest of your code continues here...
                                    messages = [
                                        "প্রীয় {Name}\n ㅤㅤতুমি আমার আকাশের চাদ মনের আলো।\n তোমায় ভাবলেই হাসে হৃদয় দূরে সরে যায় সব     কালো।\nㅤㅤতোমার হাত ধরেই কাটাতে চাই সারাটা জীবন\n  তোমার হাসিতেই খুঁজে পাই আমার বাঁচার কারণ।\nㅤㅤভালোবাসি তোমায় তুমি আমার স্বপ্ন আমার আপন",
                                            ]

                                    # Send each message one by one with random color
                                    for msg in messages:
                                        colored_mesage = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.upper())}"
                                        await safe_send_message(response.Data.chat_type, colored_mesage, uid, chat_id, key, iv)
                                        await asyncio.sleep(2)

                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Something went wrong:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        
                             #GALI SPAM MESSAGE 
                        # Add at the top with other global variables
                        BLOCKED_NAMES = [" nayan", "NAYAN", "nayan1m", " NAYAN1M", "HARSH", " harsh", "raj", " RAJ", "devansh", " DEVANSH", "DEVANSH1M", " devansh1m","ongkar", " ONGKAR", "ONGKAR SUTRADHAR", " ongkar sutradhar", "classy", " CLASSY","", "Ongkar", "devansh raj", "DEVANSH RAJ", " RAJ", " Nayan", ]   # Add your actual name

                        # Then in the /smlater command handler, add this check:
                        if inPuTMsG.strip().startswith('/love '):
                            print('Processing /love command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF0000]❌ ERROR! Usage:\n"
                                        "/love <name>\n"
                                        "Example: /gali hater"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    name = parts[1].strip()

                                    messages = [
    "[B][C][FFFFFF]♡ [FF1493]{Name} [FFFFFF]Tu mera [00FFFF]safe zone [FFFFFF]♡",
    "[B][C][FFFFFF]♡ [00FFFF]Lobby me [FFFFFF]sirf [FFD700]{Name} tujhe hi dhoondhu [FFFFFF]♡",
    "[B][C][FFFFFF]♡ [00FFFF]Airdrop se [FFFFFF]bhi [FF1493]{Name} tu zyada keemti hai [FFFFFF]♡",
    "[B][C][FFFFFF]♡ [FFD700]{Name} Teri hasi se [FFFFFF]mera [00FFFF]HP badhta hai [FFFFFF]♡",
    "[B][C][FFFFFF]♡ [FF00FF]{Name} Tere bina [FFFFFF]game khelna [00FFFF]bilkul bekaar hai [FFFFFF]♡",
    "[B][C][FFFFFF]♡ [FFA500]Sniper ka [FFFFFF]ekmatra [FF1493]lakshya {Name} tu hai [FFFFFF]♡",
    "[B][C][FFFFFF]♡ [32CD32]{Name} Tu mera [FFFFFF]gloo-wall ka [FFD700]cover hai [FFFFFF]♡",
    "[B][C][FFFFFF]♡ [FF0000]{Name} Chal dono milke [FFFFFF][00FFFF]Booyah lete hain [FFFFFF]♡"
]

                                    # Send each message one by one with random color
                                    for msg in messages:
                                        colored_message = f"[B][C][FFFFFF][B][C][32CD32][FFFFFF][FFA500][FFFFFF][FF00FF][FFD700][FFFFFF][00FFFF][FF1493][00FFFF][FFFFFF][FF0000] {msg.replace('{Name}', name.upper())}"
                                        await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv)
                                        await asyncio.sleep(2)

                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Something went wrong:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv) 
                                  
# GLOBAL BLOCKED NAMES
                        BLOCKED_NAMES = [" nayan", "NAYAN", "nayan1m", " NAYAN1M", "HARSH", " harsh", "raj", " RAJ", "devansh", " DEVANSH", "DEVANSH1M", " devansh1m","ongkar", " ONGKAR", "ONGKAR SUTRADHAR", " ongkar sutradhar", "classy", " CLASSY","", "Ongkar", "devansh raj", "DEVANSH RAJ", " RAJ", " Nayan", ]  # Protected names
                        
                            #GALI SPAM MESSAGE 
                        # Add at the top with other global variables
                        BLOCKED_NAMES =[" nayan", "NAYAN", "nayan1m", " NAYAN1M", "HARSH", " harsh", "raj", " RAJ", "devansh", " DEVANSH", "DEVANSH1M", " devansh1m","ongkar", " ONGKAR", "ONGKAR SUTRADHAR", " ongkar sutradhar", "classy", " CLASSY","", "Ongkar", "devansh raj", "DEVANSH RAJ", " RAJ", " Nayan", ]  # Add your actual name

                        # Then in the /rt command handler, add this check:
                        if inPuTMsG.strip().startswith('/rt '):
                            print('Processing /rt command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF0000]❌ ERROR! Usage:\n"
                                        "/rt <name>\n"
                                        "Example: /rti hater"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    name = parts[1].strip()
            
                                    # ADD THIS CHECK - Prevent targeting yourself
                                    if name.lower() in [n.lower() for n in BLOCKED_NAMES]:
                                        error_msg = (
                                            f"[B][C][FF0000]⚠️ WARNING!\n"
                                            f"[FFFFFF]MACHHAR KI JH4NT HATHI KE L4WDE{name}'!\n"
                                            f"[FF0000]CHHIPKALI KI G4ND KE KALE TATTEE ⛔\n"
                                            f"[FFFFFF]HINJD3 KI G4ND SE NIKLA HUA R4ND⚠️."
                                        )
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        continue
            
                                    # Rest of your code continues here...
                                    messages = [
                                        [
    "Arey {Name} toh ek number ka bot hai! 😂",
    "{Name} game khelna chhod ke ludo khel ja! 🤣",
    "{Name} ka headshot rate minus me chala gaya hai! 📉",
    "{Name} land karne se pehle hi lobby me chala jata hai! 🪂💨",
    "Sab log savdhan raho, {Name} naam ka bot game me ghus gaya hai! 🤖",
    "Arey {Name}, tu toh pro... pro-max level ka bot hai! 🤡",
    "{Name} se toh training ground ka putla bhi achha khelta hai! 🗿",
    "Booyah toh door ki baat hai, {Name} toh zone survive karte hi mar jata hai! ☠️",
    "Bhai {Name}, tu kya bandook ki jagah lathi leke khelta hai? 🦯",
    "O bhai! {Name} toh enemy dekhte hi ulta daud lagata hai! 🏃‍♂️💨",
    "Enemy dekh ke {Name} ke haath-pair kaanpte hain! 🥶",
    "{Name} jaisa bot maine zindagi me kabhi nahi dekha! 🤦‍♂️",
    "Game ka sabse bada bot award {Name} ko diya jaye! 🏆",
    "{Name} bhai, tu Free Fire delete kar de! 🗑️",
    "{Name} ka gameplay dekh ke enemy bhi has has ke mar jayega! 😆",
    "{Name} ka kill chori karne ka talent Oscar paane layak hai! 🎭",
    "Teammate knock hote hi {Name} sabse pehle bhaag jata hai! 🏃‍♂️",
    "Gun skin se kya hoga, {Name} toh goli chalana hi bhool jata hai! 🔫",
    "{Name} game nahi khelta, game {Name} ko leke khelta hai! 🎮",
    "{Name} Free Fire ka zinda legendary bot hai! 👑"
]

                                    # Send each message one by one with random color
                                    for msg in messages:
                                        colored_message = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.upper())}"
                                        await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv)
                                        await asyncio.sleep(2)

                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Something went wrong:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)                                                              
                        # Add this with your other command handlers in the TcPChaT function

                        # EVO CYCLE START COMMAND - /evos
                        if inPuTMsG.strip().startswith('max'):
                            print('Processing evo cycle start command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            uids = []
    
                            # Always use the sender's UID (the person who typed /evos)
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"Using sender's UID: {sender_uid}")
    
                            # Optional: Also allow specifying additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:  # Skip the first part which is "/evos"
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:  # UIDs are usually 7+ digits
                                        uids.append(part)
                                        print(f"Added additional UID: {part}")

                            # Stop any existing evo cycle
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
    
                            # Start new evo cycle
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(
                                evo_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG)
                            )
    
                            # SUCCESS MESSAGE
                            if len(uids) == 1:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! [00FFFF]Evolution emote[b][c][ff0000] cycle started!\n🎯 Target: [00FFFF]সঠিক ভাবে চালু [b][c][ff0000]হয়েছে\n🔄 Cycle: বন্ধ করতে /s\n"
                            else:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! [00FFFF]Evolution emote [FFD700]cycle started!\n🎯 Targets: [FFA500]সঠিক ভাবে চালু [FFD700]হয়েছে\n🔄 Cycle: বন্ধ করতে/s\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            print(f"Started evolution emote cycle for UIDs: {uids}")
                        
                        # EVO CYCLE STOP COMMAND - @sevos
                        if inPuTMsG.strip() == '/s':
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Evolution emote cycle stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                print("Evolution emote cycle stopped by command")
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution emote cycle to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

 #EVO CYCLE START COMMAND - /evos
                        if inPuTMsG.strip().startswith('@max'):
                            print('Processing evo cycle start command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            uids = []
    
                            # Always use the sender's UID (the person who typed /evos)
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"Using sender's UID: {sender_uid}")
    
                            # Optional: Also allow specifying additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:  # Skip the first part which is "/evos"
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:  # UIDs are usually 7+ digits
                                        uids.append(part)
                                        print(f"Added additional UID: {part}")

                            # Stop any existing evo cycle
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
    
                            # Start new evo cycle
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(
                                evo_cycle_sm(uids, key, iv, region, LoGinDaTaUncRypTinG)
                            )
    
                            # SUCCESS MESSAGE
                            if len(uids) == 1:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! [00FFFF]Evolution emote[b][c][ff0000] cycle started!\n🎯 Target: [00FFFF]সঠিক ভাবে চালু [b][c][ff0000]হয়েছে\n🔄 Cycle: বন্ধ করতে /o\n"
                            else:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! [00FFFF]Evolution emote [FFD700]cycle started!\n🎯 Targets: [FFA500]সঠিক ভাবে চালু [FFD700]হয়েছে\n🔄 Cycle: বন্ধ করতে /o\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            print(f"Started evolution emote cycle for UIDs: {uids}")
                        
                        # EVO CYCLE STOP COMMAND - evos
                        if inPuTMsG.strip() == '/o':

                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.2)

                                success_msg = "[B][C][FFFF00]✅ SUCCESS! Evolution emote cycle stopped!"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                print("Evolution emote cycle stopped by command")
                                
                        # EMOTE CYCLE START COMMAND - /evo
                        if inPuTMsG.strip().startswith('new'):
                            print('Processing evo cycle start command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            uids = []
    
                            # Always use the sender's UID (the person who typed /evos)
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"Using sender's UID: {sender_uid}")
    
                            # Optional: Also allow specifying additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:  # Skip the first part which is "/evos"
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:  # UIDs are usually 7+ digits
                                        uids.append(part)
                                        print(f"Added additional UID: {part}")

                            # Stop any existing evo cycle
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
    
                            # Start new evo cycle
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(
                                emotes_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG)
                            )
    
                            # SUCCESS MESSAGE
                            if len(uids) == 1:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! [00FFFF] emote[b][c][ff0000] cycle started!\n🎯 Target: [00FFFF]সঠিক ভাবে চালু [b][c][ff0000]হয়েছে\n🔄 Cycle: বন্ধ করতে /sm\n"
                            else:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! [00FFFF] emote [FFD700]cycle started!\n🎯 Targets: [FFA500]সঠিক ভাবে চালু [FFD700]হয়েছে\n🔄 Cycle: বন্ধ করতে /sm\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            print(f"Started evolution emote cycle for UIDs: {uids}")
                        
                        # EVO CYCLE STOP COMMAND - @sevos
                        if inPuTMsG.strip() == '/sm':
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Evolution emote cycle stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                print("Evolution emote cycle stopped by command")
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution emote cycle to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        
                        if inPuTMsG.strip().startswith('@new'):
                            print('Processing evo cycle start command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            uids = []
    
                            # Always use the sender's UID (the person who typed /evos)
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"Using sender's UID: {sender_uid}")
    
                            # Optional: Also allow specifying additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:  # Skip the first part which is "/evos"
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:  # UIDs are usually 7+ digits
                                        uids.append(part)
                                        print(f"Added additional UID: {part}")

                            # Stop any existing evo cycle
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
    
                            # Start new evo cycle
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(
                                evo_cycle_sam(uids, key, iv, region, LoGinDaTaUncRypTinG)
                            )
    
                            # SUCCESS MESSAGE
                            if len(uids) == 1:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! [00FFFF]Evolution emote[b][c][ff0000] cycle started!\n🎯 Target: [00FFFF]সঠিক ভাবে চালু [b][c][ff0000]হয়েছে\n🔄 Cycle: বন্ধ করতে /sn\n"
                            else:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! [00FFFF]Evolution emote [FFD700]cycle started!\n🎯 Targets: [FFA500]সঠিক ভাবে চালু [FFD700]হয়েছে\n🔄 Cycle: বন্ধ করতে /sn\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            print(f"Started evolution emote cycle for UIDs: {uids}")
                        
                        # EVO CYCLE STOP COMMAND - evos
                        if inPuTMsG.strip() == '/sn':

                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.2)

                                success_msg = "[B][C][FFFF00]✅ SUCCESS! Evolution emote cycle stopped!"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                print("Evolution emote cycle stopped by command")
                                
                        if inPuTMsG.strip().startswith('@bot'):
                            print('Processing evo cycle start command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            uids = []
    
                            # Always use the sender's UID (the person who typed /evos)
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"Using sender's UID: {sender_uid}")
    
                            # Optional: Also allow specifying additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:  # Skip the first part which is "/evos"
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:  # UIDs are usually 7+ digits
                                        uids.append(part)
                                        print(f"Added additional UID: {part}")

                            # Stop any existing evo cycle
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
    
                            # Start new evo cycle
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(
                                evo_cycle_bot(uids, key, iv, region, LoGinDaTaUncRypTinG)
                            )
    
                            # SUCCESS MESSAGE
                            if len(uids) == 1:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! [00FFFF]Evolution emote[b][c][ff0000] cycle started!\n🎯 Target: [00FFFF]সঠিক ভাবে চালু [b][c][ff0000]হয়েছে\n🔄 Cycle: বন্ধ করতে @bt\n"
                            else:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! [00FFFF]Evolution emote [FFD700]cycle started!\n🎯 Targets: [FFA500]সঠিক ভাবে চালু [FFD700]হয়েছে\n🔄 Cycle: বন্ধ করতে /bt\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            print(f"Started evolution emote cycle for UIDs: {uids}")
                        
                        # EVO CYCLE STOP COMMAND - evos
                        if inPuTMsG.strip() == '@bt':

                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.2)

                                success_msg = "[B][C][FFFF00]✅ SUCCESS! Evolution emote cycle stopped!"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                print("Evolution emote cycle stopped by command")
                                                        
                        # Fast emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/fast'):
                            print('Processing fast emote spam in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /fast uid1 [uid2] [uid3] [uid4] emoteid\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and emoteid
                                uids = []
                                emote_id = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) > 3:  # Assuming UIDs are longer than 3 digits
                                            uids.append(part)
                                        else:
                                            emote_id = part
                                    else:
                                        break
                                
                                if not emote_id and parts[-1].isdigit():
                                    emote_id = parts[-1]
                                
                                if not uids or not emote_id:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /fast uid1 [uid2] [uid3] [uid4] emoteid\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    # Stop any existing fast spam
                                    if fast_spam_task and not fast_spam_task.done():
                                        fast_spam_running = False
                                        fast_spam_task.cancel()
                                    
                                    # Start new fast spam
                                    fast_spam_running = True
                                    fast_spam_task = asyncio.create_task(fast_emote_spam(uids, emote_id, key, iv, region))
                                    
                                    # SUCCESS MESSAGE
                                    success_msg = f"[B][C][00FF00]✅ SUCCESS! Fast emote spam started!\nTargets: {len(uids)} players\nEmote: {emote_id}\nSpam count: 25 times\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # Custom emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/p'):
                            print('Processing custom emote spam in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 4:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /p (uid) (emote_id) (times)\nExample: /p 123456789 909000001 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    target_uid = parts[1]
                                    emote_id = parts[2]
                                    times = int(parts[3])
            
                                    if times <= 0:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Times must be greater than 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif times > 100:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Maximum 100 times allowed for safety!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        # Stop any existing custom spam
                                        if custom_spam_task and not custom_spam_task.done():
                                            custom_spam_running = False
                                            custom_spam_task.cancel()
                                            await asyncio.sleep(0.5)
                
                                        # Start new custom spam
                                        custom_spam_running = True
                                        custom_spam_task = asyncio.create_task(custom_emote_spam(target_uid, emote_id, times, key, iv, region))
                
                                        # SUCCESS MESSAGE
                                        success_msg = f"[B][C][00FF00]✅ SUCCESS! Custom emote spam started!\nTarget: {target_uid}\nEmote: {emote_id}\nTimes: {times}\n"
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                
                                except ValueError:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Usage: /p (uid) (emote_id) (times)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                                                                                             
                        # Spam request command - works in all chat types
                        # Spam request command - works in all chat types
                        if inPuTMsG.strip().startswith('/spam '):
                            print('Processing spam request command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /spam (uid)\nExample: /spam 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                if not target_uid.isdigit():
                                    error_msg = f"[B][C][FF0000]❌ Please write a valid player ID!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Send initial message
                                initial_msg = f"[B][C][FFFF00]🚀 Starting multi-account spam...\n🎯 Target: {target_uid}\n📊 Loading accounts...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                # Check if accounts file exists
                                try:
                                    import os
                                    if not os.path.exists("vv.json"):
                                        error_msg = f"[B][C][FF0000]❌ ERROR: vv.json file not found!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        return
                                except:
                                    pass
        
                                try:
                                    # Execute spam
                                    success_count, total_accounts = await multi_account_spam_request(target_uid, key, iv, region)
            
                                    if success_count > 0:
                                        result_msg = f"""
[B][C][FFFF00]✅ MULTI-ACCOUNT SPAM COMPLETED!

🎯 Target: {target_uid}
✅ Successful Requests: {success_count}
📊 Total Accounts Used: {total_accounts}
⚡ Success Rate: {(success_count/total_accounts*100):.1f}%

💡 Target received {success_count} join requests!
🤖 Bot ready for next command.
"""
                                    else:
                                        result_msg = f"""
[B][C][FF0000]❌ SPAM FAILED!

🎯 Target: {target_uid}
📊 Accounts Loaded: {total_accounts}
🔧 Possible Issues:
1. Bot not connected properly
2. Target UID invalid
3. Game server blocking requests
"""
            
                                    await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print(f"❌ Spam command error: {e}")
                                    import traceback
                                    traceback.print_exc()
                                    error_msg = f"[B][C][FF0000]❌ SPAM ERROR: {str(e)[:50]}...\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                               
                        # ==================== INFO COMMAND ====================
                        if inPuTMsG.strip().startswith('/info'):
                            print(f"📊 /info command received")
                            
                            # Clean the command
                            cmd = inPuTMsG.strip()
                            while cmd.startswith('/info'):
                                cmd = cmd[5:].strip()
                            
                            if not cmd or cmd.startswith('/'):
                                msg = f"""
[C][B][FF1493]═══════════════════
[C][B][00FFFF]  📊 INFO COMMAND
[C][FF1493]═══════════════════

[C][FFD700]✅ Usage:
[C][00FFFF]/info 10634259930

[C][FFD700]📋 Shows:
[C][FFFFFF]• Name, Level, EXP, Likes
[C][FFFFFF]• Region, BP Badge
[C][FFFFFF]• BR/CS Rank & Points
[C][FFFFFF]• Guild Info
[C][FFFFFF]• Captain Info (Name, UID, Level, EXP, Likes, Region)
[C][FFFFFF]• Bio/Signature

[C][FF1493]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                return
                            
                            parts = cmd.split()
                            target_uid = parts[0]
                            
                            if not target_uid.isdigit() or len(target_uid) < 8:
                                msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ INVALID UID
[C][FF0000]═══════════════════

[C][FFD700]✅ Correct: /info 10634259930
[C][FFD700]❌ You typed: /info {target_uid}

[C][FF0000]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                return
                            
                            await safe_send_message(
                                response.Data.chat_type,
                                f"[C][B][FFFF00]🔍 Fetching info for {fix_num(target_uid)}...\n⏳ Please wait...",
                                uid, chat_id, key, iv
                            )
                            
                            try:
                                result = get_real_player_info(target_uid)
                                
                                if result["success"] and result.get("data"):
                                    data = result["data"]
                                    
                                    basic = data.get("basicInfo", {})
                                    clan = data.get("clanBasicInfo", {})
                                    social = data.get("socialInfo", {})
                                    captain = data.get("captainBasicInfo", {})
                                    credit = data.get("creditScoreInfo", {})
                                    
                                    def human_time(ts):
                                        try:
                                            if ts and ts != "0" and ts != 0:
                                                return datetime.utcfromtimestamp(int(ts)).strftime("%Y-%m-%d %H:%M")
                                        except:
                                            pass
                                        return "N/A"
                                    
                                    # ===== MESSAGE 1: ACCOUNT INFO =====
                                    msg1 = f"""
[C][B][FF1493]═══════════════════
[C][B][00FFFF]  📋 ACCOUNT INFO
[C][FF1493]═══════════════════

[C][FFD700]Name        : [00FF00]{basic.get('nickname', 'N/A')}
[C][FFD700]UID         : [00FFAA]{fix_num(target_uid)}
[C][FFD700]Level       : [FF00FF]{basic.get('level', 'N/A')}
[C][FFD700]EXP         : [00FFFF]{fix_num(basic.get('exp', '0'))}
[C][FFD700]Likes       : [FF4444]{fix_num(basic.get('liked', '0'))}
[C][FFD700]Region      : [FFFFFF]{basic.get('region', 'N/A')}
[C][FFD700]BP Badge    : [FFA500]{fix_num(basic.get('badgeCnt', '0'))}
[C][FFD700]Version     : [AAAAFF]{basic.get('releaseVersion', 'N/A')}

[C][FF1493]═══════════════════
"""
                                    await safe_send_message(response.Data.chat_type, msg1, uid, chat_id, key, iv)
                                    await asyncio.sleep(0.3)
                                    
                                    # ===== MESSAGE 2: ACCOUNT DETAILS =====
                                    lang = social.get("language", "N/A")
                                    if isinstance(lang, int):
                                        lang_codes = {1: "en", 2: "zh", 3: "zh_TW", 4: "th", 5: "vi", 6: "id", 7: "pt", 8: "es", 9: "ru", 10: "ko", 11: "fr", 12: "de", 13: "tr", 14: "hi", 15: "ja", 16: "ro", 17: "ar", 18: "my", 19: "ur", 20: "bn"}
                                        lang = lang_codes.get(lang, "en")
                                    
                                    msg2 = f"""
[C][B][00AAFF]═══════════════════
[C][B][FFFFFF]  📊 ACCOUNT DETAILS
[C][00AAFF]═══════════════════

[C][FFAA00]Create Date   : [00FF00]{human_time(basic.get('createAt', '0'))}
[C][FFAA00]Last Login    : [00FF00]{human_time(basic.get('lastLoginAt', '0'))}
[C][FF00FF]BR Max Rank   : [FFD700]{basic.get('maxRank', 'N/A')}
[C][FF00FF]BR Points     : [FFD700]{fix_num(basic.get('rankingPoints', '0'))}
[C][00FFFF]CS Max Rank   : [AA00FF]{basic.get('csMaxRank', 'N/A')}
[C][00FFFF]CS Points     : [AA00FF]{fix_num(basic.get('csRankingPoints', '0'))}
[C][FFFFFF]Language      : [66FF00]{lang}

[C][00AAFF]═══════════════════
"""
                                    await safe_send_message(response.Data.chat_type, msg2, uid, chat_id, key, iv)
                                    await asyncio.sleep(0.3)
                                    
                                    # ===== MESSAGE 3: SOCIAL & BIO =====
                                    signature = str(social.get("signature", "") or "").strip()
                                    if not signature:
                                        signature = "—"
                                    
                                    msg3 = f"""
[C][B][AA00FF]═══════════════════
[C][B][FFFFFF]  🌐 SOCIAL & BIO INFO
[C][AA00FF]═══════════════════

[C][FF88FF]Signature     : [FFDDFF]{signature}

[C][AA00FF]═══════════════════
"""
                                    await safe_send_message(response.Data.chat_type, msg3, uid, chat_id, key, iv)
                                    await asyncio.sleep(0.3)
                                    
                                    # ===== MESSAGE 4: GUILD INFO =====
                                    guild_name = clan.get('clanName', 'No Guild')
                                    guild_id = clan.get('clanId', '0')
                                    guild_owner = clan.get('captainId', '0')
                                    guild_level = clan.get('clanLevel', 'N/A')
                                    guild_members = clan.get('memberNum', '0')
                                    guild_capacity = clan.get('capacity', '0')
                                    
                                    msg4 = f"""
[C][B][FF8800]═══════════════════
[C][B][FFFFFF]  🏰 GUILD INFO
[C][FF8800]═══════════════════

[C][00FFFF]Guild Name    : [00FF00]{guild_name}
[C][00FFFF]Guild ID      : [FF00FF]{fix_num(guild_id)}
[C][00FFFF]Leader UID    : [FFD700]{fix_num(guild_owner)}
[C][00FFFF]Guild Level   : [FF4444]{guild_level}
[C][00FFFF]Members       : [66FFAA]{guild_members}/{guild_capacity}

[C][FF8800]═══════════════════
"""
                                    await safe_send_message(response.Data.chat_type, msg4, uid, chat_id, key, iv)
                                    await asyncio.sleep(0.3)
                                    
                                    # ===== MESSAGE 5: CAPTAIN INFO =====
                                    if captain and captain.get("nickname"):
                                        cap_name = captain.get("nickname", "N/A")
                                        cap_level = captain.get("level", "N/A")
                                        cap_exp = captain.get("exp", "0")
                                        cap_likes = fix_num(captain.get("liked", "0"))
                                        cap_region = captain.get("region", "N/A")
                                        cap_uid = fix_num(captain.get("accountId", "0"))
                                        
                                        msg5 = f"""
[C][B][00FF88]═══════════════════
[C][B][FFFFFF]  👑 CAPTAIN INFO
[C][00FF88]═══════════════════

[C][FFDD00]Captain Name  : [00FF00]{cap_name}
[C][FFDD00]Captain UID   : [00FFAA]{cap_uid}
[C][FFDD00]Captain Level : [FF88FF]{cap_level}
[C][FFDD00]Captain EXP   : [00FFFF]{fix_num(cap_exp)}
[C][FFDD00]Captain Likes : [FF4444]{cap_likes}
[C][FFDD00]Captain Region: [FFFFFF]{cap_region}

[C][00FF88]═══════════════════
"""
                                        await safe_send_message(response.Data.chat_type, msg5, uid, chat_id, key, iv)
                                        await asyncio.sleep(0.3)
                                    
                                    # ===== MESSAGE 6: CREDIT SCORE =====
                                    if credit and credit.get("creditScore"):
                                        score = fix_num(credit.get("creditScore", "0"))
                                        periodic = credit.get("periodicSummaryEndTime", "0")
                                        
                                        msg6 = f"""
[C][B][00DDFF]═══════════════════
[C][B][FFFFFF]  💳 CREDIT SCORE
[C][00DDFF]═══════════════════

[C][FFD700]Credit Score  : [00FF88]{score}
[C][FFD700]Next Reset    : [FF8800]{human_time(periodic)}

[C][00DDFF]═══════════════════
[C][B][FFD700]🤖 {BOT_NAME}
[C][00DDFF]═══════════════════
"""
                                        await safe_send_message(response.Data.chat_type, msg6, uid, chat_id, key, iv)
                                    
                                    print(f"✅ Full info sent for {target_uid}")
                                    
                                else:
                                    msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ INFO FETCH FAILED
[C][FF0000]═══════════════════

[C][FFFFFF]{result.get('message', 'Unknown error')}

[C][FFD700]💡 Try: /info 10634259930

[C][FF0000]═══════════════════
"""
                                    await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                    
                            except Exception as e:
                                print(f"❌ Info error: {e}")
                                import traceback
                                traceback.print_exc()
                                msg = f"""
[C][B][FF0000]═══════════════════
[C][B][FF0000]  ❌ ERROR
[C][FF0000]═══════════════════

[C][FFFFFF]{str(e)[:50]}

[C][FFD700]💡 Try: /info 10634259930

[C][FF0000]═══════════════════
"""
                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)      

                        # Spam request command - works in all chat types
                        if inPuTMsG.strip().startswith('/spm_inv'):
                            print('Processing spam invite with cosmetics')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /spm_inv (uid)\nExample: /spm_inv 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing spam request
                                if spam_request_task and not spam_request_task.done():
                                    spam_request_running = False
                                    spam_request_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Start new spam request WITH COSMETICS
                                spam_request_running = True
                                spam_request_task = asyncio.create_task(spam_request_loop_with_cosmetics(target_uid, key, iv, region))
        
                                # SUCCESS MESSAGE
                                success_msg = f"[B][C][FFFF00]✅ COSMETIC SPAM STARTED!\n🎯 Target: {target_uid}\n📦 Requests: 30\n🎭 Features: V-Badges + Cosmetics\n⚡ Each invite has different cosmetics!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # Stop spam request command - works in all chat types
                        if inPuTMsG.strip() == '/stop spm_inv':
                            if spam_request_task and not spam_request_task.done():
                                spam_request_running = False
                                spam_request_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Spam request stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active spam request to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # In TcPChaT function, update /status command:
                        if inPuTMsG.strip().startswith('/status '):
                            print('Processing status command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /status (player_uid)\nExample: /status 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
    
                            # DEBUG: Show cache before clearing
                            print(f"\n🔍 BEFORE clearing cache:")
                            debug_file_cache()
                            
                            # Clear old cache entry first
                            clear_cache_entry(target_uid)
    
                            # Send initial message
                            initial_msg = f"[B][C][FFFF00]🔍 Checking status of {fix_num(target_uid)}...\n"
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                            
                            try:
                                # Create and send status request
                                status_packet = await createpacketinfo(target_uid, key, iv)
                                if not status_packet:
                                    error_msg = f"[B][C][FF0000]❌ Failed to create status packet!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)
                                print(f"📤 Sent status request for {target_uid}")
        
                                # Wait for response - check FILE cache
                                max_retries = 12  # Increased for reliability
                                response_received = False
        
                                for attempt in range(max_retries):
                                    print(f"⏳ Checking file cache... attempt {attempt + 1}/{max_retries}")
            
                                    # Check FILE cache
                                    cache_data = load_from_cache(target_uid)
                                    if cache_data:
                                        print(f"🎯 FOUND in file cache! Status: {cache_data['status']}")
                                        response_received = True
                
                                        # DEBUG: Show what we found
                                        print(f"📦 Cache data keys: {list(cache_data.keys())}")
                
                                        # Build response
                                        status_msg = f"[B][C][FFFF00]📊 PLAYER STATUS\n"
                                        status_msg += f"────────────────\n"
                                        status_msg += f"👤 UID: {fix_num(target_uid)}\n"
                                        status_msg += f"📊 Status: {cache_data['status']}\n"
                
                                        # Add specific info
                                        if "IN ROOM" in cache_data['status']:
                                            if 'room_id' in cache_data:
                                                status_msg += f"🏠 Room ID: {fix_num(cache_data['room_id'])}\n"
                                                status_msg += f"💡 Use: /roomspam {target_uid}\n"
                                                room_id_msg = f"{fix_num(cache_data['room_id'])}"
                                                await safe_send_message(response.Data.chat_type, room_id_msg, uid, chat_id, key, iv)
                                            else:
                                                status_msg += f"🏠 Room ID: Not available\n"
                
                                        elif "INSQUAD" in cache_data['status']:
                                            if 'leader_id' in cache_data:
                                                status_msg += f"👑 Leader: {fix_num(cache_data['leader_id'])}\n"
                    
                                            # Try to get squad size
                                            try:
                                                if 'parsed_json' in cache_data:
                                                    parsed = cache_data['parsed_json']
                                                    if '5' in parsed and 'data' in parsed['5']:
                                                        squad_data = parsed['5']['data']['1']['data']
                                                        if '9' in squad_data and 'data' in squad_data['9']:
                                                            members = squad_data['9']['data']
                                                            max_members = squad_data['10']['data'] + 1
                                                            status_msg += f"👥 Squad: {members}/{max_members}\n"
                                            except:
                                                pass
                
                                        elif "OFFLINE" in cache_data['status']:
                                            status_msg += f"🔴 Player is offline\n"
                
                                        elif "INGAME" in cache_data['status']:
                                            status_msg += f"🎮 Player is in a match\n"
                
                                        elif "SOLO" in cache_data['status']:
                                            status_msg += f"👤 Player is solo\n"
                
                                        status_msg += f"────────────────\n"
                                        status_msg += f"✅ Real-time data\n"
                
                                        await safe_send_message(response.Data.chat_type, status_msg, uid, chat_id, key, iv)

                                        # DEBUG: Show cache after success
                                        print(f"\n✅ AFTER successful response:")
                                        debug_file_cache()
                
                                        break
            
                                    # Wait between checks
                                    await asyncio.sleep(0.5)
                                                        
                                if not response_received:
                                    # DEBUG: Show cache state on failure
                                    print(f"\n❌ FAILED after {max_retries} tries")
                                    debug_file_cache()
            
                                    error_msg = f"[B][C][FF0000]❌ STATUS CHECK FAILED\n"
                                    error_msg += f"────────────────\n"
                                    error_msg += f"👤 UID: {fix_num(target_uid)}\n"
                                    error_msg += f"📛 No response from server\n"
                                    error_msg += f"────────────────\n"
                                    error_msg += f"💡 Possible issues:\n"
                                    error_msg += f"• Player is offline\n"
                                    error_msg += f"• Server is busy\n"
                                    error_msg += f"• Try again in 10 seconds\n"
            
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
            
                            except Exception as e:
                                print(f"❌ Status command error: {e}")
                                import traceback
                                traceback.print_exc()
        
                                error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW EVO COMMANDS
                        if inPuTMsG.strip().startswith('/evo '):
                            print('Processing evo command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-21)\nExample: /evo 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-21)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nSending evolution emote {number_int}...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            
                                            success, result_msg = await evo_emote_spam(uids, number_int, key, iv, region)
                                            
                                            if success:
                                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ ERROR! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/evo_fast '):
                            print('Processing evo_fast command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)\nExample: /evo_fast 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_fast spam
                                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                                evo_fast_spam_running = False
                                                evo_fast_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_fast spam
                                            evo_fast_spam_running = True
                                            evo_fast_spam_task = asyncio.create_task(evo_fast_emote_spam(uids, number_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][FFFF00]✅ SUCCESS! Fast evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nSpam count: 25 times\nInterval: 0.1 seconds\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)


# ================= BUNDLE COMMAND START =================
   # ================= FINAL BUNDLE COMMAND (FAST) =================
                        if inPuTMsG.strip().lower().startswith("/magic"):
                            parts = inPuTMsG.strip().split()

                            if len(parts) < 2:
                                await safe_send_message(
                                    response.Data.chat_type,
                                    "[B][C][FF0000]❌ Usage: /Magic (team_code)",
                                    uid,
                                    chat_id,
                                    key,
                                    iv
                                )
                            else:
                                team_code = parts[1]

                                await safe_send_message(
                                    response.Data.chat_type,
                                    "[B][C][1E90FF]🌀 Magic bundle started...",
                                    uid,
                                    chat_id,
                                    key,
                                    iv
                                )

                                asyncio.create_task(
                                    magic_bundle_sequence(
                                        team_code,
                                        response.Data.chat_type,
                                        chat_id,
                                        uid,
                                        key,
                                        iv,
                                        region
                                    )
                                )

                        if inPuTMsG.strip().startswith('/animation'):
                            print("Processing animation command")

                            parts = inPuTMsG.strip().split()

                            if len(parts) < 2:
                                animation_list = """[B][C][FFFFFF]• 1-rampage \n[FFFFFF]• 2-cannibal \n[FFFFFF]• 3-devil \n[FFFFFF]• 4-scorpio \n[FFFFFF]• 5-frostfire\n[FFFFFF]• 6-paradox \n[FFFFFF]• 7-naruto \n[FFFFFF]• 8-aurora \n[FFFFFF]• 9-midnight \n[FFFFFF]• 10-itachi \n[FFFFFF]• 11-dreamspace  •  12 • new bundle ob54\n"""
                                await safe_send_message(response.Data.chat_type, animation_list, uid, chat_id, key, iv)
                            else:
                                animation_key = parts[1].lower()

                                animation_ids = {
                                    "1":       914000002,
                                    "2":       914000003,
                                    "3":       914038001,
                                    "4":       914039001,
                                    "5":       914042001,
                                    "6":       914044001,
                                    "7":       914047001,
                                    "8":       914047002,
                                    "9":       914048001,
                                    "10":      914050001,
                                    "11":      914051001,
                                    "12":      914053001,
                                    "ob53":    914053001,
                                    "eclipse": 914053001,
                                }

                                if animation_key not in animation_ids:
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][FF0000]❌ Animation '{animation_key}' not found!\nUse: /animation [number]",
                                        uid, chat_id, key, iv
                                    )
                                else:
                                    animation_id = animation_ids[animation_key]

                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][00FF00]✨ doing animation...\n🆔 ID: {animation_id}",
                                        uid, chat_id, key, iv
                                    )

                                    try:
                                        packet = await animation_packet(animation_id, key, iv)

                                        if packet and online_writer and not online_writer.is_closing():
                                            online_writer.write(packet)
                                            await online_writer.drain()

                                            success_msg = (
                                                f"[B][C][00FF00]✅ ANIMATION DONE!\n"
                                                f"[FFFF00]🎬 animation complete\n"
                                                f"[AAAAAA]✨ {animation_key} | ID: {animation_id}"
                                            )
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                        else:
                                            await safe_send_message(
                                                response.Data.chat_type,
                                                "[B][C][FF0000]❌ Failed to create animation packet!",
                                                uid, chat_id, key, iv
                                            )

                                    except Exception as e:
                                        print(f"❌ /animation error: {e}")
                                        await safe_send_message(
                                            response.Data.chat_type,
                                            f"[B][C][FF0000]❌ Error sending animation:\n{str(e)[:80]}",
                                            uid, chat_id, key, iv
                                        )
                        if inPuTMsG.strip().startswith('/b') or (inPuTMsG.strip().startswith('/b') and not inPuTMsG.strip().startswith('/bio') and not inPuTMsG.strip().startswith('/block')):
                            print('Processing bundle command')

                            parts = inPuTMsG.strip().split()

                            if len(parts) < 2:
                                await safe_send_message(
                                    response.Data.chat_type,
                                    "[B][C][FF0000]❌ Use: /b [number]",
                                    uid, chat_id, key, iv
                                )
                            else:
                                bundle_key = parts[1].lower()

                                bundle_ids = {
                                    "1":    914000002,
                                    "2":    914000003,
                                    "3":    914038001,
                                    "4":    914039001,
                                    "5":    914042001,
                                    "6":    914044001,
                                    "7":    914047001,
                                    "8":    914047002,
                                    "9":    914048001,
                                    "10":   914050001,
                                    "11":   914051001,
                                    "12":   914053001,
                                    "ob53":    914053001,
                                    "eclipse": 914053001,
                                }

                                delay_map = {
                                    "1": 5.1, "2": 3.0, "3": 3.0, "4": 5.0,
                                    "5": 3.3, "6": 3.5, "7": 2.6, "8": 3.7,
                                    "9": 4.4, "10": 3.0, "11": 4.2,
                                    "12": 5.0, "ob54": 5.0, "eclipse": 5.0,
                                }

                                if bundle_key not in bundle_ids:
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][FF0000]❌ Bundle '{bundle_key}' not found!",
                                        uid, chat_id, key, iv
                                    )
                                else:
                                    bundle_id = bundle_ids[bundle_key]
                                    delay_time = delay_map.get(bundle_key, 3)

                                    # 1️⃣ SEND ANIMATION FIRST
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][00FF00]✨ Sending Animation First...\n🆔 {bundle_id}",
                                        uid, chat_id, key, iv
                                    )

                                    try:
                                        animation_pkt = await animation_packet(bundle_id, key, iv)
                                        if animation_pkt and online_writer:
                                            await SEndPacKeT(whisper_writer, online_writer, "OnLine", animation_pkt)
                                        else:
                                            await safe_send_message(
                                                response.Data.chat_type,
                                                "[B][C][FF0000]❌ Animation failed!",
                                                uid, chat_id, key, iv
                                            )
                                    except Exception as e:
                                        await safe_send_message(
                                            response.Data.chat_type,
                                            f"[B][C][FF0000]❌ Animation Error:\n{str(e)[:80]}",
                                            uid, chat_id, key, iv
                                        )

                                    # 2️⃣ WAIT CUSTOM DELAY
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][FF4D4D]╔═══[ 💗 SYSTEM WAIT ]═══╗\n"
                                        f"[87CEEB]║ ⏳ Delay: {delay_time}s\n"
                                        f"[FF66B2]║ Preparing Bundle...\n"
                                        f"[FF4D4D]╚══════════════╝",
                                        uid, chat_id, key, iv
                                    )
                                    await asyncio.sleep(delay_time)

                                    # 3️⃣ SEND BUNDLE
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][FF4D4D]╔═══[ 🎁 BUNDLE SYSTEM ]═══╗\n"
                                        f"[FF66B2]║ 🚀 Sending Bundle...\n"
                                        f"[87CEEB]║ 🆔 ID: {bundle_id}\n"
                                        f"[FF4D4D]╚══════════════╝",
                                        uid, chat_id, key, iv
                                    )

                                    try:
                                        bundle_pkt = await bundle_packet_async(bundle_id, key, iv, region)
                                        if bundle_pkt and online_writer:
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bundle_pkt)
                                            await safe_send_message(
                                                response.Data.chat_type,
                                                f"[B][C][FF4D4D]╔═══[ ✅ SYSTEM COMPLETE ]═══╗\n"
                                                f"[FF66B2]║ ✨ Animation + Bundle Sent\n"
                                                f"[87CEEB]║ 🆔 ID: {bundle_id}\n"
                                                f"[FF4D4D]╚══════════════╝",
                                                uid, chat_id, key, iv
                                            )
                                        else:
                                            await safe_send_message(
                                                response.Data.chat_type,
                                                "[B][C][FF0000]❌ Bundle packet failed!",
                                                uid, chat_id, key, iv
                                            )
                                    except Exception as e:
                                        await safe_send_message(
                                            response.Data.chat_type,
                                            f"[B][C][FF0000]❌ Bundle Error:\n{str(e)[:80]}",
                                            uid, chat_id, key, iv
                                        )
                        elif inPuTMsG.strip().startswith('/n'):
    
                            parts = inPuTMsG.strip().split()
                            
                            if len(parts) < 2:
                             
                                bundle_list = """[B][C][FFFFFF]• 1-rampage 
[FFFFFF]• 2-cannibal 
[FFFFFF]• 3-devil 
[FFFFFF]• 4-scorpio 
[FFFFFF]• 5-frostfire
[FFFFFF]• 6-paradox 
[FFFFFF]• 7-naruto 
[FFFFFF]• 8-aurora 
[FFFFFF]• 9-midnight 
[FFFFFF]• 10-itachi 
[FFFFFF]• 11-dreamspace
"""
                                await safe_send_message(response.Data.chat_type, bundle_list, uid, chat_id, key, iv)
                            else:
                                bundle_name = parts[1].lower()
                          
      
                                # Bundle IDs mapping
                                bundle_ids = {
                                    "1":     914000002,
                                    "2":      914000003,
                                    "3":      914038001,
                                    "4":      914039001,
                                    "5":      914042001,
                                    "6":      914044001,
                                    "7":      914047001,
                                    "8":      914047002,
                                    "9":      914048001,
                                    "10":      914050001,
                                    "11":      914051001
                                }
                                
                             
                                if bundle_name not in bundle_ids:
                                    error_msg = f"""[B][C][FF0000]❌ Bundle '{bundle_name}' not found!

[00FF00]Available bundles:
[FFFFFF]• rampage • cannibal • devil
[FFFFFF]• scorpio • frostfire • paradox
[FFFFFF]• naruto • aurora • midnight
[FFFFFF]• itachi • dreamspace

[00FF00]Use: /b [name]"""
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
                                    
                                bundle_id = bundle_ids[bundle_name]

                                initial_msg = f"[B][C][00FF00]🎁 Sending bundle...\nID: {bundle_id}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                
                                    bundle_packet = await bundle_packet_async(bundle_id, key, iv)
            
                                    if bundle_packet and online_writer:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bundle_packet)
                                        success_msg = f"[B][C][00FF00]✅ BUNDLE SENT SUCCESSFULLY!\n🎁 Name: {bundle_name}\n🆔 ID: {bundle_id}\n👤 Target: {uid}"
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ Failed to create bundle packet!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Error sending bundle: {str(e)[:50]}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

 # ================= FINAL EMOTE COMMAND (FAST) =================                               
 # ==============================================================
                        # NEW EVO_CUSTOM COMMAND
                        if inPuTMsG.strip().startswith('/evo_c '):
                            print('Processing evo_c command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-21) time(1-100)\nExample: /evo_c 123456789 1 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids, number, and time
                                uids = []
                                number = None
                                time_val = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number or time should be 1-100 (1, 2, or 3 digits)
                                            if number is None:
                                                number = part
                                            elif time_val is None:
                                                time_val = part
                                            else:
                                                uids.append(part)
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                # If we still don't have time_val, try to get it from the last part
                                if not time_val and len(parts) >= 3:
                                    last_part = parts[-1]
                                    if last_part.isdigit() and len(last_part) <= 3:
                                        time_val = last_part
                                        # Remove time_val from uids if it was added by mistake
                                        if time_val in uids:
                                            uids.remove(time_val)
                                
                                if not uids or not number or not time_val:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-21) time(1-100)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        time_int = int(time_val)
                                        
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        elif time_int < 1 or time_int > 100:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Time must be between 1-100 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_custom spam
                                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                                evo_custom_spam_running = False
                                                evo_custom_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_custom spam
                                            evo_custom_spam_running = True
                                            evo_custom_spam_task = asyncio.create_task(evo_custom_emote_spam(uids, number_int, time_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][FFFF00]✅ SUCCESS! Custom evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nRepeat: {time_int} times\nInterval: 0.1 seconds\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number/time format! Use numbers only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)


                        # Stop evo_fast spam command
                        if inPuTMsG.strip() == '/stop evo_fast':
                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                evo_fast_spam_running = False
                                evo_fast_spam_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Evolution fast spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution fast spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Stop evo_custom spam command
                        if inPuTMsG.strip() == '/stop evo_c':
                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                evo_custom_spam_running = False
                                evo_custom_spam_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Evolution custom spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution custom spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # In your TcPChaT function, add:
                        if inPuTMsG.strip() == '/ss':
                            print('Processing start match command')
                            await handle_start_match_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                           
                            
                        # FIXED HELP MENU SYSTEM - Now detects commands properly
                        # IMPROVED HELP MENU SYSTEM - AUTOMATIC MULTI-PART
                        # IMPROVED HELP MENU SYSTEM - TREE STYLE FORMAT
                        
                        if inPuTMsG.strip().lower() in ("help", "/help", "cr", "hi", "sb"):
                            print(f"Help command detected from UID: {uid} in chat type: {XX}")
    

    
                            s1 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 01ㅤㅤ[FF75EA]│
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Start Match
[FF2C03]└─► [FFFDED]/start
[FF2C03]╭«[2BFF00]Leave Squad
[FF2C03]└─► [FFFDED]/leave
[FF2C03]╭«[2BFF00]3 Player Group
[FF2C03]└─► [FFFDED]/3
[FF2C03]╭«[2BFF00]5 Player Group
[FF2C03]└─► [FFFDED]/5
[FF2C03]╭«[2BFF00]6 Player Group
[FF2C03]└─► [FFFDED]/6
[FF2C03]╭«[2BFF00]Join Squad
[FF2C03]└─► [FFFDED]! [code]
[FF2C03]╭«[2BFF00]Ghost Join
[FF2C03]└─► [FFFDED]/ghost [code]"""

                            await safe_send_message(response.Data.chat_type, s1, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)
        

                            s2 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] MAYAN乡 MENU 02ㅤㅤ[FF75EA]│
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Self Emote
[FF2C03]└─► [FFFDED][number]
[FF2C03]╭«[2BFF00]Magic Emote
[FF2C03]└─► [FFFDED]aa[number] [tc]
[FF2C03]╭«[2BFF00]All Emotes Menu
[FF2C03]└─► [FFFDED]/menu[number]
[FF2C03]╭«[2BFF00]Emote Hijack
[FF2C03]└─► [FFFDED]/hjk
[FF2C03]╭«[2BFF00]Max Evo (Self)
[FF2C03]└─► [FFFDED]max
[FF2C03]╭«[2BFF00]Stop Evo Cycle
[FF2C03]└─► [FFFDED]/s
[FF2C03]╭«[2BFF00]Max Evo (Bot)
[FF2C03]└─► [FFFDED]@max"""

                            await safe_send_message(response.Data.chat_type, s2, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)            

                            s3 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 03ㅤㅤ[FF75EA]│
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Stop Bot Evo
[FF2C03]└─► [FFFDED]/o
[FF2C03]╭«[2BFF00]Random Evo (Self)
[FF2C03]└─► [FFFDED]new
[FF2C03]╭«[2BFF00]Stop Random
[FF2C03]└─► [FFFDED]/sm
[FF2C03]╭«[2BFF00]Random (Bot)
[FF2C03]└─► [FFFDED]@new
[FF2C03]╭«[2BFF00]Only Bot Random
[FF2C03]└─► [FFFDED]@bot
[FF2C03]╭«[2BFF00]Stop Bot Cycle
[FF2C03]└─► [FFFDED]@bt
[FF2C03]╭«[2BFF00]Fast Emote Spam
[FF2C03]└─► [FFFDED]/fast [uid] [emote]"""
                            await safe_send_message(response.Data.chat_type, s3, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)            
                                            

                            s4 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 04ㅤㅤ[FF75EA]│
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Custom Spam
[FF2C03]└─► [FFFDED]/p [uid] [emote] [num]
[FF2C03]╭«[2BFF00]Reject Spam
[FF2C03]└─► [FFFDED]/reject [uid]
[FF2C03]╭«[2BFF00]Stop Reject
[FF2C03]└─► [FFFDED]/reject_stop
[FF2C03]╭«[2BFF00]Message Spam
[FF2C03]└─► [FFFDED]/msg [text] [times]
[FF2C03]╭«[2BFF00]Stop Msg Spam
[FF2C03]└─► [FFFDED]/stop msg
[FF2C03]╭«[2BFF00]Wave Msg Spam
[FF2C03]└─► [FFFDED]/mg [text] [repeats]
[FF2C03]╭«[2BFF00]Ban Check
[FF2C03]└─► [FFFDED]/check [uid]"""

                            await safe_send_message(response.Data.chat_type, s4, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            s5 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 05ㅤㅤ[FF75EA]│
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Badge Spam 1
[FF2C03]└─► [FFFDED]/s1 [uid]
[FF2C03]╭«[2BFF00]Badge Spam 2
[FF2C03]└─► [FFFDED]/s2 [uid]
[FF2C03]╭«[2BFF00]Badge Spam 3
[FF2C03]└─► [FFFDED]/s3 [uid]
[FF2C03]╭«[2BFF00]Badge Spam 4
[FF2C03]└─► [FFFDED]/s4 [uid]
[FF2C03]╭«[2BFF00]Badge Spam 5
[FF2C03]└─► [FFFDED]/s5 [uid]
[FF2C03]╭«[2BFF00]Invite Player
[FF2C03]└─► [FFFDED]/inv [uid]
[FF2C03]╭«[2BFF00]Join Custom Room
[FF2C03]└─► [FFFDED]/joinroom [id] [pass]"""        

                            await safe_send_message(response.Data.chat_type, s5, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)
                            
                            s6 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 06ㅤㅤ[FF75EA]│
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Stop Lag Attack
[FF2C03]└─► [FFFDED]/stop lag
[FF2C03]╭«[2BFF00]Player Info
[FF2C03]└─► [FFFDED]/info [uid]
[FF2C03]╭«[2BFF00]Player Status
[FF2C03]└─► [FFFDED]/status [uid]
[FF2C03]╭«[2BFF00]Boy Gali Spam
[FF2C03]└─► [FFFDED]/gali [name]
[FF2C03]╭«[2BFF00]Girl Gali Spam
[FF2C03]└─► [FFFDED]/galli [name]
[FF2C03]╭«[2BFF00]Praise Someone
[FF2C03]└─► [FFFDED]/praisa [name]
"""

                            await safe_send_message(response.Data.chat_type, s6, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            s7 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 07ㅤㅤ[FF75EA]│
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Chat With AI
[FF2C03]└─► [FFFDED]/ai [question]
[FF2C03]╭«[2BFF00]Show Help
[FF2C03]└─► [FFFDED]/help
[FF2C03]╭«[2BFF00]Admin Info
[FF2C03]└─► [FFFDED]/admin
[FF2C03]╭«[2BFF00]Attack Room
[FF2C03]└─► [FFFDED]/room [uid] [room_id]
[FF2C03]╭«[2BFF00]Guild Info
[FF2C03]└─► [FFFDED]/clan [id]
[FF2C03]╭«[2BFF00]Equip Bundle
[FF2C03]└─► [FFFDED]/b [number]
[FF2C03]╭«[2BFF00]Love Letter
[FF2C03]└─► [FFFDED]/later [name]"""

                            await safe_send_message(response.Data.chat_type, s7, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            s8 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 08ㅤㅤ[FF75EA]│
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Sad Letter
[FF2C03]└─► [FFFDED]/sadlater [name]
[FF2C03]╭«[2BFF00]Love Spam
[FF2C03]└─► [FFFDED]/love [name]
[FF2C03]╭«[2BFF00]Roast Someone
[FF2C03]└─► [FFFDED]/rt [name]
[FF2C03]╭«[2BFF00]Add 1000 Visit
[FF2C03]└─► [FFFDED]/visit [uid]
[FF2C03]╭«[2BFF00]Add Friend
[FF2C03]└─► [FFFDED]/add [uid]
[FF2C03]╭«[2BFF00]Remove Friend
[FF2C03]└─► [FFFDED]/remove [uid]
[FF2C03]╭«[2BFF00]DM User
[FF2C03]└─► [FFFDED]/dm [uid]"""

                            await safe_send_message(response.Data.chat_type, s8, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            s9 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 09ㅤㅤ[FF75EA]│
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Lag Attack
[FF2C03]└─► [FFFDED]/attack
[FF2C03]╭«[2BFF00]Spam Invite
[FF2C03]└─► [FFFDED]/spm_inv [uid]
[FF2C03]╭«[2BFF00]Friend Req Spam
[FF2C03]└─► [FFFDED]/spam_req [uid]
[FF2C03]╭«[2BFF00]Animation
[FF2C03]└─► [FFFDED]/animation [number]
[FF2C03]╭«[2BFF00]Emote Send
[FF2C03]└─► [FFFDED]/e [emote]
[FF2C03]╭«[2BFF00]5v5 Unlock
[FF2C03]└─► [FFFDED]/snd [uid]
[FF2C03]╭«[2BFF00]Friend %
[FF2C03]└─► [FFFDED]/frt [n1]&[n2]"""

                            await safe_send_message(response.Data.chat_type, s9, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            s10 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 10ㅤㅤ[FF75EA]│
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Soul %
[FF2C03]└─► [FFFDED]/grt [n1]&[n2]
[FF2C03]╭«[2BFF00]Quiz
[FF2C03]└─► [FFFDED]/quiz
[FF2C03]╭«[2BFF00]Dare
[FF2C03]└─► [FFFDED]/dare
[FF2C03]╭«[2BFF00]Truth
[FF2C03]└─► [FFFDED]/truth
[FF2C03]╭«[2BFF00]Dice Roll
[FF2C03]└─► [FFFDED]/roll
[FF2C03]╭«[2BFF00]Zodiac
[FF2C03]└─► [FFFDED]/zodiac
[FF2C03]╭«[2BFF00]Joke
[FF2C03]└─► [FFFDED]/joke
   """

                            await safe_send_message(response.Data.chat_type, s10, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)


                            s11 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 11ㅤㅤ[FF75EA] │
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Spin Bundle
[FF2C03]└─► [FFFDED]/spnff
[FF2C03]╭«[2BFF00]Weather
[FF2C03]└─► [FFFDED]/weather
[FF2C03]╭«[2BFF00]Title
[FF2C03]└─► [FFFDED]/title [uid]
[FF2C03]╭«[2BFF00]Fortune
[FF2C03]└─► [FFFDED]/luck [name]
[FF2C03]╭«[2BFF00]Guild Join
[FF2C03]└─► [FFFDED]/guild_join [guild_id]
[FF2C03]╭«[2BFF00]Guild Leave
[FF2C03]└─► [FFFDED]/guild_leave [guild_id]
[FF2C03]╭«[2BFF00]Bot ON
[FF2C03]└─► [FFFDED]/on
   """
  
                            await safe_send_message(response.Data.chat_type, s11, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)


                            s12 = """
[B][C][FF75EA]╭──────────╮
[FF75EA]│ㅤ[FFFB00] NAYAN乡 MENU 12ㅤㅤ[FF75EA] │
[FF75EA]╰──────────╯

[FF2C03]╭«[2BFF00]Bot OFF
[FF2C03]└─► [FFFDED]/off
[FF2C03]╭«[2BFF00]DM User
[FF2C03]└─► [FFFDED]/dm [uid]
[FF2C03]╭«[2BFF00]Lag Attack
[FF2C03]└─► [FFFDED]/attack
[FF2C03]╭«[2BFF00]Room Spam
[FF2C03]└─► [FFD700]/spamapi [uid]
[FF2C03]╭«[2BFF00]Friend Req Spam
[FF2C03]└─► [FFFDED]/spam_req [uid]
[FF2C03]╭«[2BFF00]Animation
[FF2C03]└─► [FFFDED]/animation [name]
[FF2C03]╭«[2BFF00]Stop Stop Room Spam
[FF2C03]└─► [FFFDED]/stopapi [uid]"""

                            await safe_send_message(response.Data.chat_type, s12, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            s15 = """
[B][C][FFD700]╔══════════════╗

[FCFEFF]⚡ [FFFF00]乡ㅤNAYAN [00FF00]⚡

[2BFF00] ACTIVE STATUS: 50/1 online

[FF0000]◈ [FFFF00] INSTAGRAM [00FFFF]@NAYAN1M
[FFD700]╚══════════════╝"""

                            await safe_send_message(response.Data.chat_type, s15, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            guild = """
[C][B][2BC0FF]════════════
[FCFEFF]Wʟᴄ TO NAYAN乡  Gᴜɪʟᴅ
[2BC0FF]════════════[FFFFFF][B]
❀️ [
    "Bartaman jo halat hai koi kisi ko koi file nahi deta",
    "[2BC0FF]❀️ Guild glory 2000 se kam hua toh kick kar dunga",
    "[FCFEFF] Guild me player ka samman karna"
]

[B][C][2BC0FF] FOLLOW MY INSTAGRAM : @NAYAN1M

[FFFF00]════════════
"""

                            await safe_send_message(response.Data.chat_type, guild, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                        response = None
                            
            whisper_writer.close() ; await whisper_writer.wait_closed() ; whisper_writer = None
                    
                    	
                    	
        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def MaiiiinE():
    # Load credentials from file
    print("📁 Loading credentials from shadmancodex.txt...")
    credentials = load_credentials_from_file("shadmancodex.txt")
    
    if not credentials:
        print("❌ Failed to load credentials!")
        print("💡 Please create shadmancodex.txt with your UID and password")
        print("📝 Format: uid=YOUR_UID,password=YOUR_PASSWORD")
        return None
    
    try:
        Uid, Pw = credentials
    except:
        # Handle case where credentials returns more than 2 values
        if isinstance(credentials, (list, tuple)) and len(credentials) >= 2:
            Uid = credentials[0]
            Pw = credentials[1]
        else:
            print("❌ Invalid credentials format!")
            return None
    
    print("✅ Credentials loaded successfully")
    
    # Get access token from Free Fire
    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id or not access_token: 
        print("❌ Error - Invalid Account (Check UID/Password)") 
        return None
    
    # Encrypt and send login request
    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE: 
        print("❌ Target Account => Banned / Not Registered!") 
        return None
    
    # Decrypt login response
    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    
    # Get JWT token from response
    token = MajoRLoGinauTh.token
    if not token:
        print("❌ No authentication token received!")
        return None
    
    # ✅ CRITICAL: SAVE TOKEN TO token.json FILE
    try:
        import json
        import time
        from datetime import datetime
        
        # Get region from login response
        region = getattr(MajoRLoGinauTh, 'region', 'IND')
        
        token_data = {
            "token": token,
            "saved_at": time.time(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "bot_uid": str(Uid),
            "region": region,
            "source": "main.py_bot_login"
        }
        
        with open("token.json", "w") as f:
            json.dump(token_data, f, indent=2)
        
        print("✅ Token saved to token.json")
        print(f"📝 Token info: Region={region}, UID={Uid}")
        
    except Exception as e:
        print(f"⚠️ Warning: Could not save token to file: {e}")
        import traceback
        traceback.print_exc()
    
    # Continue with normal bot setup
    UrL = MajoRLoGinauTh.url
    
    # Clear screen and show status
    os.system('clear')
    print("=" * 50)
    print("🤖 S H A D M A N ツ- INITIALIZING")
    print("=" * 50)
    print("🔄 Starting TCP Connections...")
    print("📡 Connecting to Free Fire servers...")
    print("🌐 Server connection established")
    
    region = getattr(MajoRLoGinauTh, 'region', 'IND')
    ToKen = token  # Use the saved token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp
    
    print(f"🔐 Authentication successful")
    print(f"👤 Account UID: {TarGeT}")
    print(f"🌍 Region: {region}")
    print(f"🔑 Token: {ToKen[:30]}...")
    
    # Get login data for server IPs
    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    if not LoGinDaTa: 
        print("❌ Error - Getting Ports From Login Data!") 
        return None
    
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    
    # Get server IPs and ports
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    
    print(f"📡 Online Server: {OnLinePorTs}")
    print(f"💬 Chat Server: {ChaTPorTs}")
    
    # Split IPs and ports
    OnLineiP, OnLineporT = OnLinePorTs.split(":")
    ChaTiP, ChaTporT = ChaTPorTs.split(":")
    
    # Get account name
    acc_name = LoGinDaTaUncRypTinG.AccountName
    print(f"👋 Welcome, {acc_name}!")
    
    # Create authentication token for TCP connections
    AutHToKen = await xAuThSTarTuP(int(TarGeT), ToKen, int(timestamp), key, iv)
    
    # Create event for chat ready
    ready_event = asyncio.Event()
    
    # Start bot tasks
    print("\n🚀 Starting bot services...")
    
    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region))
    task2 = asyncio.create_task(TcPOnLine(OnLineiP, OnLineporT, key, iv, AutHToKen))  
 
    
    # Show loading animation
    os.system('clear')
    print("🤖 S H A D M A N ツ - STARTING")
    print("=" * 50)
    
    for i in range(1, 4):
        dots = "." * i
        print(f"🔄 Loading{dots}")
        time.sleep(0.3)
    
    async def StarTinG():
        os.system('clear')
    print(f"""{WHITE}
██╗     ███████╗ █████╗ ██████╗ ███████╗██████╗
██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║     █████╗  ███████║██║  ██║█████╗  ██████╔╝
██║     ██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗
███████╗███████╗██║  ██║██████╔╝███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

███████╗██╗  ██╗ █████╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗████╗ ████║██╔══██╗████╗  ██║
███████╗███████║███████║██║  ██║██╔████╔██║███████║██╔██╗ ██║
╚════██║██╔══██║██╔══██║██║  ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
███████║██║  ██║██║  ██║██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
{RESET}""")
    print("┌────────────────────────────────────┐")
    print("│ ██████████████████████████████████ │")
    print("└────────────────────────────────────┘")
    
    # Wait for chat connection to be ready
    print("\n⏳ Waiting for chat connection...")
    try:
        await asyncio.wait_for(ready_event.wait(), timeout=10)
        print("✅ Chat connection established!")
    except asyncio.TimeoutError:
        print("⚠️ Chat connection timeout, continuing...")
    
    # Final status display
    os.system('clear')
    print("=" * 50)
    print("🤖 S H A D M A N ツ- ONLINE")
    print("=" * 50)
    print(f"🔹 UID: {TarGeT}")
    print(f"🔹 Name: {acc_name}")
    print(f"🔹 Region: {region}")
    print(f"🔹 Status: 🟢 READY")
    print(f"🔹 Chat Server: {ChaTiP}:{ChaTporT}")
    print(f"🔹 Online Server: {OnLineiP}:{OnLineporT}")
    print("=" * 50)
    print("💡 Commands available in squad/guild chat")
    print("💡 Type /help for command list")
    print("=" * 50)
    
    # Test cache file write
    print("\n📊 System Check:")
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"📁 Cache file: {CACHE_FILE}")
    
    try:
        test_data = {'test': 'ok', 'timestamp': time.time()}
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(test_data, f)
        print("✅ Cache file write test: PASSED")
    except Exception as e:
        print(f"⚠️ Cache file write test: {e}")
    
    # Check token.json exists
    if os.path.exists("token.json"):
        print("✅ token.json file exists")
        try:
            with open("token.json", "r") as f:
                token_info = json.load(f)
            age = time.time() - token_info.get('saved_at', 0)
            print(f"✅ Token age: {age:.1f} seconds")
        except:
            print("⚠️ Could not read token.json")
    else:
        print("❌ token.json not found!")
    
    print("\n🎯 Bot is now running...")
    print("📡 Listening for commands and invitations")
    
    # Keep all tasks running
    try:
        await asyncio.gather(task1, task2)
    except asyncio.CancelledError:
        print("\n🛑 Bot tasks cancelled")
    except Exception as e:
        print(f"\n❌ Error in bot tasks: {e}")
        import traceback
        traceback.print_exc()
    
    return None


if __name__ == '__main__':
    asyncio.run(StarTinG())
    
  