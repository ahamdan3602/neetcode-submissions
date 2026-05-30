/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        List<Integer> arr = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();
        ListNode temp = head;
        
        while (temp != null) {
            arr.add(temp.val);
            temp = temp.next;
        }
        int p1 = 0;
        int p2 = arr.size() - 1;

        while (p1 <= p2) {
            arr2.add(arr.get(p1));
            arr2.add(arr.get(p2));
            p1++;
            p2--;
        }

        temp = head;
        int i = 0;
        while (temp != null && i < arr2.size()) {
            temp.val = arr2.get(i);
            temp = temp.next;
            i++;
        }
        
    
    

        
    }
}
