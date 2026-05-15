static void aoedev_freedev(struct aoedev *d)
{
    if (d->gd)
    {
        aoedisk_rm_sysfs(d);
        put_disk(d->gd);
    }
    kfree(d->frames);
    if (d->bufpool)
        mempool_destroy(d->bufpool);
    kfree(d);
}