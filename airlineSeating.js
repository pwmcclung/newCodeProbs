function airlineSeating(seats, premium, standard) {
  
    let result = [];
    let premiumCount = 0;
    let standardCount = 0;

    // Assign Premium customers to first class
    for (let i = 0; i < seats.length; i++) {
        if (seats[i] === 'f' && premiumCount < premium) {
            result[i] = 'p';
            premiumCount++;
        }
    }

    // Assign Standard customers to coach
    for (let i = 0; i < seats.length; i++) {
        if (seats[i] === 'c' && standardCount < standard) {
            result[i] = 's';
            standardCount++;
        }
    }

    // If coach is full, try to assign Standard customers to remaining first class
    if (standardCount < standard) {
        for (let i = 0; i < seats.length; i++) {
            if (seats[i] === 'f' && result[i] === undefined && standardCount < standard) {
                result[i] = 's';
                standardCount++;
            }
        }
    }


    //Fill remaining seats with spaces
    for (let i = 0; i < seats.length; i++) {
        if (result[i] === undefined) {
            result[i] = ' ';
        }
    }

    return result;
}