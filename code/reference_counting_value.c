struct Value {
    enum ValueType is;
    union {
        bool b;
        int i;
        Object *o;
    } as;
};
