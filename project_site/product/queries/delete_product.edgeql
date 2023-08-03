select(
    delete Product filter.id=<uuid>$id
)
{
    title,description,price,categories,created_at,updated_at
}