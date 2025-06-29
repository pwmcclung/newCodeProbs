function dateChecker(date){ 
    let testDate =  /^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$/;
    return testDate.test(date);
}