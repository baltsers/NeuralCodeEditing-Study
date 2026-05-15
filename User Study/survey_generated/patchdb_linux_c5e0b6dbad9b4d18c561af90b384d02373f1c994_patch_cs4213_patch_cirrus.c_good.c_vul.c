static int patch_cs4213(struct hda_codec *codec)
{
    struct cs_spec *spec;
    int err;
    spec = kzalloc(sizeof(*spec), GFP_KERNEL);
    if (!spec)
        return -ENOMEM;
    codec->spec = spec;
    spec->vendor_nid = CS4213_VENDOR_NID;
    err = cs421x_parse_auto_config(codec);
    if (err < 0)
        goto error;
    codec->patch_ops = cs421x_patch_ops;
    return 0;
error:
    kfree(codec->spec);
    codec->spec = NULL;
    return err;
}