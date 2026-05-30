class Deque {
    class Node {
        int val;
        Node next;
        Node prev;
        Node(int value) {
            this.val = value;
            Node next = null;
            Node prev = null;
        }
    }
    Node head;
    Node tail;
    

    public Deque() {
        head = null;
        tail = null;

    }

    public boolean isEmpty() {
        if (head == null) {
            return true;
        }
        return false;

    }

    public void append(int value) {
        Node newNode = new Node(value);
        if (head == null) {
            head = newNode;
            tail = head;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
       
    }

    public void appendleft(int value) {
        if (head == null) {
            append(value);
        } else {
            Node newNode = new Node(value);
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
        
    }

    public int pop() {
        if (head == null) {
            return -1;
        } else if (head.next == null) {
            int num = tail.val;
            head = null;
            tail = null;
            return num;
        }
        int num = tail.val;
        Node temp = tail.prev;
        temp.next = null;
        tail.prev = null;
        tail = temp;
        return num;      
    }

    public int popleft() {

         if (head == null) {
            return -1;
        } else if (head.next == null) {
            int  num = head.val;
            head = null;
            tail = null;
            return num;
        }
        int num = head.val;
        Node temp = head.next;
        temp.prev = null;
        head.next = null;
        head = temp;
        return num;  
       
        
    }
}
