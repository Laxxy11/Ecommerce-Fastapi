select Product {title,description,price,categories:{name},created_at,updated_at} filter (Product.title=<str>$title);