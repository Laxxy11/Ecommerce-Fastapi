module default {
    type User{
        required username :str{
            constraint exclusive;
        }
        required email :str{
            constraint exclusive;
        }
        required password : str;
    }

}