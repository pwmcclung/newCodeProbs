function add(a, b) {
  let i = a.length - 1;
  let j = b.length - 1;
  let carry = 0;
  let result = "";

  while (i >= 0 || j >= 0 || carry > 0) {
    let digit1 = i >= 0 ? parseInt(a[i]) : 0;
    let digit2 = j >= 0 ? parseInt(b[j]) : 0;

    let sum = digit1 + digit2 + carry;
    result = (sum % 10) + result;
    carry = Math.floor(sum / 10);

    i--;
    j--;
  }

  return result;
}