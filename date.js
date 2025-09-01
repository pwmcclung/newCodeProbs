function regularMonths(currMonth) {
    const monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    function isLeap(year) {
        return (year % 400 === 0) || (year % 100 !== 0 && year % 4 === 0);
    }
    let [month, year] = currMonth.split('-').map(Number);
    let currentDayOfWeek = 4; // Day of week for Jan 1, 1970
    for (let y = 1970; y < year; y++) {
        currentDayOfWeek = (currentDayOfWeek + (isLeap(y) ? 366 : 365)) % 7;
    }
    for (let m = 1; m < month; m++) {
        let daysInMonth = monthLengths[m - 1];
        if (m === 2 && isLeap(year)) { // February
            daysInMonth = 29;
        }
        currentDayOfWeek = (currentDayOfWeek + daysInMonth) % 7;
    }
    let currentMonth = month;
    let currentYear = year;
    let daysInCurrMonth = monthLengths[currentMonth - 1];
    if (currentMonth === 2 && isLeap(currentYear)) {
        daysInCurrMonth = 29;
    }
    currentDayOfWeek = (currentDayOfWeek + daysInCurrMonth) % 7;
    currentMonth++;
    if (currentMonth > 12) {
        currentMonth = 1;
        currentYear++;
    }
    while (true) {
        if (currentDayOfWeek === 1) {
            return `${String(currentMonth).padStart(2, '0')}-${currentYear}`;
        }
        let daysInPrevMonth = monthLengths[currentMonth - 1];
        if (currentMonth === 2 && isLeap(currentYear)) {
            daysInPrevMonth = 29;
        }
        currentDayOfWeek = (currentDayOfWeek + daysInPrevMonth) % 7;
        currentMonth++;
        if (currentMonth > 12) {
            currentMonth = 1;
            currentYear++;
        }
    }
}