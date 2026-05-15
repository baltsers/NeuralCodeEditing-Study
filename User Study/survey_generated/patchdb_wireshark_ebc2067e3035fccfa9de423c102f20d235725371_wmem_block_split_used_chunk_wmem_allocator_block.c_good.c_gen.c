static void wmem_block_split_used_chunk(wmem_block_allocator_t *allocator, wmem_block_chunk_t *chunk, const size_t size)
{
    wmem_block_chunk_t *extra;
    size_t aligned_size, available;
    gboolean last;
    g_assert(chunk->used);
    aligned_size = WMEM_ALIGN_SIZE(size);
    if (aligned_size + sizeof(wmem_block_chunk_t) > WMEM_CHUNK_DATA_LEN(chunk))
    {
        return;
    }
    last = chunk->last;
    available = chunk->len;
    chunk->len = (guint32)(aligned_size + sizeof(wmem_block_chunk_t));
    chunk->last = FALSE;
    extra = WMEM_CHUNK_NEXT(chunk);
    available -= (aligned_size + sizeof(wmem_block_chunk_t));
    extra->len = (guint32)available;
    extra->last = last;
    extra->prev = (guint32)(aligned_size + sizeof(wmem_block_chunk_t));
    extra->used = FALSE;
    wmem_block_add_to_free_list(allocator, extra);
}