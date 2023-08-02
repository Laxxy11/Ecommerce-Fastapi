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


    type Category{
        required name :str{
            constraint exclusive;
        }
    }

    type Product{
        required title :str{
            constraint exclusive;
        }
        description : str;
        multi link categories:Category;
        required price : float64;
        property created_at ->datetime{
            readonly:=True;
            default:=datetime_current();
        }
        property updated_at->datetime{
            readonly:=True;
            default:=datetime_current();
        }
    }

}