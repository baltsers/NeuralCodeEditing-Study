static struct glink_channel *qcom_glink_alloc_channel(struct qcom_glink *glink, const char *name)
{
    struct glink_channel *channel;
    channel = kzalloc(sizeof(*channel), GFP_KERNEL);
    if (!channel)
        return ERR_PTR(-ENOMEM);
    spin_lock_init(&channel->recv_lock);
    spin_lock_init(&channel->intent_lock);
    channel->glink = glink;
    channel->name = kstrdup(name, GFP_KERNEL);
    init_completion(&channel->open_req);
    init_completion(&channel->open_ack);
    init_completion(&channel->intent_req_comp);
    INIT_LIST_HEAD(&channel->done_intents);
    INIT_WORK(&channel->intent_work, qcom_glink_rx_done_work);
    idr_init(&channel->liids);
    idr_init(&channel->riids);
    kref_init(&channel->refcount);
    return channel;
}