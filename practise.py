

#filenotfound error
#key error
#type error
#index error
#value error

try:
    file = open("a_file")
    dicto ={"key":"val"}
    print(dicto["disco"])
except FileNotFoundError:
    print("lmao")
except KeyError as error:
    print(f"error is {error}")
else:
    print("lol lmao happened")
finally:
    print("close the lol file")
raise KeyError("U are lmao")














