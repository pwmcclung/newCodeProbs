function squareProduct(n) {
    if (n <= 0) {
        return [];
    }
    let sqrtN = Math.sqrt(n);
    if (!Number.isInteger(sqrtN)) {
        return [];
    }
    let targetProduct = sqrtN;
    let result = [];

    let limit = Math.floor(Math.sqrt(targetProduct));

    for (let a = 1; a <= limit; a++) {
        if (targetProduct % a === 0) {
            let b = targetProduct / a;
            result.push([a, b]);
        }
    }

    return result;
}