select(insert Product{
    title:=<str>$title,
    description:=<str>$description,
    price:=<float64>$price,
    categories:=(select Category filter .name in array_unpack(<array<str>>$categories))
})
{
    title,description,price,categories,created_at
};