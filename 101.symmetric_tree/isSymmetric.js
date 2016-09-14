/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**@author HanchengZhao
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    var leftArr = [];
    var rightArr = [];
    leftPreOrder(root,leftArr);
    rightPreOrder(root, rightArr);
    return isEqualArr(leftArr,rightArr) ? true : false;
};

var leftPreOrder = function(node,arr) {
    if(node !== null){
        arr.push(node.val);
        leftPreOrder(node.left,arr);
        leftPreOrder(node.right,arr);
    }else {
        arr.push('null');//still have to compare the null position
    }
}

var rightPreOrder = function(node,arr) {
    if(node !== null){
        arr.push(node.val);
        rightPreOrder(node.right,arr);
        rightPreOrder(node.left,arr);
    }else {
        arr.push('null');
    }
}

var isEqualArr = function(arr1, arr2){
    if (arr1.length !== arr2.length) return false;
    for(var i = 0; i < arr1.length; i++){
        if(arr1[i] !== arr2[i]) return false;
    }
    return true;
}