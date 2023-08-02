select (
    insert User{
        username:=<str>$username,
        email:=<str>$email,
        password:=<str>$password
    }
){
    username,email
};