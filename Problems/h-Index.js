var hIndex = function(citations) {
    let citeList = new Array(citations.length + 1).fill(0);
    for (let i = 0; i < citations.length; ++i) {
        citeList[Math.min(citations.length, citations[i])] += 1;
    }

    let cumulative = 0;
    for (let i = citations.length; i >= 0; --i) {
        cumulative += citeList[i];
        if (cumulative >= i) {
            return i;
        }
    }

    return 0;
};
