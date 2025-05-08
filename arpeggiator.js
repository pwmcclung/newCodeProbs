function arpeggio(notes) {
 let notesArr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
 if (!notesArr.includes(notes)){
   return undefined;
 }
  while(notesArr[0] !== notes){
    let first = notesArr.shift();
    notesArr.push(first);
  }
  let newNotes = notesArr.slice().concat(notesArr[0]);
  return [newNotes[0], newNotes[2], newNotes[4], newNotes[newNotes.length-1]];
}
