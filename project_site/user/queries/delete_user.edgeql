select (
    delete User filter(User.username=<str>$username)
)
{
    username,email,user_role,
}