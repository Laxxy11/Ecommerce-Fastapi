
select(
    insert Product{
    title:=<str>$title,
    description:=<str>$description,
    price:=<float64>$price,
    categories:=(select Category filter .name in array_unpack(<array<str>>$categories)),
    user:=(select User filter .id =<uuid>$user_id)
})
{
    title,description,price,user,categories:{id, name},created_at
};    