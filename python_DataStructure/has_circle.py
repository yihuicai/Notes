def has_cycle(head):
    current=head
    linkedlistkv={}
    while current!=None:
        if linkedlistkv.get(current.data):
            return 1
        else: 
            linkedlistkv[current.data]=1
        current=current.next

    return 0
    
