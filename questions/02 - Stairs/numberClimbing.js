// Question:
// Each time, you can take 1 or 2 step(s) on the stair.
// Find the number of the climbings to the n-th step.

var numberClimbing = function(n) {
    
    // n-th step can be reached from (n-1)th step by one step
    // or from (n-2)th step by two steps.
    // It means that S(n) = S(n-1) + S(n-2)
    // which makes the question the same with fibonacci sequence

    if(n==1)
        return 1;
    if(n==2)
        return 2;
    
    var prev = 1;
    var current = 2;
    for(var i=3; i<=n; i++){
        var temp = current;
        current += prev;
        prev = temp;
    }
        
    return current;
};

// Test Cases
console.log(numberClimbing(3));     // 3
console.log(numberClimbing(12));    // 233