function convertMyDollars(usd, currency) {
  let vows = 'aeiou';
  if (vows.includes(currency[0].toLowerCase())){
    return `You now have ${usd * CONVERSION_RATES[currency]} of ${currency}.`
}else{
  let change = Number(parseInt(String(CONVERSION_RATES[currency]), 2));
  return `You now have ${usd * change} of ${currency}.`
}
}
