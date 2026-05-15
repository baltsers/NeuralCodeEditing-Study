void xf_free(xfInfo *xfi)
{
    xf_window_free(xfi);
    XCloseDisplay(xfi->display);
}