void dbus_test(void)
{
    char *str = getenv("DBUS_SESSION_BUS_ADDRESS");
    if (str)
    {
        char *bus = strdup(str);
        if (!bus)
            errExit("strdup");
        char *sockfile = strstr(bus, "unix:abstract=");
        if (sockfile)
        {
            sockfile += 13;
            *sockfile = '@';
            char *ptr = strchr(sockfile, ',');
            if (ptr)
                *ptr = '\0';
            check_session_bus(sockfile);
            sockfile -= 13;
        }
        free(bus);
    }
}