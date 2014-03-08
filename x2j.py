
from bs4 import BeautifulSoup as BS
import func_map


class x2j:
    fmap = None

    def __init__(self, func_json_file):
        self.fmap = func_map.func_map(func_json_file)
    def build_code(self, xml):
        """
        make xml to java 
        """
        self.__read_xml_file(xml)

    def __read_xml_file(self, file_name):
        with open(file_name, "r") as xml_file:
            soup = BS(xml_file, "xml")
            if len(soup) > 1:
                raise Exception("CAN NOT HAS MORE THAN ONE ROOT NODE")

            for item in soup:
                item_name = self._new_item(item)
                self._visit_child(item, item_name)
                
    def _new_item(self, item):
        has_id = item.has_attr(self._n("id"))
        if has_id:
            varible_name = self.combine_v_name(item.name, item)
            print item.name + " " + varible_name + " =" + "new " + item.name+"(context);"
        else:
            varible_name = self.combine_v_name(item.name)
            print item.name +" "+ varible_name + " =" + self._n("new") + item.name+"(context);"

        self._visit_attr(item, varible_name)
        return varible_name
   
    def _n(self, name):
        """
        name mapping for long attribute name
        """
        name_map = {"id":"android:id",
                    "new": " new "}
        return name_map[name];


    def _visit_attr(self, item, varible_name):
        """
        item.name is the tag name
        varible_name is the name of varible in java code
        """
        for attr in item.attrs:
            func = self.fmap.get_func(item.name, attr)
            if func:
                print self._set_item(varible_name, func, item[attr])

    def _set_item(self, name, func, *value):
        values = ",".join(value[:-1]) + value[-1]
        return name + "." + func + "(" + values + ");"

    def _visit_child(self, item, name):
        print "visit_child"

    def combine_v_name(self, prefix, *patterns):
        return "m" + prefix + "".join(patterns);




        
if __name__ == "__main__":
    parser = x2j("func.json")
    parser.build_code("button.xml")

