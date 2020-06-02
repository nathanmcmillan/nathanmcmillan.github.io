void matrix_frustum_corners(vec4 *corners, float *matrix) {

    corners[0] = (vec4){-1, -1, -1, 1};
    corners[1] = (vec4){1, -1, -1, 1};
    corners[2] = (vec4){-1, 1, -1, 1};
    corners[3] = (vec4){1, 1, -1, 1};
    corners[4] = (vec4){-1, -1, 1, 1};
    corners[5] = (vec4){1, -1, 1, 1};
    corners[6] = (vec4){-1, 1, 1, 1};
    corners[7] = (vec4){1, 1, 1, 1};

    vec4 transform;
    for (int i = 0; i < 8; i++) {
        matrix_multiply_vector4(&transform, matrix, &corners[i]);
        corners[i].x = transform.x / transform.w;
        corners[i].y = transform.y / transform.w;
        corners[i].z = transform.z / transform.w;
        corners[i].w = 1;
    }
}
