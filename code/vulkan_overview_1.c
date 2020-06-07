struct vulkan_pipeline {
    uint32_t swapchain_image_count;
    struct vulkan_renderbuffer *renderbuffer;
    struct vulkan_uniformbuffer *uniforms;
    struct vulkan_image **images;
    int image_count;
    char *vertex_shader_path;
    char *fragment_shader_path;
    VkDescriptorSetLayout vk_descriptor_set_layout;
    VkDescriptorPool vk_descriptor_pool;
    VkDescriptorSet *vk_descriptor_sets;
    VkPipeline vk_pipeline;
    VkPipelineLayout vk_pipeline_layout;
    bool include_depth;
};
