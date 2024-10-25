function hotSingles(arr1, arr2) {
    let arr1New = arr1.filter((x) => !arr2.includes(x));
     let arr2New = arr2.filter((x) => !arr1.includes(x));
     let combined = [...new Set(arr1New.concat(arr2New))];
     return combined;
   }