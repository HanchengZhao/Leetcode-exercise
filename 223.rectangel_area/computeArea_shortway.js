var computeArea = function(A, B, C, D, E, F, G, H) {
    var left = Math.max(A,E), right = Math.max(Math.min(C,G), left);
    var bottom = Math.max(B,F), top = Math.max(Math.min(D,H), bottom);
    return (C-A)*(D-B) - (right-left)*(top-bottom) + (G-E)*(H-F);
    // divide into two sides, using the same function
};