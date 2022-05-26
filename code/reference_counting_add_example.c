case OP_ADD: {
    Value b = pop(H);
    Value a = pop(H);
    if (is_int(a)) {
        if (is_int(b)) {
            a.as.i += b.as.i;
            push(H, a);
        }
    } else if (is_string(a)) {
        push_intern_string(H, value_concat(a, b));
    }
    dereference(H, a);
    dereference(H, b);
    break;
}
