static gboolean user_set_icon_file(AccountsUser *auser, GDBusMethodInvocation *context, const gchar *filename)
{
    User *user = (User *)auser;
    uid_t uid;
    const gchar *action_id;
    uid = method_invocation_get_uid(context);
    if (user->uid == uid)
        action_id = "org.freedesktop.accounts.change-own-user-data";
    else
        action_id = "org.freedesktop.accounts.user-administration";
    daemon_local_check_auth(user->daemon, user, action_id, TRUE, user_change_icon_file_authorized_cb, context, g_strdup(filename), (GDestroyNotify)g_free);
    return TRUE;
}