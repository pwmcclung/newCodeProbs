function stolenLunch(note) {
    let testSwitch = {'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6', 'h':'7','i':'8','j':'9',
                    '0':'a','1':'b', '2':'c','3':'d','4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}
    let noteArr = note.split('').map((x) => testSwitch[x] || x);
    return noteArr.join(''); 
  }