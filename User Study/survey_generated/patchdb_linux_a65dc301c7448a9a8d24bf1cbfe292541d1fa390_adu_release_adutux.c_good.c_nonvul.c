static int adu_release(struct inode *inode, struct file *file)
{
    struct adu_device *dev = NULL;
    int retval = 0;
    dbg(2, " %s : enter", __FUNCTION__);
    if (file == NULL)
    {
        dbg(1, " %s : file is NULL", __FUNCTION__);
        retval = -ENODEV;
        goto exit;
    }
    dev = file->private_data;
    if (dev == NULL)
    {
        dbg(1, " %s : object is NULL", __FUNCTION__);
        retval = -ENODEV;
        goto exit;
    }
    down(&dev->sem);
    if (dev->open_count <= 0)
    {
        dbg(1, " %s : device not opened", __FUNCTION__);
        retval = -ENODEV;
        goto exit;
    }
    retval = adu_release_internal(dev);
exit:
    if (dev)
        up(&dev->sem);
    dbg(2, " %s : leave, return value %d", __FUNCTION__, retval);
    return retval;
}