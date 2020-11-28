/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
      if(head == NULL) return NULL;
vector<Node*> vn;
Node* p = head;
int pos = 0;
while(p != NULL)
{
Node* q = new Node(p->val,NULL,NULL);
vn.push_back(q);
p->val = pos;
++pos;
p= p->next;
}

vn.push_back(NULL);
p = head;
pos = 0;
while(p!= NULL)
{
vn[pos]->next = vn[pos+1];
Node* r = p->random;
if(r!= NULL)
{
vn[pos]->random = vn[r->val];
}
++pos;
p= p->next;
}
return vn[0];
}
};