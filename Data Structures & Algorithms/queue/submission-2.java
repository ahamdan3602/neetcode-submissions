class Deque {

    class Node{
        int val;
        Node left;
        Node right;
        Node(int val) {
            this.val = val;
            this.left = null;
            this.right = null;
        }
    }
    private Node head;
    private Node tail;

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
        Node temp = new Node(value);
        // [1 -> 2 -3]
        if (tail == null) {
            head = temp;
            tail = temp;
        } else {
            tail.right = temp;
            temp.left = tail;
            tail = temp;
        }
    }

    public void appendleft(int value) {
        Node temp = new Node(value);
        if (head == null) {
            head = temp;
            tail = temp;
        } else {
            head.left = temp;
            temp.right = head;
            head = temp;
        }
        
    }

    public int pop() {
        if (tail == null) {
            return -1;
        } else if (tail.val == head.val) {
            int res = tail.val;
            tail = null;
            head = null;
            return res;
        }
        int val = tail.val;
        Node temp = tail;
        tail = tail.left;
        tail.right = null;
        temp.left = null;
        return val;

    }

    public int popleft() {
        if (head == null) {
            return -1;
        } else if (head.val == tail.val) {
            int res = tail.val;
            tail = null;
            head = null;
            return res;
        }
        int val = head.val;
        Node temp = head;
        head = head.right;
        temp.right = null;
        head.left = null;
        return val;
        
    }
}
