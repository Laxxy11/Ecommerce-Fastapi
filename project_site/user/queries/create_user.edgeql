select (
    insert User{
        username:=<str>$username,
        email:=<str>$email,
        password:=<str>$password,
        user_role:=<str>$user_role,
    }
){
    username,email,user_role
};