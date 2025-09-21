
var RandomizedSet = function() {
    this.values = [];
    this.valuesIdx = {};
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (val in this.valuesIdx) {
        return false;
    }

    this.valuesIdx[val] = this.values.length;
    this.values.push(val);

    return true;
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if (!(val in this.valuesIdx)) {
        return false;
    }

    const index = this.valuesIdx[val];
    this.valuesIdx[this.values[this.values.length - 1]] = index;
    delete this.valuesIdx[val];
    this.values[index] = this.values[this.values.length - 1];
    this.values.pop();

    return true;
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    const index = Math.floor(Math.random() * this.values.length);
    return this.values[index];
};
