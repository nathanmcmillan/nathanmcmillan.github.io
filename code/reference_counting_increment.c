void reference(Value value) {
    switch (value.is) {
    case VALUE_ARRAY:
    case VALUE_STRING:
        Object *object = (Object *)(value).as.o;
        object->count++;
    default:
        return;
    }
}
