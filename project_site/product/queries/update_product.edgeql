select (
    update Product filter.id=<uuid>$product_id and  .user.id=<uuid>$user_id
    set{
        title :=<str>$new_title,
        description := <str>$description,
        price := <float64>$price,
        categories := (
            select Category
            filter .name in array_unpack(<array<str>>$categories)
        ),
        user:=(select User filter .id =<uuid>$user_id),
    }       
)
{
    title,description,price,user,categories,created_at,updated_at
}



