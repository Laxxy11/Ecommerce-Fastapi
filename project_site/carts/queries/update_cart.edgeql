select (
    update Cart filter.id=<uuid>$cart_id and  .user.id=<uuid>$user_id
    set{
        
        quantity:= <int64>$quantity,
        products := (select Product filter .id =<uuid>$product_id ),
        user:=(select User filter .id =<uuid>$user_id),
    }       
)
{
   quantity,products,user
}
