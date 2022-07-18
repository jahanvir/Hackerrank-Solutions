SinglyLinkedListNode* mergeLists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
    
    if(head1==nullptr) return head2;
    else if(head2==nullptr) return head1;
    
    SinglyLinkedListNode* head;
    
    if(head1->data<=head2->data){        
        head=head1;
        head->next=mergeLists(head1->next,head2);
    }
    else {
        head=head2;
        head->next=mergeLists(head2->next,head1);
    }
    
    return head;
    
}