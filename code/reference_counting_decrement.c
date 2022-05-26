void dereference(Value value) {
    switch (value.is) {
    case VALUE_ARRAY: {
        Array *array = (Array *)(value).as.o;
        int count = array->object.count--;
        if (count == 0) {
            free(array->items);
            free(array);
        }
        return;
    }
    case VALUE_STRING: {
        String *string = (String *)(value).as.o;
        int count = string->object.count--;
        if (count == 0) {
            free(string->chars);
            free(string);
        }
        return;
    }
    default:
        return;
    }
}
