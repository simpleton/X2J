import json


class func_map:
    __fmap = {}
    def __init__(self, map_file_name):
        self.__fmap = self._read_tag_file(map_file_name)

    def _read_tag_file(self, file_name):
        with open(file_name, "r") as json_file:
            func_map = json.load(json_file)
        return func_map["func_map"]

    def get_func(self, type_name, tag_name):
        type_name = type_name + "-details"
        if type_name in self.__fmap:
            type_func_map = self.__fmap[type_name]
            if tag_name in type_func_map:
                return type_func_map[tag_name]
            else:
                return self._get_miss_func(tag_name)
        else:
            return self._get_miss_func(tag_name)
    
    def _get_miss_func(self, tag_name):
        mdict = {"android:layout_height" : "setHeight",
                 "android:layout_width": "setWidth"}
        if tag_name in mdict:
            return mdict[tag_name]
        else:
            return None
        
if __name__ == "__main__":
    mp = func_map("func.json")
    print mp.get_func("LinearLayout","android:layout_height")
