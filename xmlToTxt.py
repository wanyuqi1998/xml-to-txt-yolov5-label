import os
import xml.dom.minidom

def xmlToyolo():
    xml_anno = 'animals/labels/trainAnimals'
    txt_anno = 'animals/labels/trainAnimals1'

    classes = ['cats', 'chicken', 'cows', 'deers', 'dogs', 'ducks',
               'foxes', 'horses', 'monkeys', 'pigs', 'sheep', 'wolves']
    dest = os.listdir(xml_anno)
    for path in dest:
        dom_r = xml.dom.minidom.parse(os.path.join(xml_anno,path))
        rot = dom_r.documentElement

        if rot.getElementsByTagName("size"):
            size = rot.getElementsByTagName("size")[0]
            width = int(size.getElementsByTagName('width')[0].firstChild.data)
            height = int(size.getElementsByTagName('height')[0].firstChild.data)
        else:
            print(path, 'no size attribute')

        if path[-4:] == 'jpeg':
            target = path[:-4]
        else:
            target = path[:-3]
        if not os.path.exists(os.path.join(txt_anno,target+"txt")):
            txt = open(os.path.join(txt_anno,target+"txt"),"w")
        else:

            continue
        for ob in rot.getElementsByTagName("object"):
            cls = ob.getElementsByTagName('name')[0].firstChild.data
            if cls in classes:
                # if not os.path.exists(os.path.join(txt_anno,path[:-3]+"txt")):
                #     txt = open(os.path.join(txt_anno,path[:-3]+"txt"),"w")
                for i in range(len(classes)):
                    if cls == classes[i]:
                        label = str(i)
                bndbox_r = ob.getElementsByTagName("bndbox")[0]
                xmin = bndbox_r.getElementsByTagName("xmin")[0].firstChild.data
                ymin = bndbox_r.getElementsByTagName("ymin")[0].firstChild.data
                xmax = bndbox_r.getElementsByTagName("xmax")[0].firstChild.data
                ymax = bndbox_r.getElementsByTagName("ymax")[0].firstChild.data
                w = int(xmax)-int(xmin)
                h = int(ymax)-int(ymin)
                c_x = int(xmin) + w/2
                c_y = int(ymin) + h/2
                if width == 0 or height == 0:
                    print(path)
                txt.write(label+" "+str(c_x/width)+" "+str(c_y/height)+" "+str(w/width)+" "+str(h/height)+"\n")
            else:
                print(path,cls,'cls not in classes')
xmlToyolo()