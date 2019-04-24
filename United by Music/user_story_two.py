import json
print("Your key to music world is ready!!! Start learning...")
with open("music_data.json") as data_file:
      data = json.load(data_file)
# openning the data file that contains our variables for this project
user_data = {"user_data":{}}

print("avaliable fields are:", data["specifications"]["type"].keys())
#showing the options
for key in data:
    user_data["user_data"][key] = input("please specify what you want to learn about instrument and or vocal")

if user_data["user_data"][key] == "instrument":
#showing options and asking for specififcations to user
    print("An instrument can belong to these families:",data["specifications"]["type"]["instrument"]["family"])
    family_user = input("what is the family of your instrument?")

    print("Level options are:",data["specifications"]["type"]["instrument"]["level"])
    level_ins = input("What is your level?")
#storing the user information
    data_instrument={}
    data_usr = {}
    data_usr["data_i_u"] = []
    data_usr["data_i_u"].append({
        "type":"instrument",
        "family":family_user,
        "level":level_ins })

    with open('user_specifications.json',"w") as outfile:
        json.dump(data_usr, outfile)
#showing different materials according to different families and levels
    if family_user == "brass":
        if level_ins == "beginner":
            from PIL import Image
            image = Image.open("begbrass.png")
            image.show()
        elif level_ins == "intermediate":
            from PIL import Image
            image = Image.open("intbrass.png")
            image.show()
        elif level_ins == "advanced":
            from PIL import Image
            image = Image.open("advbrass.jpg")
            image.show()

    if family_user == "percussion":
        if level_ins == "beginner":
            from PIL import Image
            image = Image.open("begperc.jpg")
            image.show()
        elif level_ins == "intermediate":
            from PIL import Image
            image = Image.open("intperc.png")
            image.show()
        elif level_ins == "advanced":
            from PIL import Image
            image = Image.open("adperc.jpg")
            image.show()

    if family_user == "strings":
        if level_ins == "beginner":
            from PIL import Image
            image = Image.open("beginnerstring.png")
            image.show()
        elif level_ins == "intermediate":
            from PIL import Image
            image = Image.open("intstring.png")
            image.show()
        elif level_ins == "advanced":
            from PIL import Image
            image = Image.open("adstring.png")
            image.show()

    if family_user == "woodwinds":

        if level_ins == "beginner":
            from PIL import Image
            image = Image.open("firstnoel.png")
            image.show()
        elif level_ins == "intermediate":
            from PIL import Image
            image = Image.open("pourunacabeza.png")
            image.show()
        elif level_ins == "advanced":
            from PIL import Image
            image = Image.open("vivaldi.png")
            image.show()


elif user_data["user_data"][key] == "vocal":
 # showing options and asking for specififcations to user
    print("A voice can belong to the types of:", data["specifications"]["type"]["vocal"]["voice_types"])
    vtype_user = input("what is the type of your voice?")

    print("Level options are:", data["specifications"]["type"]["vocal"]["level_vocal"])
    level_v = input("What is your level?")

    data_voice = {}
    data_usr_v = {}
    data_usr_v["data_v_u"] = []
    data_usr_v["data_v_u"].append({
        "type": "vocal",
        "voice_type":vtype_user,
        "level": level_v})

    with open('user_specifications.json', "w") as outfile:
        json.dump(data_usr_v, outfile)

 # showing different materials according to different voice types and levels
    if vtype_user == "alto":
        if level_v == "beginner":
            from PIL import Image
            image = Image.open("begalto.gif")
            image.show()
        elif level_v == "intermediate":
            from PIL import Image
            image = Image.open("intalto.png")
            image.show()
        elif level_v == "advanced":
            from PIL import Image
            image = Image.open("advalto.png")
            image.show()

    if vtype_user == "soprano":
        if level_v == "beginner":
            from PIL import Image
            image = Image.open("begsoprano.jpg")
            image.show()
        elif level_v == "intermediate":
            from PIL import Image
            image = Image.open("intsoprano.png")
            image.show()
        elif level_v == "advanced":
            from PIL import Image
            image = Image.open("advsoprano.png")
            image.show()

    if vtype_user == "tenor":
        if level_v == "beginner":
            from PIL import Image
            image = Image.open("begtenor.jpg")
            image.show()
        elif level_v == "intermediate":
            from PIL import Image
            image = Image.open("inttenor.png")
            Image.show()
        elif level_v == "advanced":
            from PIL import Image
            image = Image.open("advtenor.png")
            image.show()

    if vtype_user == "bass":
        if level_v == "beginner":
            from PIL import Image
            image = Image.open("begbass.gif")
            image.show()
        elif level_v == "intermediate":
            from PIL import Image
            image = Image.open("intbass.png")
            image.show()
        elif level_v == "advanced":
            from PIL import Image
            image = Image.open("advbass.png")
            image.show()
else:
    print("please type as required")
    exit


