int generateKey(int num1, int num2, int num3) {
    int key = 0, factor = 1;

    for (int i = 0; i < 4; i++) {
        int d1 = num1 % 10;
        int d2 = num2 % 10;
        int d3 = num3 % 10;
        key += (factor * min({d1, d2, d3}));
        factor *= 10;

        num1 /= 10;
        num2 /= 10;
        num3 /= 10;
    }

    return key;
}
