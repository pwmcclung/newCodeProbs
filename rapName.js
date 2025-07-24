function rapNameGen(dob){
  let splitDob = dob.split('.');
  let day = Math.ceil(parseInt(splitDob[0]).toString().split('').map(Number).reduce((a,b)=> a + b,0)/2);
  let year = Math.ceil(parseInt(splitDob[2]).toString().split('').map(Number).reduce((a,b)=> a + b,0)/2);
  let obj = {0:'0ero', 1:'1ne', 2:'2wo', 3:'3hree', 4:'4our', 5:'5ive', 6:'6ix', 7:'7even', 8:'8ight', 9:'9ine'};
  let first = obj[day];
  let second = obj[year];
  return `${first} ${second}`;
}