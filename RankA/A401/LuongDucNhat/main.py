# Luong Duc Nhat's code

doc_dict = []
list_param = []

def main():
    doc_num = int(input())
    for i in range(doc_num):
        s = input().rstrip().split(' ')
        list_param.extend(s)

    for i in range(doc_num):
        doc_i = {
            "index": i,
            "x": int(list_param.pop(0)),
            "y": int(list_param.pop(0)),
            "w": int(list_param.pop(0)),
            "h": int(list_param.pop(0)),
            "s": int(list_param.pop(0)),
            "overlap": 0,
            "overlap_list": [],
        }
        doc_dict.append(doc_i)

    important_doc = check_important()
    checked_doc = overlap_layer()
    num_action = pickup(checked_doc, important_doc)

def check_important():
    important_doc = []
    for doc in doc_dict:
        if doc.get("s"):
            important_doc.append(doc.get("index"))
    return important_doc

def overlap_layer():
    doc_dict[-1]["overlap"] = 0
    checked_doc = list((doc_dict[-1]))
    for doc_1 in reversed(doc_dict[:-1]):
        for doc_2 in checked_doc:
            if check_overlap(doc_1, doc_2):
                doc_1["overlap"] += 1
                doc_1["overlap_list"].append(doc_2.get("index"))
        checked_doc.append(doc_1)
        return checked_doc

def check_overlap(doc_1, doc_2):
    print(type(doc_2))
    print(doc_2.get("x"))
    if (doc_2.get("x")+ doc_2.get("w") > doc_1.get("x")  and \
        doc_2.get("x")+ doc_2.get("w") < doc_1.get("x") + doc_1.get("w")) or \
        (doc_2.get("x") > doc_1.get("x")  and doc_2.get("x") < doc_1.get("x") + doc_1.get("w")):
        x_match = True    
    else:
        x_match = False

    if (doc_2.get("y") + doc_2.get("h") > doc_1.get("y") and \
        doc_2.get("y") + doc_2.get("h") < doc_1.get("y") + doc_1.get("h")) or \
        (doc_2.get("y") > doc_1.get("y") and doc_2.get("y") < doc_1.get("y") + doc_1.get("h")):
        y_match = True
    else:
        y_match = False

    if x_match and y_match:
        return True
    else:
        return False
            

def pickup(checked_doc, important_doc):
    overlap_doc = []
    for doc in important_doc:
        overlap_doc.extend(doc.get("overlap_list"))
    
    

if __name__ == "__main__":
    main()