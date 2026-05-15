GfigObject *d_load_object(gchar *desc, FILE *fp)
{
    GfigObject *new_obj = NULL;
    gint xpnt;
    gint ypnt;
    gchar buf[MAX_LOAD_LINE];
    DobjType type;
    type = gfig_read_object_type(desc);
    if (type == OBJ_TYPE_NONE)
    {
        g_message("Error loading object: type not recognized.");
        return NULL;
    }
    while (get_line(buf, MAX_LOAD_LINE, fp, 0))
    {
        if (sscanf(buf, "%d %d", &xpnt, &ypnt) != 2)
        {
            if (!strcmp("<EXTRA>", buf))
            {
                if (!new_obj)
                {
                    g_message("Error while loading object (no points)");
                    return NULL;
                }
                get_line(buf, MAX_LOAD_LINE, fp, 0);
                if (sscanf(buf, "%d", &new_obj->type_data) != 1)
                {
                    g_message("Error while loading object (no type data)");
                    return NULL;
                }
                get_line(buf, MAX_LOAD_LINE, fp, 0);
                if (strcmp("</EXTRA>", buf))
                {
                    g_message("Syntax error while loading object");
                    g_free(new_obj);
                    return NULL;
                }
                continue;
            }
            else
                return new_obj;
        }
        if (!new_obj)
            new_obj = d_new_object(type, xpnt, ypnt);
        else
            d_pnt_add_line(new_obj, xpnt, ypnt, -1);
    }
    return new_obj;
}