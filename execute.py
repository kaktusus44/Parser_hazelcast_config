
import xml.etree.ElementTree as ET

tree = ET.parse('maps.xml')
root = tree.getroot()

newlist=[]

for item in root.iter():
    innerlist = []
    if item.tag == "{http://www.hazelcast.com/schema/config}map":
        innerlist.insert(1, "".join(item.attrib.values()))
        for i in item:
            if i.tag == "{http://www.hazelcast.com/schema/config}near-cache":
                for g in i:
                    if g.tag == "{http://www.hazelcast.com/schema/config}time-to-live-seconds":
                        innerlist.insert(1, g.text)
            elif i.tag == "{http://www.hazelcast.com/schema/config}max-size":
                innerlist.insert(1, i.text)
            elif i.tag == "{http://www.hazelcast.com/schema/config}time-to-live-seconds":
                innerlist.insert(1, i.text)
        newlist.append(innerlist)


print("NAME, ", "TTL, ", "SIZE, ", "NEAR_TTL")
for i in newlist:
    string_pool = (", ".join(i))
    print(string_pool)

