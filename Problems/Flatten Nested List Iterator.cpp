class NestedIterator {
private:
    vector<int> flat;
    int index = 0;

    void flatten(const vector<NestedInteger>& nestedList) {
        for (const auto& ni : nestedList) {
            if (ni.isInteger()) {
                flat.push_back(ni.getInteger());
            } else {
                flatten(ni.getList());
            }
        }
    }

public:
    NestedIterator(vector<NestedInteger>& nestedList) {
        flatten(nestedList);
    }

    int next() {
        return flat[index++];
    }

    bool hasNext() {
        return index < flat.size();
    }
};
