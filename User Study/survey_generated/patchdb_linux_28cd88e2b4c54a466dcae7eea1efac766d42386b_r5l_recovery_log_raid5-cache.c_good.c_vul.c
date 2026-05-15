static int r5l_recovery_log(struct r5l_log *log)
{
    struct r5l_recovery_ctx ctx;
    ctx.pos = log->last_checkpoint;
    ctx.seq = log->last_cp_seq;
    ctx.meta_page = alloc_page(GFP_KERNEL);
    if (!ctx.meta_page)
        return -ENOMEM;
    r5l_recovery_flush_log(log, &ctx);
    __free_page(ctx.meta_page);
    if (ctx.seq > log->last_cp_seq + 1)
    {
        int ret;
        ret = r5l_log_write_empty_meta_block(log, ctx.pos, ctx.seq + 10);
        if (ret)
            return ret;
        log->seq = ctx.seq + 11;
        log->log_start = r5l_ring_add(log, ctx.pos, BLOCK_SECTORS);
        r5l_write_super(log, ctx.pos);
    }
    else
    {
        log->log_start = ctx.pos;
        log->seq = ctx.seq;
    }
    return 0;
}