var longestPalindrome = function(s) {
    var res = '';
    for(var i = 0; i < s.length; i++){
        var head = i, tail, count;
        while(s[i] == s[i + 1]) i++;
        tail = i;
        count = tail - head + 1;

        for(var offset = 1; head - offset > -1 && tail + offset < s.length; offset++){
            if(s[head - offset] == s[tail + offset]) count += 2;
            else break;
        }
        if(count >= res.length) res = s.substr(head - ((count - (tail - head + 1)) / 2), count);
    }
    return res;
};