function inter(s1, s2){
    let a1 = Array.from(s1);
    let a2 = Array.from(s2);
    let newS = a1.filter((x) => a2.includes(x));
    return new Set(newS);
}