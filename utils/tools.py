import discord
import io
import random

from cowpy import cow


emote_id_match = re.compile(r"<:(.+?):(\d+)>")

animated_emote_id_match = re.compile(r"<a:(.+?):(\d+)>")

py = "```py\n{}```"

xl = "```xl\n{}```"

diff = "```diff\n{}```"

# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}

encode_morse ={
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    ".":".-.-.-",
    ",":"--..--",
    ":":"---...",
    "?":"..--..",
    "'":".----.",
    "-":"-....-",
    "/":"-..-.",
    "@":".--.-.",
    "=":"-...-",
    " ":"/"
}


cowList = {
    "cow":cow.Cowacter(),
    "hellokitty":cow.HelloKitty(),
    "bunny":cow.Bunny(),
    "cheese":cow.Cheese(),
    "milk":cow.Milk(),
    "bong":cow.BongCow(),
    "eyes":cow.Eyes(),
    "legitvore":cow.HeadInCow(),
    "666":cow.Satanic(),
    "frogs":cow.BudFrogs(),
    "daemon":cow.Daemon(),
    "moofasa":cow.Moofasa(),
    "mutilated":cow.Mutilated(),
    "skeleton":cow.Skeleton(),
    "small":cow.Small(),
    "excusemewhatthefuck":cow.Sodomized(),
    "garfield":cow.Stimpy(),
    "tux":cow.Tux(),
    "vader":cow.Vader()
}
