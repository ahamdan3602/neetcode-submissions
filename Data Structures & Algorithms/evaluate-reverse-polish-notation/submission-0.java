class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<>();

        int s1;
        int s2;
        for (int i = 0; i < tokens.length;i++) {
            if (isInteger(tokens[i])) {
                s.push(Integer.parseInt(tokens[i]));
            } else if (tokens[i].equals("+")) {
                s1 = s.pop();
                s2 = s.pop() + s1;
                s.push(s2);
            } else if (tokens[i].equals("*")) {
                s1 = s.pop();
                s2 = s.pop() * s1;
                s.push(s2);
            } else if (tokens[i].equals("-")) {
                s1 = s.pop();
                s2 = s.pop() - s1;
                s.push(s2);
            } else if (tokens[i].equals("/")) {
                s1 = s.pop();
                s2 = s.pop()/s1;
                s.push(s2);
            }
        }
        return s.pop();
  
    }

    public boolean isInteger(String s) {
        try {
            Integer.valueOf(s);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}
