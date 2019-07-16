var myPow = function(x, n) {
  if (n == 0) return 1;
  if (n < 0) return 1 / myPow(x, -n);
  if (n % 2 == 0) {
    return myPow(x * x, Math.floor(n / 2));
  } else {
    return x * myPow(x * x, Math.floor(n / 2));
  }
};
