static void aoedev_freedev(struct aoedev *d)
{
    if (d->gd)
    {
        aoedisk_rm_sysfs(d);
        del_gendisk(d->gd);
        put_disk(d->gd);
    }
    kfree(d->frames);
    mempool_destroy(d->bufpool);
    kfree(d);
}