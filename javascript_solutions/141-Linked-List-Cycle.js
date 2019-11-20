/*
Question Link: https://leetcode-cn.com/problems/linked-list-cycle/
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {

    /* Method One */

    // if (!head) return false

    // let slow = head
    // let fast = head

    // while(slow.next && fast.next && fast.next.next) {
    //     slow = slow.next
    //     fast = fast.next.next

    //     if(slow === fast) return true
    // }
    // return false


    /* Method Two */
    
    if (!head) return false
    
    const nodeSet = new Set()
    let node = head

    while (node) {
        node = node.next
        if (nodeSet.has(node)) return true
        nodeSet.add(node)
    }
    return false

};
