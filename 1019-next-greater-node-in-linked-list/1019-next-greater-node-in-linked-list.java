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
    public int[] nextLargerNodes(ListNode head) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for(ListNode ptr = head; ptr != null ; ptr = ptr.next) 
            list.add(ptr.val);
        
        int[] ans = new int[list.size()];
        Stack<Integer> stack = new Stack<>();
        
        for(int i=0;i<ans.length;i++) {
            while(!stack.isEmpty() && list.get(i) > list.get(stack.peek()))
            {
                ans[stack.pop()] = list.get(i);
            }
            stack.push(i);
        }
        
        return ans;
    }
}