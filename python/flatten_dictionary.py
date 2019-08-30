def flatten_dictionary(dictionary):
    res = {}
    flatten(dictionary, "", res)
    return res


# returns key, value
def flatten(dic, upperkey, res):
    if not dic:
        return
    if type(dic) is str:
        res[upperkey] = dic
    else:
        for k in dic.keys():
            if not k:
                flatten(dic[k], upperkey, res)
            else:
                if not upperkey:
                    flatten(dic[k], k, res)
                else:
                    flatten(dic[k], upperkey+"."+k, res)


dic = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

flattened = flatten_dictionary(dic)
print(flattened)
