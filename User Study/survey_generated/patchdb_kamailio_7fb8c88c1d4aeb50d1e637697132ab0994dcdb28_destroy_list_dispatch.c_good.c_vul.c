void destroy_list(int list_id)
{
    ds_set_t *sp = NULL;
    ds_dest_t *dest = NULL;
    sp = ds_lists[list_id];
    while (sp)
    {
        for (dest = sp->dlist; dest != NULL; dest = dest->next)
        {
            if (dest->uri.s != NULL)
            {
                shm_free(dest->uri.s);
                dest->uri.s = NULL;
            }
        }
        if (sp->dlist != NULL)
            shm_free(sp->dlist);
        sp = sp->next;
    }
    ds_lists[list_id] = NULL;
}