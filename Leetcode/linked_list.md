```c++
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ptr=new ListNode(0);
        ListNode* ret=ptr;
        int ind=0;
        while(l1!=NULL&&l2!=NULL){
            ret->next=new ListNode(0);
            ret=ret->next;
            int cur=l1->val + l2->val + ind;
            if(ind=cur/10>0)
                cur=cur%10;
            ret->val=cur;
            l1=l1->next;
            l2=l2->next;
        }
        while(l1!=NULL){
            ret->next=new ListNode(0);
            ret=ret->next;
            int cur=(l1->val+ind)%10;
            ind=(l1->val+ind)/10;
            ret->val=cur;
            l1=l1->next;
        }
        while(l2!=NULL){
            ret->next=new ListNode(0);
            ret=ret->next;
            int cur=(l2->val+ind)%10;
            ind=(l2->val+ind)/10;
            ret->val=cur;
            l2=l2->next;
        }
        
        if (ind>0){
            ret->next=new ListNode(ind);
        }
        return ptr->next;
    }
};
```

#### Solution:  Adding two Numbers

- There will be a beginning with redundant 0, It's better than having a redundant 0 in the end
- Don't forget to add carry after one of the lists end
- It's common to use `    ListNode* ptr=new ListNode(0);    ListNode* ret=ptr;` when you want to return a  value.

```c++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* ptr=head;
        ListNode* ret=nullptr;
        list<int> reverse;
        if(ptr==NULL) return NULL;
        while(ptr!=NULL){
            reverse.push_back(ptr->val);
            ptr=ptr->next;
        }
        while(reverse.size()!=0){ // where you need attention on iterator
            int a=reverse.front();
            reverse.pop_front();
            ListNode* n=new ListNode(a);
            n->next=ret;
            ret=n;
        }
        return ret;
    }
};
```

#### Solution: Reverse Linked List

- Remember when you are poping things off, do not use iterators.



```c++
ListNode* removeElements(ListNode* head, int val) {
    if (head == NULL) return NULL;
    if (val == head->val) return removeElements(head->next,val);
    head->next = removeElements(head->next,val);
    return head;
}
```

#### Solution: Remove Linked List Elements

- This solution is a basis of recursive way of thinking.

- Needs an end to recursive.

- return must be object itself, at least an object with a property that needs to be function itself.

  ​