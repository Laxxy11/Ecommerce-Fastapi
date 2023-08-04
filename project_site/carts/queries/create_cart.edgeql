select(
    insert Cart{
    user:=(select User filter .id =<uuid>$user_id),
    products := (select Product filter .title =<str>$title ),
    quantity:=<int64>$quantity
})
{
    user:{username},products:{title},quantity
};    