select (
    update Product filter.id=<uuid>$product_id
    set{
        title :=<str>$new_title,
        description := <str>$description,
        price := <float64>$price,
        categories := (
            select Category
            filter .name in array_unpack(<array<str>>$categories)
        )
    }       
)
{
    title,description,price,categories,created_at,updated_at
}



