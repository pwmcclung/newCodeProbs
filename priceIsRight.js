function priceIsRight(numbers, target) {
  let numbersFilteredSorted = numbers.filter((x) => x <= target).sort((a,b) => a-b,0);
  return numbersFilteredSorted[numbersFilteredSorted.length-1];
}
