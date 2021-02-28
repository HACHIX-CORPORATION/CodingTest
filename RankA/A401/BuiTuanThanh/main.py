print("Thank you for joining coding test")

# Em tính thiếu trường hợp, khi tài liệu nằm dưới bị phủ bởi tài liệu ở trên
# Vì thế nên em nghĩ cách làm này của em không đúng.

N = int(input())


# Store the list of document
document_list = []
for i in range(N):
    s = input().rstrip().split(' ') 
    s.append('1') # Use for find the number of overlap
    s = [int(j) for j in s ]
    document_list.append(s)

# # check
# print(document_list)


# When does overlap occur?
# x1, y1, w1, h1
# x2, y2, w2, h2
# Case 1: x1 <= x2 <= x1+w1
#       & y1 <= y2 <= y1+h1
# Case 2: x1 <=  x2 <= x1+w1
#       & y1 <= y2 + h2 <= y1 +h1
# Case 3: x1 <= x2 + w2 <= x1+w1
#       & y1 <= y2 <= y1 + h1
# Case 4: x1 <= x2 + w2 <= x1+w1
#        & y1 <= y2 + h2 <= y1 +h1

# A, Bを区別,　document_listの順番
# Algorithm: Dynamic program to find and
# store overlap number.

# For example A.overlap += B.overlap (B overlap A)
# A.overlap = 1 + B.overlap
# B.overlap = 1 + C.overlap = 1 + 1 = 2
# A.overlap = 1+2 = 3 => In order to take A, we need to take 3 documents

#check
# x1,y1,w1,h1,s1,n1 = document_list[0]
# print(x1,y1,w1,h1,n1)
# print(document_list.index(['0', '40', '40', '30', '1', '1']))


overlap_list = [0 for i in range(len(document_list))]

def overlap(doc, document_list):
    x1,y1,w1,h1,s1,n1 = doc
    # print(x1,y1,w1,h1)
    # n1 : doc[5]
    for d in document_list:
        if document_list.index(d) > document_list.index(doc):
            x2,y2,w2,h2,s2,n2 = d
            # print(x2,y2,w2,h2)
            if ((x1<=x2) and (x2<=x1+w1) and (y1<=y2) and (y2<=y1+h1)) \
                or  ((x1<=x2) and (x2<=x1+w1) and (y1<=y2+h2) and (y2+h2<=y1+h1)) \
                or ((x1<=x2+w2) and (x2+w2 <=x1+w1) and (y1<=y2) and (y2<=y1+h1)) \
                or  ((x1<=x2+w2) and (x2+w2<=x1+w1) and (y1<=y2+h2) and (y2+h2<=y1+h1)) :
                n1 = n1 + overlap(d,document_list)

    overlap_list[document_list.index(doc)] = n1
    return n1


#check
# A = [0, 40, 40, 30, 1, 1]
# print(overlap(A,document_list))

for d in document_list:
    overlap(d,document_list)

# print(overlap_list)

output = 0

for d in document_list:
    if d[4] == 1:
        output += overlap_list[document_list.index(d)]

print(output)
