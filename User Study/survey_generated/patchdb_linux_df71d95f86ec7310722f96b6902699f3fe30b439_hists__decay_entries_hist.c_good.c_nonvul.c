void hists__decay_entries(struct hists *hists)
{
    struct rb_node *next = rb_first(&hists->entries);
    struct hist_entry *n;
    while (next)
    {
        n = rb_entry(next, struct hist_entry, rb_node);
        next = rb_next(&n->rb_node);
        if (hists__decay_entry(hists, n) && !n->used)
        {
            rb_erase(&n->rb_node, &hists->entries);
            if (sort__need_collapse)
                rb_erase(&n->rb_node_in, &hists->entries_collapsed);
            hist_entry__free(n);
            --hists->nr_entries;
        }
    }
}