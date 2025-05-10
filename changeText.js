function heavyMetalUmlauts(boringText) {
   let letterDict = {'A':'Ä', 'E':'Ë', 'I':'Ï','O':'Ö','U':'Ü','Y':'Ÿ',
                  'a':'ä','e':'ë', 'i':'ï', 'o':'ö', 'u':'ü', 'y':'ÿ'};
   let changedText = boringText.split('').map((x)=> letterDict[x] || x).join('');
   return changedText;
}
