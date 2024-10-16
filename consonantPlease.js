function sortLetters(...arr1) {
    let newArr = arr1.flat(Infinity);
    let arr2 = newArr.filter(v=>typeof v === 'string').map((x)=>x.toUpperCase());
    return [arr2.filter(v=>/[AEUIO]/.test(v)),arr2.filter(v=>/[^AEUIO]/.test(v))];
 }