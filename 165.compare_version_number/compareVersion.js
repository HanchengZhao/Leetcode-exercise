/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    var split1 = version1.split(".");
    var split2 = version2.split(".");
    var length = Math.max(split1.length,split2.length);
    for(var i=0; i<length; i++){
        var v1 = i < split1.length ? Number(split1[i]) : 0;
        var v2 = i < split2.length ? Number(split2[i]) : 0;
        console.log(v1);
        console.log(v2);
        if(v1 !== v2){
            return v1 > v2 ? 1:-1;
        }
    }
    return 0;
};
console.log(compareVersion("0","01"));


    // version1 += ".0.0.0.0";
    // version2 += ".0.0.0.0";
    // var ver1 = version1.split(".");
    // var ver2 = version2.split(".");
    // if(Number(ver1[0]) !== Number(ver2[0])){
    //     return Number(ver1[0]) > Number(ver2[0]) ? 1 : -1;
    // }else{//first equal
    //     if(Number(ver1[1]) !== Number(ver2[1])){
    //       return Number(ver1[1]) > Number(ver2[1]) ? 1 : -1;  
    //     }else{
    //         if(Number(ver1[2]) === Number(ver2[2])){
    //             return 0;
    //         }
    //         return Number(ver1[2]) > Number(ver2[2]) ? 1 : -1;
    //     }
    // }
// console.log(compareVersion("0","1.2"));

// console.log(compareVersion("0","2"));
// console.log(compareVersion("01","1"));