class MinStack {
    private int min;
    private Stack<Integer> s;
    private Stack<Integer> minStack;

    public MinStack() {
        s = new Stack<>();
        minStack = new Stack<>();
        
    }
    
    public void push(int val) {
        if (s.isEmpty()) {
            min = val;
        } else {
            if (val <= min) {
                minStack.push(min);
                min = val;
            }
        }
        s.add(val);
    }
    
    public void pop() {
        if (s.isEmpty()) { 
            return;
        }
        if (s.peek() == min && !minStack.isEmpty()) {
            min = minStack.pop();
        }
        s.pop();
    }
    
    public int top() {
        return s.peek();
        
    }
    
    public int getMin() {
        return min;
        
    }
}
