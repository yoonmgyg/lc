var candy = function(ratings) {
    let n = ratings.length;
    let total = n;

    let i = 1;
    while (i < n) {
        if (ratings[i] == ratings[i-1]) {
            ++i;
            continue;
        } 

        let current_peak = 0;
        while (i < n && ratings[i] > ratings[i-1]) {
            current_peak += 1;
            total += current_peak;
            ++i;
        }

        if (i == n)
            return total;
        let current_valley = 0;
        while (i < n && ratings[i] < ratings[i-1]) {
            current_valley += 1;
            total += current_valley;
            ++i;
        }
        total -= Math.min(current_peak, current_valley);
    }

    return total;
};
