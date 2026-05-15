static gboolean user_set_icon_file(AccountsUser *auser, GDBusMethodInvocation *context, const gchar *filename)
{
    User *user = (User *)auser;
    int uid;
    const gchar *action_id;
    if (!get_caller_uid(context, &uid))
    {
        throw_error(context, ERROR_FAILED, "identifying caller failed");
        return FALSE;
    }
    if (user->uid == (uid_t)uid)
        action_id = "org.freedesktop.accounts.change-own-user-data";
    else
        action_id = "org.freedesktop.accounts.user-administration";
    daemon_local_check_auth(user->daemon, user, action_id, TRUE, user_change_icon_file_authorized_cb, context, g_strdup(filename), (GDestroyNotify)g_free);
    return TRUE;
}