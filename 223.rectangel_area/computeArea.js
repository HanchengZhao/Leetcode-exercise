/**
 * @param {number} A
 * @param {number} B
 * @param {number} C
 * @param {number} D
 * @param {number} E
 * @param {number} F
 * @param {number} G
 * @param {number} H
 * @return {number}
 */
var computeArea = function(A, B, C, D, E, F, G, H) {
    var interWidth = computeLength(A,C,E,G);
    var interHeight = computeLength(B,D,F,H);

    var intersectionArea = interWidth * interHeight;
    console.log(intersectionArea);
    var area1 = (C-A) * (D-B);
    var area2 = (G-E) * (H-F);
    return area1 + area2 - intersectionArea;
    // divide into two sides, using the same function
};

var computeLength = function(A,C,E,G){
    if(Math.max(A,C) <= Math.min(E,G) || Math.min(A,C) >= Math.max(E,G)){
        return 0;
    }
    var s1 = Math.min(A,C);
    var b1 = Math.max(A,C);
    var s2 = Math.min(E,G);
    var b2 = Math.max(E,G);
    // console.log(s1,b1,s2,b2);
    if(s1 < s2 && b1 >= s2 && b1 <= b2){//1 on the left of 2
        return b1 - s2;
    }else if(s1 >= s2 && b1 <= b2){//1 at the inside of 2
        return b1 - s1;
    }else if(s1 < b2 && b1 >= b2 && s1 >= s2){//1 on the right of 2
        return b2 - s1;
    }else if(s1 < s2 && b1 > b2){//1 at the outside of 2
        return b2 - s2;
    }

};
