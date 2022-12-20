class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack<>(); 
        int j = 0; 
        
        for(int val : pushed){
            stack.push(val); 
            while(!stack.isEmpty() && stack.peek() == popped[j]){ 
                stack.pop(); 
                j++; 
            }
        }
        return stack.isEmpty(); 
    }
}