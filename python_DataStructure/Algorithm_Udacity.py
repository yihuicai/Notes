def question1(s,t):
    '''
    Anagram substring means the each character in the substring can be rearraged in order.
    One thing special about anagrams is that, when sorted, the anagrams are the same to each other.
    We can consider slicing the s in the length of t, after that sort them and compare them.
    All the anagrams can be found using this method. And all the strings found using this method are all anagrams.
    Complexity:
        Time: suppose the length of s is n, t is m.
              The bottleneck is the time taken by slicing, sorting and comparing the s and t.
              The sorted part has worst case time complexity of O((nlog(n))+ O(mlog(m)).
              And since the outer for loop takes in n-m times, the overall time complexity is O((n-m))[O(nlog(n)+O(mlog(m))].
              In general, if n is very large and m very small, that leads to the the worst case time complexity O(n^2log(n).
        Space:
              The bottleneck is in the part of for loop.
              Since the sort is O(n) in space complexity and no extra variable is used in the for loop, no extra memory is used.
              In general, the space complexity is O(n)
    
    '''
    if s is None or t is None:
        return None
    if s == "" or t == "":
        return None
    length_s=len(s)
    length_t=len(t)
    # remember the last number in range is the last element index+1
    for i in range(0,length_s-length_t+1):
        if sorted(s[i:i+length_t])==sorted(t):
            return True
    return False



def question2(s):
    '''
    The paradromic string is symmetric, so we can find the substring by looping over all the char,
    and then comparing the left and right part of the char.
    Because we have to deal with both odd numbers and even numbers, it's easy to make mistakes doing string manipulation.
    So I make the both cases unified by adding a character so the paradromic substrings can be even number in length all the time.
    In the end, of course, I have to get rid of the added string.
    Complexity:
        Time: The worst case time complexity is the case that all the letters are the same. That takes 2*(1+2+..+n/2) times. That is O(n^2)
        Space: the bottle neck is the adding of special character and the declaration of returned string, so the space complexity is O(n).

    '''
    if s == None or len(s) == 0:
        return None
    mainstring=""
    for i in s:
        mainstring += "#"
        mainstring += i
    mainstring += "#"
    maxpali=0
    index=0
    for j in xrange(0, len(mainstring)):
        k=1
        while j-k>=0 and j+k<len(mainstring)and mainstring[j+k]==mainstring[j-k]:
            if maxpali<k:
                maxpali = k
                index=j
            k += 1
    unformatted_ret=mainstring[index-maxpali:index+maxpali+1]
    unformatted_ret=unformatted_ret.split("#")
    ret=""
    return ret.join(unformatted_ret)

    

def question3(G):
    '''
    This problem has two famous algorithm to solve: Kruscal and Prim.
    Kruscal algorithm has to sort the edges and pick them one by one from the smallest in order to connect unchosen vertices.
    This algorithm has to sort edges and utilize Union-Find data structure. And Since the Union-Find has to be defined by ourselves,
    it's very unnecessary and inconvenient.
    This makes me use Prim Algorithm.
    Suppose we have a starter vertex, we can push all the edges connected to it.
    Then choose the shortest edge that connected to an undiscovered vertex.
    Add the vertex into the container and add the edges for next vertex.
    Complexity:
        Time:  Since each time we add one vertex to the container, all the vertices has to be traversed once every time.
               And each edge connected to the newly added vertex would be put into the container.
               So the worst case is each time a vertex is traversed, all the edges in the graph is travered also.
               That leads to the worst case time complexity O(|V||E|).
        Space:
               The maximums space that will be taken is number of vertices and edges O(|V| + |E|)
    
    '''
    if not G:
        return None
    ver_container={}
    ver_cache=[]
    ver_cache += G.get('A')
    ver_container['A']=[]
    while len(G)!=len(ver_container):
        min_edge=-1
        min_ver=""
        for edge in ver_cache:
            ver_a = edge[0]
            ver_exist = ver_container.get(ver_a)
            if ver_exist != None:
                ver_cache.remove((ver_a, edge[1]))
            elif (min_edge == -1 or edge[1] < min_edge):
                min_edge = edge[1]
                min_ver = edge[0]
        ver_cache.remove((min_ver, min_edge))
        for e in G[min_ver]:
            if e[1]==min_edge and ver_container.get(e[0]) != None:
                ver_container[e[0]].append((min_ver, min_edge))
                ver_container[min_ver]=[(e[0],min_edge),]
        ver_cache += G[min_ver]

    return ver_container


    
def question4(T, r, n1, n2):
    '''
    Since the tree is binary search tree, the tree rotation can be done after just observing the values.
    If we have both element on one side, we should go to that side
    If we have them in two different sides, that is the lowest ancestor.
    In order to make it simple, I use the recursive method.
    I found condition to rotate tree in different directions as induction and the condition to return the node.
    Complexity:
        Time: The recursive method has terrible time complexity performance.
              For each recursive call, we have at most n matrix elements to iterate over.
              The number of recursive calls is at most the depth of tree, i.e., log(n).
              The overall worst case time complexity is O(nlog(n))
        Space: Recursive method saves space and this question is not the exception.
               In each recursive call, no new memory in proportion to the size of Tree Matrix is created.
               So the Space Complexity is Constant O(1)
              
    
    '''
    if n1 == n2 or r == n1 or r == n2 or T is None or len(T) == 0:
        return None
    if (r-n1)*(r-n2)<0:
        return r
    elif r<n1:
        it=0
        for i in range(0, len(T[r])):
            if it==0 and T[r][i]>0:
                it += 1
            elif it==1 and T[r][i]>0:
                return question4(T, i, n1, n2)
    elif r>n1:
        for i in range(0, len(T[r])):
            if T[r][i]>0:
                return question4(T, i, n1, n2)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
def question5(ll, m):
        '''
        This linked list problem can be solved by add each element of the linked list into an array
        When finished, we can directly access the last mth element using indexing.
        Complexity:
            Time:
                Pushing all the elements is the bottleneck and it takes O(n).
                So overall time complexity is O(n).
            Space:
                Storing the elements into the list takes O(n) space.
                So the overall space complexity is O(n).

        '''
        li=[]
        length=0
        while ll != None:
            li.insert(0,ll.data)
            ll=ll.next
            length += 1
        if length - m <0:
            return None
        return li[m-1]


#------------------------------------------------Start tests from here-----------------------------------------------------------------------------------

print "-----Question 1 Test: -----\n\nShall return: \nNone None False True True False\n"
print "Test Results:"
print question1(None,None), question1("Udacity",""), question1("Udacity","bda"), question1("Udacity","ad"), question1("cinema","iceman"),question1("ddac",
"daac")
print "\n"

print "-----Question 2 Test: -----\n\nShall return:\nNone None ababa abacaba\n"
print "Test Result:"
print question2(""), question2(None), question2("dsabababccc"), question2("abacabadab")
print "\n"

print '''-----Question 3 Test: -----\n\nShall return:
None
None
{'A': [('C', 1), ('B', 2)], 'C': [('A', 1)], 'B': [('A', 2)]}
{'A': [('C', 1), ('B', 2), ('E', 4)], 'C': [('A', 1)], 'B': [('A', 2), ('D', 2)], 'E': [('A', 4)], 'D': [('B', 2)]}
      '''
print "Test Result:"
print question3(None)
print question3({})
print question3({'A': [('B', 2), ('C', 1)],
     'B': [('A', 2), ('C', 5)], 
     'C': [('B', 5), ('A', 1)]})
print question3({'A': [('B', 2), ('C', 1),('E', 4)],
     'B': [('A', 2), ('D', 2)], 
     'C': [('A', 1),('D', 4)],
     'D': [('C', 4),('B', 2),('E', 10)],
     'E': [('A', 4),('D', 10)]})
print "\n"

print '''-----Question 4 Test: -----\n\nShall return:
None
None
3
1
'''

print "Test Result:"

    

print question4([[0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]],
              3,
              1,
              1)

print question4([],
              3,
              1,
              4)

print question4([[0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]],
              3,
              1,
              4)
print question4([[0, 0, 0, 0, 0],
               [1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 1, 0, 0, 1],
               [0, 0, 0, 0, 0]],
              3,
              0,
              2)
print "\n"



print '''-----Question 5 Test: -----\n\nShall return:
None
None
4
3
10
    '''

l0=Node(data=1)
l1=Node(data=4)
l2=Node(data=3)
l3=Node(data=10)


print "Test Result:"
print question5(None,1)
print question5(l0,3)
l0.next=l1
print question5(l0,1)
l1.next=l2
print question5(l0,1)
l2.next=l3
print question5(l0,1)


