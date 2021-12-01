dic1 = {"hello": "world", "goede": "middag"}
dic2 = {"au": "gustus", 10:1000}
dic3 = {"Auto": "matisch", "fijn": "he"}
dic_samen = {}

def dict_samenvoegen():
    dic_samen.update(dic1)
    dic_samen.update(dic2)
    dic_samen.update(dic3)
    print(dic_samen)

dict_samenvoegen()
