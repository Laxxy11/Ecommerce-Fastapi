select
 User
{id,
 username,
 email,
 user_role } 
filter .id=<uuid>$user_id and .user_role=<str>"admin" 